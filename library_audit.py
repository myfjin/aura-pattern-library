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

VERDICTS = ("PASS", "FAIL", "FLAG", "UNVERIFIABLE", "SKIP")
STATUSES = ("pass", "fail", "flag", "unverifiable", "skip")

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
ANALYSER_COVERAGE = {
    "hollow":               LANES,          # ASSERT_PAT + stripper for all six
    "dangerous_primitives": LANES,          # DANGEROUS  + stripper for all six
    "determinism_markers":  LANES,          # NONDET     + stripper for all six
    "hardcoded_abs_path":   LANES,          # stripper for all six
    "assert_nonvacuous":    ("python",),    # python AST only
    "importable":           ("python",),    # python AST only
    "deps":                 ("python",),    # python AST only
    "doc_behavior":         ("python",),    # the description slot differs per language
}


def _u(code: str, detail: str) -> str:
    """Tag an unverifiable detail with its reason code. Raises on an unknown code, so a new
    unverifiable path cannot enter the tool without declaring which remedy it needs."""
    if code not in REASON_SUBCLASS:
        raise KeyError(f"unknown unverifiable reason code {code!r}")
    return f"[{code}] {detail}"


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
        (r"\binput\s*\(", "input() — blocks a non-interactive gate"),
    ],
    "javascript": [
        (r"\beval\s*\(", "eval()"),
        (r"new\s+Function\s*\(", "new Function()"),
        (r"child_process", "child_process"),
        (r"\.innerHTML\s*=", "innerHTML assignment"),
        (r"createHash\(\s*['\"]md5", "md5"),
        (r"createHash\(\s*['\"]sha1", "sha1"),
    ],
    "cpp": [
        (r"\bsystem\s*\(", "system()"),
        (r"\bstrcpy\s*\(", "strcpy"),
        (r"\bsprintf\s*\(", "sprintf"),
        (r"\bgets\s*\(", "gets"),
        (r"\bMD5[_(]", "MD5"),
    ],
    "go": [
        (r"os/exec", "os/exec"),
        (r"crypto/md5", "crypto/md5"),
        (r"crypto/sha1", "crypto/sha1"),
        (r"unsafe\.", "unsafe"),
    ],
    "rust": [
        (r"\bunsafe\s*\{", "unsafe block"),
        (r"std::process::Command", "process::Command"),
        (r"\.unwrap\(\)", "unwrap() — panics instead of handling"),
    ],
    "r": [
        (r"\beval\s*\(", "eval()"),
        (r"\bsystem\s*\(", "system()"),
        (r"\bparse\s*\(\s*text\s*=", "parse(text=)"),
    ],
}

# ---------------------------------------------------------------- C10 determinism markers
NONDET = {
    "python": [(r"\brandom\.", "random"), (r"\bnp\.random\.", "numpy.random"),
               (r"\btime\.time\s*\(", "time.time"), (r"datetime\.now\s*\(", "datetime.now"),
               (r"\buuid\.", "uuid"), (r"\brequests\.", "network: requests"),
               (r"urllib\.request", "network: urllib"), (r"\bsocket\.", "network: socket")],
    "javascript": [(r"Math\.random", "Math.random"), (r"Date\.now", "Date.now"),
                   (r"\bfetch\s*\(", "network: fetch"), (r"require\(['\"]http", "network: http")],
    "cpp": [(r"\brand\s*\(", "rand()"), (r"random_device", "random_device"),
            (r"chrono::.*now", "chrono::now")],
    "go": [(r"math/rand", "math/rand"), (r"time\.Now", "time.Now"), (r"net/http", "network")],
    "rust": [(r"\brand::", "rand crate"), (r"SystemTime::now", "SystemTime::now")],
    "r": [(r"\brunif\s*\(|\brnorm\s*\(|\bsample\s*\(", "random"), (r"Sys\.time\s*\(", "Sys.time")],
}

ASSERT_PAT = {
    "python": r"\bassert\b",
    "javascript": r"\bassert\b|\bthrow\s+new\s+Error",
    "cpp": r"\bassert\s*\(",
    "go": r"\bpanic\s*\(",
    "rust": r"\bassert!|\bassert_eq!|\bassert_ne!",
    "r": r"\bstopifnot\s*\(",
}

ABS_PATH = re.compile(r"['\"](/(?:home|Users|srv|opt|var|tmp)/[^'\"]{2,})['\"]|['\"][A-Z]:\\\\")



_IMPORT_LINE = {
    "go": re.compile(r'^\s*(import\s|")'),
    "rust": re.compile(r'^\s*(use|extern)\s'),
    "javascript": re.compile(r'^\s*(import\s|const\s+\w+\s*=\s*require|.*\brequire\s*\()'),
    "cpp": re.compile(r'^\s*#\s*include\b'),
    "r": re.compile(r'^\s*(library|require)\s*\('),
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
    keep, in_block = [], False
    for ln in text.splitlines():
        st = ln.strip()
        if lane == "go":
            if re.match(r'^import\s*\($', st):
                in_block = True
                continue
            if in_block:
                if st == ")":
                    in_block = False
                else:
                    keep.append(ln)
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
    """Regex-table check on COMMENT- AND STRING-STRIPPED source.

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
                _u("NO_STRIPPER", f"no comment/string stripper for lane '{lane}' — "
                   "scanning raw text would match prose, so nothing was measured"), [])
    hit = [(pat, label) for pat, label in table[lane] if re.search(pat, code)]
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
        code, ok = strip_noncode(text, lane)
        if ok and SEEDED.search(code):
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
                _u("NO_STRIPPER", f"no comment stripper for lane '{lane}' — a path in a "
                   "comment would have counted as a hardcoded path"))
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
                _u("NO_STRIPPER", f"no comment/string stripper for lane '{lane}' — an "
                   "assertion inside a comment would have counted as one -- 4Q F3"))
    n = len(re.findall(pat, code))
    if n == 0:
        return ("hollow", "flag", f"no assertion construct found in CODE (looked for /{pat}/)")
    return ("hollow", "pass", f"{n} assertion construct(s) in code")


def check_assert_nonvacuous(text, lane, tree):
    """C4 — an assert that cannot fail is decoration. Decidable on the python AST: an assert
    whose test contains no Name/Call/Attribute/Subscript is comparing literals to literals."""
    if lane != "python":
        return ("assert_nonvacuous", "unverifiable",
                _u("NON_PYTHON_AST", f"decidable on the python AST only; lane is '{lane}'"))
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
        if isinstance(n, (ast.Import, ast.ImportFrom, ast.FunctionDef, ast.AsyncFunctionDef,
                          ast.ClassDef, ast.Assign, ast.AnnAssign, ast.Pass)):
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
    return ("importable", "pass", f"{len(defs)} importable def(s), no import side effects")


_STDLIB = getattr(sys, "stdlib_module_names", frozenset())


def check_deps(text, lane, tree):
    """C6 — a third-party import runs here and crashes in the customer's clean environment.
    There is no dependency manifest in the library, so ANY third-party import is a flag."""
    if lane != "python":
        return ("deps", "unverifiable",
                _u("NON_PYTHON_AST", f"import classification implemented for python "
                   f"only; lane is '{lane}'"))
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
            return ("doc_behavior", "fail", "no module docstring — nothing states what it does")
        return ("doc_behavior", "skip",
                f"docstring present ({len(d)} chars); code-vs-claim is judgement (6E C7), "
                "not tool-decidable")
    return ("doc_behavior", "unverifiable",
            _u("NO_DOC_SLOT", f"description slot differs per language; not implemented "
               f"for '{lane}'"))


# ⛔ KEYED BY (stem, LANE), NOT BY STEM. 6E verified these by reading the PYTHON files;
# `atomic_snapshot` and `cow_backup` each also exist in Go, and a stem-only key handed the
# Go twins a finding nobody had checked -- 2 live false positives (4Q round 3, F4). Their
# Go similarity is 0.51 against 0.65 for Python: a different pair of files, unexamined.
KNOWN_FINDINGS = {
    ("atomic_snapshot", "python"): ("flag", "6E verified BY READING (2026-08-30): a genuine SEMANTIC "
                        "duplicate of cow_backup — both are temp-write + atomic-rename. No "
                        "shingle statistic can find this (containment 0.87 sits inside the "
                        "false-positive range 0.81-0.94), so it is recorded here rather "
                        "than lost to a silent PASS."),
    ("cow_backup", "python"): ("flag", "6E verified BY READING (2026-08-30): a genuine SEMANTIC "
                   "duplicate of atomic_snapshot — both are temp-write + atomic-rename. "
                   "Recorded because the detector cannot derive it."),
}


def check_known_findings(text, lane, tree, stem=None):
    """Findings a human or model verified by READING, which the tool cannot derive itself.
    Without this, a defect somebody already confirmed silently becomes a PASS."""
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
def verdict_for(checks):
    st = {c[1] for c in checks}
    if "fail" in st:
        return "FAIL"
    if "flag" in st:
        return "FLAG"
    if "unverifiable" in st:
        return "UNVERIFIABLE"
    if st <= {"skip"}:
        return "SKIP"
    return "PASS"


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
    ap.add_argument("--acknowledge-unverifiable", action="store_true",
                    help="suppress the non-zero exit when UNVERIFIABLE records exist — use "
                         "only once they have actually been dispositioned")
    ap.add_argument("--self-test", action="store_true",
                    help="prove every check can BOTH fire and stay quiet, then exit")
    args = ap.parse_args()
    if args.self_test:
        return self_test()

    files, lane_of = [], {}
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
        "library_verify_md5": hashlib.md5((ROOT / "library_verify.py").read_bytes()).hexdigest(),
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
                           "was found. It fails closed (never a false PASS), but the compiled "
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
                "A PASS in this file means 'no defect among the CHECKED classes' — it does "
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
                "checks": [{"name": n, "status": s, "detail": d} for n, s, d in checks],
                "evidence": "; ".join(f"{n}: {d}" for n, s, d in nonpass)[:1200],
                "triage_owner": sorted({TRIAGE_OWNER.get(n, "6E") for n, s, _ in nonpass
                                        if s in ("fail", "flag")}) or None,
                "unverifiable_checks": _unv or None,
                "unverifiable_subclass": sorted(_subs) or None,
                "remedy": sorted({SUBCLASS_REMEDY[x][1] for x in _subs}) or None,
                # Filled by a triage session, never by this tool. One of DISPOSITIONS, and
                # WAIVE additionally requires a disposition_ref (6E).
                "disposition": None,
                "disposition_ref": None,
                "needs_judgement": any(s in ("flag", "unverifiable") for _, s, _ in checks),
                # 6E: PASS must never be read as "clean". These classes were never assessed
                # for ANY pattern, so they are stated on every record, not just the flagged.
                "unassessed_classes": ["C1_semantic_incorrectness", "C3_twin_equivalence",
                                       "C11_provenance"],
                "verdict_semantics": (
                    "A PASS means no defect was found among the classes this tool CAN check. "
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
                     "FLAG->UNVERIFIABLE, 2 FLAG->PASS) — 6E measured this; the earlier "
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
    lines = open(args.out, encoding="utf-8").read().splitlines()
    lines[0] = json.dumps(header)
    open(args.out, "w", encoding="utf-8").write("\n".join(lines) + "\n")

    print(f"\n{len(files)} pattern(s) audited in {time.time()-t0:.0f}s -> {args.out}")
    for v in VERDICTS:
        if counts.get(v):
            print(f"  {v:<14} {counts[v]}")
    print("\nper check:")
    for name in sorted(check_counts):
        row = check_counts[name]
        print(f"  {name:<22} " + "  ".join(f"{s}={row[s]}" for s in STATUSES if row.get(s)))
    # A header field cannot force anyone to act on UNVERIFIABLE (6E). This can: a run with
    # unmeasured patterns cannot exit 0 until someone says out loud that they looked.
    nu = counts.get("UNVERIFIABLE", 0)
    if nu and not args.acknowledge_unverifiable:
        print(f"\n⛔ {nu} pattern(s) are UNVERIFIABLE — the tool COULD NOT MEASURE them.")
        print("   That is a FINDING, not a footnote. See run.coverage_gaps for which checks")
        print("   could not run and why. Re-run with --acknowledge-unverifiable once they")
        print("   have been dispositioned.")
        return 2
    return 0




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
    ("assert: non-python is UNVERIFIABLE not pass", check_assert_nonvacuous, "go", "x", "unverifiable"),

    ("importable: no defs is script-only", check_importable, "python", "print(1)\n", "flag"),
    ("importable: side effect at module level", check_importable, "python",
     "def f():\n    return 1\nprint(f())\n", "flag"),
    ("importable: __main__ guard is NOT a side effect", check_importable, "python",
     "def f():\n    return 1\nif __name__ == '__main__':\n    print(f())\n", "pass"),

    ("deps: third-party import is flagged", check_deps, "python", "import numpy\n", "flag"),
    ("deps: stdlib only passes", check_deps, "python", "import json, os\n", "pass"),
    ("deps: relative import is not third-party", check_deps, "python", "from . import x\n", "pass"),
    ("deps: non-python is UNVERIFIABLE not pass", check_deps, "rust", "use foo;", "unverifiable"),

    ("dangerous: eval is flagged", check_dangerous, "python", "eval('1')\n", "flag"),
    ("dangerous: shell=True is flagged", check_dangerous, "python", "run(x, shell=True)\n", "flag"),
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
    ("doc: non-python is UNVERIFIABLE not pass", check_doc_behavior, "cpp", "// x", "unverifiable"),

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
    agg = [("fail beats flag", [("a", "fail", ""), ("b", "flag", "")], "FAIL"),
           ("flag beats unverifiable", [("a", "flag", ""), ("b", "unverifiable", "")], "FLAG"),
           ("unverifiable beats pass", [("a", "unverifiable", ""), ("b", "pass", "")],
            "UNVERIFIABLE"),
           ("all pass is PASS", [("a", "pass", ""), ("b", "pass", "")], "PASS"),
           ("all skip is SKIP", [("a", "skip", "")], "SKIP")]
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
                  verdict_for([("a", "flag", ""), ("b", "pass", "")]) == "FLAG"))

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
                  and verdict_for([("gate", "pass", ""), _nd]) == "PASS"))
    _ex = duplicate_check("fail", "EXACT duplicate of x.py")
    extra.append(("an EXACT duplicate still fails the verdict",
                  _ex[1] == "fail"
                  and verdict_for([("gate", "pass", ""), _ex]) == "FAIL"))

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
                    "deps": "import numpy\n", "doc_behavior": "x = 1\n"}
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
