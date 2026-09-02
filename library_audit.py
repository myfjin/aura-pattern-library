#!/usr/bin/env python3
"""library_audit.py — the SECOND layer of library verification.

`library_verify.py` proves the library **is what it claims to be**: signed, watermarked,
catalogued, counted, internally consistent. It does NOT prove that any individual pattern
**is worth anything**. That gap was named by 6E on 2026-08-30 as twelve classes; this tool
implements the mechanically decidable ones and FLAGS the rest with evidence.

⛔ WHY THIS IS A SEPARATE FILE. `census_mismatches` in library_verify.py graduated on
2026-08-30 after eight red-team rounds with 4Q (round 8: zero findings) plus Ver's honesty
pass. Adding twelve new check classes to that file would restart its graduation clock. The
graduated gate stays graduated; this layer is red-teamed on its own.

⛔ THE LAW OF THIS FILE: A CHECK THAT COULD NOT RUN MUST NEVER REPORT `pass`.
Every check returns one of:
    pass          — measured, and it is fine
    fail          — MEASURED AND WRONG (deterministic defect)
    flag          — measured something suspicious that needs judgement; evidence attached
    unverifiable  — could not measure (no implementation for this language, hang, missing tool)
    skip          — genuinely not applicable, or not requested (detail says which)
A language with no implementation for a check gets `unverifiable`, never `pass`. That is the
vacuous-fixture trap: a check that cannot fail scores as a pass no matter how broken it is.

Output: JSONL. Line 1 is the run header; every subsequent line is one pattern record.
Record design is 6E's, from REPORT-6E-VALIDATOR-DESIGN.md §3.
"""
from __future__ import annotations

import argparse
import ast
import hashlib
import json
import re
import subprocess
import sys
import time
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

import library_verify as LV

ROOT = Path(__file__).resolve().parent
LANE_EXT = {"python": ".py", "cpp": ".cpp", "rust": ".rs", "go": ".go", "r": ".R",
            "javascript": ".js"}
EXT_LANE = {v: k for k, v in LANE_EXT.items()}

# ⛔ Ver honesty pass, 2026-08-30, finding 1: the clean verdict is NO_FINDING, not PASS.
# "PASS" told a reader "this pattern is good"; the tool only ever measured the classes it can
# check, and C1/C3/C11 were never assessed for ANY pattern. The disclosure existed per record
# but a summary view shows the headline word, not the footnote. The word now matches the
# measurement: no finding was made, which is not the same as nothing being wrong.
# ⛔ 2026-08-30, Illia: "UNVERIFIABLE" as a RECORD verdict described the TOOL, not the
# pattern. All 729 of them ran 6-7 checks CLEAN and were unverifiable only on the three
# python-AST checks; a clean cpp file read as UNVERIFIABLE while an identical python file
# read as NO_FINDING. One enum was carrying two orthogonal facts -- WAS ANYTHING FOUND and
# HOW MUCH OF THE SUITE RAN -- so no single word could be honest. They are now two axes and
# the verdict is their COMPOUND. This does NOT reopen PASS_WITH_GAPS (Ver's ruling stands):
# a partially-measured record never renders as a bare "NO_FINDING", because the coverage
# half is part of the verdict string itself and cannot be dropped by a consumer that reads
# only `verdict`.
FINDINGS = ("NO_FINDING", "FAIL", "FLAG", "SKIP")
COVERAGES = ("FULL", "PARTIAL", "NONE")
# NONE coverage means nothing at all could be measured -- the ONLY honest use of the word.
VERDICTS = tuple("%s/%s" % (f, c) for f in FINDINGS for c in COVERAGES)
STATUSES = ("pass", "fail", "flag", "unverifiable", "skip")

# ⛔ 4Q round 8, F1: THREE places each hardcoded their own idea of which statuses are clean
# (`triage_fields`, the invariant probe loop, `verdict_for`). That is the exact shape of the
# round-7 U3 bug: a value added to the enum and forgotten in one consumer routes a real
# finding to nobody. There is now ONE partition; every consumer derives from it, and a
# status that belongs to no part cannot reach runtime -- the import fails.
CLEAN_STATUSES = ("pass", "skip")            # nothing found, nothing to route
FINDING_STATUSES = ("fail", "flag")          # a human must read the pattern
UNMEASURED_STATUSES = ("unverifiable",)      # the tool could not look at all
# a second, orthogonal partition: what the coverage counters divide the checks into
MEASURED_STATUSES = ("pass", "fail", "flag")
SKIPPED_STATUSES = ("skip",)
# severity order -- first match wins in verdict_for
# severity order for the FINDING axis only. `unverifiable` is deliberately absent: it is
# a coverage fact, not a finding, and routing it here is what produced the wrong label.
STATUS_VERDICT = {"fail": "FAIL", "flag": "FLAG"}

def _partition_check():
    for name, parts in (
        ("routing", (CLEAN_STATUSES, FINDING_STATUSES, UNMEASURED_STATUSES)),
        ("coverage", (MEASURED_STATUSES, UNMEASURED_STATUSES, SKIPPED_STATUSES)),
    ):
        seen = [x for part in parts for x in part]
        if sorted(seen) != sorted(set(seen)) or set(seen) != set(STATUSES):
            raise KeyError(
                "STATUSES and the %s partition disagree (%r vs %r). A status must belong to "
                "exactly one part of every partition, or a consumer will silently drop it."
                % (name, sorted(set(STATUSES)), sorted(seen)))
    _declared = set(STATUS_VERDICT) | set(CLEAN_STATUSES) | set(UNMEASURED_STATUSES)
    if _declared != set(STATUSES):
        raise KeyError("every status needs a finding verdict, or must be declared clean, or "
                       "must be declared unmeasured; missing %r"
                       % sorted(set(STATUSES) - _declared))

_partition_check()

# ================================================================= UNVERIFIABLE taxonomy
# 6E, 2026-08-30: UNVERIFIABLE as ONE bucket is useless for triage -- "the tool has no R
# analyser" and "this twin has no source" do not have the same remedy. Every unverifiable
# return therefore names a REASON CODE, and each code maps to a subclass that names its own
# remedy. The code is emitted as a "[CODE] " prefix by _u(); the prefix is a typed constant
# at the return site, not prose to be grepped, and a self-test probe asserts that EVERY
# unverifiable detail in the whole run carries one.
#   U1 NO ANALYSER        -> the tool is the gap             -> TOOL_WORK
#   U2 MISSING PREREQUISITE -> environment/data is the gap   -> PROVISION
#   U3 PATHOLOGICAL       -> the FILE blocked measurement    -> INVESTIGATE
# 6E's fourth class ("shape the check cannot decide") is deliberately NOT here: that is
# already `skip` or `unassessed_classes`, and folding it in would make every documented
# python pattern UNVERIFIABLE.
REASON_SUBCLASS = {
    "NO_RULE_TABLE":    "U1", "EMPTY_RULE_TABLE": "U1", "NO_STRIPPER":      "U1",
    "NO_ASSERT_GRAMMAR": "U1", "NON_PYTHON_AST":  "U1", "NO_DOC_SLOT":      "U1",
    "NO_REPEAT_RUNNER": "U1",
    "NO_STDLIB_LIST":   "U2", "NO_TOOLCHAIN":     "U2", "NO_INDEX":         "U2",
    # ⛔ 6E conformance 3: PARSE_FAIL is tagged with this code but EMITTED with status
    # "fail" (check_hollow, check_assert_nonvacuous, check_doc_behavior) -- `_u()` only
    # tags the string, it does not set the status. So the claim test takes the
    # FINDING_STATUSES branch and this U3 never routes. The subclass is the TAXONOMY answer
    # ("the file itself blocked measurement"); the ROUTING answer is needs_review, whose
    # disposition set includes REJECT and is the right one for a malformed file. Documented
    # and locked by a probe, not vestigial by accident. (Measured: 0 of the 1500 records
    # carry a PARSE_FAIL check — the class is real but unexercised by this library.)
    "PARSE_FAIL":       "U3", "HANG":             "U3", "REPEAT_ERROR":     "U3",
}
SUBCLASS_REMEDY = {
    "U1": ("NO_ANALYSER", "tool work: build the analyser for this check x lane"),
    "U2": ("MISSING_PREREQUISITE", "environment/data work: provide the prerequisite"),
    "U3": ("PATHOLOGICAL", "investigate the file: defect (fix/quarantine) or documented"),
}
# Closed set. A triage session assigns one of these; WAIVE additionally REQUIRES a
# disposition_ref, or it is a silent pass wearing another name (6E).
DISPOSITIONS = ("FIX", "QUARANTINE", "ACCEPT", "REJECT", "TOOL_WORK", "PROVISION",
                "WAIVE", "ESCALATE")
SUBCLASS_DISPOSITIONS = {
    "U1": ("TOOL_WORK", "WAIVE", "ESCALATE"),
    "U2": ("PROVISION", "WAIVE", "ESCALATE"),
    "U3": ("FIX", "QUARANTINE", "ACCEPT", "ESCALATE"),
}


LANES = ("python", "cpp", "go", "rust", "r", "javascript")

# 6E's structural guard against THE trap. U1 (no analyser) is the subclass most likely to be
# quietly converted to PASS by a well-meaning edit -- and exit-2 cannot catch that, because a
# record turned `pass` LEAVES the unverifiable bucket and the forcing function goes blind.
# So the coverage is DECLARED here and asserted cell by cell in the self-test: a cell with no
# analyser must return `unverifiable` with a U1 code, and a cell WITH one must not. Adding a
# fallback that returns `pass` when it found nothing to measure breaks a probe, loudly.
# Decorators that transform the decorated object and touch NOTHING else. Everything not
# here is treated as a possible import side effect, which is the safe direction: `@register`
# and `@app.route` must keep flagging. See the adjudication note in check_importable.
PURE_DECORATORS = frozenset((
    "dataclass", "contextmanager", "asynccontextmanager", "property", "staticmethod",
    "classmethod", "abstractmethod", "abstractproperty", "cached_property", "wraps",
    "lru_cache", "cache", "total_ordering", "singledispatch", "singledispatchmethod",
    "override", "final", "runtime_checkable", "no_type_check", "setter", "getter",
    "deleter",
))


ANALYSER_COVERAGE = {
    "hollow":               LANES,          # ASSERT_PAT + stripper for all six
    "dangerous_primitives": LANES,          # DANGEROUS  + stripper for all six
    "determinism_markers":  LANES,          # NONDET     + stripper for all six
    "hardcoded_abs_path":   LANES,          # stripper for all six
    "assert_nonvacuous":    LANES,          # python AST + a literal-only rule per lane
    "importable":           ("python",),    # python AST only
    "deps":                 LANES,          # python AST + a lexical rule per lane
    # ROUND 19: the description SLOT differs per language, but it is a lexical fact in each,
    # and build_patterns_index's frozen ruler already reads all six for PATTERNS_INDEX.md.
    # This was one of the four U1 sources that made every non-python pattern UNVERIFIABLE.
    "doc_behavior":         LANES,
}


def _u(code: str, detail: str) -> str:
    """Tag an unverifiable detail with its reason code. Raises on an unknown code, so a new
    unverifiable path cannot enter the tool without declaring which remedy it needs."""
    if code not in REASON_SUBCLASS:
        raise KeyError(f"unknown unverifiable reason code {code!r}")
    return f"[{code}] {detail}"


def _strip_fail_reason(lane: str) -> str:
    """Why did strip_noncode fail for this lane? Two very different causes wore one code.

    ⛔ 4Q round 6. For python, `ok=False` can ONLY mean the source did not tokenise -- python
    HAS a stripper. Reporting NO_STRIPPER (U1 "build an analyser") sent a triage session to
    build tooling that already exists, when the real remedy is U3: the FILE is broken. For
    every other lane, ok=False does mean no stripper exists.
    """
    return "PARSE_FAIL" if lane == "python" else "NO_STRIPPER"


def reason_of(detail: str):
    """(code, subclass) for an unverifiable detail, or (None, None) if it carries no code."""
    if detail.startswith("["):
        c = detail[1:detail.index("]")] if "]" in detail else ""
        if c in REASON_SUBCLASS:
            return c, REASON_SUBCLASS[c]
    return None, None


def _norm_source(text: str, lane: str) -> str:
    """Strip the AURA watermark block and normalise whitespace, so duplicate detection sees
    the CODE and not the three lines every file carries by construction."""
    out = []
    for ln in text.splitlines():
        s = ln.strip()
        if not s:
            continue
        if "△ AURA Pattern Library" in s:
            continue
        # Only a COMMENT/mark line carrying AE1. is watermark. A line of real code that
        # merely mentions AE1. must survive, or two different patterns collide -- 4Q D2.
        if "AE1." in s and re.match(r'^\s*(#|//|/\*|--|;)', s):
            continue
        if re.match(r'^\s*(static\s+const\s+char\s*\*)?\s*_?[aA]ura_?[mM]ark\s*[:=]', s):
            continue
        out.append(re.sub(r"\s+", " ", s))
    return "\n".join(out)


# ---------------------------------------------------------------- C2 dangerous primitives
# A SECURITY pattern library may legitimately DEMONSTRATE a weak primitive, so these are
# `flag` with evidence, never `fail`. Deciding exploitability in context is judgement (6E).
DANGEROUS = {
    "python": [
        (r"\beval\s*\(", "eval()"),
        (r"\bexec\s*\(", "exec()"),
        (r"\bos\.system\s*\(", "os.system()"),
        (r"shell\s*=\s*True", "subprocess shell=True"),
        (r"\bpickle\.loads?\s*\(", "pickle.load/loads"),
        (r"\byaml\.load\s*\((?![^)]*Safe)", "yaml.load without SafeLoader"),
        (r"\bhashlib\.md5\s*\(", "hashlib.md5"),
        (r"\bhashlib\.sha1\s*\(", "hashlib.sha1"),
        (r"\bos\.popen\s*\(", "os.popen"),
        # ⛔ 6E round 15: the table enumerated SPELLINGS, not primitives. os.system and
        # os.popen were flagged while subprocess.Popen/call/run — the canonical process
        # execution API — passed outright, and `from os import system; system(...)` walked
        # past the dotted regex entirely. Every one of these is the same primitive under a
        # different name, in the check whose whole mandate is surfacing weak primitives in
        # a SECURITY library. Measured false NO_FINDINGs, not hypotheticals.
        (r"\bsubprocess\.(?:Popen|call|check_call|check_output|run)\s*\(",
         "subprocess process execution"),
        (r"^\s*from\s+os\s+import\s+[^\n]*\b(?:system|popen)\b",
         "os.system/os.popen imported under a bare name"),
        (r"\bos\.exec[lv][pe]{0,2}\s*\(", "os.exec*"),
        (r"\bos\.spawn[lv][pe]{0,2}\s*\(", "os.spawn*"),
        (r"\binput\s*\(", "input() — blocks a non-interactive gate"),
    ],
    "javascript": [
        (r"\beval\s*\(", "eval()"),
        # 4Q R16: `Function(...)` without `new` is the same code-from-string primitive.
        (r"\bnew\s+Function\s*\(|(?<![\w.])Function\s*\(\s*['\"]", "Function() from a string"),
        # ⛔ 6E R17 F1 (mechanism corrected, defect real): a bare substring flagged any path
        # that MENTIONS the module -- require("./docs/child_process_notes"). MEASURED against
        # commit 2cba6d4: it flagged there too, so this is PRE-EXISTING, not a round-17
        # regression. An import rule must match the WHOLE specifier, not a piece of one.
        (r"['\"](?:node:)?child_process['\"]", "child_process"),
        # 6E R16 F5: .innerHTML= was one sink of a family. These all write attacker-
        # controlled markup or script into the DOM -- the exact XSS class the rule exists
        # to surface, under four other spellings.
        (r"\.innerHTML\s*=", "innerHTML assignment"),
        (r"\.outerHTML\s*=", "outerHTML assignment"),
        (r"\.insertAdjacentHTML\s*\(", "insertAdjacentHTML"),
        (r"document\.write(?:ln)?\s*\(", "document.write"),
        (r"createElement\s*\(\s*['\"]script", "dynamic <script> injection"),
        (r"createHash\(\s*['\"]md5", "md5"),
        (r"createHash\(\s*['\"]sha1", "sha1"),
        # 4Q R18 F1: setTimeout/setInterval with a STRING argument parses and executes that
        # string -- the eval class under a fourth spelling. A function argument is fine.
        (r"\bset(?:Timeout|Interval)\s*\(\s*['\"]", "setTimeout(string) — eval-like"),
    ],
    "cpp": [
        # 4Q R18 F2: too BROAD, the opposite of every round-16 finding. `\bsystem\s*\(`
        # matched `hw.system(42)` -- a method on an object, not <cstdlib>'s system(). A call
        # reached through `.` or `->` is BY CONSTRUCTION a member call and cannot be the C
        # library function, so this is decidable lexically and needs no type resolution.
        (r"(?<![.\w])(?<!->)system\s*\(", "system()"),
        (r"\bpopen\s*\(", "popen"),
        (r"\bexec[lv][pe]{0,2}\s*\(", "exec*"),
        (r"\bstrcpy\s*\(", "strcpy"),
        # 6E R16 F3: strcat is strcpy's unbounded sibling; the scanf %s family is the
        # gets-class overflow; SHA1 was flagged in PYTHON but not here, so the two tables
        # disagreed about one weak-hash class.
        (r"\bstrcat\s*\(", "strcat"),
        (r"\bsprintf\s*\(", "sprintf"),
        (r"\bgets\s*\(", "gets"),
        (r"\bs?scanf\s*\([^)]*%\s*(?:s|\[)", "unbounded scanf %s"),
        (r"\bMD5[_(]", "MD5"),
        (r"\bSHA1[_(]", "SHA1"),
        # 4Q R18 F1: vsprintf is sprintf's variadic twin with the identical unbounded-write
        # risk, and tmpnam returns a PREDICTABLE name -- the classic temp-file race.
        (r"\bvs?printf\s*\(", "vsprintf"),
        (r"\btmpnam\s*\(", "tmpnam — predictable temp name"),
    ],
    "go": [
        # ⛔ 6E R17 F1: same class -- "example.com/old/os/exec-wrapper" is a wrapper package,
        # not os/exec. A Go import path IS a string literal, so anchor on the whole literal.
        (r"['\"]os/exec['\"]", "os/exec"),
        # 6E R16 F2: os/exec is the WRAPPER. syscall.Exec/ForkExec is the raw primitive it
        # wraps -- the same relationship as os.system vs subprocess in python.
        (r"syscall\.(?:Exec|ForkExec|StartProcess)\s*\(", "syscall raw exec"),
        (r"crypto/md5", "crypto/md5"),
        (r"crypto/sha1", "crypto/sha1"),
        # 4Q R18 F1: the go table flagged weak HASHES and no weak CIPHERS. DES and RC4 are
        # deprecated ciphers; a pattern demonstrating either is broken in the same way.
        (r"crypto/des", "crypto/des — weak cipher"),
        (r"crypto/rc4", "crypto/rc4 — weak cipher"),
        (r"unsafe\.", "unsafe"),
    ],
    "rust": [
        (r"\bunsafe\s*\{", "unsafe block"),
        # 4Q R18 F1: the rule required the FULLY-QUALIFIED path, so `use std::process;` +
        # `process::Command::new()` and `use std::process::*;` + `Command::new()` both walked
        # past it. Same class as 6E's `from os import system` in python: an import alias is a
        # second spelling of the same call. The bare form is admitted only when the file
        # actually imports it, so an unrelated local `Command` type is not flagged.
        (r"(?:std::)?process::Command", "process::Command"),
        (r"use\s+std::process::\*\s*;[\s\S]*?\bCommand::new\s*\(",
         "process::Command (glob-imported)"),
        # 6E R16 F4: libc::system is C system() over FFI -- the same primitive the cpp
        # table flags. It was caught ONLY when it happened to sit inside an unsafe block,
        # so 6E proved the miss by writing it outside one.
        (r"libc::(?:system|execv?p?|popen)\s*\(", "libc process execution over FFI"),
        (r"\b(?:std::mem::)?transmute\s*(?:::<|\()", "mem::transmute"),
        (r"\.unwrap\(\)", "unwrap() — panics instead of handling"),
    ],
    "r": [
        (r"\beval\s*\(", "eval()"),
        # 6E R16 F1: base R's shell family is system/system2/shell -- three names in one
        # documentation chapter. `\bsystem\s*\(` cannot match `system2(`.
        (r"\bsystem2?\s*\(", "system()/system2()"),
        (r"\bshell\s*\(", "shell()"),
        (r"\.(?:Call|C|Fortran)\s*\(", "compiled-code FFI"),
        (r"\bsource\s*\(\s*['\"]https?://", "source() from a URL"),
        (r"\bparse\s*\(\s*text\s*=", "parse(text=)"),
    ],
}

# ---------------------------------------------------------------- C10 determinism markers
# ⛔ 4Q and 6E, round 16, independently: this table enumerated SPELLINGS of
# nondeterminism and every lane had a sibling under another name. os.urandom is not
# matched by `\brandom\.` (no word boundary after `os.`), hash(str) is randomised per
# process by PYTHONHASHSEED, time(NULL) is the C spelling of chrono::now, Instant::now is
# the Rust spelling of SystemTime::now. Twelve demonstrated false passes across six lanes.
NONDET = {
    "python": [(r"\brandom\.", "random"), (r"\bnp\.random\.", "numpy.random"),
               (r"\bos\.urandom\s*\(", "os.urandom"), (r"\bsecrets\.", "secrets"),
               (r"\btime\.time\s*\(", "time.time"), (r"datetime\.now\s*\(", "datetime.now"),
               (r"\btime\.(?:perf_counter|process_time|monotonic)\s*\(", "time counters"),
               (r"\bos\.getpid\s*\(", "os.getpid"),
                       # ⛔ TRIAGE, 6E: this matched `def hash(self, item, max_value)` -- a pattern that
        # DEFINES a hash method was accused of depending on PYTHONHASHSEED. 1 of the 12
        # hash() flags (bloom_filter.py) was this; the other 11 are genuine builtin calls.
        (r"(?<![\w.])(?<!def[ \t])hash\s*\(", "hash() — PYTHONHASHSEED randomises str hashing"),
               (r"\buuid\.", "uuid"), (r"\brequests\.", "network: requests"),
               (r"urllib\.request", "network: urllib"), (r"\bsocket\.", "network: socket")],
    "javascript": [(r"Math\.random", "Math.random"), (r"Date\.now", "Date.now"),
                   (r"performance\.now", "performance.now"),
                   (r"crypto\.getRandomValues", "crypto.getRandomValues"),
                   (r"\bXMLHttpRequest\b", "network: XMLHttpRequest"),
                   (r"\bWebSocket\b", "network: WebSocket"),
                   (r"\bfetch\s*\(", "network: fetch"), (r"require\(['\"]http", "network: http")],
    "cpp": [(r"\brand\s*\(", "rand()"), (r"random_device", "random_device"),
            (r"\btime\s*\(\s*(?:NULL|nullptr|0|&)", "time()"),
            (r"\bgettimeofday\s*\(", "gettimeofday"), (r"\bclock\s*\(\s*\)", "clock()"),
            (r"chrono::.*now", "chrono::now")],
    "go": [(r"math/rand", "math/rand"), (r"crypto/rand", "crypto/rand"),
           (r"time\.Now", "time.Now"), (r"net/http", "network")],
    "rust": [(r"\brand::", "rand crate"), (r"SystemTime::now", "SystemTime::now"),
             (r"Instant::now", "Instant::now")],
    "r": [(r"\brunif\s*\(|\brnorm\s*\(|\bsample\s*\(", "random"),
          (r"Sys\.time\s*\(|Sys\.Date\s*\(", "Sys.time/Sys.Date"),
          (r"(?<![\w.])date\s*\(\s*\)", "date()")],
}

# ⛔ Round 16, and this one had a FALSE POSITIVE in it, which is the worse flavour: a rust
# file whose only assertions are debug_assert! was told "no assertion construct found in
# CODE" -- `\bassert!` cannot match `debug_assert!` because `_` is a word character, so the
# tool accused a real assertion of not existing (6E). The rest are false hollows: a C++
# file asserting only with static_assert, a JS file throwing TypeError rather than Error.
ASSERT_PAT = {
    "python": r"\bassert\b",
    "javascript": (r"\bassert\b|\bthrow\s+new\s+\w*(?:Error|Exception)\b"
                   r"|\bexpect\s*\(|\.should\b"),
    "cpp": r"\bassert\s*\(|\bstatic_assert\s*\(|\b\w*_ASSERT\w*\s*\(",
    # ⛔ TRIAGE, 4Q: this flagged 86 of 93 go patterns as `hollow` and was WRONG on all 86.
    # Go has no assert statement. For a main-package program the canonical assertion is
    # `if cond { fmt.Fprintf(os.Stderr, ...); os.Exit(1) }`. MEASURED over the 86: os.Exit
    # non-zero 86/86, an `if` 86/86, panic 1/86, t.Error 0/86 — the table enumerated two
    # spellings and missed the one in use. `os.Exit(0)` is deliberately NOT an assertion:
    # a successful exit states nothing. log.Fatal* is included because it IS os.Exit(1).
    "go": (r"\bpanic\s*\(|\bt\.(?:Error|Fatal)f?\s*\(|\bos\.Exit\s*\(\s*[1-9]"
           r"|\blog\.Fatal(?:f|ln)?\s*\("),
    "rust": r"\b(?:debug_)?assert(?:_eq|_ne)?!",
    "r": r"\bstopifnot\s*\(|\bstop\s*\(|\bexpect_\w+\s*\(",
}

# ⛔ Round 16, both agents: this enumerated six directories and missed every other standard
# one. A hardcoded "/etc/passwd" or "/root/.ssh/id_rsa" in a SECURITY pattern is a more
# serious finding than a hardcoded /tmp file, and both passed silently. Enumerating the
# ROOTS was the mistake; the rule is now "any absolute unix path", with the handful of
# genuinely portable device/null paths carved out by name.
# ⛔ ROUND 17 — MEASURED, then CORRECTED. Round 16 rewrote this to match ANY quoted "/word",
# because the old list (/home|Users|srv|opt|var|tmp) was missing /etc, /usr, /bin, /dev and
# more -- `"/etc/passwd"` returned a clean pass. That hole was real. The rewrite's cure was
# worse: swept over the library it added 32 flags of which SIXTEEN were false -- HTTP route
# templates and URL components, not filesystem paths at all:
#     "/user/{id}"  "/api/users"  "/health"  "/index.html"  "/path"  "/users"
# A URL path is not a hardcoded filesystem path and this check's harm is non-portability of
# a FILESYSTEM path. So the closed set stays a closed set -- it is the filesystem hierarchy,
# which is finite and stable, unlike a list of dangerous primitives -- but it is now COMPLETE
# rather than the six roots someone happened to think of. Under-flags a rootless literal like
# "/durable.bin"; that is the conservative direction and it is declared, not hidden.
_FS_ROOT = (r"home|Users|srv|opt|var|tmp|etc|usr|bin|sbin|lib|lib64|dev|proc|sys|run|root"
            r"|mnt|media|boot|private|Applications|Library|System|Volumes")
ABS_PATH = re.compile(
    r"['\"](?!/dev/(?:null|zero|urandom|random)['\"])(/(?:" + _FS_ROOT + r")(?:/[^'\"]*)?)['\"]"
    r"|['\"][A-Z]:\\\\")



# ⛔ THIS TABLE AND `DEPS_EXTRACT` MUST AGREE ABOUT WHAT A DEPENDENCY LINE LOOKS LIKE.
# They are two independent tables and NOTHING used to enforce their agreement, which is the
# single defect behind four of 4Q's round-21 findings and behind the round-20 regression:
#   restore DROPS a line the extractor could parse  -> FALSE NEGATIVE  (go alias, R
#                                                       requireNamespace, js dynamic import)
#   restore KEEPS a line that is not an import      -> FALSE POSITIVE  (go raw string)
# `_probe_restore_extract_agreement` in the self-test now asserts the invariant per lane.
_IMPORT_LINE = {
    # ⛔ 4Q ROUND 21 FINDING 2: the bare `"` alternative matched ANY line starting with
    # whitespace + a quote, including lines inside a backtick raw string, and
    # `csv_validator.go` flagged a line of CSV test data as a third-party import. Grouped
    # imports are restored by the dedicated block branch below, not by this pattern, so
    # dropping the alternative loses nothing and closes the hole.
    "go": re.compile(r'^\s*import\s'),
    "rust": re.compile(r'^\s*(use|extern)\s'),
    # ⛔ 4Q ROUND 21 FINDING 4: dynamic `import("express")` has `(` immediately after the
    # keyword, so `import\s` never matched and the line was dropped before `_deps_js` saw it.
    "javascript": re.compile(r'^\s*(import\s|const\s+\w+\s*=\s*require|.*\b(?:require|import)\s*\()'),
    "cpp": re.compile(r'^\s*#\s*include\b'),
    # ⛔ 4Q ROUND 21 FINDING 3: `require\s*\(` cannot match `requireNamespace(` (an `N`
    # follows, not a paren), so the line was dropped and `_deps_r` — which DOES look for
    # requireNamespace — never saw the package name. Longest alternative first.
    # ⛔ AND IT MUST NOT BE ANCHORED TO THE LINE START. `requireNamespace` is idiomatically
    # written inside a guard -- `if (!requireNamespace("dplyr", quietly = TRUE))` -- so an
    # anchored pattern still dropped the line while `_deps_r`, which is UNANCHORED, expected
    # it. My first pass at this finding fixed the vocabulary and left the anchoring wrong:
    # the two tables have to agree on BOTH, which is the whole point of the invariant probe.
    # The restore loop uses `.match`, which anchors at position 0 whatever the pattern says,
    # so the leading `^.*` is load-bearing -- a bare `\b` alternation here matches nothing
    # but a line that STARTS with the keyword, which is the bug this line is fixing.
    "r": re.compile(r'^.*\b(library|requireNamespace|require)\s*\('),
}


# A regex literal is also legal directly after these keywords, where `prev_sig` is the last
# LETTER of the keyword and so never matched the operator set (4Q round 3, F3).
_JS_RE_KW = re.compile(
    r"(?:^|[^\w$.#])(return|typeof|case|delete|void|instanceof|in|of|new|do|else|yield|await)"
    r"\s*$")


def _js_regex_after_kw(text: str, i: int) -> bool:
    lo = max(0, i - 32)
    m = _JS_RE_KW.search(text[lo:i])
    if not m:
        return False
    if m.start(1) == 0 and lo > 0 and (text[lo - 1].isalnum() or text[lo - 1] in "_$.#"):
        return False                 # the window cut a longer identifier in half
    return True


def _import_lines(text: str, lane: str) -> str:
    """Import/include lines put back after stripping. In Go an import path IS a string
    literal (`import "os/exec"`), so blanking strings would delete the dependency the rule
    tables exist to find. An import is code, not prose."""
    pat = _IMPORT_LINE.get(lane)
    if pat is None:
        return ""
    keep, in_block, raw = [], False, False
    for ln in text.splitlines():
        st = ln.strip()
        if lane == "go":
            # ⛔ 4Q ROUND 21 FINDING 2. A backtick raw string can contain a whole import
            # block as prose (a code sample, a generator template, a test fixture). Track
            # backtick parity and restore NOTHING while inside one -- otherwise the block
            # detector fires on quoted text and every line of it becomes a dependency.
            if raw:
                if ln.count("`") % 2:
                    raw = False
                continue
            opened = bool(ln.count("`") % 2)
            if re.match(r'^import\s*\($', st):
                in_block, raw = True, opened
                continue
            if in_block:
                if st == ")":
                    in_block = False
                else:
                    keep.append(ln)
                raw = opened
                continue
            if pat.match(ln):
                keep.append(ln)
            raw = opened
            continue
        if pat.match(ln):
            keep.append(ln)
    # ⛔ Strip comments from the RESTORED lines too. Restoring the original line undid the
    # comment blanking for exactly those lines -- `import "fmt" // uses crypto/md5` would
    # have been flagged for a primitive that lives only in a comment (4Q round 2, F3).
    # ⛔ Scan, do not `find`. A blind find() cut at a `//` inside the import path itself
    # (`import "http://x/exec"` -> `import "http:`, F5) and never saw `/* */` at all, so
    # `#include <cstdlib> /* uses system() */` leaked `system()` as code (F2).
    tok = "#" if lane == "r" else "//"
    out = []
    for ln in keep:
        buf, k, m, q = [], 0, len(ln), ""
        while k < m:
            ch = ln[k]
            if q:
                if ch == "\\":
                    buf.append(ln[k:k + 2]); k += 2; continue
                if ch == q:
                    q = ""
                buf.append(ch); k += 1; continue
            if ch in "\"'`":
                q = ch; buf.append(ch); k += 1; continue
            if ln.startswith(tok, k):
                break                       # line comment, outside any string
            if lane != "r" and ln.startswith("/*", k):
                e = ln.find("*/", k + 2)
                if e == -1:
                    break
                k = e + 2; continue          # block comment, dropped
            buf.append(ch); k += 1
        out.append("".join(buf))
    return "\n".join(out)


def strip_noncode(text: str, lane: str, keep_strings: bool = False):
    """Remove comments (and, unless keep_strings, string literals) so a regex table measures
    CODE, not prose. Returns (stripped_text, ok); ok=False means no stripper exists for the
    lane and the caller MUST report `unverifiable`.

    ⛔ FOUR LANGUAGE TRAPS, all measured. A defect here silences EVERY regex check at once:
      - RUST LIFETIMES. `&'static str` is not a string. Treating that `'` as a quote opened
        a "string" that ran to the next `'` dozens of lines later. MEASURED on the shipping
        library: url_authority_parser.rs lost 17 of 17 asserts and 6 of 6 unwrap() calls,
        and `dangerous_primitives` returned a false `pass` (4Q round 2, F1).
      - C++ RAW STRINGS. `R"(...)"` may contain bare quotes; naive scanning closes early and
        leaks the remainder as code (F2).
      - JS REGEX LITERALS. `/['"]/` contains quotes that are not string delimiters (F4).
      - GO IMPORT PATHS ARE STRING LITERALS, so they are restored afterwards (round 2, F5).
    """
    if lane == "python":
        import io, tokenize
        try:
            lines = text.splitlines(keepends=True)
            spans = []
            for tok in tokenize.generate_tokens(io.StringIO(text).readline):
                if tok.type == tokenize.COMMENT or (
                        tok.type == tokenize.STRING and not keep_strings):
                    spans.append((tok.start, tok.end))
            # Blank the spans IN PLACE. Joining tokens with spaces turned `random.shuffle`
            # into `random . shuffle` and silenced every regex spanning a token boundary.
            for (sr, sc), (er, ec) in spans:
                for row in range(sr, er + 1):
                    if row - 1 >= len(lines):
                        break
                    ln = lines[row - 1]
                    a = sc if row == sr else 0
                    b = ec if row == er else len(ln)
                    b = min(b, len(ln))
                    if a >= b:
                        continue
                    keep_nl = ln[a:b].count("\n")
                    lines[row - 1] = ln[:a] + (" " * (b - a - keep_nl)) + "\n" * keep_nl + ln[b:]
            return "".join(lines), True
        except Exception:
            return text, False          # unparseable -> do NOT pretend we measured code
    if lane in ("cpp", "go", "rust", "javascript", "r"):
        line_tok = "#" if lane == "r" else "//"
        block = lane != "r"
        quotes = "'\"" + ("`" if lane in ("go", "javascript") else "")
        out, i, n = [], 0, len(text)
        prev_sig = ""                    # last significant char, for JS regex detection
        while i < n:
            c = text[i]
            if text.startswith(line_tok, i):
                while i < n and text[i] != "\n":
                    out.append(" "); i += 1
                continue
            if block and text.startswith("/*", i):
                j = text.find("*/", i + 2)
                j = n if j == -1 else j + 2
                out.append(" " * (j - i)); i = j; continue
            # C++ raw string: R"delim( ... )delim"
            if lane == "cpp" and c == "R" and i + 1 < n and text[i + 1] == '"':
                op = text.find("(", i + 2)
                if op != -1:
                    delim = text[i + 2:op]
                    close = ")" + delim + '"'
                    j = text.find(close, op + 1)
                    j = n if j == -1 else j + len(close)
                    seg = text[i:j]
                    out.append(seg if keep_strings else
                               "".join(ch if ch == "\n" else " " for ch in seg))
                    i = j; prev_sig = '"'; continue
            # JS regex literal: /.../ in a position where a value is expected
            if lane == "javascript" and c == "/" and (
                    prev_sig in "=(,:[!&|?{};+*%~^" or _js_regex_after_kw(text, i)):
                j, ok_r, cls = i + 1, False, False
                while j < n:
                    if text[j] == "\\":
                        j += 2; continue
                    if text[j] == "[":
                        cls = True
                    elif text[j] == "]":
                        cls = False
                    elif text[j] == "/" and not cls:
                        ok_r = True; j += 1; break
                    elif text[j] == "\n":
                        break
                    j += 1
                if ok_r:
                    seg = text[i:j]
                    out.append(seg if keep_strings else " " * len(seg))
                    i = j; prev_sig = "/"; continue
            # Rust raw string: r"..." / r#"..."# / r##"..."##. The `r` and `#`s are code
            # and the opening `"` looked like a normal string, so content holding a bare
            # quote closed early and leaked the remainder as code (4Q round 3, F1).
            if lane == "rust" and c in "rb":
                _st = i                     # literal start, INCLUDING a `b` byte prefix
                _rp = i + 1 if (c == "b" and i + 1 < n and text[i + 1] == "r") else i
                if text[_rp] == "r" and not (
                        _st and (text[_st - 1].isalnum() or text[_st - 1] == "_")):
                    k = _rp + 1
                    while k < n and text[k] == "#":
                        k += 1
                    if k < n and text[k] == '"':
                        close = '"' + "#" * (k - _rp - 1)
                        j = text.find(close, k + 1)
                        j = n if j == -1 else j + len(close)
                        seg = text[_st:j]
                        out.append(seg if keep_strings else
                                   "".join(ch if ch == "\n" else " " for ch in seg))
                        i = j; prev_sig = '"'; continue
            # Rust lifetime: `&'a`, `<'static>` -- NOT a character literal, NOT a string.
            # A char literal is 'X' or '\X' or '\u{..}'; anything else after ' is a lifetime.
            if lane == "rust" and c == "'":
                is_char = (i + 1 < n and text[i + 1] == "\\") or \
                          (i + 2 < n and text[i + 2] == "'")
                if not is_char:
                    out.append(c); i += 1; prev_sig = "'"; continue
            # ⛔ 6E round 15, finding 3: a JS template literal is not a plain string. The
            # generic scanner below treats ` as an ordinary quote, so a backtick inside an
            # interpolation -- `a ${'b`c'} d` -- CLOSED the template early and re-parsed the
            # remainder, blanking real code. 6E measured a false pass: eval('1') after such
            # a template became `eval( )`. And the naive fix (blank the whole template) would
            # create the OPPOSITE false pass, because ${eval(x)} is code that runs. So the
            # literal halves are blanked and the interpolations are kept AS CODE.
            if lane == "javascript" and c == "`":
                j, depth, seg = i + 1, 0, [" "]
                while j < n:
                    ch = text[j]
                    if ch == "\\":
                        seg.append("  " if depth == 0 else text[j:j + 2])
                        j += 2
                        continue
                    if depth == 0:
                        if ch == "$" and j + 1 < n and text[j + 1] == "{":
                            depth = 1; seg.append("  "); j += 2; continue
                        if ch == "`":
                            seg.append(" "); j += 1; break
                        seg.append("\n" if ch == "\n" else " "); j += 1; continue
                    # inside ${...}: real code, but its own strings must not be scanned for
                    # braces or the depth count walks off.
                    if ch in "'\"`":
                        q2, k = ch, j + 1
                        while k < n:
                            if text[k] == "\\":
                                k += 2; continue
                            if text[k] == q2:
                                k += 1; break
                            k += 1
                        seg.append("".join(" " if x != "\n" else "\n"
                                           for x in text[j:k]))
                        j = k; continue
                    if ch == "{":
                        depth += 1
                    elif ch == "}":
                        depth -= 1
                        if depth == 0:
                            seg.append(" "); j += 1; continue
                    seg.append(ch); j += 1
                out.append(text[i:j] if keep_strings else "".join(seg))
                i = j; prev_sig = "`"; continue
            if c in quotes:
                q, j = c, i + 1
                while j < n:
                    if text[j] == "\\":
                        j += 2; continue
                    if text[j] == q:
                        j += 1; break
                    if text[j] == "\n" and q != "`":
                        break            # unterminated -- do not eat the rest of the file
                    j += 1
                seg = text[i:j]
                out.append(seg if keep_strings else
                           "".join(ch if ch == "\n" else " " for ch in seg))
                i = j; prev_sig = q; continue
            out.append(c)
            if not c.isspace():
                prev_sig = c
            i += 1
        stripped = "".join(out)
        return stripped + "\n" + _import_lines(text, lane), True
    return text, False


def _text_check(text, lane, table, name, ok_detail, want_pats=False):
    """Regex-table check on COMMENT-stripped source, matched over TWO passes.

    Pass 1 strips string literals (a rule measures CODE, not prose). Pass 2 keeps them, so a
    rule whose signal IS a literal -- createHash("md5"), scanf("%s") -- can fire at all. A
    rule matches if EITHER pass matches. See the round-17 comment at the match site.

    Three ways this must refuse to say `pass`: no rule table for the lane, an EMPTY rule
    table (4Q F6 -- zero rules measured nothing), and no comment-stripper for the lane
    (4Q F3/F5 -- scanning raw text measures prose)."""
    if lane not in table:
        return (name, "unverifiable", _u("NO_RULE_TABLE", f"no {name} rule table for lane '{lane}'"), [])
    if not table[lane]:
        return (name, "unverifiable", _u("EMPTY_RULE_TABLE", f"{name} rule table for lane "
                    f"'{lane}' is EMPTY — zero rules measured nothing"), [])
    code, ok = strip_noncode(text, lane)
    if not ok:
        return (name, "unverifiable",
                _u(_strip_fail_reason(lane),
                   f"could not strip lane '{lane}' — raw text would match prose, so nothing "
                   "was measured" if lane != "python" else
                   "python source did not tokenise, so nothing could be measured"), [])
    # ⛔ ROUND 17 — DEAD BY CONSTRUCTION. Stripping string LITERALS silences every rule whose
    # signal lives inside one. SIX rules were dead this way and four had SHIPPED for sixteen
    # rounds: js createElement("script"), createHash("md5"), createHash("sha1"),
    # Function("..."), plus r source("https://…") and cpp scanf("%s"). Each returned a clean
    # `pass` on a file that contained the primitive in plain sight.
    #
    # I first tried to SNIFF which rules are literal-dependent by looking for a quote class in
    # the pattern. That sniffer is itself an enumeration and it MISSED the cpp scanf rule,
    # whose signal is `%s` with no quote in the pattern at all. So there is no marking step to
    # forget and no list to keep correct: EVERY rule is matched against BOTH passes and fires
    # on either. Comments are stripped in both, so prose in a comment still cannot match; only
    # a primitive spelled inside a string literal is newly reachable. That residual cost was
    # MEASURED across the whole library, not assumed -- see the round-17 delta.
    # Matching pass 2 outright is TOO WIDE and the negative arms proved it: it resurrected
    # `eval` written INSIDE a string, the literal half of a JS template, and the contents of a
    # C++ raw string -- three guarantees earned in earlier rounds. The precise invariant is
    # not "literals are visible" but: A MATCH MUST START IN CODE. `createHash("md5")` starts
    # at `createHash`, which is code; a bare `eval(` inside a string starts inside the literal.
    # Both passes blank IN PLACE, so offsets align and a position survived pass 1 exactly when
    # code[i] == lit[i]. No rule list, no marking, nothing to forget.
    lit, lit_ok = strip_noncode(text, lane, keep_strings=True)
    lit_ok = lit_ok and len(lit) == len(code)      # alignment is the premise; never assume it

    # ⛔ 6E ROUND 17 F1 — the restored-import region makes the invariant VACUOUS. strip_noncode
    # ends with `stripped + "\n" + _import_lines(text, lane)`, appending the ORIGINAL import /
    # require lines (round-2 F5: a Go import path IS a string literal and is code). Both passes
    # append the SAME text, so throughout that region code[i] == lit[i] unconditionally and
    # `starts in code` is true of ANYTHING there. Bare-substring rules then fired on a path that
    # merely MENTIONS the name -- 6E measured both live:
    #     require('./docs/child_process_notes')   -> flag "child_process"
    #     import "example.com/old/os/exec-wrapper" -> flag "os/exec"
    # A false FINDING, the direction this tool has spent seventeen rounds refusing. The restore
    # itself must stay; it is pass 2's extra reach over that region that must not. A genuine
    # import still fires through `re.search(pat, code)`, because the restored lines are IN code.
    #
    # My negative arms could not have caught it: they are python-only, and python has no
    # _IMPORT_LINE restore -- so the class is structurally invisible to every arm I wrote.
    # I first "fixed" 6E's finding by excluding the restored-import region from pass 2. That
    # guard was DECORATION and I am recording why rather than leaving it in to look thorough:
    # pass 1 contains the restored lines IDENTICALLY, so any match there is already found by
    # `re.search(pat, code)` and excluding it from pass 2 changes no verdict. The false
    # positives were never about the two passes -- measured against commit 2cba6d4, both fired
    # before round 17 existed. The defect was the RULES matching a bare substring of a path.
    def _starts_in_code(pat):
        for m in re.finditer(pat, lit):
            i = m.start()
            # 4Q round 17: a blanked literal becomes SPACES, so a literal that CONTAINS a space
            # has code[i] == lit[i] == " " and reads as code. No rule starts with \s today, so
            # this was fragility rather than a defect -- closed here instead of left as a note.
            if i < len(code) and code[i] == lit[i] and not lit[i].isspace():
                return True
        return False

    hit = [(pat, label) for pat, label in table[lane]
           if re.search(pat, code) or (lit_ok and _starts_in_code(pat))]
    if hit:
        return (name, "flag", ", ".join(sorted({l for _, l in hit})), [p for p, _ in hit])
    return (name, "pass", ok_detail, [])


# ================================================================= per-file checks
def check_dangerous(text, lane, tree):
    n, st, d, _ = _text_check(text, lane, DANGEROUS, "dangerous_primitives",
                              "no listed primitive")
    return (n, st, d)


# ⛔ EVERY branch must require a NON-EMPTY argument. `random.seed()` with empty parens
# seeds from OS entropy and is NOT reproducible -- 4Q F1.
_ARG = r"\s*\(\s*[^)\s]"
SEEDED = re.compile(r"random\.seed" + _ARG + r"|np\.random\.seed" + _ARG
                    + r"|default_rng\s*\(\s*\d|Random\s*\(\s*\d|srand\s*\(\s*\d"
                    + r"|StdRng::seed_from_u64|rand\.New\s*\(\s*rand\.NewSource\s*\(\s*\d"
                    + r"|set\.seed" + _ARG)


# Only these PATTERNS describe a generator a seed can actually make reproducible.
# `random_device` is hardware entropy and is NOT one of them -- 4Q F4.
SEEDABLE_PATS = {r"\brandom\.", r"\bnp\.random\.", r"Math\.random", r"\brand\s*\(",
                 r"math/rand", r"\brand::", r"\brunif\s*\(|\brnorm\s*\(|\bsample\s*\("}


def check_determinism_markers(text, lane, tree):
    name, status, detail, pats = _text_check(text, lane, NONDET, "determinism_markers",
                                             "no random/time/network marker", want_pats=True)
    if status == "flag":
        # ⛔ 4Q ROUND 17 F1 — I fixed the ENGINE and left a caller that bypasses it. SEEDED ran
        # on pass 1 alone, and SEEDED's whole point is the seed VALUE: `random.seed("42")` is
        # reproducible, but blanking the literal leaves `random.seed(    )` and `[^)\s]` cannot
        # match spaces. So a seeded, reproducible pattern was reported as needing judgement --
        # a false FLAG, the same dead-by-construction class one function over.
        code, ok = strip_noncode(text, lane)
        _slit, _sok = strip_noncode(text, lane, keep_strings=True)
        _sok = _sok and len(_slit) == len(code)
        _seeded = SEEDED.search(code) or (_sok and any(
            m.start() < len(code) and code[m.start()] == _slit[m.start()]
            and not _slit[m.start()].isspace()
            for m in SEEDED.finditer(_slit)))
        if ok and _seeded:
            # filter by PATTERN IDENTITY, never by substring of the human label
            left = [p for p in pats if p not in SEEDABLE_PATS]
            labels = sorted({l for pt, l in NONDET[lane] if pt in left})
            if not left:
                return (name, "pass", f"RNG is SEEDED ({detail}) — reproducible")
            return (name, "flag", ", ".join(labels) + " (a seedable RNG marker is seeded, "
                                                      "these are not)")
    return (name, status, detail)


def check_abs_paths(text, lane, tree):
    # This check intentionally looks for paths inside STRING LITERALS, so it keeps strings
    # -- but a quoted path inside a COMMENT is prose, not a hardcoded path (4Q round 2, F5).
    code, ok = strip_noncode(text, lane, keep_strings=True)
    if not ok:
        return ("hardcoded_abs_path", "unverifiable",
                _u(_strip_fail_reason(lane),
                   f"could not strip lane '{lane}' — a path in a comment would have counted "
                   "as a hardcoded path" if lane != "python" else
                   "python source did not tokenise, so no path could be measured"))
    text = code
    m = ABS_PATH.search(text)
    if m:
        return ("hardcoded_abs_path", "flag", f"literal absolute path {m.group(0)[:60]}")
    return ("hardcoded_abs_path", "pass", "no absolute path literal")


def check_hollow(text, lane, tree):
    """C9 — nothing is actually there. Python is decided on the AST; other lanes on the
    presence of ANY assertion construct, which is weaker, so they are flagged not failed."""
    if lane == "python":
        if tree is None:
            return ("hollow", "fail",
                _u("PARSE_FAIL", "python source did not parse — a malformed file is "
                   "measured-and-wrong, not unmeasurable (6E 2026-08-30)"))
        asserts = [n for n in ast.walk(tree) if isinstance(n, ast.Assert)]
        calls = [n for n in ast.walk(tree) if isinstance(n, ast.Call)]
        defs = [n for n in ast.walk(tree)
                if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef))]
        if not asserts and not calls:
            return ("hollow", "fail", "no asserts and no calls anywhere — the file does nothing")
        if not asserts:
            return ("hollow", "flag",
                    f"no assert statements ({len(defs)} def(s), {len(calls)} call(s)) — "
                    "nothing in the file states what it guarantees")
        return ("hollow", "pass", f"{len(asserts)} assert(s), {len(defs)} def(s)")
    pat = ASSERT_PAT.get(lane)
    if pat is None:
        return ("hollow", "unverifiable",
                _u("NO_ASSERT_GRAMMAR", f"no assertion grammar for lane '{lane}'"))
    code, ok = strip_noncode(text, lane)
    if not ok:
        return ("hollow", "unverifiable",
                _u(_strip_fail_reason(lane),
                   f"could not strip lane '{lane}' — an assertion inside a comment would "
                   "have counted as one -- 4Q F3" if lane != "python" else
                   "python source did not tokenise, so no assertion could be measured"))
    n = len(re.findall(pat, code))
    if n == 0:
        return ("hollow", "flag", f"no assertion construct found in CODE (looked for /{pat}/)")
    return ("hollow", "pass", f"{n} assertion construct(s) in code")


# ============================================ C4 for the five non-python lanes
# ⛔ WHAT THIS CAN AND CANNOT DECIDE. The python arm walks an AST and knows an assert's test
# contains no Name/Call/Attribute/Subscript. Outside python there is no AST here, so the rule
# is deliberately NARROWER: an assertion is judged ONLY when its tested expression is
# LITERAL-ONLY (numbers, strings, true/false, operators — no identifier, no call). Anything
# else is counted live and nothing is claimed about it. That direction is the safe one: the
# expensive error is a FALSE accusation against a good pattern, and a literal-only expression
# cannot be a real test. A `pass` therefore means "no literal-only assertion that can never
# fire was found", which is a measurement, not a fallback.
_LIT_TOKEN = re.compile(r"""
      \b\d+(?:\.\d+)?(?:[uUlLfF]+)?\b        # numeric literal, C/Rust suffixes allowed
    | \b(?:true|false|TRUE|FALSE|True|False)\b
    | [-+*/%()<>=!&|^~,\s]                   # operators, punctuation, whitespace
""", re.X)
_C4_NORM = (("!==", "!="), ("===", "=="), ("&&", " and "), ("||", " or "))
# The call/macro heads that carry a tested expression, per lane.
_C4_HEAD = {
    "cpp":  re.compile(r"\b(?:assert|static_assert|\w*_ASSERT\w*)\s*(?=\()"),
    "rust": re.compile(r"\b(?:debug_)?assert(_eq|_ne)?!\s*(?=[\(\[])"),
    "r":    re.compile(r"\bstopifnot\s*(?=\()"),
    "javascript": re.compile(r"\b(?:assert|console\.assert)\s*(?=\()"),
}
# go and js also spell an assertion as `if <cond> { ...exit/throw... }` (see ASSERT_PAT's go
# note: os.Exit(1) is the canonical go assertion and there is no assert statement).
_C4_IF = {
    "go": (re.compile(r"\bif\s+([^{\n]+?)\s*\{"),
           re.compile(r"\bos\.Exit\s*\(\s*[1-9]|\bpanic\s*\(|\blog\.Fatal")),
    "javascript": (re.compile(r"\bif\s*\(([^{\n]+?)\)\s*\{"),
                   re.compile(r"\bthrow\s+new\s+\w*(?:Error|Exception)")),
}


def _c4_literal_only(expr: str) -> bool:
    return expr.strip() != "" and not _LIT_TOKEN.sub("", expr).strip()


def _c4_fold(expr: str):
    """True/False if the literal-only expression folds; None if it cannot be evaluated."""
    e = expr
    for a, b in _C4_NORM:
        e = e.replace(a, b)
    e = re.sub(r"\b(?:true|TRUE)\b", "True", e)
    e = re.sub(r"\b(?:false|FALSE)\b", "False", e)
    e = re.sub(r"(?<=\d)[uUlLfF]+\b", "", e)          # 1u / 2L / 3.0f
    e = re.sub(r"!(?!=)", " not ", e)
    try:
        return bool(eval(compile(ast.parse(e.strip(), mode="eval"), "<a>", "eval"),
                         {"__builtins__": {}}, {}))
    except Exception:
        return None


def _c4_args_at(text: str, open_idx: int):
    """Split the argument list starting at text[open_idx]=='(' on TOP-LEVEL commas."""
    depth, i, start, args = 0, open_idx, open_idx + 1, []
    while i < len(text):
        c = text[i]
        if c in "\"'":
            q, i = c, i + 1
            while i < len(text) and text[i] != q:
                i += 2 if text[i] == "\\" else 1
        elif c == "(":
            depth += 1
        elif c == ")":
            depth -= 1
            if depth == 0:
                args.append(text[start:i])
                return args, i
        elif c == "," and depth == 1:
            args.append(text[start:i]); start = i + 1
        i += 1
    return None, -1


def _c4_sites(code: str, lane: str):
    """Every assertion site as (expression, POLARITY).

    ⛔ THE POLARITY INVERTS THE VERDICT — reversing it would call every good guard vacuous
    and every vacuous one good:
      "assert"  `assert(E)` / `stopifnot(E)` — PASSES when E is true, so it can never fire
                when E folds TRUE.
      "guard"   `if (E) { throw / os.Exit(1) }` — FIRES when E is true, so it can never fire
                when E folds FALSE.
    """
    out = []
    head = _C4_HEAD.get(lane)
    if head:
        for m in head.finditer(code):
            args, _ = _c4_args_at(code, m.end())
            if not args:
                continue
            if lane == "rust" and m.group(1) in ("_eq", "_ne") and len(args) >= 2:
                out.append((f"({args[0]}) {'==' if m.group(1) == '_eq' else '!='} ({args[1]})",
                            "assert"))
            else:
                out.append((args[0], "assert"))
    pair = _C4_IF.get(lane)
    if pair:
        ifpat, bodypat = pair
        for m in ifpat.finditer(code):
            if bodypat.search(code[m.end():m.end() + 300]):
                out.append((m.group(1), "guard"))
    return out


def _assert_nonvacuous_lexical(text, lane):
    code, ok = strip_noncode(text, lane, keep_strings=True)
    if not ok:
        return ("assert_nonvacuous", "unverifiable",
                _u(_strip_fail_reason(lane),
                   f"could not strip lane '{lane}' — an assertion inside a COMMENT would "
                   "count, so nothing was measured"))
    sites = _c4_sites(code, lane)
    if not sites:
        return ("assert_nonvacuous", "skip", "no asserts — reported by the hollow check")
    dead, markers, live = [], [], 0
    for expr, pol in sites:
        if not _c4_literal_only(expr):
            live += 1; continue
        val = _c4_fold(expr)
        if val is None:
            live += 1; continue
        vacuous = (val is True) if pol == "assert" else (val is False)
        (dead if vacuous else markers).append(expr.strip()[:60])
    if dead:
        return ("assert_nonvacuous", "fail" if not live else "flag",
                f"{len(dead)} assertion(s) that can never fire: {sorted(dead)}"
                + ("" if live else " — and there are no live assertions at all"))
    if not live and not markers:
        return ("assert_nonvacuous", "fail", "no assert can fire")
    return ("assert_nonvacuous", "pass",
            f"{live} live assert(s), {len(markers)} failure-path marker(s)")


def check_assert_nonvacuous(text, lane, tree):
    """C4 — an assert that cannot fail is decoration. Decidable on the python AST: an assert
    whose test contains no Name/Call/Attribute/Subscript is comparing literals to literals."""
    if lane != "python":
        return _assert_nonvacuous_lexical(text, lane)
    if tree is None:
        return ("assert_nonvacuous", "fail",
                _u("PARSE_FAIL", "python source did not parse — a malformed file is "
                   "measured-and-wrong, not unmeasurable (6E 2026-08-30)"))
    asserts = [n for n in ast.walk(tree) if isinstance(n, ast.Assert)]
    if not asserts:
        return ("assert_nonvacuous", "skip", "no asserts — reported by the hollow check")
    live, dead, markers = [], [], []
    for a in asserts:
        dynamic = any(isinstance(x, (ast.Name, ast.Call, ast.Attribute, ast.Subscript))
                      for x in ast.walk(a.test))
        if dynamic:
            live.append(a.lineno)
            continue
        try:
            # `dynamic` is False, so the test provably contains no Name/Call/Attribute/
            # Subscript -- only literals and operators. literal_eval cannot fold a
            # COMPARISON (`assert 1 == 1` raised ValueError and was scored live), so
            # compile and evaluate it in an empty namespace instead.
            const = bool(eval(compile(ast.Expression(a.test), "<assert>", "eval"),
                              {"__builtins__": {}}, {}))
        except Exception:
            live.append(a.lineno)          # cannot fold it -> do not accuse it
            continue
        # `assert False, "..."` can never PASS: it is an unreachable-marker, the canonical
        # way to assert an expected exception WAS raised. That is the failure path, not a
        # vacuous assert. Only an always-TRUE assert can never fire.
        (markers if not const else dead).append(a.lineno)
    if dead:
        st = "fail" if not live else "flag"
        return ("assert_nonvacuous", st,
                f"{len(dead)} always-true assert(s) at lines {sorted(dead)} can never fire"
                + ("" if live else " — and there are no live asserts at all"))
    if not live and not markers:
        return ("assert_nonvacuous", "fail", "no assert can fire")
    return ("assert_nonvacuous", "pass",
            f"{len(live)} live assert(s), {len(markers)} failure-path marker(s)")


def _is_main_guard(t) -> bool:
    """`if __name__ == "__main__":` on either side. The OPERATOR matters: `!=` runs its body
    ON IMPORT and is the opposite of a guard -- 4Q F2."""
    if not isinstance(t, ast.Compare) or len(t.ops) != 1:
        return False
    if not isinstance(t.ops[0], ast.Eq):
        return False
    sides = [t.left, t.comparators[0]]
    has_name = any(isinstance(x, ast.Name) and x.id == "__name__" for x in sides)
    has_main = any(isinstance(x, ast.Constant) and x.value == "__main__" for x in sides)
    return has_name and has_main


def check_importable(text, lane, tree):
    """C5 — usable as a library, not just runnable as a script. Python-decidable."""
    if lane != "python":
        return ("importable", "unverifiable",
                _u("NON_PYTHON_AST", f"decidable on the python AST only; lane is '{lane}'"))
    if tree is None:
        return ("importable", "fail",
                _u("PARSE_FAIL", "python source did not parse — a malformed file is "
                   "measured-and-wrong, not unmeasurable (6E 2026-08-30)"))
    defs = [n for n in tree.body
            if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef))]
    side = []
    for n in tree.body:
        # ⛔ 6E round 15: a DECORATOR is a module-level call that runs at import — the
        # canonical import side effect (@app.route, @register). This loop skipped every
        # FunctionDef and ClassDef whole, so a decorated def reported "no import side
        # effects" while importing it populated a registry. The prose was not merely
        # incomplete, it was FALSE, and the same effect written as a top-level
        # registry.append(...) was flagged. Two spellings of one thing cannot get two
        # verdicts.
        if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            # ⛔ TRIAGE, 4Q. Round 15 made EVERY decorator an import side effect. True for
            # `@app.route(...)` and `@atexit.register`; FALSE for `@dataclass`, which is a
            # pure transformer. It flagged 34 patterns on nothing but `@dataclass` /
            # `@contextmanager` -- a real fix that opened a wider false hole, invisible until
            # somebody read the FLAG set BY SHAPE instead of counting it.
            #
            # 4Q's discriminator is structural, so there is no name list to keep correct:
            #   Name            @dataclass              pure: takes the object, returns one
            #   Call(Name)      @dataclass(frozen=True) pure, just configured
            #   Attribute       @atexit.register        references an EXTERNAL object
            #   Call(Attribute) @app.route("/x")        calls a method ON an external object
            # DECLARED COST (4Q): `@functools.lru_cache(...)` is Call(Attribute) and pure, so
            # it still flags. Separating a module from an instance needs import tracking. The
            # verdict is `flag` (judgement), not `fail`, and the shape needs no maintenance.
            # ⛔ I OVERRULED 4Q'S DISCRIMINATOR AND 6E'S OWN PROBES ARE WHY. 4Q proposed
            # "bare Name = pure": `@dataclass` is a Name, so skip it. But `@register` is ALSO
            # a bare Name and it genuinely CALLS register(f) at import -- 6E's round-15
            # finding, with two probes that failed the moment I applied the shape rule.
            # EVERY decorator executes; `dataclass(cls)` returns a new class and touches
            # nothing, `register(f)` appends to a registry. The AST shape cannot tell them
            # apart, so the discriminator is not shape -- it is WHICH TRANSFORMER.
            #
            # That makes this an enumeration, and 6E drew the line in round 18: a bounded
            # EXTERNAL fact (like `sys.stdlib_module_names`) is the legitimate kind; a table
            # of spellings someone thought of is not. These are the stdlib's pure decorators.
            # DECLARED COST: a user-defined decorator that happens to be named `dataclass`
            # would be wrongly cleared. Unlike a spelling table, this list has an external
            # authority to check it against.
            for _dec in n.decorator_list:
                _base = _dec.func if isinstance(_dec, ast.Call) else _dec
                _nm = (_base.id if isinstance(_base, ast.Name)
                       else _base.attr if isinstance(_base, ast.Attribute) else None)
                if _nm in PURE_DECORATORS:
                    continue
                side.append(_dec.lineno)
            continue
        if isinstance(n, (ast.Import, ast.ImportFrom, ast.Assign, ast.AnnAssign, ast.Pass)):
            continue
        if isinstance(n, ast.Expr) and isinstance(n.value, ast.Constant):
            continue                      # docstring
        if isinstance(n, ast.If) and _is_main_guard(n.test):
            # The guard BODY does not run on import -- but its elif/else DOES.
            for sub in n.orelse:
                side.append(sub.lineno)
            continue
        side.append(n.lineno)
    if not defs:
        return ("importable", "flag", "no importable function or class — script only")
    if side:
        return ("importable", "flag",
                f"module-level statements run on import at lines {side[:8]}")
    return ("importable", "pass",
            f"{len(defs)} importable def(s), no import side effects "
            "(module-level statements AND decorators both checked — 6E round 15)")


_STDLIB = getattr(sys, "stdlib_module_names", frozenset())


# ================================================== C6 for the five non-python lanes
# ⛔ WHY A LEXICAL SCAN IS HONEST HERE. The python arm walks an AST; these walk regexes over
# COMMENT-STRIPPED-BUT-STRING-KEPT source, because in go/js/R the import target IS a string
# literal — stripping literals (the default) deletes the very thing being measured.
#
# ⛔ WHAT EACH RULE CAN AND CANNOT DECIDE — stated so a `pass` is never read as more than it is:
#   go     EXACT. The language defines it: a first path segment containing "." is a remote
#          module path; everything else is the standard library.
#   rust   `use X::…` / `extern crate X` only. A bare path call (`rand::random()`) with no
#          `use` is NOT counted — conservative, so this under-reports rather than invents.
#   cpp    angle-bracket includes against the C++17 + C standard header set. `#include "x"`
#          is local by definition and is not counted.
#   js     require()/import specifiers; "./" and "../" are local, "node:" is builtin.
#   r      library()/require()/requireNamespace() and `pkg::` namespacing.
_CPP_STD_HEADERS = frozenset("""
algorithm any array atomic bitset charconv chrono codecvt complex condition_variable deque
exception execution filesystem forward_list fstream functional future initializer_list iomanip
ios iosfwd iostream istream iterator limits list locale map memory memory_resource mutex new
numeric optional ostream queue random ratio regex scoped_allocator set shared_mutex sstream
stack stdexcept streambuf string string_view strstream system_error thread tuple type_traits
typeindex typeinfo unordered_map unordered_set utility valarray variant vector version
cassert cctype cerrno cfenv cfloat cinttypes climits clocale cmath csetjmp csignal cstdarg
cstddef cstdint cstdio cstdlib cstring ctime cuchar cwchar cwctype cstdalign cstdbool
assert.h ctype.h errno.h fenv.h float.h inttypes.h limits.h locale.h math.h setjmp.h signal.h
stdarg.h stddef.h stdint.h stdio.h stdlib.h string.h time.h wchar.h wctype.h
unistd.h sys/wait.h sys/types.h sys/stat.h sys/mman.h fcntl.h pthread.h dlfcn.h sys/time.h
# ⛔ 4Q ROUND 20 FINDING 1. `#include <arpa/inet.h>` was flagged as a third-party package.
# It is POSIX.1-2001, shipped with every POSIX OS -- a system header, not a dependency.
# The omission was not one header but a whole FAMILY: sockets, terminals, users, signals.
arpa/inet.h netdb.h netinet/in.h netinet/tcp.h sys/socket.h sys/un.h sys/select.h
sys/ioctl.h sys/uio.h sys/resource.h sys/utsname.h sys/file.h sys/param.h sys/sysctl.h
poll.h termios.h pwd.h grp.h glob.h fnmatch.h regex.h dirent.h libgen.h syslog.h utime.h
sched.h semaphore.h aio.h spawn.h iconv.h langinfo.h monetary.h nl_types.h search.h
strings.h sys/statvfs.h sys/times.h sys/wait.h ucontext.h wordexp.h ftw.h tar.h cpio.h
""".split())
_NODE_BUILTINS = frozenset("""
assert async_hooks buffer child_process cluster console constants crypto dgram diagnostics_channel
dns domain events fs http http2 https inspector module net os path perf_hooks process punycode
querystring readline repl stream string_decoder timers tls trace_events tty url util v8 vm
worker_threads zlib
""".split())
_R_BASE_PKGS = frozenset("""
base compiler datasets grDevices graphics grid methods parallel splines stats stats4 tcltk
tools utils
""".split())
_RUST_LOCAL_ROOTS = frozenset({"std", "core", "alloc", "crate", "self", "super"})


def _deps_cpp(code):
    hs = set(re.findall(r"#\s*include\s*<([^>]+)>", code))
    # ⛔ 4Q ROUND 21 FINDING 6 — ADOPTED AS A STRUCTURAL GUARD, NOT AS A CATCH.
    # MEASURED 2026-09-02: 0 of 420 cpp files in the library use the quote form, so this
    # changes ZERO records today and must not be reported as having caught anything.
    #
    # ⚠️ AND IT IS NARROWER THAN 4Q PROPOSED, because adopting the finding as written broke
    # an existing probe: `#include "local_helper.h"` must stay SILENT, and my first pass
    # flagged it. The probe was right and the reasoning I wrote to justify the change ("a
    # single-file pattern has no sibling, so a quote include must be external") proved too
    # much -- it makes a missing local header into a dependency, which it is not.
    # THE BRACKET FORM DOES NOT DECIDE. What decides is whether the header is named by a
    # PACKAGE-QUALIFIED PATH: third-party C/C++ headers are conventionally included as
    # `openssl/sha.h`, `boost/asio.hpp`, `gtest/gtest.h`. A bare `foo.h` in quotes is a
    # local header (possibly a broken reference, but that is not this check's class).
    hs |= {h for h in re.findall(r'#\s*include\s*"([^"]+)"', code) if "/" in h}
    return hs, {h for h in hs if h not in _CPP_STD_HEADERS}


def _deps_go(code):
    paths = set()
    for m in re.finditer(r"import\s*\(([^)]*)\)", code, re.S):
        paths |= set(re.findall(r'"([^"]+)"', m.group(1)))
    paths |= set(re.findall(r'import\s+(?:[\w.]+\s+)?"([^"]+)"', code))
    # ⛔ REGRESSION CAUGHT BY 6E's CORPUS, 2026-09-02, minutes after 4Q's F2/F4 fix landed.
    # Stripping string literals blanks the BODY of a grouped `import ( ... )`, and
    # _IMPORT_LINE re-appends those paths as BARE quoted lines at the end of the file —
    # belonging to neither the block regex nor the single-import regex. Result: a real
    # third-party import in the grouped form (which is the IDIOMATIC form) reported
    # "0 import(s), all standard". My own check of the fix used a single-line import and
    # missed it entirely; re-running the corpus is what found it.
    # A bare quoted line is what the RESTORE produces, and it is not valid go statement
    # syntax otherwise, so reading it here does not reopen the prose hole F2/F4 closed.
    # ⛔ 4Q ROUND 21 FINDING 1: `e "github.com/pkg/errors"` is an ALIASED grouped import and
    # is idiomatic Go. The alias sits between the leading whitespace and the quote, so the
    # bare-path form below missed it. My round-20 fix was verified with the unaliased form
    # only -- the same "I tested the form I happened to type" defect, one round later.
    # The optional prefix covers an alias, a dot import (`. "fmt"`) and a blank import
    # (`_ "net/http/pprof"`).
    paths |= set(re.findall(r'^[ \t]*(?:[\w.]+[ \t]+)?"([^"]+)"[ \t]*(?://.*)?$', code, re.M))
    return paths, {p for p in paths if "." in p.split("/")[0]}


def _deps_rust(code):
    # ⛔ 4Q ROUND 20 FINDING 5: `use ::serde::Deserialize;` is valid, crate-relative Rust.
    # The character class excluded ':' so the leading `::` form matched nothing and a real
    # third-party crate reported "0 import(s), all standard".
    cs = set(re.findall(r"\buse\s+(?:::)?([A-Za-z_][A-Za-z0-9_]*)\s*(?:::|;)", code))
    cs |= set(re.findall(r"\bextern\s+crate\s+([A-Za-z_][A-Za-z0-9_]*)", code))
    # ⛔ KNOWN LIMITATION, 4Q ROUND 21 FINDING 7 — MEASURED AND REJECTED, do not re-propose.
    # In Rust 2018+ a crate is reachable at the root without `use`, so
    # `serde_json::from_str(...)` with no `use` line is invisible here. The obvious cure is
    # R's trick -- a `([a-z][a-z0-9_]*)::` root regex -- and it is unusable: MEASURED
    # 2026-09-02 it matches 120 of 200 rust files, and the roots it returns are
    # collections 51 · sync 28 · thread 25 · u32 22 · atomic 18 · collect 10 · hint 9 —
    # fragments of `std::collections::HashMap`, `u32::MAX` and `.collect::<Vec<_>>()`
    # turbofish, not crates. ~120 false flags. A signal that cannot separate true from
    # false must not decide verdicts (the near-duplicate ruling, 6E 2026-08-30).
    return cs, {c for c in cs if c not in _RUST_LOCAL_ROOTS}


# ⛔ MEASURED against an EXTERNAL oracle, 2026-09-02: 978 real .js files across 426 npm
# packages, scoring this rule's third-party set against each package's OWN package.json
# `dependencies`. Agreement 726, false negatives 0. But 32 of the 56 disagreements were
# junk this rule INVENTED, in three classes my own fixtures could never have produced:
#   18  `from '${rawId}'` — a `from '...'` sitting inside a TEMPLATE LITERAL error message
#    8  `from ', path.call(print$1, '` — the word `from` inside ordinary quoted prose
#    6  `#minpath` — Node SUBPATH IMPORTS, which resolve to a LOCAL file, not a package
# The cure is not a tighter `from` regex (the text is genuinely ambiguous) but a shape test:
# a string that CANNOT be an npm specifier is not a dependency. Re-scored after: agreement
# 726 (unchanged), noise 56 -> 24, false negatives still 0. The remaining 24 are real
# packages npm HOISTED to a parent node_modules — an undeclared dependency is a true finding.
_NPM_SPECIFIER = re.compile(r"^(?:@[a-z0-9][\w.-]*/)?[a-z0-9][\w.-]*(?:/[\w.@-]+)*$", re.I)


def _deps_js(code):
    ms = set(re.findall(r"""require\s*\(\s*["']([^"']+)["']""", code))
    ms |= set(re.findall(r"""\bfrom\s+["']([^"']+)["']""", code))
    ms |= set(re.findall(r"""\bimport\s+["']([^"']+)["']""", code))
    # ⛔ 4Q ROUND 21 FINDING 4: dynamic `import("express")` is ES2020 and is how lazy loading
    # is written. `import\s+` requires whitespace and cannot match it. The `_NPM_SPECIFIER`
    # shape test below still guards against a template literal or prose being read as a
    # package, so widening the capture here does not reopen the F4 prose hole.
    ms |= set(re.findall(r"""\bimport\s*\(\s*["']([^"']+)["']""", code))
    third = set()
    for m in ms:
        if m.startswith((".", "/")):           # relative or absolute -> a local file
            continue
        # ⛔ A Node SUBPATH import ("#minpath") needs no clause of its own: _NPM_SPECIFIER
        # rejects a leading "#" already. MEASURED 2026-09-02 — a mutant deleting an explicit
        # "#" test SURVIVED, because the shape test below subsumed it. Two mechanisms for
        # one job means neither can be shown to work; the explicit clause is gone and the
        # subpath probe now exercises the shape test, which is the thing actually deciding.
        base = m[5:] if m.startswith("node:") else m
        if not _NPM_SPECIFIER.match(base):     # not a package name at all -> not a dependency
            continue
        if base.split("/")[0] not in _NODE_BUILTINS:
            third.add(m)
    return ms, third


def _deps_r(code):
    ps = set(re.findall(r"""\b(?:library|require|requireNamespace)\s*\(\s*["']?([A-Za-z][A-Za-z0-9._]*)""", code))
    ps |= set(re.findall(r"\b([A-Za-z][A-Za-z0-9._]*)::", code))
    return ps, {x for x in ps if x not in _R_BASE_PKGS}


DEPS_EXTRACT = {"cpp": _deps_cpp, "go": _deps_go, "rust": _deps_rust,
                "javascript": _deps_js, "r": _deps_r}


def _deps_nonpython(text, lane):
    """C6 outside python. Refuses to say `pass` when it could not read the source."""
    if lane not in DEPS_EXTRACT:
        return ("deps", "unverifiable",
                _u("NO_RULE_TABLE", f"no dependency rule for lane '{lane}'"))
    # ⛔ 4Q ROUND 20 FINDINGS 2 AND 4 — and this line is the opposite of what I first wrote.
    # It USED to pass keep_strings=True, reasoning that in go/js/R the import target IS a
    # string literal and stripping literals would delete the thing being measured. That
    # reasoning was wrong, because `_IMPORT_LINE` RESTORES whole import lines after the
    # strip: the genuine import survives either way. What keep_strings=True additionally
    # preserved was PROSE — `"Tip: use dplyr::filter"` and
    # `'To load express: from "express" import {Router}'` were both read as imports.
    # MEASURED after the flip: every real import still found (go/js/R, quoted and bare),
    # both prose cases clean. Stripping is strictly better here.
    code, ok = strip_noncode(text, lane, keep_strings=False)
    if not ok:
        return ("deps", "unverifiable",
                _u(_strip_fail_reason(lane),
                   f"could not strip lane '{lane}' — an import named in a COMMENT would "
                   "count, so nothing was measured"))
    allm, third = DEPS_EXTRACT[lane](code)
    if third:
        return ("deps", "flag", "third-party import(s) with no dependency manifest: "
                                + ", ".join(sorted(third)))
    return ("deps", "pass", f"{len(allm)} import(s), all standard")


def check_deps(text, lane, tree):
    """C6 — a third-party import runs here and crashes in the customer's clean environment.
    There is no dependency manifest in the library, so ANY third-party import is a flag."""
    if lane != "python":
        return _deps_nonpython(text, lane)
    if tree is None:
        return ("deps", "fail",
                _u("PARSE_FAIL", "python source did not parse — a malformed file is "
                   "measured-and-wrong, not unmeasurable (6E 2026-08-30)"))
    if not _STDLIB:
        return ("deps", "unverifiable",
                _u("NO_STDLIB_LIST", "sys.stdlib_module_names unavailable on this python"))
    typing_only = set()
    for n in ast.walk(tree):
        if isinstance(n, ast.If):
            t = n.test
            names = {x.id for x in ast.walk(t) if isinstance(x, ast.Name)}
            names |= {x.attr for x in ast.walk(t) if isinstance(x, ast.Attribute)}
            if "TYPE_CHECKING" in names:
                for sub in ast.walk(n):
                    if isinstance(sub, (ast.Import, ast.ImportFrom)):
                        typing_only.add(id(sub))
    mods = set()
    for n in ast.walk(tree):
        if id(n) in typing_only:
            continue          # runs only under a type checker, never at runtime -- 4Q F7
        if isinstance(n, ast.Import):
            mods |= {a.name.split(".")[0] for a in n.names}
        elif isinstance(n, ast.ImportFrom):
            if n.level == 0 and n.module:
                mods.add(n.module.split(".")[0])
        # ⛔ 4Q ROUND 21 FINDING 5: `importlib.import_module("numpy")` is an ast.Call, not an
        # ast.Import, so the walker never saw the module it names. `import importlib` alone
        # is stdlib and passed. Only a CONSTANT argument is read -- a computed module name
        # is genuinely undecidable here and is left alone rather than guessed at.
        elif isinstance(n, ast.Call):
            f = n.func
            named = ((isinstance(f, ast.Attribute) and f.attr == "import_module")
                     or (isinstance(f, ast.Name) and f.id == "import_module"))
            if named and n.args and isinstance(n.args[0], ast.Constant) \
                    and isinstance(n.args[0].value, str):
                mods.add(n.args[0].value.split(".")[0])
    third = sorted(m for m in mods if m not in _STDLIB and not m.startswith("_"))
    if third:
        return ("deps", "flag", "third-party import(s) with no dependency manifest: "
                                + ", ".join(third))
    return ("deps", "pass", f"{len(mods)} import(s), all stdlib")


def check_doc_behavior(text, lane, tree):
    """C7 — judgement-only (6E). Report whether there is even a description to judge."""
    if lane == "python":
        if tree is None:
            return ("doc_behavior", "fail",
                _u("PARSE_FAIL", "python source did not parse — a malformed file is "
                   "measured-and-wrong, not unmeasurable (6E 2026-08-30)"))
        d = ast.get_docstring(tree)
        if not d:
            # ⛔ 4Q R20 O2: the python branch uses ast.get_docstring and the INDEX uses the
            # ruler, which has a fallback for a string literal that is not the first statement.
            # Two methods, so they CAN disagree -- 0 files have that shape today (the 35 that
            # did were relocated in 95ebea9), but the fallback is kept because the shape is
            # easy to reintroduce and silent when it happens. Rather than pick one method, the
            # divergence is now REPORTED: a description a human can see and every docstring-
            # reading tool cannot is a more useful finding than a bare "no docstring".
            try:
                import build_patterns_index as _BPI
                _seen = _BPI.extract_claim_text(text, "python")
            except Exception:
                _seen = ""
            if _seen:
                return ("doc_behavior", "fail",
                        "a description is present but is NOT the module docstring — put an "
                        "import above it and __doc__ is None, so a human sees it and every "
                        "docstring-reading tool sees nothing (35 files were in this shape "
                        "until 95ebea9)")
            return ("doc_behavior", "fail", "no module docstring — nothing states what it does")
        return ("doc_behavior", "skip",
                f"docstring present ({len(d)} chars); code-vs-claim is judgement (6E C7), "
                "not tool-decidable")
    # ⛔ ROUND 19 — 824 patterns used to get NO_DOC_SLOT here, one of the four U1 sources that
    # made every non-python pattern UNVERIFIABLE. 6E's round-18 design answer: this check only
    # asks "is there a description to judge?", which is a LEXICAL fact per language, needing no
    # parser. It does not need writing either -- `build_patterns_index.extract_claim` is the
    # FROZEN RULER that already reads descriptions out of these exact files for
    # PATTERNS_INDEX.md, in all six languages. Growing a second description-finder here would
    # have produced two definitions of "has a description" that drift; this asks the same
    # question the index asks, so the audit and the index cannot disagree by construction.
    # A lane outside the six has no description slot DEFINED, so it stays U1 -- the coverage
    # matrix caught me answering `fail` for a cobol fixture, which would have claimed the file
    # has no description when the truth is that nobody has said where one would live.
    if lane not in LANES:
        return ("doc_behavior", "unverifiable",
                _u("NO_DOC_SLOT", f"no description slot is defined for lane '{lane}'"))
    try:
        import build_patterns_index as _BPI
        claim = _BPI.extract_claim_text(text, lane)
    except Exception as _e:                       # never let a helper import fake a measurement
        return ("doc_behavior", "unverifiable",
                _u("NO_DOC_SLOT", f"the frozen ruler could not be applied to '{lane}': {_e}"))
    if not claim:
        return ("doc_behavior", "fail",
                "no description in this language's slot — nothing states what it does "
                "(same ruler PATTERNS_INDEX.md uses)")
    return ("doc_behavior", "skip",
            f"description present ({len(claim)} chars); code-vs-claim is judgement (6E C7), "
            "not tool-decidable")


# ⛔ KEYED BY (stem, LANE), NOT BY STEM. 6E verified these by reading the PYTHON files;
# `atomic_snapshot` and `cow_backup` each also exist in Go, and a stem-only key handed the
# Go twins a finding nobody had checked -- 2 live false positives (4Q round 3, F4). Their
# Go similarity is 0.51 against 0.65 for Python: a different pair of files, unexamined.
KNOWN_FINDINGS = {
    ("atomic_snapshot", "python"): ("flag", "6E verified BY READING (2026-08-30): a genuine SEMANTIC "
                        "duplicate of cow_backup — both are temp-write + atomic-rename. No "
                        "shingle statistic can find this (containment 0.87 sits inside the "
                        "false-positive range 0.81-0.94), so it is recorded here rather "
                        "than lost to a silent NO_FINDING."),
    ("cow_backup", "python"): ("flag", "6E verified BY READING (2026-08-30): a genuine SEMANTIC "
                   "duplicate of atomic_snapshot — both are temp-write + atomic-rename. "
                   "Recorded because the detector cannot derive it."),
}


def check_known_findings(text, lane, tree, stem=None):
    """Findings a human or model verified by READING, which the tool cannot derive itself.
    Without this, a defect somebody already confirmed silently becomes a NO_FINDING."""
    hit = KNOWN_FINDINGS.get((stem, lane))
    if hit:
        return ("known_finding", hit[0], hit[1])
    return ("known_finding", "pass", "no hand-verified finding recorded for this pattern")


FILE_CHECKS = [check_hollow, check_assert_nonvacuous, check_importable, check_deps,
               check_dangerous, check_determinism_markers, check_abs_paths,
               check_doc_behavior]


# ================================================================= gate + determinism
def run_gate_twice(p: Path, repeat: int, timeout: int):
    """The gate check, plus C10's dynamic half. `run_gate` is library_verify's own runner —
    orphan-safe (start_new_session + killpg) and four-outcome honest."""
    v = LV.run_gate(p, timeout=timeout)
    kind, detail = LV.gate_outcome(v)
    status = {"pass": "pass", "fail": "fail", "skip": "unverifiable",
              "inconclusive": "unverifiable"}[kind]
    _gd = detail or f"verdict {v!r}"
    if status == "unverifiable":       # a missing toolchain and a HANG are different remedies
        _gd = _u("NO_TOOLCHAIN" if kind == "skip" else "HANG", _gd)
    gate = ("gate", status, _gd)
    if repeat < 2:
        return gate, ("determinism_repeat", "skip",
                      f"not requested (--repeat {repeat}); only the static marker scan ran")
    if p.suffix != ".py":
        return gate, ("determinism_repeat", "unverifiable",
                      _u("NO_REPEAT_RUNNER",
                         "repeat-run comparison implemented for python only"))
    if status != "pass":
        return gate, ("determinism_repeat", "skip", "gate did not pass; nothing to compare")
    outs = []
    for _ in range(repeat):
        try:
            r = subprocess.run([sys.executable, str(p)], capture_output=True, text=True,
                               timeout=timeout, start_new_session=True)
            outs.append(r.stdout)
        except Exception as e:
            return gate, ("determinism_repeat", "unverifiable",
                          _u("REPEAT_ERROR", f"repeat run failed: {e}"))
    if len(set(outs)) > 1:
        return gate, ("determinism_repeat", "fail",
                      f"{repeat} runs produced {len(set(outs))} different outputs")
    return gate, ("determinism_repeat", "pass", f"{repeat} runs, identical output")


# ================================================================= cross-file checks
IDENT = re.compile(r"[A-Za-z_][A-Za-z_0-9]*")
KEYWORDS = {"if", "else", "elif", "for", "while", "return", "def", "class", "import", "from",
            "in", "not", "and", "or", "is", "None", "True", "False", "try", "except",
            "finally", "with", "as", "pass", "break", "continue", "lambda", "yield", "raise",
            "int", "float", "str", "bool", "let", "fn", "func", "var", "const", "struct",
            "impl", "pub", "use", "package", "type", "range", "nil", "null", "function"}
SHINGLE_FLOOR = 20
# A shingle present in more than this fraction of a lane is shared scaffolding, not
# algorithm -- it is removed before any similarity is computed.
DF_FRACTION = 0.10


def _shingles(code: str):
    """Identifier-NORMALISED shingles. 6E predicted a renamed copy-paste falls under 0.75
    with literal tokens, and renames are the norm in a code library. Structure survives a
    rename; identifiers do not, so identifiers become a placeholder."""
    toks = []
    for m in re.finditer(r"[A-Za-z_][A-Za-z_0-9]*|[0-9]+|[^\s\w]", code):
        t = m.group(0)
        if IDENT.fullmatch(t) and t not in KEYWORDS:
            toks.append("ID")
        elif t.isdigit():
            toks.append("NUM")
        else:
            toks.append(t)
    return {tuple(toks[i:i + 5]) for i in range(max(0, len(toks) - 4))}


def duplicate_map(files, lane_of, root=None):
    """C8. Exact duplicates by normalised hash; near-duplicates by identifier-normalised
    5-shingle Jaccard, WITHIN a lane only (a python source and its cpp twin are not
    duplicates). Returns path -> (status, detail); a file below the shingle floor gets an
    explicit `skip`, never a `pass` claiming no near-duplicate exists -- 6E."""
    root = root or ROOT
    norm, sh = {}, {}
    for p in files:
        try:
            t = _norm_source(p.read_text(encoding="utf-8", errors="replace"), lane_of[p])
        except Exception:
            continue
        norm[p] = hashlib.sha256(t.encode()).hexdigest()
        code, _ok = strip_noncode(t, lane_of[p])
        sh[p] = _shingles(code)
    by_hash = defaultdict(list)
    for p, h in norm.items():
        by_hash[h].append(p)
    result = {}
    for h, group in by_hash.items():
        if len(group) > 1:
            for p in group:
                others = [str(q.relative_to(root)) for q in group if q is not p]
                result[p] = ("fail", "EXACT duplicate of " + ", ".join(others[:4]))
    by_lane = defaultdict(list)
    for p in files:
        if p in sh and p not in result:
            by_lane[lane_of[p]].append(p)
    for lane, ps in by_lane.items():
        # ⛔ DOCUMENT-FREQUENCY FILTER. Measured by 6E: all 91/91 javascript patterns share
        # one verbatim test harness, so identifier-normalised shingles made every pair in a
        # family look 75-100% identical -- ~98% false positives. A shingle that appears in a
        # large fraction of the lane is BOILERPLATE and carries no discriminating
        # information, so it is removed before comparison. Language-agnostic: it finds
        # whatever the shared scaffold happens to be, per lane, without naming it.
        df = defaultdict(int)
        for q in ps:
            for g in sh[q]:
                df[g] += 1
        cutoff = max(3, int(DF_FRACTION * len(ps)))
        sig = {q: {g for g in sh[q] if df[g] <= cutoff} for q in ps}
        big = [p for p in ps if len(sig[p]) >= SHINGLE_FLOOR]
        for p in ps:
            if p not in big:
                result[p] = ("skip", f"only {len(sig[p])} distinctive shingle(s) after "
                                     f"removing lane boilerplate (floor {SHINGLE_FLOOR}) — "
                                     "near-duplicate NOT compared")
        for i, a in enumerate(big):
            for b in big[i + 1:]:
                la, lb = len(sig[a]), len(sig[b])
                if min(la, lb) / max(la, lb) < 0.7:
                    continue
                inter = len(sig[a] & sig[b])
                j = inter / (la + lb - inter)
                if j >= 0.75:
                    for x, y in ((a, b), (b, a)):
                        if result.get(x, ("", ""))[0] != "fail":
                            result[x] = ("flag", "near-duplicate of "
                                                 f"{y.relative_to(root)} "
                                                 f"(jaccard {j:.2f} on boilerplate-filtered, "
                                                 f"identifier-normalised shingles)")
    return result


SOURCE_LANES = {"python", "r", "javascript"}
# ⛔ Only these lanes are REQUIRED to have a python/r source -- library_verify.py:643
# (`for tl in ("cpp", "go")`). A rust file with no source is a STANDALONE pattern, not an
# orphan. Calling it twin_orphan routes 191 healthy files to fix/quarantine -- 6E round 2.
SOURCE_REQUIRED_LANES = {"cpp", "go"}


def role_index(files, lane_of, manifest):
    """C3 precondition. A compiled-lane file is a TWIN of the python/r stem it shares, unless
    it is DECLARED native. A compiled file with neither is `twin_orphan` — library_verify's
    RED case — and triage should route it straight to fix or quarantine."""
    native = {k: set(v) for k, v in ((manifest or {}).get("native_patterns") or {}).items()}
    src_stems = defaultdict(set)
    for f in files:
        if lane_of[f] in ("python", "r"):
            src_stems[f.stem].add(lane_of[f])
    out = {}
    for f in files:
        lane, stem = lane_of[f], f.stem
        if lane in SOURCE_LANES:
            out[f] = ("source", None, False)
        elif stem in native.get(lane, ()):
            out[f] = ("native", None, False)
        elif stem in src_stems:
            out[f] = ("twin", stem, len(src_stems[stem]) > 1)
        elif lane in SOURCE_REQUIRED_LANES:
            out[f] = ("twin_orphan", None, False)
        else:
            out[f] = ("standalone", None, False)
    return out


def duplicate_check(status, detail):
    """Map duplicate_map's result to a per-record check. NEAR-duplicate is ADVISORY: it is
    recorded but must never change a verdict (precision 4/7 on 6E's hand-verified ground
    truth). EXACT duplication is hash equality and stays verdict-changing."""
    if status == "flag":
        return ("duplicate", "skip",
                "ADVISORY (does not affect the verdict): " + detail
                + " — near-duplicate precision is 4/7 on 6E's hand-verified ground truth;"
                  " treat as a lead, not a finding")
    return ("duplicate", status, detail)


def index_parity(files):
    """C12 — a pattern in the catalog but missing from PATTERNS_INDEX.md is undiscoverable."""
    idx = ROOT / "PATTERNS_INDEX.md"
    if not idx.exists():
        return None, "PATTERNS_INDEX.md is missing"
    txt = idx.read_text(encoding="utf-8", errors="replace")
    present = set()
    for p in files:
        # FULL RELATIVE PATH ONLY. `p.name in txt` was a substring match: "sha256.rs" is a
        # substring of "hmac_sha256.rs", so a missing file could be covered by a different
        # file's entry -- a false pass, and the library has three such collisions (4Q D3).
        if str(p.relative_to(ROOT)) in txt:
            present.add(p)
    return present, None


# ================================================================= driver
def _raises(fn, exc):
    """A probe helper: did this call fail LOUDLY, the way it is supposed to?"""
    try:
        fn()
    except exc:
        return True
    except Exception:
        return False
    return False


def triage_fields(checks, subclasses):
    """How this record should be ROUTED.

    6E design review 3 (2026-08-30) rewrote this, and the correction was to the DESTINATION,
    not the mechanism. My round-7 fix sent an unclaimed record to a human. 6E: an unclaimed
    record is not thin evidence about a pattern, it is a DROPPED REASON CODE or a MISSING
    ROUTING RULE -- a defect in this tool. A human cannot fix either. That is Ver's finding 5
    one level deeper, and I wrote it twelve hours after quoting Ver's finding 5 at 4Q.

    Two changes follow:

    * the claim test is PER CHECK, not per record, so `which rule claimed this` is answerable
      for each check instead of being a single boolean for the whole file;
    * the three things `needs_human_judgement` used to mean are three fields. It survives
      only as the union of the two that really are human work, and NEVER includes a tool
      defect, so an old consumer cannot count one as human work.
    """
    unknown = {c[1] for c in checks} - set(STATUSES)
    if unknown:
        raise KeyError("triage_fields: undeclared status %r -- add it to STATUSES and to "
                       "both partitions" % sorted(unknown))

    review = pathology = impl = False
    unclaimed, derived = [], set()
    for _n, _st, _d in checks:
        if _st in CLEAN_STATUSES:
            continue
        if _st in FINDING_STATUSES:
            review = True                      # R1: read the pattern, it may be broken
            continue
        _c, _sub = reason_of(_d)
        if _sub:
            derived.add(_sub)
        if _sub in ("U1", "U2"):
            impl = True                        # R2: build the analyser / provide the input
        elif _sub == "U3":
            pathology = True                   # R3: defect or documented edge case?
        else:
            # No rule claims this check. It is a tool defect and it is NAMED, so the reader
            # can tell "the U1 rule claimed this" from "nothing claimed it".
            unclaimed.append({"name": _n, "status": _st,
                              "reason_code": _c, "subclass": _sub})
    if derived != set(subclasses):
        # The caller and the router disagreeing about the same record is itself a defect.
        raise KeyError("triage_fields: caller passed subclasses %r but the check details "
                       "yield %r" % (sorted(subclasses), sorted(derived)))

    out = {
        "needs_review": review,
        "needs_pathology_triage": pathology,
        "needs_implementation": impl,
        # ⛔ NOT human work. Routes to whoever maintains this tool.
        "needs_tool_fix": bool(unclaimed),
        "unclaimed_checks": unclaimed or None,
        # derived union, kept for consumers of the old name. Deliberately EXCLUDES
        # needs_tool_fix: a tool defect must never be counted as human triage.
        "needs_human_judgement": review or pathology,
        "unowned_fallback": bool(unclaimed),
        "checks_measured": sum(1 for c in checks if c[1] in MEASURED_STATUSES),
        "checks_unmeasured": sum(1 for c in checks if c[1] in UNMEASURED_STATUSES),
        "checks_skipped": sum(1 for c in checks if c[1] in SKIPPED_STATUSES),
    }
    # 6E question 3: the verdict is about the PATTERN, the coverage is about the TOOL, and
    # they are orthogonal. Stated as how much could NOT be measured -- "unverified 1/8"
    # cannot be misread as a pass, where "measured 7/8" can. Same numbers, opposite reading.
    out["unverified"] = "%d/%d" % (out["checks_unmeasured"], len(checks))
    # ⛔ THE INVARIANT. Anything that is not a clean pass or a deliberate skip MUST reach
    # someone -- and now every one of them reaches a NAMED someone.
    out["needs_routing"] = any(c[1] not in CLEAN_STATUSES for c in checks)
    out["routed"] = review or pathology or impl or out["needs_tool_fix"]
    return out


def clip_evidence(text, limit=1200):
    """Ver finding 7: truncating mid-sentence with no marker hides that anything was cut."""
    mark = " …[TRUNCATED, see checks]"
    return text if len(text) <= limit else text[:limit - len(mark)] + mark


def _statuses_of(checks):
    # 4Q round 8, attack 5: this hardcoded the same status list a third time, so a new
    # status fell through to the CLEAN verdict -- the worst possible default.
    st = {c[1] for c in checks}
    unknown = st - set(STATUSES)
    if unknown:
        raise KeyError("undeclared status %r -- add it to STATUSES and to STATUS_VERDICT, "
                       "CLEAN_STATUSES or UNMEASURED_STATUSES" % sorted(unknown))
    return st


def finding_for(checks):
    """The FINDING axis: was anything actually found among the checks that RAN?

    Never returns a coverage answer. A check that could not run contributes NOTHING here --
    that is the whole point of the split. It cannot manufacture a finding, and it cannot
    hide one either, because the coverage axis is reported alongside it and is mandatory.
    """
    st = _statuses_of(checks)
    for _s, _v in STATUS_VERDICT.items():        # insertion order == severity order
        if _s in st:
            return _v
    if st <= set(SKIPPED_STATUSES):
        return "SKIP"
    return "NO_FINDING"


def coverage_for(checks):
    """The COVERAGE axis: how much of the suite could actually look at this file?

    FULL    every check that was requested returned a measurement.
    PARTIAL at least one check ran and at least one could not.
    NONE    nothing could be measured -- the only state that deserves the word
            UNVERIFIABLE, and the only one where the tool truly knows nothing.
    """
    st = _statuses_of(checks)
    unmeasured = st & set(UNMEASURED_STATUSES)
    measured = st & set(MEASURED_STATUSES)
    if not unmeasured:
        return "FULL"
    return "PARTIAL" if measured else "NONE"


# ================================================================= the WAIVER mechanism
# 6E, REPORT-6E-TRIAGE.md (2026-08-30): "WAIVE is an explicit, named, dated, instance-scoped
# record that stays visible and auditably separate from clean; the pattern is not marked good,
# it is marked ACCEPTED-WITH-REASON."
#
# ⛔ THE FAILURE THIS EXISTS TO PREVENT is a waiver that behaves like a pass. Five rules, all
# mechanical:
#   1. INSTANCE-SCOPED. Keyed (path, check, detail) -- never to a pattern's verdict -- so a
#      waiver covers one finding on one file, not "this pattern is fine".
#   2. STAYS LISTED. A waived finding keeps status `flag`. It is NEVER rewritten to pass and
#      NEVER changes the finding axis, so it cannot vanish into NO_FINDING.
#   3. THE REF IS MANDATORY AND ENFORCED. A waiver without a non-empty `ref` and `owner`
#      RAISES at load. Without that it is a silent NO_FINDING wearing a different name.
#   4. NOT THE BLANKET FLAG. Waivers are per-finding adjudication and do not ride
#      --acknowledge-unverifiable, which is about COVERAGE.
#   5. ROUND-TRIP VISIBLE. Re-running re-derives the waiver from the file; it reappears under
#      WAIVED with its ref every sweep, so the decision is part of the record.
#
# ⛔ AND THE SIXTH, WHICH IS MINE: A WAIVER PINS THE FILE IT WAS GRANTED AGAINST.
# 6E's rule 1 wants the raw flag back "if the code changes and a DIFFERENT unwrap appears".
# The detail string cannot deliver that -- `dangerous_primitives` reports WHICH primitive, not
# which site, so a second unwrap added to an already-waived file would be silently absorbed by
# the existing waiver. So each waiver records the file's sha256 at the moment it was granted.
# Any edit to that file makes the waiver STALE, the finding re-surfaces, and the stale waiver
# is reported. It fails CLOSED: an unrelated typo fix also forces a re-waive, which is cheap.
WAIVER_REQUIRED = ("path", "check", "detail", "file_sha256", "owner", "date", "ref")


def _file_sha256(p):
    import hashlib as _h
    return _h.sha256(Path(p).read_bytes()).hexdigest()


def load_waivers(path):
    """Read and VALIDATE the waiver ledger. Raises on any waiver that could act as a pass."""
    out = []
    if not Path(path).exists():
        return out
    for _n, _line in enumerate(Path(path).read_text(encoding="utf-8").splitlines(), 1):
        _line = _line.strip()
        if not _line or _line.startswith("#"):
            continue
        try:
            w = json.loads(_line)
        except Exception as e:
            raise ValueError("WAIVERS line %d is not JSON: %s" % (_n, e))
        missing = [k for k in WAIVER_REQUIRED if not str(w.get(k) or "").strip()]
        if missing:
            raise ValueError(
                "WAIVERS line %d is missing %r. A waiver without an owner, a date and a ref "
                "is an accepted risk nobody signed -- that is a silent NO_FINDING wearing a "
                "different name (6E). Refusing to load it." % (_n, missing))
        out.append(w)
    return out


def apply_waivers(records, waivers, root):
    """Attach waivers to the findings they name. Returns (applied, stale, orphan).

    Never mutates a check's status: a waived finding is still a finding. It records the
    adjudication beside it so a reader sees the finding AND the reason it was accepted.
    """
    index = {}
    for w in waivers:
        index.setdefault((w["path"], w["check"], w["detail"]), []).append(w)
    applied, stale, matched = 0, [], set()
    for r in records:
        for c in r.get("checks", []):
            if c.get("status") not in FINDING_STATUSES:
                continue
            key = (r.get("path"), c.get("name"), c.get("detail"))
            for w in index.get(key, []):
                matched.add(id(w))
                try:
                    live = _file_sha256(Path(root) / r["path"])
                except Exception:
                    live = None
                if live != w["file_sha256"]:
                    # The file moved under the waiver. The finding STANDS.
                    stale.append({"waiver": w, "live_sha256": live})
                    continue
                c["waived"] = {"owner": w["owner"], "date": w["date"], "ref": w["ref"],
                               "construct": w.get("construct")}
                r.setdefault("waived_checks", []).append(c["name"])
                r["disposition"] = "WAIVE"
                r["disposition_ref"] = "%s (%s, %s)" % (w["ref"], w["owner"], w["date"])
                applied += 1
    orphan = [w for w in waivers if id(w) not in matched]
    return applied, stale, orphan


def axes_of(rec):
    """Read the two axes off a record. They are NESTED under `axes` on purpose.

    ⛔ 6E, REPORT-6E-2AXIS.md (2026-08-30), reader path 2 -- the sharper of his two findings.
    When `finding` and `coverage` were top-level siblings, `finding` was a SEAM: any consumer
    that read it and dropped `coverage` renders 1285 records as NO_FINDING, silently merging
    the 556 that are FULLY measured with the 729 that are not. The old atomic UNVERIFIABLE
    could not be split off a record that way, so making `finding` first-class REINTRODUCED the
    exact failure the taxonomy exists to prevent -- "a silent NO_FINDING wearing a different
    name" -- as a field name rather than as a verdict.

    Nesting does not make a bad read impossible; it makes it LOUD. `jq '.finding'` now returns
    null instead of a reassuring word, which is a detectable error rather than a wrong answer.
    A consumer that reaches into `axes.finding` alone can still drop the gap, and that limit is
    stated rather than papered over. `verdict` stays top-level and compound, so the cheapest
    read of all is still the honest one.
    """
    a = rec.get("axes") or {}
    return a.get("finding"), a.get("coverage")


def coverage_exit_code(records, acknowledged):
    """Should this run be allowed to exit 0? Returns (code, the records that block it).

    ⛔ EXTRACTED BECAUSE A MUTANT SURVIVED. Disarming this guard while it lived inline in
    `main()` changed no probe: I had only ever checked the exit code BY HAND. That is the
    same defect Ver found in `triage_fields` -- a decision computed inline in main() is a
    decision no probe can reach -- and it recurred here because a hand-run FEELS like a test.

    6E's rule is what this enforces: a coverage gap is a FINDING, not a footnote. A run must
    not go green while any record is less than FULLY covered, unless a human says out loud
    that they looked. It deliberately does NOT read `disposition`.
    """
    blocking = [r for r in records if axes_of(r)[1] != "FULL"]
    return (2 if blocking and not acknowledged else 0), blocking


def verdict_for(checks):
    """The COMPOUND verdict -- always both axes, never one word.

    ⛔ WHY IT IS COMPOUND AND NOT A CHOICE BETWEEN THE TWO. A single word had to lie in one
    direction or the other: "UNVERIFIABLE" told the reader nothing was measured when 7 checks
    had run clean, and a bare "NO_FINDING" would have told them the suite was complete when
    3 checks never ran. Ver rejected PASS_WITH_GAPS for the second reason and was right; the
    fix is not to pick the other lie but to stop emitting a single word. A consumer reading
    only `verdict` still cannot miss the gap -- it is inside the string.
    """
    return "%s/%s" % (finding_for(checks), coverage_for(checks))


TRIAGE_OWNER = {"known_finding": "6E", "deps": "tool", "hollow": "4Q", "assert_nonvacuous": "4Q",
                "importable": "4Q", "dangerous_primitives": "6E",
                "determinism_markers": "6E", "determinism_repeat": "6E",
                "hardcoded_abs_path": "tool", "doc_behavior": "6E",
                "provenance": "illia", "duplicate": "6E", "index_parity": "tool",
                "gate": "4Q"}


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--out", default="AUDIT-RESULTS.jsonl")
    ap.add_argument("--gate", action="store_true", help="also compile/run every file")
    ap.add_argument("--repeat", type=int, default=0,
                    help="run each python file N times and compare stdout (C10 dynamic half)")
    ap.add_argument("--timeout", type=int, default=120)
    ap.add_argument("--limit", type=int, default=0, help="audit only the first N files (smoke)")
    ap.add_argument("--waivers", default=None,
                    help="path to the waiver ledger (default: WAIVERS.jsonl beside the tool)")
    ap.add_argument("--acknowledge-unverifiable", action="store_true",
                    help="suppress the non-zero exit when UNVERIFIABLE records exist — use "
                         "only once they have actually been dispositioned")
    ap.add_argument("--root", default=None,
                    help="audit an arbitrary directory instead of the signed library. Lanes "
                         "are derived from FILE EXTENSION, not from subtree names, because a "
                         "corpus is not laid out like the library. The run is marked "
                         "root_mode=corpus and library-only facts (manifest, census, index "
                         "parity, verifier md5) are absent BY CONSTRUCTION, not clean.")
    ap.add_argument("--self-test", action="store_true",
                    help="prove every check can BOTH fire and stay quiet, then exit")
    args = ap.parse_args()
    if args.self_test:
        return self_test()

    files, lane_of = [], {}
    if args.root:
        # ⛔ REBINDING THE MODULE ROOT is the tested idiom here -- the self-test already does
        # it (`global ROOT`) for duplicate_map and index_parity. Threading a second root
        # through every call site would leave two roots that can disagree; one root that
        # MOVES cannot. Everything downstream (relative_to, duplicate_map, index_parity)
        # then resolves against the corpus, and the library-only artefacts are simply
        # absent -- which the existing guards already report as unverifiable rather than
        # pass.
        global ROOT
        ROOT = Path(args.root).resolve()
        if not ROOT.is_dir():
            ap.error(f"--root {ROOT} is not a directory")
        for p in sorted(ROOT.rglob("*")):
            if p.is_file() and p.suffix in EXT_LANE and "__pycache__" not in p.parts:
                files.append(p)
                lane_of[p] = EXT_LANE[p.suffix]
    else:
      for st in LV.SIGNED_SUBTREES:
          sroot = ROOT / st
          if not sroot.is_dir():
              continue
          lane = st.split("/")[0]
          ext = LANE_EXT.get(lane)
          if ext is None:
              continue
          for p in sorted(sroot.rglob("*")):
              if p.suffix == ext and "__pycache__" not in p.parts:
                  files.append(p)
                  lane_of[p] = lane
    if args.limit:
        files = files[:args.limit]

    t0 = time.time()
    dups = duplicate_map(files, lane_of, ROOT)
    present, idx_err = index_parity(files)

    manifest_path = ROOT / "MANIFEST.json"
    mf_bytes = manifest_path.read_bytes() if manifest_path.exists() else b""
    mf = json.loads(mf_bytes) if mf_bytes else None
    try:
        census = LV.census_mismatches(ROOT, mf)
    except Exception as e:
        census = [f"census raised {type(e).__name__}: {e}"]
    roles = role_index(files, lane_of, mf)

    import shutil as _sh
    _self_md5 = hashlib.md5(Path(__file__).read_bytes()).hexdigest()
    _run_started = datetime.now(timezone.utc).isoformat()
    RUN_ID = f"{_run_started[:19].replace(':', '').replace('-', '')}-{_self_md5[:8]}"
    header = {"run": {
        "tool": "library_audit.py",
        "run_id": RUN_ID,
        "tool_md5": _self_md5,
        "run_date": _run_started,
        "host": subprocess.run(["hostname"], capture_output=True, text=True).stdout.strip(),
        "root": str(ROOT),
        "manifest_sha256": hashlib.sha256(mf_bytes).hexdigest() if mf_bytes else None,
        "root_mode": "corpus" if args.root else "library",
        "library_verify_md5": (hashlib.md5((ROOT / "library_verify.py").read_bytes()).hexdigest()
                               if (ROOT / "library_verify.py").exists() else None),
        "gate": bool(args.gate),
        "repeat": args.repeat,
        "toolchains_present": {t: bool(_sh.which(t)) for t in
                               ("python3", "Rscript", "node", "g++", "go", "rustc")},
        "census_mismatches": census,
        "expected_deliberate_drifts": [
            "On .8 ONLY: total_signed_files / multi_language_patterns / languages_present. "
            ".8's MANIFEST.json is 7 commits behind .5's corrected one. On .5 the census is "
            "GREEN and ANY mismatch here is real."],
        "analyser_coverage": {k: list(v) for k, v in ANALYSER_COVERAGE.items()},
        "unverifiable_taxonomy": {
            "subclasses": {k: {"name": v[0], "remedy": v[1]}
                           for k, v in SUBCLASS_REMEDY.items()},
            "reason_codes": REASON_SUBCLASS,
            "dispositions": list(DISPOSITIONS),
            "per_subclass_dispositions": {k: list(v)
                                          for k, v in SUBCLASS_DISPOSITIONS.items()},
            "source": "6E, REPORT-6E-TRIAGE-TAXONOMY.md, 2026-08-30",
            "note": "PARSE_FAIL is a FAIL, not UNVERIFIABLE (a malformed file is "
                    "measured-and-wrong). STRUCTURAL GUARD ONLY: all 676 python files parse, "
                    "so it changes zero records today.",
        },
        "coverage_gaps": {
            "python_only_checks": ["assert_nonvacuous", "importable", "deps", "doc_behavior",
                                   "determinism_repeat"],
            "consequence": "A compiled-lane file (cpp/rust/go) aggregates to UNVERIFIABLE "
                           "because those AST checks cannot run on it — NOT because anything "
                           "was found. It fails closed (never a false NO_FINDING), but the compiled "
                           "lanes get materially less scrutiny than python.",
            "⛔ rule": "UNVERIFIABLE IS A FINDING, NOT A TOOL FOOTNOTE. If it is triaged as "
                       "'just a limitation', the compiled lanes are silently unverified and "
                       "this file's honesty becomes decoration."},
        "index_parity_error": idx_err,
        "checks_not_requested": ([] if args.gate else ["gate"])
                                + ([] if args.repeat >= 2 else ["determinism_repeat"]),
        "total_patterns": len(files),
        "judgement_only_classes": {
            "C1_semantic_incorrectness": "⛔ THE HIGHEST-DAMAGE CLASS AND IT IS NOT CHECKED. "
                "The gate is a SMOKE TEST: it proves a file executes and exits 0. It does NOT "
                "prove the algorithm is right. Every assert in a pattern is SELF-AUTHORED, so "
                "a wrong pattern can assert its own wrongness and pass. `assert_nonvacuous` "
                "only proves the asserts CAN fire, never that what they assert is correct. "
                "A NO_FINDING verdict in this file means 'no defect among the CHECKED "
                  "classes' — it does "
                "NOT mean the pattern is correct. Closing C1 needs a reference oracle.",
            "C11_provenance": "no provenance record exists anywhere in the library; applies to "
                              "ALL patterns, so it is stated once here rather than flagged "
                              "1500 times. Needs Illia.",
            "C7_doc_behavior": "where a description exists, whether the code matches it is not "
                               "tool-decidable (6E). The per-pattern check reports only its "
                               "ABSENCE, which is decidable.",
            "C3_twin_equivalence": "no shared test vectors exist, so twin behavioural "
                                   "equivalence cannot be decided by any tool today (6E).",
        },
    }}

    records = []
    near_dup_advisory = []
    counts = defaultdict(int)
    check_counts = defaultdict(lambda: defaultdict(int))
    with open(args.out, "w", encoding="utf-8") as fh:
        fh.write(json.dumps(header) + "\n")
        for i, p in enumerate(files, 1):
            lane = lane_of[p]
            text = p.read_text(encoding="utf-8", errors="replace")
            tree = None
            if lane == "python":
                try:
                    tree = ast.parse(text)
                except SyntaxError:
                    tree = None
            checks = [fn(text, lane, tree) for fn in FILE_CHECKS]
            checks.append(check_known_findings(text, lane, tree, stem=p.stem))
            if lane == "python" and tree is None:
                checks.append(("parse", "fail", "python source does not parse"))
            if args.gate:
                g, d = run_gate_twice(p, args.repeat, args.timeout)
                checks += [g, d]
            else:
                checks.append(("gate", "skip", "not requested (--gate)"))
                checks.append(("determinism_repeat", "skip", "not requested (--gate)"))
            st_, dt_ = dups.get(p, ("pass", "no exact duplicate in its lane"))
            checks.append(duplicate_check(st_, dt_))
            if st_ == "flag":
                near_dup_advisory.append({"path": str(p.relative_to(ROOT)), "detail": dt_})
            if present is None:
                checks.append(("index_parity", "unverifiable", _u("NO_INDEX", idx_err)))
            elif p in present:
                checks.append(("index_parity", "pass", "listed in PATTERNS_INDEX.md"))
            else:
                checks.append(("index_parity", "fail", "not listed in PATTERNS_INDEX.md"))

            # An empirical repeat-run that came back identical DECIDES determinism; the
            # static marker was only a guess and must not outrank the measurement.
            byname = {n: (i, s_, d) for i, (n, s_, d) in enumerate(checks)}
            if byname.get("determinism_repeat", (None, None, None))[1] == "pass":
                i, st, dt = byname.get("determinism_markers", (None, None, None))
                if st == "flag":
                    checks[i] = ("determinism_markers", "pass",
                                 f"markers present ({dt}) but the repeat run was identical")
            v = verdict_for(checks)
            counts[v] += 1
            for name, status, _ in checks:
                check_counts[name][status] += 1
            nonpass = [(n, s, d) for n, s, d in checks if s in ("fail", "flag", "unverifiable")]
            role, source_id, multi_src = roles.get(p, ("unknown", None, False))
            # 6E section 3: the triage session must be possible WITHOUT reopening the
            # file. That needs the unverifiable checks grouped, each with a machine-readable
            # reason code and subclass, and the remedy pre-derived. `detail` is prose and
            # must never be the triage key.
            _unv, _subs = [], set()
            for _n, _st, _d in checks:
                if _st != "unverifiable":
                    continue
                _c, _sub = reason_of(_d)
                _unv.append({"name": _n, "reason_code": _c, "subclass": _sub})
                if _sub:
                    _subs.add(_sub)
            rec = {
                "pattern_id": p.stem,
                "run_id": RUN_ID,
                "role": role,
                "source_id": source_id,
                "multi_source": multi_src,
                "path": str(p.relative_to(ROOT)),
                "language": lane,
                "subtree": next((st for st in LV.SIGNED_SUBTREES
                                 if str(p.relative_to(ROOT)).startswith(st + "/")), None),
                "verdict": v,
                # ⛔ NESTED, NOT TOP-LEVEL -- see axes_of(). A top-level `finding` is a seam
                # a consumer can read alone, which merges measured and unmeasured records.
                "axes": {"finding": finding_for(checks),
                         "coverage": coverage_for(checks)},
                "checks": [{"name": n, "status": s, "detail": d} for n, s, d in checks],
                "evidence": clip_evidence(
                    "; ".join(f"{n}: {d}" for n, s, d in nonpass)),
                "triage_owner": sorted({TRIAGE_OWNER.get(n, "6E") for n, s, _ in nonpass
                                        if s in ("fail", "flag")}) or None,
                "unverifiable_checks": _unv or None,
                "unverifiable_subclass": sorted(_subs) or None,
                "remedy": sorted({SUBCLASS_REMEDY[x][1] for x in _subs}) or None,
                # Filled by a triage session, never by this tool. One of DISPOSITIONS, and
                # WAIVE additionally requires a disposition_ref (6E).
                "disposition": None,
                "disposition_ref": None,
                **triage_fields(checks, _subs),
                # 6E: PASS must never be read as "clean". These classes were never assessed
                # for ANY pattern, so they are stated on every record, not just the flagged.
                "unassessed_classes": ["C1_semantic_incorrectness", "C3_twin_equivalence",
                                       "C11_provenance"],
                "verdict_semantics": (
                    "A NO_FINDING verdict means no defect was found among the classes this tool "
                    "CAN check. "
                    "It does NOT mean the pattern is correct: C1 (algorithm correctness), "
                    "C3 (twin equivalence) and C11 (provenance) were never assessed for "
                    "this pattern."),
            }
            fh.write(json.dumps(rec) + "\n")
            records.append(rec)
            if i % 100 == 0:
                print(f"  ... {i}/{len(files)}  {time.time()-t0:.0f}s", flush=True)

    header["run"]["summary"] = dict(counts)
    per_lane = defaultdict(lambda: defaultdict(int))
    per_role = defaultdict(int)
    for r in records:
        per_lane[r["language"]][r["verdict"]] += 1
        per_role[r["role"]] += 1
    header["run"]["near_duplicate_advisory"] = {
        "⛔ status": "ADVISORY ONLY — a near-duplicate no longer SETS a verdict. But "
                     "removing it from the verdict calculus CHANGED 93 records (91 "
                     "FLAG->UNVERIFIABLE, 2 FLAG->NO_FINDING) — 6E measured this; the earlier "
                     "claim that it changed nothing was wrong.",
        "⛔ precision": "accuracy on 6E's 7 hand-verified pairs is 4/7, but PRECISION AMONG "
                        "THE SURVIVING FLAGS IS 0/14 — 6E read all 14 and every one is a "
                        "false positive. The 4 'correct' outcomes are removals, not correct "
                        "flags. Do not quote 4/7 as precision.",
        "⛔ not salvageable": "Near-duplicate detection by shingle similarity does not work "
                              "on this library. 6E measured containment, Jaccard and size "
                              "ratio on the ground truth: the one TRUE positive (0.87) sits "
                              "INSIDE the false-positive range (0.81-0.94). The genuine "
                              "duplicate is a SEMANTIC duplicate — same mechanism, different "
                              "name — which is C1 territory, not a threshold problem. Treat "
                              "this list as a structural-similarity hint at best.",
        "why": "Measured against 6E's hand-verified ground truth (7 pairs he read): the "
               "original literal-token scheme produced ~98% false positives because all "
               "91/91 javascript patterns share one verbatim test harness. A "
               "document-frequency filter (a shingle in >10% of a lane is boilerplate) "
               "removed all four javascript false positives and cut 93 flags to "
               f"{len(near_dup_advisory)}, but it still keeps rust crypto-core false "
               "positives and it LOSES a confirmed true positive "
               "(atomic_snapshot/cow_backup). Precision on ground truth: 4/7.",
        "how to use": "A lead for a human to read, never evidence of duplication. Exact "
                      "duplication is a separate check and IS reliable (hash equality).",
        "pairs": near_dup_advisory,
    }
    header["run"]["per_lane"] = {k: dict(v) for k, v in per_lane.items()}
    header["run"]["per_role"] = dict(per_role)
    header["run"]["per_check"] = {k: dict(v) for k, v in check_counts.items()}
    header["run"]["elapsed_s"] = round(time.time() - t0, 1)
    # ---- waivers. Applied AFTER every verdict is computed, and deliberately WITHOUT the
    # power to change one: a waived finding keeps status `flag` and keeps its place in the
    # finding axis. All a waiver does is attach a named, dated, referenced adjudication to it.
    _waivers = load_waivers(args.waivers or (ROOT / "WAIVERS.jsonl"))
    _wapplied, _wstale, _worphan = apply_waivers(records, _waivers, ROOT)
    header["run"]["waivers"] = {
        "ledger": str(args.waivers or (ROOT / "WAIVERS.jsonl")),
        "loaded": len(_waivers), "applied": _wapplied,
        "stale": [{"path": x["waiver"]["path"], "check": x["waiver"]["check"],
                   "waived_sha256": x["waiver"]["file_sha256"],
                   "live_sha256": x["live_sha256"]} for x in _wstale],
        "orphan": [{"path": w["path"], "check": w["check"]} for w in _worphan],
        "⛔ semantics": "A waived finding is STILL A FINDING. It keeps status `flag`, it never "
                       "becomes pass/NO_FINDING, and it is counted separately as ACCEPTED-"
                       "WITH-REASON. A stale waiver (the file changed since it was granted) "
                       "does NOT apply and the raw finding stands.",
    }
    # rewrite the whole file: the records were streamed before waivers could be attached
    with open(args.out, "w", encoding="utf-8") as fh:
        fh.write(json.dumps(header) + "\n")
        for _r in records:
            fh.write(json.dumps(_r) + "\n")

    print(f"\n{len(files)} pattern(s) audited in {time.time()-t0:.0f}s -> {args.out}")
    for v in VERDICTS:
        if counts.get(v):
            print(f"  {v:<14} {counts[v]}")
    if _waivers or _wstale or _worphan:
        print(f"\nwaivers: {len(_waivers)} loaded, {_wapplied} finding(s) accepted-with-reason"
              f", {len(_wstale)} STALE, {len(_worphan)} orphan")
        for _x in _wstale[:5]:
            print(f"  ⛔ STALE (file changed since it was waived; the finding STANDS): "
                  f"{_x['waiver']['path']} / {_x['waiver']['check']}")
        for _w in _worphan[:5]:
            print(f"  ⚠️  orphan (matches no finding — fixed, or a typo): "
                  f"{_w['path']} / {_w['check']}")
    print("\nper check:")
    for name in sorted(check_counts):
        row = check_counts[name]
        print(f"  {name:<22} " + "  ".join(f"{s}={row[s]}" for s in STATUSES if row.get(s)))
    # A header field cannot force anyone to act on UNVERIFIABLE (6E). This can: a run with
    # unmeasured patterns cannot exit 0 until someone says out loud that they looked.
    # ⛔ 6E: an unowned record means THIS TOOL's routing is broken, so a green run must be
    # impossible while one exists. --acknowledge-unverifiable exists so an honest
    # UNVERIFIABLE does not redden the run; if a tool defect rode the same exit code, that
    # flag would silence it too and the loud error would be one flag away from the comfort
    # blanket it replaced. Tool defects are UNACKNOWLEDGEABLE, and they are checked FIRST.
    _td = [r for r in records if r.get("needs_tool_fix")]
    if _td:
        print(f"\n⛔ {len(_td)} record(s) carry a check NO ROUTING RULE CLAIMED. That is a "
              "defect in THIS TOOL")
        print("   (a dropped reason code or a missing routing rule), not human triage work.")
        for _r in _td[:5]:
            # 4Q round 15 O1: the same raw-repr class as his round-12 F1, in the TOOL's
            # console output rather than the renderer. The console is where a routing bug
            # is read first.
            _uc_txt = "; ".join(
                "%s (%s/%s)" % (_c.get("name"), _c.get("reason_code"), _c.get("subclass"))
                for _c in (_r.get("unclaimed_checks") or []))
            print(f"     {_r['path']}: {clip_evidence(_uc_txt, 200)}")
        print("   No flag suppresses this. Fix the routing, then re-run.")
        return 3
    # ⛔ THE GUARD MOVED, IT DID NOT GO AWAY. 6E's rule was "UNVERIFIABLE IS A FINDING, NOT A
    # TOOL FOOTNOTE" -- a run must not go green while the compiled lanes are under-measured.
    # That rule was attached to a VERDICT WORD; the word was wrong, the rule was not. It is
    # now attached to the COVERAGE AXIS, which is the thing it was always about. Relabelling
    # without moving the guard would have made the compiled lanes silently unverified, which
    # is precisely the failure 6E built the taxonomy to prevent.
    _code, _partial = coverage_exit_code(records, args.acknowledge_unverifiable)
    _none = [r for r in records if axes_of(r)[1] == "NONE"]
    if _code:
        print(f"\n⛔ {len(_partial)} pattern(s) were only PARTIALLY MEASURED "
              f"({len(_none)} of them not measured at all).")
        print("   Their verdict reads e.g. NO_FINDING/PARTIAL: nothing was found among the")
        print("   checks that RAN, and some checks could not run at all. That gap is a")
        print("   FINDING about this tool's lane coverage, not a footnote. See")
        print("   run.coverage_gaps for which checks could not run and why. Re-run with")
        print("   --acknowledge-unverifiable once they have been dispositioned.")
        return _code
    return _code




# ================================================================= self-test
# ⛔ A CHECK THAT HAS NEVER FAILED IS NOT KNOWN TO WORK. Every check below gets BOTH arms:
# a positive fixture that MUST fire and a negative fixture that MUST stay quiet. A check
# that only ever sees one arm passes no matter how broken it is (the vacuous-fixture trap).
SELFTEST_CASES = [
    # (label, check fn, lane, source, expected status)
    ("hollow: no asserts and no calls", check_hollow, "python", "x = 1\ny = 2\n", "fail"),
    ("hollow: calls but no asserts", check_hollow, "python", "def f():\n    return 1\nf()\n", "flag"),
    ("hollow: has asserts", check_hollow, "python", "def f():\n    return 1\nassert f() == 1\n", "pass"),
    ("hollow: unknown lane is UNVERIFIABLE not pass", check_hollow, "cobol", "x", "unverifiable"),

    ("assert: always-true literal cannot fire", check_assert_nonvacuous, "python",
     "assert True\n", "fail"),
    ("assert: 1 == 1 cannot fire", check_assert_nonvacuous, "python", "assert 1 == 1\n", "fail"),
    ("assert: `assert False` is a FAILURE-PATH MARKER, not vacuous", check_assert_nonvacuous,
     "python", "try:\n    f()\nexcept ValueError:\n    pass\nelse:\n    assert False, 'no raise'\n",
     "pass"),
    ("assert: live assert passes", check_assert_nonvacuous, "python",
     "x = 2\nassert x == 2\n", "pass"),
    ("assert: mixed live + always-true is a flag", check_assert_nonvacuous, "python",
     "x = 2\nassert x == 2\nassert True\n", "flag"),
    # ⛔ ROUND 20 — this slot asserted the LIMITATION ("non-python is UNVERIFIABLE"), the
    # shape Round 19 removed from doc_behavior and C6 removed from deps. C4 now decides in
    # all six lanes; both arms of every lane are probed in the matrix and in the C4-<lane>
    # block near the end of the self-test.
    ("assert: a go guard on two literals can never fire", check_assert_nonvacuous, "go",
     "package main\nfunc main(){ if 1 != 1 { os.Exit(1) } }\n", "fail"),
    ("assert: a go guard on a variable is live", check_assert_nonvacuous, "go",
     "package main\nfunc main(){ if got != 1 { os.Exit(1) } }\n", "pass"),

    ("importable: no defs is script-only", check_importable, "python", "print(1)\n", "flag"),
    ("importable: side effect at module level", check_importable, "python",
     "def f():\n    return 1\nprint(f())\n", "flag"),
    ("importable: __main__ guard is NOT a side effect", check_importable, "python",
     "def f():\n    return 1\nif __name__ == '__main__':\n    print(f())\n", "pass"),

    ("deps: third-party import is flagged", check_deps, "python", "import numpy\n", "flag"),
    ("deps: stdlib only passes", check_deps, "python", "import json, os\n", "pass"),
    ("deps: relative import is not third-party", check_deps, "python", "from . import x\n", "pass"),
    # ⛔ ROUND 20 — this slot held `("deps: non-python is UNVERIFIABLE not pass", ...
    # "rust", "use foo;", "unverifiable")`: a probe asserting the LIMITATION, exactly the
    # shape Round 19 removed from doc_behavior. It defended the gap, not the tool. C6 now
    # decides in all six lanes; both arms of every lane are probed in the matrix and in the
    # C6-<lane> false-positive block near the end of the self-test.
    ("deps: a rust crate that is not std IS third-party", check_deps, "rust", "use foo;",
     "flag"),

    ("dangerous: eval is flagged", check_dangerous, "python", "eval('1')\n", "flag"),
    ("dangerous: shell=True is flagged", check_dangerous, "python", "run(x, shell=True)\n", "flag"),
    # ⛔ 6E round 15. Both classes below were FALSE PASSES and neither had a single probe:
    # "a change that added or removed decorator handling would not move one of the 288".
    ("6E-R15 importable: a DECORATED def runs register(f) at import — the canonical import "
     "side effect, and it used to report 'no import side effects'",
     check_importable, "python",
     "registry = []\ndef register(f):\n    registry.append(f)\n    return f\n"
     "@register\ndef hello():\n    return 1\n", "flag"),
    ("6E-R15 importable: a decorated CLASS is the same class of side effect",
     check_importable, "python",
     "def reg(c):\n    return c\n@reg\nclass A:\n    pass\n", "flag"),
    ("6E-R15 importable NEGATIVE ARM: an UNdecorated def is still clean, so the new rule "
     "did not simply flag everything",
     check_importable, "python", "def hello():\n    return 1\n", "pass"),
    ("6E-R15 dangerous: subprocess.Popen is the same primitive as os.system",
     check_dangerous, "python", "import subprocess\nsubprocess.Popen('ls')\n", "flag"),
    ("6E-R15 dangerous: subprocess.run is flagged", check_dangerous, "python",
     "subprocess.run(['ls'])\n", "flag"),
    ("6E-R15 dangerous: subprocess.check_output is flagged", check_dangerous, "python",
     "subprocess.check_output(['ls'])\n", "flag"),
    ("6E-R15 dangerous: `from os import system` walked past the dotted regex",
     check_dangerous, "python", "from os import system\nsystem('ls')\n", "flag"),
    ("6E-R15 dangerous: os.execv is process execution too", check_dangerous, "python",
     "import os\nos.execv('/bin/ls', [])\n", "flag"),
    # ⛔ TRIAGE SESSION — three classes that made the tool lie about the LIBRARY, not about a
    # fixture. All three survived twenty red-team rounds because no probe used the idiom the
    # library actually uses. Found by decomposing the 281 FLAGs by shape instead of counting.
    ("TRIAGE-A go: `if x != y { fmt.Print; os.Exit(1) }` IS the assertion for a main-package "
     "program — go has no assert statement, and this flagged 86 of 93 go patterns",
     check_hollow, "go",
     'package main\nimport ("fmt"; "os")\nfunc main(){ x := 1\nif x != 1 { '
     'fmt.Println("bad"); os.Exit(1) } }\n', "pass"),
    ("TRIAGE-A go: log.Fatal IS os.Exit(1) and states the same guarantee", check_hollow, "go",
     'package main\nimport ("log")\nfunc main(){ x := 1\nif x != 1 { log.Fatal("bad") } }\n',
     "pass"),
    ("TRIAGE-A go NEGATIVE ARM: os.Exit(0) is a SUCCESSFUL exit and states nothing — the "
     "rule must not become `any os.Exit passes`", check_hollow, "go",
     'package main\nimport "os"\nfunc main(){ os.Exit(0) }\n', "flag"),
    ("TRIAGE-A go NEGATIVE ARM: a program that verifies nothing is still hollow",
     check_hollow, "go",
     'package main\nimport "fmt"\nfunc main(){ fmt.Println("hi") }\n', "flag"),
    ("TRIAGE-B py: the dataclass decorator is a PURE transformer — it returns a new class "
     "and touches nothing, and it flagged 34 patterns as import side effects",
     check_importable, "python",
     "from dataclasses import dataclass\n@dataclass\nclass E:\n    x: int = 1\n", "pass"),
    ("TRIAGE-B py: the same when configured", check_importable, "python",
     "from dataclasses import dataclass\n@dataclass(frozen=True)\nclass E:\n    x: int = 1\n",
     "pass"),
    ("TRIAGE-B py NEGATIVE ARM: a bare @register is ALSO a bare Name and it genuinely calls "
     "register(f) at import — this is why 4Q's shape rule was overruled", check_importable,
     "python", "from r import register\n@register\ndef f(): pass\n", "flag"),
    ("TRIAGE-B py NEGATIVE ARM: a route decorator mutates an external object", check_importable,
     "python", "from a import app\n@app.route('/x')\ndef f(): pass\n", "flag"),
    ("TRIAGE-B py NEGATIVE ARM: logging.basicConfig at module level reconfigures the ROOT "
     "logger of whatever application imports the pattern — 6 patterns really do this",
     check_importable, "python",
     "import logging\nlogging.basicConfig(level=logging.INFO)\ndef f(): pass\n", "flag"),
    ("TRIAGE-C py: a pattern that DEFINES a hash method was accused of depending on "
     "PYTHONHASHSEED", check_determinism_markers, "python",
     "class B:\n    def hash(self, item, n):\n        return 1\n", "pass"),
    ("TRIAGE-C py NEGATIVE ARM: a genuine builtin hash() call is still nondeterministic "
     "across runs", check_determinism_markers, "python", "x = hash('abc')\n", "flag"),
    # ⛔ 4Q ROUND 20 — the frozen ruler's own two defects, found by attacking the round-19 work.
    ("R20-F1 r: `#!/usr/bin/Rscript` is an interpreter directive, not a description — R was "
     "excluded from the shebang skip, so the # handler read the shebang as the claim",
     check_doc_behavior, "r", "#!/usr/bin/Rscript\nx <- 1\n", "fail"),
    ("R20-F1 r POSITIVE ARM: a real description BELOW a shebang must survive, not be "
     "prefixed with the shebang text", check_doc_behavior, "r",
     "#!/usr/bin/Rscript\n# Computes a SHA-256 hash.\nf <- function(x) x\n", "skip"),
    ("R20-F2 js: a description written in // comments had no route to a claim at all — "
     "javascript was absent from the // branch", check_doc_behavior, "javascript",
     "// AES encryption pattern\n// Usage: encrypt(text, key)\nfunction encrypt(){}\n", "skip"),
    ("R20-F2 js: the scan BROKE at an import before it could reach the /* */ block below",
     check_doc_behavior, "javascript",
     'import { c } from "crypto";\n/* AES pattern */\nfunction e(){}\n', "skip"),
    ("R20-F2 js: the same for the require idiom", check_doc_behavior, "javascript",
     'const fs = require("fs");\n/* Reads a file. */\nfunction f(){}\n', "skip"),
    ("R20-F2 js NEGATIVE ARM: skipping imports must not make the ruler walk past real code "
     "and adopt some unrelated comment — a file with no description still fails",
     check_doc_behavior, "javascript", "function f(){ return 1; }\n", "fail"),
    ("R20-O2 py: a description that is NOT the module docstring is reported AS SUCH — the "
     "audit and the index use different methods here, so the divergence is surfaced",
     check_doc_behavior, "python", 'import os\n"""Real description."""\ndef f(): pass\n',
     "fail"),
    # ⛔ 4Q R20 O1, DECLARED LIMITATION. Scoping rust `.unwrap()` to Option/Result needs type
    # resolution -- a parser, not a regex. Unlike cpp system(), where `.`/`->` decides it
    # lexically, nothing in the text distinguishes a custom unwrap() from Option::unwrap().
    # Over-flagging is the safe direction here (the verdict is `flag`, meaning judgement, and
    # on this library every hit is a real Option/Result unwrap), and under-flagging would lose
    # real panics. Recorded as a probe asserting today's behaviour, not left to be rediscovered.
    ("R20-O1 rust LIMITATION: a CUSTOM unwrap() that never panics is still flagged — telling "
     "it from Option::unwrap() needs type resolution, which a regex cannot do",
     check_dangerous, "rust",
     "struct S;\nimpl S { fn unwrap(&self) -> i32 { 42 } }\nfn main(){ let x = S.unwrap(); }\n",
     "flag"),
    # ⛔ 4Q ROUND 18 F1 — seven dangerous primitives absent from the tables. Each fixture is
    # 4Q's, and each got a clean UNVERIFIABLE, which a reader mistakes for "nothing found".
    ("R18-F1 js: setTimeout with a STRING argument parses and executes it — the eval class",
     check_dangerous, "javascript", 'setTimeout("malicious_code()", 100);\n', "flag"),
    ("R18-F1 js NEGATIVE ARM: setTimeout with a FUNCTION is the ordinary, safe use",
     check_dangerous, "javascript", 'setTimeout(function(){ go(); }, 100);\n', "pass"),
    ("R18-F1 cpp: vsprintf is sprintf's variadic twin, same unbounded write",
     check_dangerous, "cpp", 'void f(char* b, const char* m, ...){ vsprintf(b, m, a); }\n',
     "flag"),
    ("R18-F1 cpp: tmpnam returns a PREDICTABLE name — the temp-file race", check_dangerous,
     "cpp", 'char* f(){ return tmpnam(NULL); }\n', "flag"),
    ("R18-F1 go: crypto/des is a weak CIPHER — the table had weak hashes and no ciphers",
     check_dangerous, "go", 'import "crypto/des"\n', "flag"),
    ("R18-F1 go: crypto/rc4 is the other deprecated cipher", check_dangerous, "go",
     'import "crypto/rc4"\n', "flag"),
    ("R18-F1 rust: `use std::process;` then process::Command::new — the rule demanded the "
     "fully-qualified path, so an import alias walked straight past it", check_dangerous,
     "rust", 'use std::process;\nfn r(){ process::Command::new("ls").output(); }\n', "flag"),
    ("R18-F1 rust: a GLOB import leaves the call bare — Command::new with no path at all",
     check_dangerous, "rust",
     'use std::process::*;\nfn r(){ Command::new("ls").output(); }\n', "flag"),
    ("R18-F1 rust NEGATIVE ARM: a local type named Command, with no std::process import, is "
     "not process execution — the bare spelling must not become a keyword grep",
     check_dangerous, "rust",
     'struct Command;\nimpl Command { fn new() -> Self { Command } }\nfn f(){ Command::new(); }\n',
     "pass"),
    # ⛔ 4Q ROUND 18 F2 — the FIRST finding in the other direction. Every round-16 finding said
    # the tables were too narrow; this one says a rule is too BROAD.
    ("R18-F2 cpp: hw.system(42) is a METHOD on an object, not <cstdlib>'s system()",
     check_dangerous, "cpp", 'int main(){ H hw; hw.system(42); }\n', "pass"),
    # DECLARED LIMITATION, not a passing test dressed up. 4Q's original fixture also DECLARED
    # the member (`void system(int m){}`), and a declaration is preceded by its return type,
    # not by `.` or `->`, so it still flags. Distinguishing `void system(int)` from
    # `return system(cmd)` needs to know a return type from a keyword -- that is parsing, and
    # this rule is lexical. The CALL half is decidable and fixed; the DECLARATION half is not,
    # and the honest record of that is a probe asserting today's real behaviour.
    ("R18-F2 cpp LIMITATION: a class that DECLARES a member named system still flags — the "
     "call is decidable from `.`/`->`, the declaration is not without a parser",
     check_dangerous, "cpp",
     'class H { public: void system(int m){} };\nint main(){ return 0; }\n', "flag"),
    ("R18-F2 cpp: the same through a pointer — hw->system(42)", check_dangerous, "cpp",
     'int main(){ H* hw = get(); hw->system(42); }\n', "pass"),
    ("R18-F2 cpp POSITIVE ARM: a REAL system() call must still fire — narrowing a rule is "
     "where a real finding gets lost", check_dangerous, "cpp",
     'int main(){ system("ls"); return 0; }\n', "flag"),
    ("R17-F1 js: node:child_process is the modern spelling of the SAME import and must fire",
     check_dangerous, "javascript", "const cp = require('node:child_process');\n", "flag"),
    # ⛔ 6E ROUND 17 F1 — the restored-import leak. These are 6E's two MEASURED false
    # positives, and they are in js and go ON PURPOSE: every arm I wrote for the two-pass
    # engine was python, and python has no import restore, so the class could not be seen.
    ("R17-F1 js: a require path that merely MENTIONS child_process is not an import of it",
     check_dangerous, "javascript", "var a = require('./docs/child_process_notes');\n",
     "pass"),
    ("R17-F1 go: a wrapper package whose PATH contains os/exec is not os/exec",
     check_dangerous, "go", 'import "example.com/old/os/exec-wrapper"\n', "pass"),
    ("R17-F1 POSITIVE ARM js: a REAL require of child_process must still fire — the restore "
     "exists so an import path counts as code, and pass 1 must still see it",
     check_dangerous, "javascript", "var a = require('child_process');\n", "flag"),
    ("R17-F1 POSITIVE ARM go: a REAL os/exec import must still fire", check_dangerous, "go",
     'import "os/exec"\n', "flag"),
    # ⛔ 4Q ROUND 17 F1 — SEEDED bypassed the two-pass engine.
    ("R17-F1 4Q: random.seed(\"42\") IS reproducible — the seed value lives in a literal and "
     "blanking it left random.seed(    ), so a seeded pattern was flagged for judgement",
     check_determinism_markers, "python", 'import random\nrandom.seed("42")\nx=random.random()\n',
     "pass"),
    ("R17-F1 4Q NEGATIVE ARM: random.seed() with EMPTY parens seeds from OS entropy and is "
     "NOT reproducible — the literal fix must not swallow this",
     check_determinism_markers, "python", 'import random\nrandom.seed()\nx=random.random()\n',
     "flag"),
    ("R17 4Q: a literal CONTAINING a space blanks to spaces, so code[i]==lit[i]==\" \" reads "
     "as code — no rule starts with whitespace today, and now none can exploit it",
     check_dangerous, "python", 'x = "shell = True"\n', "pass"),
    # ⛔ ROUND 17. Six rules were DEAD BY CONSTRUCTION -- the engine stripped the string
    # literal their signal lived in. Four had shipped since round 1. Each probe below is a
    # file that contains the primitive in plain sight and was returned as a clean `pass`.
    ("R17 js createElement(\"script\") — SHIPPED DEAD, string-literal signal",
     check_dangerous, "javascript", 'const s = document.createElement("script");\n', "flag"),
    ("R17 js createHash(\"md5\") — SHIPPED DEAD", check_dangerous, "javascript",
     'const h = crypto.createHash("md5");\n', "flag"),
    ("R17 js createHash(\"sha1\") — SHIPPED DEAD", check_dangerous, "javascript",
     'const h = crypto.createHash("sha1");\n', "flag"),
    ("R17 js Function(\"...\") without new — SHIPPED DEAD", check_dangerous, "javascript",
     'const f = Function("return 1");\n', "flag"),
    ("R17 NEGATIVE ARM: the primitive named in a COMMENT is prose, not code — comments are "
     "stripped in BOTH passes, so keeping literals must not resurrect prose matching",
     check_dangerous, "javascript", '// never use eval() or new Function() here\nlet x = 1;\n',
     "pass"),
    ("R17 NEGATIVE ARM: a python docstring naming a primitive is still not a finding",
     check_dangerous, "python", '"""Avoid eval() and os.system() in this module."""\nx = 1\n',
     "pass"),
    # ⛔ ROUND 16. Both agents attacked every regex table as an ENUMERATION and every one
    # had holes. Each probe below is a demonstrated false pass (or, for rust, a false
    # POSITIVE), and each broadened rule carries a NEGATIVE ARM so the fix cannot quietly
    # become a keyword grep.
    ("R16 r: system2() is the same primitive as system()", check_dangerous, "r",
     'system2("ls")\n', "flag"),
    ("R16 r: shell() is the third spelling", check_dangerous, "r", 'shell("ls")\n', "flag"),
    ("R16 r: source() from a URL is remote code", check_dangerous, "r",
     'source("https://x/y.R")\n', "flag"),
    ("R16 r NEGATIVE ARM: an ordinary call is not a finding", check_dangerous, "r",
     'mean(x)\n', "pass"),
    ("R16 go: syscall.Exec is the raw primitive os/exec wraps", check_dangerous, "go",
     'syscall.Exec("/bin/sh", a, b)\n', "flag"),
    ("R16 go NEGATIVE ARM: plain code is not a finding", check_dangerous, "go",
     'func f() int { return 1 }\n', "pass"),
    ("R16 cpp: strcat is strcpy's unbounded sibling", check_dangerous, "cpp",
     'int main(){ strcat(d, s); }\n', "flag"),
    ("R16 cpp: SHA1 was flagged in python but not here", check_dangerous, "cpp",
     'int main(){ SHA1(x, 1, d); }\n', "flag"),
    ("R16 cpp: unbounded scanf %s is the gets class", check_dangerous, "cpp",
     'int main(){ scanf("%s", buf); }\n', "flag"),
    ("R16 cpp NEGATIVE ARM: a bounded snprintf is not flagged by the scanf rule",
     check_dangerous, "cpp", 'int main(){ int n = 1; return n; }\n', "pass"),
    ("R16 rust: libc::system OUTSIDE an unsafe block was a clean miss", check_dangerous,
     "rust", 'fn f(){ libc::system(x); }\n', "flag"),
    ("R16 rust NEGATIVE ARM: ordinary rust is not a finding", check_dangerous, "rust",
     'fn f() -> i32 { 1 }\n', "pass"),
    ("R16 js: document.write is an XSS sink like innerHTML", check_dangerous, "javascript",
     'document.write(x);\n', "flag"),
    ("R16 js: insertAdjacentHTML is an XSS sink", check_dangerous, "javascript",
     'el.insertAdjacentHTML("beforeend", x);\n', "flag"),
    ("R16 js: outerHTML assignment is an XSS sink", check_dangerous, "javascript",
     'el.outerHTML = x;\n', "flag"),
    ("R16 js NEGATIVE ARM: reading .innerHTML is not writing it", check_dangerous,
     "javascript", 'const v = el.textContent;\n', "pass"),
    # --- NONDET
    ("R16 nondet python: os.urandom is not matched by `random.`", check_determinism_markers,
     "python", "import os\nx = os.urandom(4)\n", "flag"),
    ("R16 nondet python: hash() of a str is PYTHONHASHSEED-dependent",
     check_determinism_markers, "python", "x = hash('a')\n", "flag"),
    ("R16 nondet python NEGATIVE ARM: arithmetic is deterministic",
     check_determinism_markers, "python", "x = 1 + 2\n", "pass"),
    ("R16 nondet cpp: time(NULL) is the C spelling of chrono::now",
     check_determinism_markers, "cpp", "int main(){ time(NULL); }\n", "flag"),
    ("R16 nondet rust: Instant::now is a timer", check_determinism_markers, "rust",
     "fn f(){ let t = Instant::now(); }\n", "flag"),
    ("R16 nondet go: crypto/rand is nondeterministic too", check_determinism_markers, "go",
     'import "crypto/rand"\n', "flag"),
    ("R16 nondet js: XMLHttpRequest is the classic network call",
     check_determinism_markers, "javascript", "const r = new XMLHttpRequest();\n", "flag"),
    ("R16 nondet r: Sys.Date() is the date spelling of Sys.time()",
     check_determinism_markers, "r", "d <- Sys.Date()\n", "flag"),
    # --- ABS_PATH
    ("R16 abs_path: /etc/passwd is a more serious finding than /tmp and it PASSED",
     check_abs_paths, "python", 'p = "/etc/passwd"\n', "flag"),
    ("R16 abs_path: /root/.ssh/id_rsa", check_abs_paths, "python",
     'p = "/root/.ssh/id_rsa"\n', "flag"),
    ("R16 abs_path: /usr/local/bin", check_abs_paths, "python",
     'p = "/usr/local/bin/x"\n', "flag"),
    # These five negative arms are not invented: they are the FALSE POSITIVES the round-16
    # rewrite produced on the real library, measured before this fix.
    ("R17 abs_path NEGATIVE ARM: an HTTP route template is not a filesystem path",
     check_abs_paths, "python", 'ROUTE = "/user/{id}"\n', "pass"),
    ("R17 abs_path NEGATIVE ARM: a URL path is not a filesystem path", check_abs_paths,
     "python", 'r.get("/api/users")\n', "pass"),
    ("R17 abs_path NEGATIVE ARM: a health endpoint is not a filesystem path",
     check_abs_paths, "python", 'app.route("/health")\n', "pass"),
    ("R17 abs_path NEGATIVE ARM: a URL document path is not a filesystem path",
     check_abs_paths, "python", 'req = "GET /index.html"\n', "pass"),
    ("R17 abs_path: /dev/sda1 is a real hardcoded device and must NOT be swallowed by the "
     "/dev/null carve-out", check_abs_paths, "python", 'd = "/dev/sda1"\n', "flag"),
    ("R16 abs_path NEGATIVE ARM: a relative path is not absolute", check_abs_paths,
     "python", 'p = "data/x.csv"\n', "pass"),
    ("R16 abs_path NEGATIVE ARM: /dev/null is portable and carved out by name",
     check_abs_paths, "python", 'p = "/dev/null"\n', "pass"),
    # --- ASSERT_PAT. The rust one is a false POSITIVE: the tool accused a real assertion
    # of not existing. That is the worse flavour and it had no probe.
    ("R16 hollow rust: debug_assert! IS an assertion — `\\bassert!` cannot match it because "
     "`_` is a word character, so the tool called a real assertion missing",
     check_hollow, "rust", "fn f(){ debug_assert!(1 == 1); }\n", "pass"),
    ("R16 hollow cpp: static_assert is an assertion", check_hollow, "cpp",
     "int main(){ static_assert(true, \"x\"); return 0; }\n", "pass"),
    ("R16 hollow js: throwing a TypeError is a check, same as throwing an Error",
     check_hollow, "javascript",
     "function f(x){ if(!x) throw new TypeError('bad'); return 1; }\nf(1);\n", "pass"),
    ("R16 hollow NEGATIVE ARM: a file with NO assertion of any spelling is still hollow",
     check_hollow, "rust", "fn f() -> i32 { 1 }\nfn main(){ f(); }\n", "flag"),
    # 6E round 15, finding 3: the template-literal scanner. He reported it with an honest
    # caveat that the blast radius was input-dependent; it reproduced, so it is fixed and
    # probed. The third case is the arm that stops the fix becoming the opposite defect.
    ("6E-R15 js: a backtick inside an interpolation does NOT close the template and blank "
     "the real code after it", check_dangerous, "javascript",
     # ⛔ SINGLE LINE ON PURPOSE. My first version of this probe put eval() on the next
     # line and PASSED against the un-fixed scanner -- 6E's report said the blast radius is
     # input-dependent and my fixture was the shape that survives. Measured: the two-line
     # form does not discriminate, this one does.
     "const t = `a ${'b`c'} d`; eval('1');\n", "flag"),
    ("6E-R15 js: code INSIDE ${...} still runs, so it is still scanned", check_dangerous,
     "javascript", "const x = `v=${eval(y)}`;\n", "flag"),
    ("6E-R15 js NEGATIVE ARM: a bare `eval(` in the LITERAL half of a template is text, "
     "not a call — the fix must not turn the template into a keyword grep", check_dangerous,
     "javascript", "const s = `eval( is a word`;\n", "pass"),
    ("6E-R15 dangerous NEGATIVE ARM: importing subprocess without calling it is NOT a "
     "finding, so the new rules did not turn the check into a keyword grep",
     check_dangerous, "python", "import subprocess\ndef f():\n    return 1\n", "pass"),
    ("dangerous: clean file passes", check_dangerous, "python", "import json\n", "pass"),
    ("dangerous: unknown lane is UNVERIFIABLE not pass", check_dangerous, "cobol", "eval(", "unverifiable"),

    ("determinism: bare random is flagged", check_determinism_markers, "python",
     "import random\nrandom.shuffle(x)\n", "flag"),
    ("determinism: SEEDED random is not nondeterminism", check_determinism_markers, "python",
     "import random\nrandom.seed(42)\nrandom.shuffle(x)\n", "pass"),
    ("determinism: seeded rng + unseeded CLOCK still flags", check_determinism_markers, "python",
     "import random, time\nrandom.seed(1)\nt = time.time()\n", "flag"),
    ("determinism: clean file passes", check_determinism_markers, "python", "x = 1\n", "pass"),

    ("abs path: /home literal is flagged", check_abs_paths, "python", "p = '/home/au/x'\n", "flag"),
    ("abs path: relative path passes", check_abs_paths, "python", "p = 'data/x'\n", "pass"),

    ("doc: missing module docstring is a FAIL", check_doc_behavior, "python", "x = 1\n", "fail"),
    ("doc: present docstring is SKIP (judgement, not decidable)", check_doc_behavior, "python",
     "'''does a thing.'''\nx = 1\n", "skip"),
    # ⛔ ROUND 19 — this slot held `("doc: non-python is UNVERIFIABLE not pass", ... "cpp",
    # "// x", "unverifiable")`, a probe that asserted the LIMITATION. It passed for sixteen
    # rounds and defended nothing except the gap itself. Both arms, every lane, now:
    ("R19 doc cpp: the description is the /* */ block after the watermark", check_doc_behavior,
     "cpp", 'static const char *_aura_mark = "AE1.x";\n/* Computes a rolling hash. */\n'
     '#include <cstdio>\n', "skip"),
    ("R19 doc cpp NEGATIVE ARM: includes alone are structural, not a description",
     check_doc_behavior, "cpp", '#include <cstdio>\nint main(){ return 0; }\n', "fail"),
    ("R19 doc go: the // block after the imports, before the watermark", check_doc_behavior,
     "go", 'package main\n\nimport "fmt"\n\n// Counts distinct items.\nfunc main(){}\n',
     "skip"),
    ("R19 doc go NEGATIVE ARM: package and import lines are structural", check_doc_behavior,
     "go", 'package main\n\nimport "fmt"\n\nfunc main(){ fmt.Println(1) }\n', "fail"),
    ("R19 doc rust: the // block after the use lines", check_doc_behavior, "rust",
     'use std::io;\n// Parses a URL authority.\nfn f(){}\n', "skip"),
    ("R19 doc rust NEGATIVE ARM: use lines are structural", check_doc_behavior, "rust",
     'use std::io;\nfn f(){}\n', "fail"),
    ("R19 doc r: the # block at the top", check_doc_behavior, "r",
     '# Fits a linear model.\nf <- function(x) x\n', "skip"),
    ("R19 doc r NEGATIVE ARM: no comment block at all", check_doc_behavior, "r",
     'f <- function(x) x\n', "fail"),
    ("R19 doc js: the leading /** */ JSDoc block", check_doc_behavior, "javascript",
     '/** Debounces a callback. */\nfunction d(){}\n', "skip"),
    ("R19 doc js NEGATIVE ARM: a @forge-family TAG is provenance, not a description",
     check_doc_behavior, "javascript", '// @forge-family debounce\nfunction d(){}\n', "fail"),
    ("R19 doc: a lane with NO slot defined stays U1 — answering `fail` there would claim the "
     "file has no description when the truth is nobody has said where one lives",
     check_doc_behavior, "cobol", "       IDENTIFICATION DIVISION.\n", "unverifiable"),

    # ---- 4Q round-1 findings F1-F7: every one gets a probe so it cannot come back -------
    ("F1 determinism: bare random.seed() is NOT reproducible", check_determinism_markers,
     "python", "import random\nrandom.seed()\nrandom.shuffle(x)\n", "flag"),
    ("F1 determinism: np.random.seed() bare is NOT reproducible", check_determinism_markers,
     "python", "import numpy as np\nnp.random.seed()\nnp.random.rand()\n", "flag"),
    ("F1 determinism: random.seed(42) IS reproducible", check_determinism_markers,
     "python", "import random\nrandom.seed(42)\nrandom.shuffle(x)\n", "pass"),
    ("F2 importable: INVERTED __name__ guard runs on import", check_importable, "python",
     "def f():\n    return 1\nif __name__ != '__main__':\n    print(1)\n", "flag"),
    ("F2 importable: elif of a main guard runs on import", check_importable, "python",
     "def f():\n    return 1\nif __name__ == '__main__':\n    pass\nelse:\n    print(1)\n",
     "flag"),
    ("F8 importable: a side effect in a NON-guard if block is not exempt", check_importable,
     "python", "def f():\n    return 1\nif True:\n    print(1)\n", "flag"),
    ("F2 importable: '__main__' == __name__ IS a guard", check_importable, "python",
     "def f():\n    return 1\nif '__main__' == __name__:\n    print(f())\n", "pass"),
    ("F3 hollow: an assertion in a COMMENT does not count", check_hollow, "go",
     "package main\n// panic(err)\nfunc main() { x := 1; _ = x }\n", "flag"),
    ("F3 hollow: an assertion in a STRING does not count", check_hollow, "go",
     'package main\nfunc main() { s := "panic(err)"; _ = s }\n', "flag"),
    ("F3 hollow: a real assertion in code counts", check_hollow, "go",
     "package main\nfunc main() { panic(\"bad\") }\n", "pass"),
    ("F4 determinism: random_device is NOT made reproducible by srand(42)",
     check_determinism_markers, "cpp",
     "#include <random>\nint main(){ std::random_device rd; srand(42); return 0; }\n", "flag"),
    ("F5 dangerous: a match inside a COMMENT is not a finding", check_dangerous, "r",
     "# solve as linear system (R gamma = gamma_acov)\nx <- 1\n", "pass"),
    ("F5 dangerous: a real system() call in R code IS a finding", check_dangerous, "r",
     "system('ls')\n", "flag"),
    ("F5 dangerous: python eval inside a comment is not a finding", check_dangerous,
     "python", "# do not use eval(x) here\nx = 1\n", "pass"),
    ("F5 dangerous: python eval inside a STRING is not a finding", check_dangerous,
     "python", "msg = 'never call eval(x)'\n", "pass"),
    ("F7 deps: a TYPE_CHECKING-only import is not a runtime dependency", check_deps, "python",
     "from typing import TYPE_CHECKING\nif TYPE_CHECKING:\n    import pandas\n", "pass"),
    ("F7 deps: a REAL runtime third-party import is still flagged", check_deps, "python",
     "from typing import TYPE_CHECKING\nif TYPE_CHECKING:\n    import pandas\nimport numpy\n",
     "flag"),

    # ---- 4Q F8: paths the self-test never exercised -------------------------------------
    ("F8 dangerous: a non-python lane really is scanned", check_dangerous, "go",
     "package main\nimport \"os/exec\"\n", "flag"),
    ("F8 determinism: a non-python lane really is scanned", check_determinism_markers, "go",
     "package main\nimport \"math/rand\"\n", "flag"),
    ("F8 abs_path: non-python is scanned too", check_abs_paths, "go",
     "package main\nvar p = \"/home/au/x\"\n", "flag"),
    ("F8 hollow: a non-python lane with NO assertion is flagged", check_hollow, "cpp",
     "int main(){ return 0; }\n", "flag"),
    # ---- 4Q round 2. F1 was LIVE: 38 assertions and 6 unwrap() hidden across 3 shipping
    # rust files, and `dangerous` returned a false `pass`. -----------------------------
    ("F1 rust: a &'static LIFETIME is not a string opener", check_hollow, "rust",
     "fn parse(d: &'static str) -> bool { assert!(!d.is_empty()); true }\n", "pass"),
    ("F1 rust: a lifetime does not swallow the code after it", check_dangerous, "rust",
     "fn f(d: &'static str) { let x: u8 = d.parse().unwrap(); }\n", "flag"),
    ("F1 rust: a real CHAR literal is still a literal", check_dangerous, "rust",
     "fn f() { let c = '@'; let s = \"unwrap()\"; }\n", "pass"),
    ("F1 rust: an escaped char literal is still a literal", check_dangerous, "rust",
     "fn f() { let c = '\\n'; let s = \"unwrap()\"; }\n", "pass"),
    ("F2 cpp: a RAW STRING with embedded quotes does not leak as code", check_dangerous,
     "cpp", 'const char* x = R"("system(1)")";\nint main(){return 0;}\n', "pass"),
    ("F2 cpp: real code after a raw string is still seen", check_dangerous, "cpp",
     'const char* x = R"(hi)";\nint main(){ system("ls"); }\n', "flag"),
    # Single line ON PURPOSE: the string scanner stops at a newline, so a two-line fixture
    # could not detect the regex handling being removed -- the mutant SURVIVED it.
    ("F4 js: a REGEX LITERAL containing quotes does not swallow the REST OF ITS LINE",
     check_dangerous, "javascript", "var x = /['\"]/g; var y = eval('1');\n", "flag"),
    ("F3 go: a dangerous name in an IMPORT-LINE COMMENT is not a finding", check_dangerous,
     "go", 'package main\nimport "fmt" // uses crypto/md5 for hashing\n', "pass"),
    ("F3 go: a real dangerous import is still a finding", check_dangerous, "go",
     'package main\nimport "crypto/md5"\n', "flag"),
    ("F5 abs_path: a quoted path inside a COMMENT is not a hardcoded path", check_abs_paths,
     "python", '# the config is at "/home/au/x"\nx = 1\n', "pass"),
    ("F5 abs_path: a quoted path in real CODE still is", check_abs_paths, "python",
     'p = "/home/au/x"\n', "flag"),
    ("F8 assert: `assert False` outside try/except is still a marker",
     check_assert_nonvacuous, "python", "x = 1\nassert False, 'unreachable'\n", "pass"),
]


def self_test() -> int:
    fails = []
    nprobe = [0]          # counted, never computed -- see D1 (4Q round 3)
    print("library_audit self-test — both arms of every check\n")
    for label, fn, lane, src, expect in SELFTEST_CASES:
        tree = None
        if lane == "python":
            try:
                tree = ast.parse(src)
            except SyntaxError:
                tree = None
        try:
            name, status, detail = fn(src, lane, tree)
        except Exception as e:
            status, detail = f"CRASH:{type(e).__name__}", str(e)
        ok = (status == expect)
        nprobe[0] += 1
        if not ok:
            fails.append(label)
        print(f"  {'ok  ' if ok else 'FAIL'}  {label}\n"
              f"          expect={expect} got={status}" + (f"  ({detail})" if not ok else ""))

    # verdict aggregation is itself a decision rule and must be proven
    # ⛔ "unverifiable beats pass" USED TO LIVE HERE and it encoded the defect Illia caught:
    # an unmeasured check OUTRANKED a clean measurement, so one missing analyser relabelled a
    # file that had passed everything else. Severity is now the FINDING axis only, and an
    # unmeasured check moves the COVERAGE axis instead of overriding what was measured.
    agg = [("fail beats flag", [("a", "fail", ""), ("b", "flag", "")], "FAIL/FULL"),
           ("flag outranks nothing-found on the FINDING axis, and an unmeasured check "
            "shows up on the COVERAGE axis instead of erasing it",
            [("a", "flag", ""), ("b", "unverifiable", "")], "FLAG/PARTIAL"),
           ("an unmeasured check NO LONGER outranks a clean measurement (Illia 2026-08-30) "
            "-- it reports as partially-covered, not as unmeasured",
            [("a", "unverifiable", ""), ("b", "pass", "")], "NO_FINDING/PARTIAL"),
           ("nothing measured at all is the ONLY state that means unmeasured",
            [("a", "unverifiable", ""), ("b", "unverifiable", "")], "NO_FINDING/NONE"),
           ("all pass is NO_FINDING, never PASS (Ver finding 1)",
            [("a", "pass", ""), ("b", "pass", "")], "NO_FINDING/FULL"),
           ("all skip is SKIP", [("a", "skip", "")], "SKIP/FULL")]
    print()
    for label, checks, expect in agg:
        got = verdict_for(checks)
        ok = got == expect
        nprobe[0] += 1
        if not ok:
            fails.append("verdict: " + label)
        print(f"  {'ok  ' if ok else 'FAIL'}  verdict: {label} -> {got}")

    # duplicate detection needs a real tree, not a synthetic status
    import tempfile
    with tempfile.TemporaryDirectory() as td:
        d = Path(td) / "python" / "programming"
        d.mkdir(parents=True)
        body = "\n".join(f"def f{i}(x):\n    return x + {i}" for i in range(40))
        (d / "a.py").write_text(body, encoding="utf-8")
        (d / "b.py").write_text(body, encoding="utf-8")            # exact duplicate
        (d / "c.py").write_text("def g(y):\n    return y * 2\n", encoding="utf-8")
        fs = [d / "a.py", d / "b.py", d / "c.py"]
        lane_of = {f: "python" for f in fs}
        global ROOT
        _saved, ROOT = ROOT, Path(td)
        try:
            dm = duplicate_map(fs, lane_of)
        finally:
            ROOT = _saved
        for label, cond in (("duplicate: exact pair is caught", (d / "a.py") in dm
                             and dm[d / "a.py"][0] == "fail"),
                            ("duplicate: the distinct file is NOT accused",
                             dm.get(d / "c.py", ("skip", ""))[0] in ("skip", "pass"))):
            nprobe[0] += 1
            if not cond:
                fails.append(label)
            print(f"  {'ok  ' if cond else 'FAIL'}  {label}")

    # F6 -- an EMPTY rule table measured nothing and must not report pass
    _saved_go = DANGEROUS["go"]
    DANGEROUS["go"] = []          # a lane that HAS a stripper, so only the empty-table
    try:                          # guard can produce the verdict
        st = _text_check("package main\n", "go", DANGEROUS, "dangerous_primitives", "x")[1]
    finally:
        DANGEROUS["go"] = _saved_go
    extra = [("F6: an EMPTY rule table on a STRIPPABLE lane is UNVERIFIABLE, not pass",
              st == "unverifiable")]

    # 4Q D2 -- a CODE line mentioning AE1. must survive normalisation
    # Behavioural, not a grep of my own source: an index that lists ONLY hmac_sha256.rs
    # must not make sha256.rs count as present. Both names really exist in the library.
    with tempfile.TemporaryDirectory() as td:
        r2 = Path(td)
        (r2 / "rust").mkdir()
        a2 = r2 / "rust" / "sha256.rs"
        b2 = r2 / "rust" / "hmac_sha256.rs"
        a2.write_text("x", encoding="utf-8")
        b2.write_text("x", encoding="utf-8")
        (r2 / "PATTERNS_INDEX.md").write_text("- rust/hmac_sha256.rs\n", encoding="utf-8")
        _k, ROOT = ROOT, r2
        try:
            pres, _err = index_parity([a2, b2])
        finally:
            ROOT = _k
        extra.append(("4Q D3: a name that is a SUBSTRING of a listed file is not counted "
                      "present", b2 in pres and a2 not in pres))
    _d2b = _norm_source("*ptr = AE1.value\n# △ AURA Pattern Library AE1.abc\n", "cpp")
    extra.append(("4Q D2: a *-prefixed CODE line containing AE1. survives",
                  "AE1.value" in _d2b and "AURA Pattern Library" not in _d2b))
    _d2 = _norm_source("cipher = AE1.encrypt(data)\n# △ AURA Pattern Library AE1.abc\n",
                       "python")
    extra.append(("D2: _norm_source keeps a CODE line containing AE1. but drops the mark",
                  "AE1.encrypt" in _d2 and "AURA Pattern Library" not in _d2))
    extra.append(("verdict: flag + pass is FLAG",
                  verdict_for([("a", "flag", ""), ("b", "pass", "")]) == "FLAG/FULL"))

    # 6E -- a RENAMED copy-paste must still be caught (literal tokens missed it), and a
    # sub-floor file must be SKIPped, never passed as "no near-duplicate exists".
    with tempfile.TemporaryDirectory() as td:
        d = Path(td) / "python" / "programming"
        d.mkdir(parents=True)
        ops = ["+", "-", "*", "%", "//", "&", "|", "^"]
        base = "\n".join(
            f"def compute_hash_{i}(payload, salt_{i}):\n"
            f"    acc_{i} = payload {ops[i % len(ops)]} {i}\n"
            f"    for step_{i} in range({i + 2}):\n"
            f"        acc_{i} = (acc_{i} {ops[(i + 3) % len(ops)]} step_{i}) & 0xFF{i:02x}\n"
            f"    return acc_{i} {ops[(i + 5) % len(ops)]} salt_{i}\n"
            for i in range(30))
        renamed = (base.replace("compute_hash", "calc_digest").replace("payload", "buf")
                       .replace("acc_", "total_").replace("salt_", "pepper_")
                       .replace("step_", "idx_"))
        (d / "orig.py").write_text(base, encoding="utf-8")
        (d / "clone.py").write_text(renamed, encoding="utf-8")
        (d / "tiny.py").write_text("x = 1\n", encoding="utf-8")
        fs = [d / "orig.py", d / "clone.py", d / "tiny.py"]
        dm = duplicate_map(fs, {f: "python" for f in fs}, Path(td))
        extra.append(("6E: a RENAMED copy-paste is caught by identifier normalisation",
                      dm.get(d / "clone.py", ("", ""))[0] == "flag"))
        extra.append(("6E: a sub-floor file is SKIP, not a pass claiming no near-duplicate",
                      dm.get(d / "tiny.py", ("", ""))[0] == "skip"))

    # role derivation (6E): the C3 precondition
    with tempfile.TemporaryDirectory() as td:
        r = Path(td)
        rels = ("python/a.py", "r/d.R", "python/d.py", "cpp/a.cpp", "cpp/b.cpp",
                "go/c.go", "rust/e.rs", "cpp/d.cpp")
        for rel in rels:
            f = r / rel
            f.parent.mkdir(parents=True, exist_ok=True)
            f.write_text("x", encoding="utf-8")
        fs = [r / x for x in rels]
        lo = {r / x: x.split("/")[0] for x in rels}
        ri = role_index(fs, lo, {"native_patterns": {"go": ["c"]}})
        extra += [("role: a python file is a source", ri[r / "python/a.py"][0] == "source"),
                  ("role: a cpp file sharing a python stem is a twin",
                   ri[r / "cpp/a.cpp"][:2] == ("twin", "a")),
                  ("role: a DECLARED native is native", ri[r / "go/c.go"][0] == "native"),
                  ("role: a cpp file with no source and no declaration is twin_orphan",
                   ri[r / "cpp/b.cpp"][0] == "twin_orphan"),
                  ("6E: a RUST file with no source is STANDALONE, not twin_orphan "
                   "(rust is not a source-requiring lane)",
                   ri[r / "rust/e.rs"][0] == "standalone"),
                  ("6E: a twin of a stem in BOTH python and r is flagged multi_source",
                   ri[r / "cpp/d.cpp"][2] is True),
                  ("6E: a twin of a single-lane stem is NOT multi_source",
                   ri[r / "cpp/a.cpp"][2] is False)]

    # The DEMOTION itself needs a probe: if a near-duplicate advisory still reached the
    # verdict, every probe above would pass unchanged. Verdict aggregation is where the
    # demotion either holds or silently does not.
    extra.append(("6E: a hand-verified KNOWN finding is flagged, not silently passed",
                  check_known_findings("", "python", None, stem="atomic_snapshot")[1]
                  == "flag"))
    extra.append(("known_finding: an ordinary pattern is not accused",
                  check_known_findings("", "python", None, stem="some_other_pattern")[1]
                  == "pass"))
    _nd = duplicate_check("flag", "near-duplicate of x.py (jaccard 0.80)")
    extra.append(("6E: a near-duplicate ADVISORY does not change the verdict",
                  _nd[1] == "skip"
                  and verdict_for([("gate", "pass", ""), _nd]) == "NO_FINDING/FULL"))
    _ex = duplicate_check("fail", "EXACT duplicate of x.py")
    extra.append(("an EXACT duplicate still fails the verdict",
                  _ex[1] == "fail"
                  and verdict_for([("gate", "pass", ""), _ex]) == "FAIL/FULL"))

    # The DF filter needs a fixture where it can actually DO something, and BOTH ARMS
    # measured. The first version used repetitive generated code, which collapses under
    # identifier normalisation to too few unique shingles -- both arms then fell below the
    # floor and looked identical, so the mutant SURVIVED. This fixture has structural
    # variety, and the probe asserts the filter-OFF arm really does produce the false
    # positives the filter is there to remove.
    _harness = ("def _load(cfg):\n    data = {}\n    for key, val in cfg.items():\n"
                "        if isinstance(val, list):\n            data[key] = [x for x in val if x]\n"
                "        elif isinstance(val, dict):\n            data[key] = _load(val)\n"
                "        else:\n            data[key] = val\n    return data\n\n"
                "def _check(got, want, tol=1e-9):\n    try:\n        delta = abs(got - want)\n"
                "    except TypeError:\n        raise AssertionError('type')\n"
                "    while delta > tol:\n        raise AssertionError(f'{got} != {want}')\n"
                "    return True\n\n"
                "def _report(name, rows):\n    out = []\n    for i, row in enumerate(rows):\n"
                "        prefix = '*' if i % 2 else '-'\n        out.append(f'{prefix} {name} {row}')\n"
                "    return '\\n'.join(out)\n")
    _shapes = [
        "def algo(v):\n    s = 0\n    for x in v:\n        if x > 0:\n            s += x\n"
        "        else:\n            s -= x\n    return s\n",
        "def algo(v):\n    acc = []\n    i = 0\n    while i < len(v):\n        acc.append(v[i] ** 2)\n"
        "        i += 2\n    return sum(acc)\n",
        "def algo(v):\n    try:\n        return max(v) / min(v)\n    except ZeroDivisionError:\n"
        "        return float('inf')\n",
        "def algo(v):\n    seen = set()\n    dup = [x for x in v if x in seen or seen.add(x)]\n"
        "    return sorted(dup, reverse=True)\n",
        "def algo(v):\n    lo, hi = 0, len(v) - 1\n    while lo < hi:\n        v[lo], v[hi] = v[hi], v[lo]\n"
        "        lo += 1\n        hi -= 1\n    return v\n",
    ]

    def _df_arm(frac):
        global DF_FRACTION
        _keep, DF_FRACTION = DF_FRACTION, frac
        try:
            with tempfile.TemporaryDirectory() as td:
                d = Path(td) / "python" / "programming"
                d.mkdir(parents=True)
                fs = []
                for n in range(20):
                    f = d / f"fam_{n}.py"
                    f.write_text(_harness + "\n"
                                 + _shapes[n % len(_shapes)].replace("algo", f"algo_{n}"),
                                 encoding="utf-8")
                    fs.append(f)
                dmf = duplicate_map(fs, {f: "python" for f in fs}, Path(td))
                return sum(1 for f in fs if dmf.get(f, ("", ""))[0] == "flag")
        finally:
            DF_FRACTION = _keep

    # ---- 4Q round 3. Each was a live or demonstrated defect; both arms, always.
    _rs = 'fn main() { let s = r#"a "unwrap()" b"#; let v: Vec<i32> = w.unwrap(); }'
    _rst = strip_noncode(_rs, "rust")[0]
    extra.append(("F1 rust raw string r#\"..\"# with embedded quotes does not leak as code",
                  _rst.count("unwrap") == 1))
    extra.append(("F1 the REAL unwrap() beside it still survives", "w.unwrap()" in _rst))
    _rst2 = strip_noncode('fn f() { let s = r"plain unsafe"; unsafe { g(); } }', "rust")[0]
    extra.append(("F1 rust plain raw string r\"..\" is stripped, real unsafe survives",
                  _rst2.count("unsafe") == 1))

    _br = 'fn main() { let s = br#"a "unwrap()" b"#; let v = w.unwrap(); }'
    extra.append(("4Q-S2 rust BYTE raw string br#\"..\"# does not leak as code",
                  strip_noncode(_br, "rust")[0].count("unwrap") == 1))
    extra.append(("4Q-S2 br\"..\" without # delimiters is still stripped",
                  strip_noncode('fn f() { let s = br"x unsafe"; unsafe { g(); } }',
                                "rust")[0].count("unsafe") == 1))
    _dot = "." + "return" + " " * 26 + "/x/"
    extra.append(("4Q-S1 `.return` at the 32-char window edge is a PROPERTY ACCESS, not the "
                  "keyword — the boundary guard must reject it",
                  not _js_regex_after_kw(_dot, 33)))
    extra.append(("4Q-S1 a bare `return` at the same window edge IS the keyword",
                  _js_regex_after_kw(";" + "return" + " " * 26 + "/x/", 33)))

    # ---- Ver honesty pass. Every field it asked for gets a probe; a routing field nobody
    # can test is a routing field nobody HAS tested.
    # ---- routing. Every probe here names WHICH rule claimed the check, because a probe
    # that only asks "did somebody get it?" passes even after the rule is deleted -- 4Q
    # round 9 F1 found exactly that hole in the flag/fail lane after I had closed it in the
    # subclass lane. Details carry real reason codes now: a check whose detail has no code
    # is a TOOL DEFECT by construction, so a probe cannot pass an empty one by accident.
    _U1D, _U3D = "[NO_RULE_TABLE] x", "[HANG] x"
    _cm = [("a", "pass", ""), ("b", "unverifiable", _U1D), ("c", "unverifiable", _U1D)]
    _tf = triage_fields(_cm, {"U1"})
    extra.append(("Ver-5 an UNVERIFIABLE-only record needs IMPLEMENTATION, not a human",
                  _tf["needs_implementation"] and not _tf["needs_human_judgement"]
                  and not _tf["needs_tool_fix"]))
    _tf2 = triage_fields([("a", "flag", ""), ("b", "pass", "")], set())
    extra.append(("Ver-5/4Q-R9-F1 a FLAGGED record needs a human BY THE FINDING RULE, not by "
                  "the tool-defect lane absorbing it (the hole 4Q found in round 9)",
                  _tf2["needs_review"] and _tf2["needs_human_judgement"]
                  and not _tf2["needs_implementation"] and not _tf2["needs_tool_fix"]))
    # 4Q round 7 F1: I enumerated the cases I had thought of, not every value of the enum.
    # The loop runs over every REASON CODE, not every subclass -- strictly more exhaustive,
    # and it exercises the code->subclass mapping the router now depends on.
    for _code, _sub in sorted(REASON_SUBCLASS.items()):
        _tfx = triage_fields([("a", "pass", ""), ("b", "unverifiable", f"[{_code}] x")],
                             {_sub})
        extra.append((f"4Q-R7 a record whose only problem is {_code}/{_sub} is ROUTED to "
                      f"someone (impl={_tfx['needs_implementation']} "
                      f"pathology={_tfx['needs_pathology_triage']})", _tfx["routed"]))
        # ⛔ and routed BY ITS OWN RULE. Without this clause a deleted subclass rule is
        # absorbed by the tool-defect lane and every probe above still passes -- measured:
        # the mutation harness reported SURVIVED for "U3 dropped from routing".
        extra.append((f"4Q-R8 {_code}/{_sub} is claimed by its OWN routing rule, never by "
                      "the tool-defect lane (which would hide the rule's removal)",
                      not _tfx["needs_tool_fix"]))
        extra.append((f"6E-D3 {_code}/{_sub} goes to exactly ONE of the three lanes, so the "
                      "824-record triage session cannot double-count it",
                      [_tfx["needs_review"], _tfx["needs_pathology_triage"],
                       _tfx["needs_implementation"]].count(True) == 1))
    # 4Q round 8 F1: this loop used to hardcode the three non-clean statuses -- the same
    # shape as the bug it exists to prevent. Derived from STATUSES, so a status added
    # tomorrow is tested tomorrow.
    for _stat in STATUSES:
        if _stat in CLEAN_STATUSES:
            continue
        _d = _U3D if _stat in UNMEASURED_STATUSES else ""
        _tfy = triage_fields([("a", "pass", ""), ("b", _stat, _d)],
                             {"U3"} if _d else set())
        extra.append((f"4Q-R8 a record carrying a {_stat} check needs routing AND gets it "
                      "(loop derived from STATUSES, not hand-listed)",
                      _tfy["needs_routing"] and _tfy["routed"]))
        extra.append((f"4Q-R9-F1 a {_stat} check is claimed by a NAMED rule, never by the "
                      "tool-defect lane", not _tfy["needs_tool_fix"]))
    # 6E design review 3, Q1: an unverifiable check carrying NO reason code is a dropped
    # code or a missing rule -- a defect in THIS TOOL. It used to be routed to a human, who
    # can fix neither. It now routes to the tool-builder and NAMES the check.
    _bare = triage_fields([("a", "pass", ""), ("b", "unverifiable", "no code here")], set())
    extra.append(("6E-D3-Q1 an unverifiable check with NO reason code is a TOOL DEFECT, not "
                  "human triage work",
                  _bare["needs_tool_fix"] and not _bare["needs_human_judgement"]
                  and not _bare["needs_implementation"] and _bare["routed"]))
    extra.append(("6E-D3-Q1 the tool defect NAMES the check and its missing subclass, so a "
                  "reader can tell it from a rule-claimed record",
                  _bare["unclaimed_checks"] == [{"name": "b", "status": "unverifiable",
                                                 "reason_code": None, "subclass": None}]))
    extra.append(("6E-D3-Q2 needs_human_judgement EXCLUDES a tool defect, so an old consumer "
                  "cannot count one as human work",
                  not _bare["needs_human_judgement"]))
    extra.append(("6E-D3-Q1 a caller whose subclasses disagree with the check details RAISES "
                  "-- the two disagreeing about one record is itself a defect",
                  _raises(lambda: triage_fields([("a", "unverifiable", _U1D)], {"U3"}),
                          KeyError)))
    extra.append(("4Q-R8 the routing partition covers STATUSES exactly, so no status can "
                  "belong to none of them",
                  sorted(CLEAN_STATUSES + FINDING_STATUSES + UNMEASURED_STATUSES)
                  == sorted(STATUSES)))
    extra.append(("4Q-R8 the coverage partition covers STATUSES exactly",
                  sorted(MEASURED_STATUSES + UNMEASURED_STATUSES + SKIPPED_STATUSES)
                  == sorted(STATUSES)))
    extra.append(("4Q-R8 a clean record raises no tool defect (it would route every pattern "
                  "in the library to the tool-builder)",
                  not triage_fields([("a", "pass", "")], set())["needs_tool_fix"]))
    extra.append(("4Q-R8 an undeclared status RAISES in triage_fields instead of escaping "
                  "every counter",
                  _raises(lambda: triage_fields([("a", "warn", "")], set()), KeyError)))
    extra.append(("4Q-R8 an undeclared status RAISES in verdict_for instead of falling "
                  "through to the clean verdict",
                  _raises(lambda: verdict_for([("a", "warn", "")]), KeyError)))
    # 4Q round 9 F2: STATUS_VERDICT relies on insertion order for SEVERITY, and only the
    # membership was tested. The ordering itself is a design decision; assert it.
    extra.append(("4Q-R9-F2 severity order: fail beats flag AND unverifiable",
                  verdict_for([("a", "fail", ""), ("b", "flag", "")]) == "FAIL/FULL"
                  and verdict_for([("a", "fail", ""), ("b", "unverifiable", "")])
                  == "FAIL/PARTIAL"))
    extra.append(("4Q-R9-F2 severity order: flag beats unverifiable",
                  verdict_for([("a", "flag", ""), ("b", "unverifiable", "")]) == "FLAG/PARTIAL"))
    extra.append(("4Q-R9-F2 severity order: every finding status beats SKIP",
                  all(not verdict_for([("a", _s, ""), ("b", "skip", "")]).startswith("SKIP")
                      for _s in STATUS_VERDICT)))
    _pf = triage_fields([("a", "fail", "[PARSE_FAIL] broken")], set())
    extra.append(("6E-C3 PARSE_FAIL is declared U3 but EMITTED as fail, so it routes to "
                  "REVIEW, not pathology triage -- documented, not accidental",
                  _pf["needs_review"] and not _pf["needs_pathology_triage"]
                  and not _pf["needs_tool_fix"]))
    extra.append(("6E-C3 a finding-status check carrying a reason code does NOT leak that "
                  "code into the derived subclasses (a caller that thought it did would "
                  "disagree with the router, and that raises)",
                  _raises(lambda: triage_fields([("a", "fail", "[PARSE_FAIL] x")], {"U3"}),
                          KeyError)))
    # ---- THE RENDERER. Eleven rounds of attack went into this module and the renderer had
    # none, and BOTH agents' round-11 findings were in it -- it is what a human actually
    # reads. Fixture: two UNVERIFIABLE records (one dispositioned, one not), one FAIL and
    # one FLAG that each also carry an unverifiable check, and one over-long detail. Every
    # assertion below FAILED against the renderer as it stood before this round.
    with tempfile.TemporaryDirectory() as _rtd:
        _rp = Path(_rtd) / "fixture.jsonl"
        _hdr = {"run": {"total_patterns": 4, "run_date": "2026-08-30", "host": "fixture",
                        "elapsed_s": 1, "library_verify_md5": "x", "toolchains_present": {},
                        "census_mismatches": []}}
        _long = "L" * 400
        # ⛔ THE FIXTURE DERIVES ITS OWN VERDICT FROM ITS OWN CHECKS. The previous version
        # passed the verdict word in by hand, so a record could claim FAIL while carrying a
        # flag check -- a fixture that cannot be inconsistent with the production rule is
        # worth more than one that merely asserts what I typed.
        # `_v` overrides the derived verdict and exists ONLY for the adversarial fixtures:
        # the verdict is a closed enum now, so a hostile verdict string can no longer arrive
        # by derivation -- but the renderer still INDEXES by it, and retiring the injection
        # probe because the happy path stopped producing bad values would be removing a guard
        # for the reason it is passing.
        def _mk(_pid, _disp, _unv, _det="", _st="flag", _extra=0, _v=None):
            _ch = [{"name": "deps", "status": "unverifiable", "detail": "[NO_STDLIB_LIST] x"}]
            if _det:
                _ch.append({"name": "hollow", "status": _st, "detail": _det})
            for _i in range(_extra):
                _ch.append({"name": f"x{_i}", "status": "pass", "detail": ""})
            _tup = [(c["name"], c["status"], c["detail"]) for c in _ch]
            return {"pattern_id": _pid, "path": f"python/{_pid}.py", "language": "python",
                    "verdict": _v if _v is not None else verdict_for(_tup),
                    "axes": {"finding": finding_for(_tup), "coverage": coverage_for(_tup)},
                    "disposition": _disp,
                    "checks": _ch,
                    "unverifiable_checks": _unv,
                    "unverifiable_subclass": ["U2"],
                    "checks_unmeasured": 1, "checks_skipped": 0, "needs_tool_fix": False,
                    "census_mismatches": [], "toolchains_present": {}}
        _uc = [{"name": "deps", "reason_code": "NO_STDLIB_LIST", "subclass": "U2"}]
        # a,b measure NOTHING (coverage NONE); c,d measure 1 and 2 (coverage PARTIAL, and the
        # differing counts force the "checks actually run" figure to print as a SPAN, which is
        # what proves it is derived per record rather than hardcoded.
        _rows = [_mk("a", None, _uc), _mk("b", "WAIVE", _uc),
                 _mk("c", None, _uc, _long, "fail"), _mk("d", None, _uc, _long, "flag", 1)]
        _rp.write_text("\n".join([json.dumps(_hdr)] + [json.dumps(r) for r in _rows]),
                       encoding="utf-8")
        _rout = Path(_rtd) / "out.md"
        _rr = subprocess.run([sys.executable, str(Path(__file__).with_name("audit_report.py")),
                              str(_rp), str(_rout)], capture_output=True, text=True,
                             cwd=str(Path(__file__).parent))
        _rtxt = _rout.read_text(encoding="utf-8") if _rout.exists() else _rr.stderr
        extra.append(("RENDER the renderer runs at all on a synthetic record set",
                      _rout.exists() and _rr.returncode == 0))
        # 4Q R11 F1 / 6E #3: it printed the UNDISPOSITIONED count (1) where it meant the
        # count carrying the verdict (2). Equal on a fresh run, wrong the moment a triage
        # session sets one disposition -- and this report IS that triage session.
        extra.append(("RENDER 4Q-R11-F1 the printed count is the COVERAGE count (4), not the "
                      "undispositioned count (3) -- they diverge the moment a triage session "
                      "sets one disposition, which is what this report IS",
                      "4 records are not FULLY covered" in _rtxt
                      and "3 are still undispositioned" in _rtxt))
        # ⛔ THE OLD PROBE HERE COUNTED THE RECORDS THAT HID THEIR OWN COVERAGE GAP. That gap
        # is now unhideable by construction, so asserting the old arithmetic would be
        # asserting a bug still exists. The replacement asserts the INVARIANT that makes it
        # zero, which is falsifiable: break coverage_for and this fails.
        extra.append(("RENDER Illia-4 NO record can hide an unmeasured check: every record "
                      "with an unverifiable check reports less than FULL coverage",
                      all(axes_of(_r)[1] != "FULL" for _r in _rows
                          if any(_c["status"] == "unverifiable" for _c in _r["checks"]))
                      and "No record hides an unmeasured check" in _rtxt))
        extra.append(("RENDER Illia-5 PARTIAL and NONE are reported as DIFFERENT facts, never "
                      "summed into one 'partially measured' sentence",
                      "2 records were only partially measured" in _rtxt
                      and "NOTHING could be measured: 2" in _rtxt))
        # 6E #4: it asserted the outranked records "report as FLAG". FAIL outranks too, and
        # the shipped sweep is a --gate run, which is exactly how a FAIL lands here.
        # ⛔ CONSISTENT DATA CAN NO LONGER PRODUCE AN OUTRANKED RECORD -- coverage is its own
        # axis. The renderer's branch for one still exists, and a branch that no fixture can
        # reach is a branch nobody is testing, so this drives it with a record that is
        # deliberately INCONSISTENT (an unverifiable check while claiming FULL coverage),
        # which is exactly what a future regression in coverage_for would look like.
        _rows_h = [_mk("h1", None, _uc, _long, "fail"), _mk("h2", None, _uc, _long, "flag")]
        for _rh, _vh in zip(_rows_h, ("FAIL", "FLAG")):
            _rh["axes"]["coverage"] = "FULL"  # the lie under test
            _rh["verdict"] = _vh + "/FULL"
        _fh = Path(_rtd) / "hidden.jsonl"; _oh = Path(_rtd) / "hidden.md"
        _fh.write_text("\n".join([json.dumps(_hdr)] + [json.dumps(x) for x in _rows_h]),
                       encoding="utf-8")
        subprocess.run([sys.executable, str(Path(__file__).with_name("audit_report.py")),
                        str(_fh), str(_oh)], capture_output=True, text=True,
                       cwd=str(Path(__file__).parent))
        _htxt = _oh.read_text(encoding="utf-8") if _oh.exists() else ""
        # ---- 6E REPORT-6E-2AXIS.md, both reader paths. These assert the FIX, not the shape.

        # ---- WAIVERS, RENDERED. The mechanism is only half the guarantee: 6E's rule is that
        # a waived finding stays VISIBLE with its evidence. A renderer that quietly dropped it
        # would satisfy every unit probe above and still lose the finding.
        _wv_hdr = json.loads(json.dumps(_hdr))
        _wv_hdr["run"]["waivers"] = {
            "ledger": "WAIVERS.jsonl", "loaded": 3, "applied": 1,
            "stale": [{"path": "rust/stale.rs", "check": "dangerous_primitives",
                       "waived_sha256": "a" * 64, "live_sha256": "b" * 64}],
            "orphan": [{"path": "go/gone.go", "check": "determinism_markers"}]}
        _wv_rec = {"pattern_id": "demo", "path": "rust/demo.rs", "language": "rust",
                   "verdict": "FLAG/PARTIAL",
                   "axes": {"finding": "FLAG", "coverage": "PARTIAL"},
                   "disposition": "WAIVE",
                   "disposition_ref": "REPORT-6E-TRIAGE.md#1 (6E, 2026-08-30)",
                   "waived_checks": ["dangerous_primitives"],
                   "checks": [{"name": "dangerous_primitives", "status": "flag",
                               "detail": "UNWRAPEVIDENCE panics instead of handling",
                               "waived": {"owner": "6E", "date": "2026-08-30",
                                          "ref": "TRIAGEREF invariant guard",
                                          "construct": "fixed-size slice"}}],
                   "unverifiable_checks": None, "unverifiable_subclass": [],
                   "checks_unmeasured": 0, "checks_skipped": 0, "needs_tool_fix": False,
                   "census_mismatches": [], "toolchains_present": {}}
        _wf = Path(_rtd) / "waived.jsonl"; _wo = Path(_rtd) / "waived.md"
        _wf.write_text(json.dumps(_wv_hdr) + "\n" + json.dumps(_wv_rec) + "\n",
                       encoding="utf-8")
        subprocess.run([sys.executable, str(Path(__file__).with_name("audit_report.py")),
                        str(_wf), str(_wo)], capture_output=True, text=True,
                       cwd=str(Path(__file__).parent))
        _wtxt = _wo.read_text(encoding="utf-8") if _wo.exists() else ""
        # ⛔ THIS PROBE USED TO PASS FOR THE WRONG REASON. It asserted the evidence appeared
        # ANYWHERE on the page -- and it does, in the triage queue -- so deleting the WAIVED
        # table entirely left it green (the mutant scored KILLED-BY-OTHER). Scoped to the
        # section it is actually about.
        _wsec = _wtxt.split("### WAIVED")[1].split("\n## ")[0] if "### WAIVED" in _wtxt else ""
        extra.append(("RENDER WAIVER the waived finding KEEPS ITS EVIDENCE **in the WAIVED "
                      "section itself** — not merely somewhere on the page",
                      "UNWRAPEVIDENCE" in _wsec))
        extra.append(("RENDER WAIVER the reference is printed, so an accepted risk names who "
                      "accepted it and why", "TRIAGEREF" in _wtxt and "6E" in _wtxt))
        extra.append(("RENDER WAIVER the page says in words that a waived finding is STILL a "
                      "finding, so the section cannot read as a clean bill",
                      "still a finding" in _wtxt.lower()))
        extra.append(("RENDER WAIVER a STALE waiver is surfaced as the finding STANDING, not "
                      "hidden", "STALE" in _wtxt and "rust/stale.rs" in _wtxt))
        extra.append(("RENDER WAIVER an ORPHAN waiver is surfaced (fixed pattern, or a typo "
                      "that protects nothing)", "orphan" in _wtxt and "go/gone.go" in _wtxt))
        extra.append(("RENDER WAIVER NEGATIVE ARM: with no waivers at all the section does "
                      "NOT appear, so its presence means something",
                      "Accepted with reason" not in _rtxt))

        # ---- WAIVERS. The mechanism exists to stop a waiver behaving like a pass, so every
        # probe here is aimed at that one failure.
        _wroot = Path(_rtd) / "wlib"; (_wroot / "rust").mkdir(parents=True, exist_ok=True)
        _wfile = _wroot / "rust" / "demo.rs"
        _wfile.write_text("fn main(){ let _ = x.unwrap(); }", encoding="utf-8")
        _wsha = _file_sha256(_wfile)
        def _wrec():
            return {"path": "rust/demo.rs",
                    "axes": {"finding": "FLAG", "coverage": "PARTIAL"},
                    "verdict": "FLAG/PARTIAL", "disposition": None, "disposition_ref": None,
                    "checks": [{"name": "dangerous_primitives", "status": "flag",
                                "detail": "unwrap() — panics instead of handling"},
                               {"name": "determinism_markers", "status": "flag",
                                "detail": "time.Now"},
                               {"name": "hollow", "status": "pass", "detail": "ok"}]}
        def _w(**kw):
            base = {"path": "rust/demo.rs", "check": "dangerous_primitives",
                    "detail": "unwrap() — panics instead of handling",
                    "file_sha256": _wsha, "owner": "6E", "date": "2026-08-30",
                    "ref": "REPORT-6E-TRIAGE.md#1 invariant guard"}
            base.update(kw); return base
        def _wload(rows):
            _f = Path(_rtd) / "w.jsonl"
            _f.write_text("\n".join(json.dumps(r) for r in rows), encoding="utf-8")
            return load_waivers(_f)
        for _missing in ("ref", "owner", "date", "file_sha256"):
            extra.append((f"WAIVER a waiver with no `{_missing}` REFUSES TO LOAD — an accepted "
                          f"risk nobody signed is a silent NO_FINDING under another name",
                          _raises(lambda _m=_missing: _wload([_w(**{_m: ""})]), ValueError)))
        _r_ok = [_wrec()]
        _a, _st, _or = apply_waivers(_r_ok, _wload([_w()]), _wroot)
        _wchk = _r_ok[0]["checks"][0]
        extra.append(("WAIVER a valid waiver attaches owner/date/ref to the finding it names",
                      _a == 1 and _wchk.get("waived", {}).get("owner") == "6E"
                      and _r_ok[0]["disposition"] == "WAIVE"
                      and "REPORT-6E-TRIAGE" in (_r_ok[0]["disposition_ref"] or "")))
        extra.append(("WAIVER ⛔ THE CENTRAL ONE: a waived finding is STILL A FINDING — its "
                      "status stays `flag`, and the finding axis does NOT go clean",
                      _wchk["status"] == "flag"
                      and axes_of(_r_ok[0])[0] == "FLAG"
                      and verdict_for([(c["name"], c["status"], c["detail"])
                                       for c in _r_ok[0]["checks"]]).startswith("FLAG")))
        extra.append(("WAIVER is INSTANCE-SCOPED: waiving one check leaves the other finding "
                      "on the same file untouched",
                      "waived" not in _r_ok[0]["checks"][1]
                      and _r_ok[0]["waived_checks"] == ["dangerous_primitives"]))
        _r_st = [_wrec()]
        _a2, _st2, _ = apply_waivers(_r_st, _wload([_w(file_sha256="0" * 64)]), _wroot)
        extra.append(("WAIVER ⛔ a STALE waiver (the file changed since it was granted) does "
                      "NOT apply and the raw finding STANDS — this is what stops a waiver "
                      "absorbing a DIFFERENT construct added later",
                      _a2 == 0 and len(_st2) == 1
                      and "waived" not in _r_st[0]["checks"][0]
                      and _r_st[0]["disposition"] is None))
        _r_or = [_wrec()]
        _a3, _, _or3 = apply_waivers(_r_or, _wload([_w(check="hollow")]), _wroot)
        extra.append(("WAIVER an ORPHAN waiver (matches no finding) is reported, never "
                      "silently ignored — it is a fixed pattern or a typo, and both matter",
                      _a3 == 0 and len(_or3) == 1))
        _r_np = [_wrec()]
        apply_waivers(_r_np, _wload([_w(check="hollow", detail="ok")]), _wroot)
        extra.append(("WAIVER NEGATIVE ARM: a waiver can never attach to a PASSING check, so "
                      "it cannot be used to annotate something that was never a finding",
                      "waived" not in _r_np[0]["checks"][2]))
        extra.append(("WAIVER an absent ledger is empty, not an error (waivers are opt-in)",
                      load_waivers(Path(_rtd) / "nope.jsonl") == []))

        # ⛔ THE EXIT-2 GUARD WAS UNPROBED AND A MUTANT PROVED IT (see coverage_exit_code).
        _ax = lambda c: {"axes": {"finding": "NO_FINDING", "coverage": c}}
        _g_full = [_ax("FULL"), _ax("FULL")]
        _g_part = [_ax("FULL"), _ax("PARTIAL")]
        _g_none = [_ax("NONE")]
        extra.append(("EXIT-GUARD a partially-covered record forces exit 2",
                      coverage_exit_code(_g_part, False)[0] == 2))
        extra.append(("EXIT-GUARD an unmeasured record forces exit 2",
                      coverage_exit_code(_g_none, False)[0] == 2))
        extra.append(("EXIT-GUARD NEGATIVE ARM: an all-FULL run exits 0, so the 2 above is "
                      "the guard firing and not a constant",
                      coverage_exit_code(_g_full, False)[0] == 0))
        extra.append(("EXIT-GUARD acknowledging clears it, and names the SAME blocking "
                      "records either way (the flag suppresses the exit, not the evidence)",
                      coverage_exit_code(_g_part, True)[0] == 0
                      and coverage_exit_code(_g_part, True)[1]
                      == coverage_exit_code(_g_part, False)[1]))
        extra.append(("EXIT-GUARD a record MISSING the coverage field blocks too -- an "
                      "absent axis is not a FULL one", coverage_exit_code([{}], False)[0] == 2))
        # WIRING ARM: main() must actually honour it. Cheap because the first files audited
        # are python, which is the only fully-covered lane -- so this proves an all-FULL real
        # run exits 0 through the real argv path.
        _eout = Path(_rtd) / "exitcode.jsonl"
        _e_ok = subprocess.run(
            [sys.executable, str(Path(__file__)), "--limit", "3", "--out", str(_eout)],
            capture_output=True, text=True, cwd=str(Path(__file__).parent))
        _e_recs = [json.loads(l) for l in
                   _eout.read_text(encoding="utf-8").splitlines()[1:]] if _eout.exists() else []
        # ⛔ THESE MUST READ A REAL RECORD, NOT A FIXTURE. The first version asserted the
        # shape of `_mk`, a self-test fixture that builds its own dict -- so a mutant that
        # re-added the top-level `finding` to the PRODUCTION record builder in main() scored
        # SURVIVED. A probe over a fixture measures the fixture. `_e_recs` above comes out of
        # a real audit run, so it is the tool's own output being checked.
        extra.append(("6E-2AXIS path 2: a REAL record has NO top-level `finding`/`coverage` "
                      "key, so a consumer reading one alone gets null (a LOUD error) rather "
                      "than a reassuring word that merges measured with unmeasured records",
                      bool(_e_recs)
                      and all("finding" not in r and "coverage" not in r for r in _e_recs)
                      and all((r.get("axes") or {}).get("finding") for r in _e_recs)))
        extra.append(("6E-2AXIS path 2: the compound verdict is still top-level on a REAL "
                      "record, so the CHEAPEST read is the one carrying both halves",
                      bool(_e_recs) and all("/" in (r.get("verdict") or "") for r in _e_recs)))
        extra.append(("EXIT-GUARD WIRING: a real all-FULL run exits 0 through main(), and "
                      "the fixture really is all-FULL (so this is not an empty-set pass)",
                      bool(_e_recs) and all(axes_of(r)[1] == "FULL" for r in _e_recs)
                      and _e_ok.returncode == 0))
        extra.append(("RENDER 6E-R11 an outranked record is named by its ACTUAL verdict "
                      "(FAIL is one of them), not asserted to all be FLAG — driven by a "
                      "record whose coverage contradicts its own checks",
                      "**FAIL/FULL** (1)" in _htxt and "**FLAG/FULL** (1)" in _htxt))
        # 6E #2: exit 2 keys on the UNVERIFIABLE count and never reads `disposition`.
        extra.append(("RENDER 6E-R11 the exit-2 sentence does not promise that "
                      "dispositioning clears it",
                      "does not read `disposition` at all" in _rtxt))
        # 6E #1: Ver's finding 7, live in the renderer -- a hard cut with no marker.
        extra.append(("RENDER 6E-R11 an over-long detail is cut WITH a truncation marker, "
                      "not silently (Ver finding 7, in the renderer this time)",
                      "TRUNCATED" in _rtxt and _long not in _rtxt))
        # 6E round 10, guarded: a record that never carried the field is not a clean record.
        _rp2 = Path(_rtd) / "pre.jsonl"
        for _r in _rows:
            for _k in ("checks_unmeasured", "checks_skipped", "needs_tool_fix"):
                _r.pop(_k, None)
        _rp2.write_text("\n".join([json.dumps(_hdr)] + [json.dumps(r) for r in _rows]),
                        encoding="utf-8")
        _rout2 = Path(_rtd) / "out2.md"
        subprocess.run([sys.executable, str(Path(__file__).with_name("audit_report.py")),
                        str(_rp2), str(_rout2)], capture_output=True, text=True,
                       cwd=str(Path(__file__).parent))
        _rtxt2 = _rout2.read_text(encoding="utf-8") if _rout2.exists() else ""
        # ⛔ 4Q round 12: he inventoried all 14 text-to-page paths and found two more
        # unclipped AFTER I had fixed the two 6E named. Patching instances was losing to
        # this class three times running, so the probe is now an INVARIANT over the whole
        # page: plant an absurd string in every data-derived slot and assert nothing
        # escapes. A future slot added without the funnel fails here, unnamed and unimagined.
        # ⛔ THE PAGE-LEVEL INVARIANT. The first version of this planted a 4000-char
        # string and asserted no line exceeded 700 -- a LENGTH invariant. 6E round 13 built
        # a page proving length was never the grammar: a THREE-character ``` opens a fence
        # that swallows the rest of the document, `<img src=x onerror=...>` arrived byte for
        # byte, and a `\|` shifted a table column (4Q round 13, same hour, different route).
        # Every one of those is far under every limit I had set. So the planted values are
        # now HOSTILE AND SHORT as well as huge, and the assertions are about markdown
        # grammar: no fence, no raw tag, and every table row carrying its header's column
        # count. That last one holds for a slot nobody funnelled, which is the only kind
        # that has ever bitten.
        _huge = "Z" * 4000
        _nasty = "``` <img src=x onerror=y> a\\|b \r\n c |d| \\"
        _rp3 = Path(_rtd) / "huge.jsonl"
        # ⛔ 6E round 14 found the SIXTH slot -- the header metadata line -- and the reason
        # it was invisible was NOT that the renderer missed it: the probe never SEEDED it.
        # "Plant a hostile value in every slot" was a promise kept only for the slots I
        # remembered to name, which is the same overclaim as the round-13 comment one level
        # up. So the seeding is structural now: _poison walks the whole fixture and replaces
        # EVERY string leaf and EVERY dict key, so a field added tomorrow is seeded tomorrow
        # without anyone remembering it. Only the values the renderer looks UP by are spared.
        # ⛔ 4Q round 15 found BOTH of my exemptions wider than their justification.
        # "Keys are schema" is true of a RECORD's field names, which the renderer looks
        # records up by -- and false of a map whose keys ARE the payload
        # (toolchains_present, the coverage map). "verdict is a lookup" is true, and it is
        # ALSO displayed. So: keys are poisoned unless they are known schema names, and a
        # dedicated record below carries a hostile verdict into the one place a verdict is
        # printed rather than indexed.
        _KEEP = {"verdict", "status"} | set(_hdr["run"]) | set(_rows[0]) | {
            "name", "detail", "reason_code", "subclass"}
        def _poison(obj, key=None):
            if isinstance(obj, dict):
                return {(k if k in _KEEP else _nasty + str(k)): _poison(v, k)
                        for k, v in obj.items()}
            if isinstance(obj, list):
                return [_poison(v, key) for v in obj]
            if isinstance(obj, str) and key not in _KEEP:
                return _nasty + obj
            return obj
        _h3 = json.loads(json.dumps(_hdr))
        _h3["run"]["census_mismatches"] = [_huge, _nasty]
        _h3["run"]["judgement_only_classes"] = {_nasty: _huge, "k2": _nasty}
        _h3["run"]["unverifiable_taxonomy"] = {"U1": {"name": _nasty, "remedy": _huge,
                                                      "meaning": _nasty}}
        _h3["run"]["analyser_coverage"] = {"per_check": {_nasty: [_nasty]}}
        # 4Q R15 F2: the toolchain map's KEYS are the payload and reach the page raw.
        _h3["run"]["toolchains_present"] = _poison({"gcc": True, "rustc": False})
        _h3["run"]["checks_not_requested"] = [_nasty]
        # every remaining header string -- host, run_date, library_verify_md5, and anything
        # a later version adds -- gets the hostile value without being named here.
        for _k, _v in list(_h3["run"].items()):
            if isinstance(_v, str):
                _h3["run"][_k] = _nasty + _v
        _r3 = _mk("z", None, _uc, _huge, _v="UNVERIFIABLE")
        _r3["path"] = "python/" + _nasty + ".py"
        _r3["language"] = _nasty
        _r3["needs_tool_fix"] = True
        _r3["unclaimed_checks"] = [{"name": _nasty, "status": "unverifiable",
                                    "reason_code": None, "subclass": None}] * 3
        _r3["census_mismatches"] = [_nasty]
        _r4 = _poison(_mk("y", None, _uc, _nasty, _v="FLAG"))
        _r4["checks"].append({"name": _nasty, "status": "flag", "detail": _nasty})
        # 4Q R15 F1: a verdict cannot be poisoned wholesale (the renderer indexes by it),
        # so ONE record carries a hostile one into hidden_by_verdict, which PRINTS it.
        _r5 = _mk("w", None, _uc, "x", _v="FLAG" + _nasty)
        _rp3.write_text("\n".join([json.dumps(_h3), json.dumps(_r3),
                                    json.dumps(_r4), json.dumps(_r5)]),
                        encoding="utf-8")
        _rout3 = Path(_rtd) / "out3.md"
        subprocess.run([sys.executable, str(Path(__file__).with_name("audit_report.py")),
                        str(_rp3), str(_rout3)], capture_output=True, text=True,
                       cwd=str(Path(__file__).parent))
        _t3 = _rout3.read_text(encoding="utf-8") if _rout3.exists() else ""
        _lines3 = _t3.splitlines()
        # ⛔ PROVENANCE, BOTH ARMS. The page named only the VERIFIER's md5, so a reader could
        # not tell which version of the tool produced the verdicts -- and every red-team round
        # changed the tool. This fixture's header carries NO tool_md5 (it predates the field),
        # so it is the NEGATIVE arm: the renderer must say UNKNOWN out loud rather than print
        # a blank or, worse, hash whatever tool it happens to be running beside. Same shape as
        # the _has_routing guard: a missing measurement is reported, never defaulted.
        extra.append(("RENDER PROVENANCE negative arm: a header with no tool_md5 prints "
                      "UNKNOWN, never a blank and never a fabricated hash",
                      bool(_t3) and "UNKNOWN" in _t3
                      and "md5 ``" not in _t3))
        # ⛔ 4Q R20 O2. SELFTEST_CASES compares STATUS only, and both branches return `fail`,
        # so a status probe cannot tell the informative message from the bare one -- the
        # mutation harness proved it by gutting the branch and surviving. The distinction IS
        # the detail, so the probe has to read the detail.
        _d_hidden = check_doc_behavior('import os\n"""Real description."""\ndef f(): pass\n',
                                       "python", ast.parse(
            'import os\n"""Real description."""\ndef f(): pass\n'))[2]
        _d_none = check_doc_behavior("import os\ndef f(): pass\n", "python",
                                     ast.parse("import os\ndef f(): pass\n"))[2]
        extra.append(("R20-O2 a description that is NOT the module docstring is reported as "
                      "such, not as a bare 'no docstring' — a human sees it and every "
                      "docstring-reading tool does not",
                      "NOT the module docstring" in _d_hidden))
        extra.append(("R20-O2 NEGATIVE ARM: a file with NO description anywhere still gets "
                      "the plain message, so the informative one cannot become the default",
                      "NOT the module docstring" not in _d_none))
        # ⛔ 6E ROUND 20, both findings, both arms. The page's numbers were all exact; what
        # misled was the GLOSS. These probes fix the wording in place so it cannot drift back.
        def _erec(_pid, gate_status, extra_pass=2):
            ch = [{"name": "deps", "status": "unverifiable", "detail": "[NO_STDLIB_LIST] x"},
                  {"name": "gate", "status": gate_status, "detail": "g"},
                  {"name": "determinism_repeat", "status": gate_status, "detail": "d"}]
            ch += [{"name": f"c{i}", "status": "pass", "detail": "ok"}
                   for i in range(extra_pass)]
            _tp = [(c["name"], c["status"], c.get("detail", "")) for c in ch]
            return {"pattern_id": _pid, "path": f"python/{_pid}.py", "language": "python",
                    "verdict": verdict_for(_tp),
                    "axes": {"finding": finding_for(_tp), "coverage": coverage_for(_tp)},
                    "disposition": None, "checks": ch,
                    "unverifiable_checks": _uc, "unverifiable_subclass": ["U2"],
                    "checks_unmeasured": 1, "checks_skipped": 2, "needs_tool_fix": False,
                    "census_mismatches": [], "toolchains_present": {}}
        def _render(_name, _rows_in):
            _f = Path(_rtd) / (_name + ".jsonl"); _o = Path(_rtd) / (_name + ".md")
            _f.write_text("\n".join([json.dumps(_hdr)] + [json.dumps(x) for x in _rows_in]),
                          encoding="utf-8")
            subprocess.run([sys.executable, str(Path(__file__).with_name("audit_report.py")),
                            str(_f), str(_o)], capture_output=True, text=True,
                           cwd=str(Path(__file__).parent))
            return _o.read_text(encoding="utf-8") if _o.exists() else ""
        _t_noexec = _render("noexec", [_erec("a", "skip"), _erec("b", "skip", 3)])
        _t_exec   = _render("exec",   [_erec("a", "pass"), _erec("b", "pass", 3)])
        extra.append(("RENDER 6E-R20 F2: when NOTHING was executed the page says so — gate "
                      "and determinism_repeat skipped on every record",
                      "NOTHING WAS EXECUTED" in _t_noexec))
        extra.append(("RENDER 6E-R20 F2 NEGATIVE ARM: when the gate DID run, the banner must "
                      "NOT appear — a false 'nothing executed' is its own lie",
                      bool(_t_exec) and "NOTHING WAS EXECUTED" not in _t_exec))
        # ⛔ ONE FIXTURE COULD NOT TELL DERIVED FROM CONSTANT. A mutant that hardcoded the
        # span to "2-3" SURVIVED, because 2-3 is exactly what this fixture's records really
        # produce. A second fixture with a different true span is what makes the assertion
        # discriminating: no constant can satisfy both.
        _t_span2 = _render("span2", [_erec("a", "skip", 5), _erec("b", "skip", 9)])
        _head_txt = _render("cov_head", [_erec("a", "skip"), _erec("b", "skip", 3)])
        _ix_cov = _head_txt.find("were NOT fully measured")
        _ix_tbl = _head_txt.find("| **NO_FINDING**")
        extra.append(("6E-2AXIS path 1: the COVERAGE tally is the headline and appears BEFORE "
                      "the verdict table, so the gap is read first and NO_FINDING is what a "
                      "reader must get past",
                      _ix_cov != -1 and _ix_tbl != -1 and _ix_cov < _ix_tbl))

        extra.append(("RENDER 6E-R20 F1: partial coverage is explained as COVERAGE, and the "
                      "count of checks that DID run is derived from the records, not "
                      "hardcoded — two fixtures with DIFFERENT true spans (2-3 and 5-9) must "
                      "each print their own, which no constant can do",
                      "What PARTIAL coverage means here" in _t_noexec
                      and "2-3 checks actually run" in _t_noexec
                      and "5-9 checks actually run" in _t_span2))
        extra.append(("RENDER 6E-R20 F1: the one-line gloss no longer says only 'could not "
                      "measure it', which outranked six passes and read as unexamined",
                      "the tool could not measure it" not in _t_noexec))
        _rp6 = Path(_rtd) / "prov.jsonl"
        _h6 = json.loads(json.dumps(_hdr))
        _h6["run"]["tool"] = "library_audit.py"
        _h6["run"]["tool_md5"] = "deadbeefdeadbeefdeadbeefdeadbeef"
        _h6["run"]["run_id"] = "20260830T000000-deadbeef"
        _rp6.write_text("\n".join([json.dumps(_h6),
                                   json.dumps(_mk("p", None, _uc, "x", _v="FLAG"))]),
                        encoding="utf-8")
        _rout6 = Path(_rtd) / "out6.md"
        subprocess.run([sys.executable, str(Path(__file__).with_name("audit_report.py")),
                        str(_rp6), str(_rout6)], capture_output=True, text=True,
                       cwd=str(Path(__file__).parent))
        _t6 = _rout6.read_text(encoding="utf-8") if _rout6.exists() else ""
        extra.append(("RENDER PROVENANCE positive arm: the page names the PRODUCING tool and "
                      "its md5, so a report can be traced to the version that made it",
                      "deadbeefdeadbeefdeadbeefdeadbeef" in _t6
                      and "library_audit.py" in _t6))
        _over = [ln[:50] for ln in _lines3 if len(ln) > 700]
        extra.append(("RENDER 4Q-R12 no data-derived value reaches the page UNCLIPPED "
                      "(length arm): %r" % (_over[:2],), bool(_t3) and not _over))
        extra.append(("RENDER 4Q-R12 the tool-defects cell is FORMATTED, never a raw python "
                      "repr of a list of dicts",
                      "[{'name'" not in _t3 and "TRUNCATED" in _t3))
        # 6E R13 / 4Q R13 F2: the renderer emits NO fence of its own, so one in the output
        # can only have come from data, and it swallows every section below it.
        extra.append(("RENDER 6E-R13 a ``` planted in every slot NEVER opens a fence — the "
                      "renderer writes no fences, so one in the page came from data and "
                      "swallows the rest of the document", "```" not in _t3))
        # 6E R13: uncontrolled inline HTML.
        extra.append(("RENDER 6E-R13 no raw `<` survives to the page (an <img onerror=> "
                      "arrived byte for byte before this)", "<" not in _t3))
        extra.append(("RENDER 6E-R13 a raw carriage return never reaches the page",
                      "\r" not in _t3))
        # ⛔ 4Q R13 F1 + 6E R13: the COLUMN-COUNT invariant. This is the one that holds for
        # a path nobody funnelled: every row of a table must carry its header's column
        # count, so any live separator that arrives from data breaks it here.
        def _cols(ln):
            n, i = 0, 0
            while i < len(ln):
                if ln[i] == "\\":
                    i += 2
                    continue
                if ln[i] == "|":
                    n += 1
                i += 1
            return n
        _bad_rows, _hdr_cols = [], None
        for _ln in _lines3:
            if _ln.startswith("|"):
                if _hdr_cols is None:
                    _hdr_cols = _cols(_ln)
                elif set(_ln.replace("|", "").replace("-", "").replace(":", "")
                         .strip()) == set():
                    continue
                elif _cols(_ln) != _hdr_cols:
                    _bad_rows.append((_cols(_ln), _hdr_cols, _ln[:50]))
            else:
                _hdr_cols = None
        extra.append(("RENDER 4Q-R13-F1 every table row carries its header's column count, "
                      "so a live `|` arriving from data cannot silently move every number "
                      "under the wrong heading: %r" % (_bad_rows[:2],), not _bad_rows))

        extra.append(("RENDER 6E-R10 a pre-routing JSONL reports UNKNOWN, never zero, and "
                      "quotes no coverage number at all",
                      "UNKNOWN, not zero" in _rtxt2
                      and "had EVERY check run" not in _rtxt2))

    _clean = triage_fields([("a", "pass", ""), ("b", "skip", "")], set())
    extra.append(("4Q-R7 a clean record needs NO routing (the invariant does not cry wolf)",
                  not _clean["needs_routing"] and not _clean["routed"]))
    _mix = [("a", "pass", ""), ("b", "skip", ""), ("c", "unverifiable", _U1D),
            ("d", "flag", "")]
    _tfm = triage_fields(_mix, {"U1"})
    extra.append(("4Q-R7-O1 measured + unmeasured + skipped == every check, so the coverage "
                  "ratio cannot overstate itself",
                  _tfm["checks_measured"] + _tfm["checks_unmeasured"]
                  + _tfm["checks_skipped"] == len(_mix)))
    # 6E design review 3, Q3: stated as how much could NOT be measured. "unverified 1/4"
    # cannot be misread as a pass; "measured 3/4" can.
    extra.append(("6E-D3-Q3 the coverage axis is stated as UNVERIFIED, so it cannot be read "
                  "as a pass, and it matches the counters",
                  _tfm["unverified"] == "1/4"
                  and _tfm["unverified"].split("/")[0] == str(_tfm["checks_unmeasured"])))
    extra.append(("6E-D3-Q3 the coverage axis does NOT move the verdict (rejecting "
                  "PASS_WITH_GAPS a second time)", verdict_for(_mix).startswith("FLAG")))
    # 4Q round 8 F2: one hand-written needle ("A PASS") caught one phrasing and missed
    # three others ("silent PASS", "becomes a PASS", "false PASS"). A needle is a guess.
    # This walks EVERY string literal the module can emit -- comments are excluded by the
    # parser, and a literal that discusses the rename must name the new verdict.
    # ...and it must walk the RENDERER too. The reader never opens this module; they read
    # what audit_report.py prints. Scoping the probe to my own file left two stale
    # user-facing strings alive, including a column heading (found while briefing 4Q R9).
    _P = "PA" + "SS"
    _stale = []
    for _mod in (Path(__file__), Path(__file__).with_name("audit_report.py")):
        if not _mod.exists():
            _stale.append((_mod.name, "MISSING — cannot be checked, so it is not clean"))
            continue
        try:
            _tree = ast.parse(_mod.read_text(encoding="utf-8"))
        except SyntaxError as _e:
            # MEASURED on .8: audit_report.py used a backslash inside an f-string, legal on
            # 3.12 and a SyntaxError on 3.10, so this probe took the WHOLE self-test down on
            # the machine the crew runs it on. A check that could not run is not a pass.
            _stale.append((_mod.name, "UNPARSEABLE by this interpreter (%s) — the check did "
                                      "NOT run, so it cannot report clean" % _e))
            continue
        for _n in ast.walk(_tree):
            if (isinstance(_n, ast.Constant) and isinstance(_n.value, str)
                    and re.search(r"\b" + _P + r"\b", _n.value)
                    and "NO_FINDING" not in _n.value):
                _stale.append((_mod.name, _n.lineno, _n.value[:60]))
    _stale.sort()
    extra.append(("Ver-1/4Q-R8-F2 NO string literal in the audit layer OR its renderer "
                  "still uses the old verdict name (ast walk over every literal in both "
                  "modules, not one hand-written needle): %r" % (_stale[:3],), not _stale))

    _tf3 = triage_fields([("a", "flag", ""), ("b", "unverifiable", _U1D)], {"U1"})
    extra.append(("Ver-5 a record that is BOTH needs both, not one or the other",
                  _tf3["needs_human_judgement"] and _tf3["needs_implementation"]))
    extra.append(("Ver-6 the measured/unmeasured ratio is carried so a reader sees the gap "
                  "WITHOUT the verdict going green",
                  _tf["checks_measured"] == 1 and _tf["checks_unmeasured"] == 2))
    # ⛔ VER-6 KEPT ITS TEETH THROUGH THE TWO-AXIS REWRITE. Ver's ruling was that a
    # half-unmeasured record must never READ AS a clean NO_FINDING. It used to assert the
    # word UNVERIFIABLE; that word was the wrong fix (it claimed nothing was measured when
    # 7 checks had run clean). The RULING is unchanged and is asserted directly: the verdict
    # of a half-unmeasured record is not the bare clean verdict, and it still carries the gap.
    extra.append(("Ver-6 a half-unmeasured record NEVER reads as a clean NO_FINDING "
                  "(rejecting PASS_WITH_GAPS: it would soften the one signal 6E "
                  "built the taxonomy to protect)",
                  verdict_for(_cm) != "NO_FINDING/FULL"
                  and verdict_for(_cm).endswith("/PARTIAL")
                  and coverage_for(_cm) == "PARTIAL"))
    extra.append(("Ver-6b the gap is inside the verdict STRING, so a consumer that reads "
                  "only `verdict` cannot drop it",
                  "PARTIAL" in verdict_for(_cm)))
    extra.append(("Ver-1 an all-clean record is NO_FINDING, not PASS",
                  verdict_for([("a", "pass", "")]) == "NO_FINDING/FULL"))
    # Illia 2026-08-30: the defect that started the rewrite. A file clean on everything the
    # tool CAN run must not be labelled with a word meaning "nothing was measured".
    _clean_partial = [("hollow", "pass", ""), ("dangerous_primitives", "pass", ""),
                      ("deps", "unverifiable", _U1D)]
    extra.append(("ILLIA-1 a non-python file that is CLEAN on every check that ran is not "
                  "called UNVERIFIABLE -- it is NO_FINDING/PARTIAL",
                  verdict_for(_clean_partial) == "NO_FINDING/PARTIAL"))
    extra.append(("ILLIA-2 UNVERIFIABLE-as-coverage is reserved for a record where NOTHING "
                  "was measured, and nothing else",
                  coverage_for([("deps", "unverifiable", _U1D)]) == "NONE"
                  and coverage_for(_clean_partial) == "PARTIAL"))
    extra.append(("ILLIA-3 the finding axis is INDEPENDENT of coverage: identical findings "
                  "with different coverage differ only in the coverage half",
                  finding_for(_clean_partial) == finding_for([("hollow", "pass", "")])
                  == "NO_FINDING"))
    extra.append(("Ver-7 short evidence is untouched", clip_evidence("abc") == "abc"))
    _long = clip_evidence("x" * 5000)
    extra.append(("Ver-7 long evidence is MARKED as truncated, not silently cut",
                  len(_long) <= 1200 and _long.endswith("…[TRUNCATED, see checks]")))

    # 4Q round 6: a reason code that misnames its own cause misroutes the remedy.
    _unparseable = "def f(:\n    return 1\n"
    for _fn2, _nm in ((check_dangerous, "dangerous_primitives"),
                      (check_determinism_markers, "determinism_markers"),
                      (check_abs_paths, "hardcoded_abs_path"),
                      (check_hollow, "hollow")):
        _r = _fn2(_unparseable, "python", None)
        _c2, _s2 = reason_of(_r[2])
        extra.append((f"4Q-R6 unparseable PYTHON in {_nm} is U3 PARSE_FAIL (the FILE is "
                      f"broken), never U1 NO_ANALYSER (python HAS an analyser) "
                      f"— got {_r[1]}/{_c2}/{_s2}",
                      _r[1] == "fail" or (_c2 == "PARSE_FAIL" and _s2 == "U3")))
    _r = check_dangerous("x", "cobol", None)
    _c2, _s2 = reason_of(_r[2])
    extra.append(("4Q-R6 a genuinely unknown lane is still U1, not PARSE_FAIL "
                  f"— got {_c2}/{_s2}", _s2 == "U1"))

    _hash = "#" + "return" + " " * 26 + "/foo/"
    extra.append(("4Q-S1 `#return` at the window edge is a PRIVATE FIELD, not the keyword",
                  not _js_regex_after_kw(_hash, 33)))
    extra.append(("4Q-S1 `#return` INSIDE the window is also not the keyword",
                  not _js_regex_after_kw("x.#return /foo/", 10)))
    extra.append(("4Q-S1 the private field does not swallow the code after it",
                  "eval(" in strip_noncode(
                      "#" + "return" + " " * 26 + "/foo; eval('1'); /bar/ x",
                      "javascript")[0]))

    _cpp = '#include <cstdlib> /* uses system() */\nint main(){ return 0; }\n'
    extra.append(("F2 a /* */ comment on a restored #include line does not leak",
                  "system(" not in strip_noncode(_cpp, "cpp")[0]))
    extra.append(("F2 the #include itself is still restored",
                  "cstdlib" in strip_noncode(_cpp, "cpp")[0]))

    _js = "function f() { return /['\"]/g; eval('1'); }\n"
    extra.append(("F3 a JS regex after `return` does not swallow the code after it",
                  "eval(" in strip_noncode(_js, "javascript")[0]))
    extra.append(("F3 a JS DIVISION after an identifier is still not read as a regex",
                  "eval(" in strip_noncode("var r = a / b; eval('1');\n", "javascript")[0]))

    _go = 'package main\nimport "http://example.com/exec"\n'
    extra.append(("F5 an import path containing // is not truncated at it",
                  "exec" in strip_noncode(_go, "go")[0]))
    extra.append(("F5 a REAL // comment on an import line is still stripped",
                  "crypto/md5" not in
                  strip_noncode('package main\nimport "fmt" // crypto/md5\n', "go")[0]))

    extra.append(("F4 a KNOWN_FINDING flags the LANE it was verified in",
                  check_known_findings("", "python", None,
                                       stem="atomic_snapshot")[1] == "flag"))
    extra.append(("F4 it does NOT flag the same stem in an unverified lane",
                  check_known_findings("", "go", None,
                                       stem="atomic_snapshot")[1] == "pass"))

    # ---- 6E: the EXHAUSTIVE (check x lane) matrix. Every cell, every run.
    _SAMPLE = {
        "python": "def f(x):\n    return x\n\n\nassert f(1) == 1\n",
        "cpp": "#include <cassert>\nint main(){ assert(1 == 1); return 0; }\n",
        "go": "package main\n\nimport \"fmt\"\n\nfunc main(){ fmt.Print(1) }\n",
        "rust": "fn main() { assert!(1 == 1); }\n",
        "r": "stopifnot(1 == 1)\n",
        "javascript": "if (1 !== 1) { throw new Error(\"x\"); }\n",
        "cobol": "IDENTIFICATION DIVISION.\n",      # a lane the tool has never heard of
    }
    # Positive samples: each must trip the check it is aimed at. A dirty sample carries a
    # dangerous primitive, a nondeterminism marker AND an absolute path, so one sample serves
    # the three all-lane checks; `hollow` needs the opposite (a file with no assertion), and
    # the python-only checks each need their own defect.
    _DIRTY = {
        "python": 'import random\nx = random.random()\neval("1")\np = "/home/u/f"\n',
        "cpp": '#include <cstdlib>\nint main(){ system("x"); rand();\n'
               '  const char* p = "/home/u/f"; return 0; }\n',
        "go": 'package main\n\nimport (\n\t"os/exec"\n\t"math/rand"\n)\n\n'
              'func main(){ p := "/home/u/f"; _ = p }\n',
        "rust": 'fn main() { unsafe { g(); } let x = rand::random::<u8>();\n'
                '  let p = "/home/u/f"; }\n',
        "r": 'x <- runif(1)\nsystem("ls")\np <- "/home/u/f"\n',
        "javascript": 'eval("1");\nconst x = Math.random();\nconst p = "/home/u/f";\n',
    }
    _NOASSERT = {
        "python": "def f():\n    return 1\n",
        "cpp": "int main(){ return 0; }\n",
        "go": "package main\n\nfunc main(){ }\n",
        "rust": "fn main() { }\n",
        "r": "f <- function(x) x\n",
        "javascript": "function f(){ return 1; }\n",
    }
    _PY_POSITIVE = {"assert_nonvacuous": "assert 1 == 1\n", "importable": "print(1)\n",
                    "doc_behavior": "x = 1\n"}
    # `deps` is the one check whose positive is LANE-SPECIFIC: a third-party import is
    # spelled differently in each of the six, so one python fixture cannot serve them.
    # Feeding `import numpy` to the cpp arm would return `pass` and the MATRIX+ probe would
    # (correctly) fail -- these exist so the probe passes for the RIGHT reason.
    # Like deps, C4's positive is LANE-SPECIFIC: a vacuous assertion is spelled differently
    # in each lane, and `assert 1 == 1` is not valid in any of the other five.
    _C4_POSITIVE = {
        "python":     "assert 1 == 1\n",
        "cpp":        "int main(){ assert(1 == 1); return 0; }\n",
        "go":         "package main\nfunc main(){ if 1 != 1 { os.Exit(1) } }\n",
        "rust":       "fn main(){ assert_eq!(1, 1); }\n",
        "r":          "stopifnot(TRUE)\n",
        "javascript": 'if (1 !== 1) { throw new Error("x"); }\n',
    }
    _DEPS_POSITIVE = {
        "python":     "import numpy\n",
        "cpp":        "#include <boost/asio.hpp>\nint main(){ return 0; }\n",
        "go":         'package main\n\nimport "github.com/pkg/errors"\n\nfunc main(){}\n',
        "rust":       "use serde::Serialize;\nfn main() { }\n",
        "r":          "library(dplyr)\n",
        "javascript": 'const _ = require("lodash");\n',
    }
    _byname = {f.__name__: f for f in FILE_CHECKS}
    _cells = _gaps = 0
    for _cname, _lanes in sorted(ANALYSER_COVERAGE.items()):
        _fn = next(f for f in FILE_CHECKS if f(_SAMPLE["python"], "python",
                                               ast.parse(_SAMPLE["python"]))[0] == _cname)
        for _lane in list(LANES) + ["cobol"]:
            _cells += 1
            _tree = ast.parse(_SAMPLE[_lane]) if _lane == "python" else None
            try:
                _n, _st, _d = _fn(_SAMPLE[_lane], _lane, _tree)
            except Exception as _e:
                extra.append((f"MATRIX {_cname} x {_lane}: CRASHED ({type(_e).__name__})",
                              False))
                continue
            _code, _sub = reason_of(_d) if _st == "unverifiable" else (None, None)
            if _lane in _lanes:
                extra.append((f"MATRIX {_cname} x {_lane}: an analyser is declared, so it "
                              f"must NOT report U1 no-analyser (got {_st}/{_code})",
                              not (_st == "unverifiable" and _sub == "U1")))
                # POSITIVE ARM (6E conformance pass, 2026-08-30). The clean arm above only
                # says the cell is not U1 -- and `pass` is not U1 either, so a cell that
                # measures NOTHING sailed through it. 10 of 28 covered cells had no probe
                # that could tell "analysed and found nothing" from "did not analyse".
                # Feed each covered cell something it MUST catch.
                if _cname == "hollow":
                    _pos = _NOASSERT[_lane]
                elif _cname == "deps":
                    _pos = _DEPS_POSITIVE[_lane]
                elif _cname == "assert_nonvacuous":
                    _pos = _C4_POSITIVE[_lane]
                elif _cname in _PY_POSITIVE:
                    _pos = _PY_POSITIVE[_cname]
                else:
                    _pos = _DIRTY[_lane]
                _pt = ast.parse(_pos) if _lane == "python" else None
                try:
                    _, _pst, _pd = _fn(_pos, _lane, _pt)
                except Exception as _e:
                    _pst, _pd = f"CRASH:{type(_e).__name__}", str(_e)
                extra.append((f"MATRIX+ {_cname} x {_lane}: the analyser must actually "
                              f"MEASURE — a sample it should catch must not come back pass "
                              f"(got {_pst}: {_pd[:60]})", _pst in ("flag", "fail")))
            else:
                _gaps += 1
                extra.append((f"MATRIX {_cname} x {_lane}: NO analyser declared, so it must "
                              f"be unverifiable/U1 and never pass (got {_st}/{_code})",
                              _st == "unverifiable" and _sub == "U1"))
    extra.append((f"MATRIX is exhaustive: {_cells} cells covered "
                  f"({len(ANALYSER_COVERAGE)} checks x {len(LANES) + 1} lanes), "
                  f"{_gaps} of them declared analyser-less",
                  _cells == len(ANALYSER_COVERAGE) * (len(LANES) + 1) and _gaps > 0))

    # ---- C4 non-python: BOTH ARMS, and the POLARITY trap ---------------------------------
    # The dangerous error here is the inverted one: reading `if (1 != 1) { os.Exit(1) }` as a
    # good assertion and `assert(1 == 1)` as a bad one. Each lane is probed in both
    # directions, and the `live` arm is what stops this from becoming an accusation machine.
    for _lane9, _dead9, _live9 in (
        ("cpp", "int main(){ assert(1 == 1); }\n", "int main(){ assert(x == 1); }\n"),
        ("rust", "fn main(){ assert_eq!(1, 1); }\n", "fn main(){ assert_eq!(got, 1); }\n"),
        ("rust", "fn main(){ assert!(true); }\n", "fn main(){ assert!(ok); }\n"),
        ("r", "stopifnot(TRUE)\n", "stopifnot(x == 1)\n"),
        ("javascript", 'if (1 !== 1) { throw new Error("x"); }\n',
                       'if (a !== 1) { throw new Error("x"); }\n'),
        ("go", "package main\nfunc main(){ if 1 != 1 { os.Exit(1) } }\n",
               "package main\nfunc main(){ if got != 1 { os.Exit(1) } }\n"),
    ):
        _sd = check_assert_nonvacuous(_dead9, _lane9, None)
        _sl = check_assert_nonvacuous(_live9, _lane9, None)
        extra.append((f"C4-{_lane9} an assertion on two LITERALS is caught "
                      f"(got {_sd[1]}: {_sd[2][:44]})", _sd[1] in ("fail", "flag")))
        extra.append((f"C4-{_lane9} the SAME assertion on a variable is left alone — the "
                      f"check is not an accusation machine (got {_sl[1]})", _sl[1] == "pass"))
    # POLARITY: an always-TRUE guard FIRES every time; it is a failure-path marker, not
    # decoration. Reading it as vacuous would be the inverted verdict.
    _pol = check_assert_nonvacuous('if (1 === 1) { throw new Error("x"); }\n', "javascript", None)
    extra.append((f"C4-js an always-TRUE guard is a failure-path MARKER, not a vacuous "
                  f"assertion (got {_pol[1]}: {_pol[2][:40]})", _pol[1] == "pass"))
    _polc = check_assert_nonvacuous("int main(){ assert(1 == 2); }\n", "cpp", None)
    extra.append((f"C4-cpp assert(1 == 2) is a MARKER (it always fires), not vacuous "
                  f"(got {_polc[1]})", _polc[1] == "pass"))
    # ⛔ WHY THE LITERAL-ONLY GUARD IS NOT REDUNDANT WITH _c4_fold's except-branch.
    # MEASURED 2026-09-02: a mutant deleting the guard SURVIVED at first, because for any
    # expression containing an identifier `_c4_fold` already fails with NameError and the
    # expression is counted live. But the two disagree on expressions with NO identifier
    # that python CAN still evaluate — `"abc"[0] == "a"` and `[1,2][0] == 1` fold to True.
    # Dropping the guard would call those vacuous, and THAT IS THE BUG: _c4_fold evaluates
    # under PYTHON semantics, and these are cpp/go/rust/r/js files. Indexing, truthiness and
    # array literals do not mean the same thing across those languages, so the check must
    # only fold where the languages genuinely agree — literal arithmetic and comparison.
    # The guard is what confines it to that, and these two probes are what defend the guard.
    for _sub in ('int main(){ assert("abc"[0] == \'a\'); }\n',
                 "int main(){ assert([1,2][0] == 1); }\n"):
        _r5 = check_assert_nonvacuous(_sub, "cpp", None)
        extra.append((f"C4 a SUBSCRIPT expression is out of the declared literal-only scope "
                      f"and is left live — the tool does not judge foreign source by python "
                      f"semantics (got {_r5[1]})", _r5[1] == "pass"))
    extra.append(("C4 a file with no assertion at all is SKIP, deferred to the hollow check",
                  check_assert_nonvacuous("int main(){ return 0; }\n", "cpp", None)[1] == "skip"))
    extra.append(("C4 an assertion named only in a COMMENT is not an assertion",
                  check_assert_nonvacuous("// assert(1 == 1);\nint main(){ assert(x); }\n",
                                          "cpp", None)[1] == "pass"))

    # ---- 4Q ROUND 20: five measured defects, five regression probes ---------------------
    # Each input below is 4Q's verbatim discriminating case. Four were FALSE POSITIVES
    # (the expensive direction: an accusation against correct code) and one a false
    # negative. None of them came from my own fixtures — I looked for exactly these and
    # did not find them.
    for _lbl4, _lane4, _src4, _fn4, _want4 in (
        ("F1 a POSIX system header is not a third-party package", "cpp",
         "#include <arpa/inet.h>\n#include <cstdint>\nint main(){ return htonl(1); }\n",
         "deps", "pass"),
        ("F2 an R `pkg::` inside a STRING is prose, not an import", "r",
         'msg <- "Tip: use dplyr::filter to subset data frames"\ncat(msg)\n',
         "deps", "pass"),
        ("F3 a C++ string-literal comparison must NOT be folded by python semantics "
         "(C++ compares pointers, so the assert CAN fire)", "cpp",
         '#include <cassert>\nint main(){ assert("x" == "x"); return 0; }\n',
         "assert_nonvacuous", "pass"),
        ("F4 a JS `from \"pkg\"` inside a STRING is prose, not an import", "javascript",
         """const h = 'To load express: from "express" import { Router }';\n""",
         "deps", "pass"),
        ("F5 rust `use ::serde::X` is crate-relative and IS third-party", "rust",
         "use ::serde::Deserialize;\nfn main(){}\n", "deps", "flag"),
    ):
        _got4 = (check_deps if _fn4 == "deps" else check_assert_nonvacuous)(_src4, _lane4, None)
        extra.append((f"4Q-R20 {_lbl4} (got {_got4[1]}: {_got4[2][:40]})",
                      _got4[1] == _want4))
    # The other half of F2/F4: stripping prose must not cost a REAL import. Every one of
    # these targets is a string literal, and each must still be found.
    for _lane4b, _src4b in (
        ("r", "library(dplyr)\n"), ("r", 'library("dplyr")\n'),
        ("javascript", 'const _ = require("lodash");\n'),
        ("javascript", 'import x from "lodash";\n'),
        ("go", 'package main\nimport "github.com/pkg/errors"\nfunc main(){}\n'),
    ):
        extra.append((f"4Q-R20 stripping prose does not lose a REAL {_lane4b} import "
                      f"({_src4b.strip().splitlines()[-1][:34]!r})",
                      check_deps(_src4b, _lane4b, None)[1] == "flag"))

    # ⛔ THE GROUPED GO IMPORT — a regression I introduced with 4Q's F2/F4 fix and did not
    # catch, because my own check used the single-line form. 6E's corpus caught it within
    # minutes. The grouped form is the IDIOMATIC one, so this was a false negative on most
    # real go files. Both arms below, plus a prose control STRONGER than the one that
    # started this: a string containing a complete import statement.
    for _lbl0, _src0, _want0 in (
        ("a GROUPED import ( ... ) block finds the third-party path",
         'package main\n\nimport (\n\t"fmt"\n\t"gopkg.in/yaml.v3"\n)\nfunc main(){}\n', "flag"),
        ("a single-line import still works",
         'package main\nimport "github.com/pkg/errors"\nfunc main(){}\n', "flag"),
        ("a GROUPED stdlib-only block is silent",
         'package main\n\nimport (\n\t"fmt"\n\t"os/exec"\n)\nfunc main(){}\n', "pass"),
        ("prose naming a module path is not an import",
         'package main\nvar s = "see github.com/x/y for docs"\nfunc main(){}\n', "pass"),
        ("prose CONTAINING a whole import statement is still not an import",
         'package main\nvar s = "use import \\"github.com/evil/x\\" here"\nfunc main(){}\n', "pass"),
    ):
        _g0 = check_deps(_src0, "go", None)
        extra.append((f"C6-go {_lbl0} (got {_g0[1]}: {_g0[2][:38]})", _g0[1] == _want0))

    # ---- C6 non-python: the FALSE-POSITIVE arm ------------------------------------------
    # MATRIX+ proves each lane's rule can FIRE. Nothing above proves it stays silent on a
    # standard import -- and a `deps` rule that flags the standard library would mark most
    # of 1,150 non-python patterns and look strict while being useless. That is trap 3 from
    # `sanitizer-detonation`: a checker red-teamed only with bad controls blocks correct
    # work. Each pair below is (source, must_flag).
    for _lane6, _cases in {
        "cpp": [('#include <vector>\n#include <sys/wait.h>\nint main(){return 0;}\n', False),
                ('#include "local_helper.h"\nint main(){return 0;}\n', False),
                ('#include <boost/asio.hpp>\nint main(){return 0;}\n', True)],
        "go":  [('package main\nimport (\n\t"fmt"\n\t"os/exec"\n)\nfunc main(){}\n', False),
                ('package main\nimport "github.com/x/y"\nfunc main(){}\n', True),
                ('package main\nimport f "gopkg.in/yaml.v2"\nfunc main(){}\n', True)],
        "rust": [("use std::collections::HashMap;\nuse crate::helper;\nfn main(){}\n", False),
                 ("extern crate serde;\nfn main(){}\n", True)],
        "javascript": [('const fs = require("fs");\nconst p = require("node:path");\n'
                        'const h = require("./helper");\n', False),
                       ('import x from "lodash";\n', True)],
        "r":  [('x <- stats::median(c(1,2))\nlibrary(utils)\n', False),
               ('library(dplyr)\n', True)],
    }.items():
        for _src6, _want6 in _cases:
            _n6, _st6, _d6 = check_deps(_src6, _lane6, None)
            extra.append((f"C6-{_lane6} {'flags' if _want6 else 'is SILENT on'} "
                          f"{_src6.splitlines()[0][:34]!r} (got {_st6}: {_d6[:44]})",
                          (_st6 == "flag") == _want6 and _st6 in ("flag", "pass")))
    # The three false-positive classes the npm corpus exposed (see _NPM_SPECIFIER).
    for _lbl8, _src8 in (
        # ⛔ These two are VERBATIM from the npm corpus (astro's code-generating source).
        # The fixture that stood here was invented, did not match the extraction regex at
        # all, and so passed with or without the shape test — it measured nothing.
        ("a TEMPLATE-LITERAL specifier in code that GENERATES js source",
         "const code = `import { renderers } from '${ASTRO_RENDERERS_MODULE_ID}';`;\n"),
        ("an INTERPOLATED subpath inside an otherwise real-looking specifier",
         'const c = `export { default as P } from '
         '"astro/components/${imageComponentPrefix}Picture.astro";`;\n'),
        ("the word `from` inside ordinary quoted prose",
         "const msg = 'copied from ', path.call(print$1, ' here';\n"),
        ("a Node SUBPATH import (#foo), which resolves to a LOCAL file",
         'const p = require("#minpath");\n'),
    ):
        _st8, _d8 = check_deps(_src8, "javascript", None)[1:]
        extra.append((f"C6-js {_lbl8} is not a dependency (got {_st8}: {_d8[:40]})",
                      _st8 == "pass"))
    extra.append(("C6-js a REAL scoped package is still caught after the shape test",
                  check_deps('import x from "@babel/core";\n', "javascript", None)[1] == "flag"))

    # A comment naming a third-party package must NOT count as an import -- this is the
    # whole reason the extraction runs on stripped source.
    extra.append(("C6 a package named only in a COMMENT is not an import",
                  check_deps('package main\n// import "github.com/x/y"\n'
                             'import "fmt"\nfunc main(){}\n', "go", None)[1] == "pass"))

    # ---- ROUND 21: THE _IMPORT_LINE <-> DEPS_EXTRACT AGREEMENT INVARIANT ----------------
    # ⛔ THE STRUCTURAL DEFECT BEHIND FOUR OF 4Q'S ROUND-21 FINDINGS AND THE ROUND-20
    # REGRESSION. `_IMPORT_LINE` (which decides what survives string-blanking) and
    # `DEPS_EXTRACT` (which parses what survived) are two INDEPENDENT tables that must agree
    # about what a dependency line looks like. Nothing enforced that, so every disagreement
    # became a silent verdict:
    #     restore DROPS a line the extractor could parse  -> FALSE NEGATIVE
    #     restore KEEPS a line that is not an import      -> FALSE POSITIVE
    # Each row below is a REAL syntactic form the tables claim to handle, paired with the
    # third-party name that must come back. A future edit to either table that breaks their
    # agreement turns one of these red instead of silently mis-verdicting the library.
    # ⚠️ These are round-trip probes THROUGH strip_noncode(keep_strings=False) -- the whole
    # point is the interaction, so do not "simplify" them by calling the extractor directly.
    for _lane9, _cases9 in {
        "go": [
            ("plain grouped", 'package main\nimport (\n\t"fmt"\n\t"github.com/x/y"\n)\n', True),
            # 4Q R21 F1 -- the alias sits between the whitespace and the quote.
            ("ALIASED grouped", 'package main\nimport (\n\tf "fmt"\n\te "github.com/x/y"\n)\n', True),
            ("BLANK-identifier grouped", 'package main\nimport (\n\t_ "github.com/x/y"\n)\n', True),
            ("DOT-import grouped", 'package main\nimport (\n\t. "github.com/x/y"\n)\n', True),
            ("single-line", 'package main\nimport "github.com/x/y"\n', True),
            ("single-line ALIASED", 'package main\nimport e "github.com/x/y"\n', True),
            ("grouped, stdlib only", 'package main\nimport (\n\t"fmt"\n\t"os"\n)\n', False),
            # 4Q R21 F2 -- an import block quoted inside a backtick raw string is PROSE.
            ("raw string holding a whole import block",
             'package main\nimport "fmt"\nfunc main(){\n\tc := `import (\n\t"github.com/x/y"\n)`\n\tfmt.Println(c)\n}\n', False),
            ("raw string holding a bare quoted path",
             'package main\nimport "fmt"\nfunc main(){\n\tc := `\n\t"github.com/x/y"\n`\n\tfmt.Println(c)\n}\n', False),
            # ⛔ THESE TWO EXIST BECAUSE THE MUTANTS SAID THE OTHER GO FP PROBES WERE
            # DECORATION. The FP is defended by two INDEPENDENT mechanisms -- `_IMPORT_LINE`
            # no longer matching a bare quote, and the raw-string tracker -- and every probe
            # I first wrote used 4Q's fixture shape, which BOTH mechanisms defend. So either
            # one could be deleted and nothing went red. MEASURED 2026-09-02, each shape
            # below is caught by exactly ONE of the two:
            #   concatenated regular strings  -> only the `_IMPORT_LINE` fix catches it
            #   `import (` alone on its line  -> only the raw-string tracker catches it
            # ⚠️ The first is `csv_validator.go`'s REAL shape (`"a\\n" + "b\\n"`), which is
            # not a backtick raw string at all. I found the defect in the library and then
            # wrote its probe using the crew's fixture form instead of the form I had
            # actually found -- the third time in one day that a test inherited the shape
            # its author happened to type. Do not "simplify" these into one case.
            ("CONCATENATED regular strings holding a package-like path (csv_validator's shape)",
             'package main\nimport "fmt"\nfunc main(){\n\tcsv := "1,Alice,30\\n" +\n'
             '\t\t"2,Bob,35\\n" +\n\t\t"github.com/x/y\\n"\n\tfmt.Println(csv)\n}\n', False),
            ("raw string whose `import (` sits ALONE on its own line",
             'package main\nimport "fmt"\nfunc main(){\n\tc := `\nimport (\n\t"github.com/x/y"\n)\n`\n'
             '\tfmt.Println(c)\n}\n', False),
        ],
        "r": [
            ("library() at line start", 'library(dplyr)\n', True),
            # 4Q R21 F3 -- requireNamespace is idiomatically written inside a guard, so the
            # restore pattern must be unanchored AND carry the longer keyword.
            ("requireNamespace inside a guard",
             'if (!requireNamespace("dplyr", quietly = TRUE)) {\n  stop("needed")\n}\n', True),
            ("requireNamespace at line start", 'requireNamespace("dplyr")\n', True),
            ("base package only", 'library(utils)\nx <- stats::median(c(1,2))\n', False),
        ],
        "javascript": [
            ("static import ... from", 'import x from "lodash";\n', True),
            ("require()", 'const x = require("lodash");\n', True),
            # 4Q R21 F4 -- `import(` has no whitespace after the keyword.
            ("DYNAMIC import()", 'const m = await import("express");\n', True),
            ("dynamic import() of a builtin", 'const m = await import("node:fs");\n', False),
            ("relative dynamic import()", 'const m = await import("./helper.js");\n', False),
        ],
        "cpp": [
            ("angle-bracket third-party", '#include <boost/asio.hpp>\nint main(){return 0;}\n', True),
            # 4Q R21 F6 -- STRUCTURAL GUARD. 0 of 420 library files use this form today.
            ("QUOTE-form third-party", '#include "openssl/sha.h"\nint main(){return 0;}\n', True),
            # The bracket form does not decide -- the package-qualified PATH does.
            ("QUOTE-form bare local header stays silent",
             '#include "local_helper.h"\nint main(){return 0;}\n', False),
            ("ANGLE-form bare header is still stdlib-checked",
             '#include <vector>\nint main(){return 0;}\n', False),
            ("angle-bracket stdlib", '#include <vector>\nint main(){return 0;}\n', False),
        ],
        "rust": [
            ("use", "use serde::Serialize;\nfn main(){}\n", True),
            ("leading-colon use", "use ::serde::Serialize;\nfn main(){}\n", True),
            ("extern crate", "extern crate serde;\nfn main(){}\n", True),
            ("std only", "use std::collections::HashMap;\nfn main(){}\n", False),
        ],
    }.items():
        for _lbl9, _src9, _want9 in _cases9:
            _st9, _d9 = check_deps(_src9, _lane9, None)[1:]
            extra.append((f"C6-AGREE {_lane9} {_lbl9} -> "
                          f"{'flag' if _want9 else 'pass'} (got {_st9}: {_d9[:40]})",
                          (_st9 == "flag") == _want9 and _st9 in ("flag", "pass")))

    # 4Q R21 F5 -- importlib.import_module is an ast.Call, invisible to an Import/ImportFrom
    # walker. Only a CONSTANT argument is read; a computed name stays undecidable.
    for _lbl5, _src5, _want5 in (
        ("importlib.import_module of a third-party module",
         'import importlib\ndef f():\n    return importlib.import_module("numpy")\n', True),
        ("importlib.import_module of a stdlib module",
         'import importlib\ndef f():\n    return importlib.import_module("json")\n', False),
        ("a COMPUTED module name is left alone, not guessed at",
         'import importlib\ndef f(n):\n    return importlib.import_module(n)\n', False),
        ("bare import_module() after a from-import",
         'from importlib import import_module\ndef f():\n    return import_module("numpy")\n', True),
    ):
        _r5 = check_deps(_src5, "python", ast.parse(_src5))
        extra.append((f"C6-py {_lbl5} (got {_r5[1]}: {_r5[2][:40]})",
                      (_r5[1] == "flag") == _want5 and _r5[1] in ("flag", "pass")))

    # ⛔ 4Q R21 F7 REJECTED, and this probe PINS THE REJECTION so a future session cannot
    # quietly "fix" it. A rust `::` path-root regex was MEASURED to match 120 of 200 library
    # files (collections 51, sync 28, thread 25, u32 22, atomic 18 -- std path fragments and
    # turbofish, not crates). Direct path access without `use` stays INVISIBLE on purpose.
    extra.append(("C6-rust F7 REJECTED: direct `serde_json::` path with no `use` stays pass",
                  check_deps('fn main(){ let _v: serde_json::Value = '
                             'serde_json::from_str("{}").unwrap(); }\n',
                             "rust", None)[1] == "pass"))
    # ⛔ THE `if not ok` BRANCH IN _deps_nonpython IS UNREACHABLE FOR THESE FIVE LANES.
    # MEASURED 2026-09-02: strip_noncode returns ok=True for cpp/go/rust/r/javascript on
    # every malformed input tried — only python's tokeniser can report failure, and python
    # never reaches _deps_nonpython. The branch is kept because strip_noncode's CONTRACT
    # returns a bool and a future stripper may use it, but it must not be read as an active
    # safety net. So the real question is not "does it refuse" but "does a mangled literal
    # SWALLOW a later import and yield a confident false pass?" Measured: it does not —
    # the strippers resync at the newline. These four are that measurement, and they are
    # the probes that would go red if a stripper were rewritten to consume to EOF.
    for _lane7, _src7 in (
        ("rust", 'fn f() { let s = r#"oops;\nuse serde::Serialize;\nfn main(){}\n'),
        ("go", 'package main\nvar s = "oops\nimport "github.com/x/y"\nfunc main(){}\n'),
        ("cpp", '/* oops\n#include <boost/asio.hpp>\nint main(){return 0;}\n'),
        ("javascript", 'const a = "oops;\nconst _ = require("lodash");\n'),
    ):
        _st7 = check_deps(_src7, _lane7, None)[1]
        extra.append((f"C6-{_lane7} a MALFORMED literal does not swallow the import that "
                      f"follows it — no confident false pass (got {_st7})", _st7 == "flag"))

    # every unverifiable detail in the tool must carry a reason code -- prose is not a key
    extra.append(("every unverifiable return carries a [REASON_CODE]",
                  all(reason_of(_u(_c, "x"))[0] == _c for _c in REASON_SUBCLASS)))
    try:
        _u("NOT_A_REAL_CODE", "x"); _bad = True
    except KeyError:
        _bad = False
    extra.append(("_u REFUSES an undeclared reason code (a new unverifiable path cannot "
                  "enter without naming its remedy)", not _bad))
    extra.append(("an untagged detail yields no subclass, so it cannot be silently triaged",
                  reason_of("plain prose") == (None, None)))
    extra.append(("every subclass has a remedy and a disposition set",
                  set(SUBCLASS_REMEDY) == set(SUBCLASS_DISPOSITIONS)
                  == set(REASON_SUBCLASS.values())))
    extra.append(("every per-subclass disposition is in the closed DISPOSITIONS set",
                  all(d in DISPOSITIONS for v in SUBCLASS_DISPOSITIONS.values() for d in v)))

    _off, _on = _df_arm(1.0), _df_arm(0.10)
    extra.append((f"DF filter NEGATIVE ARM: without it, harness-sharing files ARE falsely "
                  f"linked ({_off}/20)", _off >= 15))
    extra.append((f"DF filter POSITIVE ARM: with it, they are not ({_on}/20)", _on == 0))

    print()
    for label, cond in extra:
        nprobe[0] += 1
        if not cond:
            fails.append(label)
        print(f"  {'ok  ' if cond else 'FAIL'}  {label}")

    print(f"\n{nprobe[0]} probe(s), {len(fails)} failure(s)")
    for f in fails:
        print("   FAILED:", f)
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
