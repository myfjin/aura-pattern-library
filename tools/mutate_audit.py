"""Mutation-test library_audit's self-test. A probe that survives its fix being gutted is
decoration. Control is checked for BOTH failures AND crash (a crashing control scores every
mutant KILLED for free -- measured 2026-08-29)."""
import ast, hashlib, os, shutil, subprocess, sys, tempfile

# Self-locating: this file lives in <library>/tools/, so the root is its grandparent.
# The baselines are taken from the LIVE files at startup and the control below refuses to
# continue unless they are clean.
# BAK once pointed into a session-scoped scratchpad. When such a directory goes away the
# restore fails WITH A MUTATED PRODUCTION FILE LEFT ON DISK -- which is exactly how this
# harness nearly shipped a gutted verdict_for on 2026-08-30. Never hardcode it again.
ROOT = os.environ.get("AURA_LIB_ROOT") or os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))
BAKDIR = os.environ.get("MUTBASE_DIR") or tempfile.mkdtemp(prefix="aura-mutbase-")


def _pick_python():
    """The interpreter differs per machine. .5 (Mac) has a working library venv; .8 does
    NOT -- its .venv is an rsync'd Mac fossil whose python symlink dangles, and the working
    interpreter there is /usr/bin/python3 (3.10.12), which does carry folder_nature+yaml."""
    cand = os.environ.get("AURA_PY") or os.path.join(ROOT, ".venv/bin/python")
    if os.access(cand, os.X_OK) and subprocess.run(
            [cand, "-c", ""], capture_output=True).returncode == 0:
        return cand
    return "/usr/bin/python3" if os.access("/usr/bin/python3", os.X_OK) else sys.executable


P = os.path.join(ROOT, "library_audit.py")
BAK = os.path.join(BAKDIR, "library_audit.py.mutbase")
PY_ = _pick_python()
print("root: %s | python: %s | baselines: %s" % (ROOT, PY_, BAKDIR))

shutil.copy(P, BAK)
base = hashlib.md5(open(P,"rb").read()).hexdigest()
print("baseline md5:", base)

R = os.path.join(ROOT, "audit_report.py")
RBAK = BAK.replace("library_audit.py.mutbase", "audit_report.py.mutbase")
shutil.copy(R, RBAK)
rbase = hashlib.md5(open(R,"rb").read()).hexdigest()
print("renderer baseline md5:", rbase)
BX = os.path.join(ROOT, "build_patterns_index.py")
BXBAK = BAK.replace("library_audit.py.mutbase", "build_patterns_index.py.mutbase")
shutil.copy(BX, BXBAK)
bxbase = hashlib.md5(open(BX,"rb").read()).hexdigest()
print("ruler baseline md5:", bxbase)

MUTANTS = [
    ('TRIAGE-A go os.Exit assertion removed (86 false hollow flags return)',
     '|\\bos\\.Exit\\s*\\(\\s*[1-9]"', '|XXTRIAGEA"', 'TRIAGE-A go: `if x != y'),
 # ⛔ ROUND 20: the anchor was the bare `os.Exit` fragment, which C4's _C4_IF table
 # duplicated -> it matched TWICE and the guard went dark. Re-aimed at ASSERT_PAT's go
 # entry, where the [1-9] vs [0-9] distinction actually lives.
 ("TRIAGE-A go os.Exit accepted with ANY argument (os.Exit(0) becomes an assertion)",
  'r"\\bpanic\\s*\\(|\\bt\\.(?:Error|Fatal)f?\\s*\\(|\\bos\\.Exit\\s*\\(\\s*[1-9]"',
  'r"\\bpanic\\s*\\(|\\bt\\.(?:Error|Fatal)f?\\s*\\(|\\bos\\.Exit\\s*\\(\\s*[0-9]"',
  'os.Exit(0) is a SUCCESSFUL exit'),
    ('TRIAGE-A go log.Fatal dropped', '|\\blog\\.Fatal(?:f|ln)?\\s*\\("', '|XXTRIAGEA2"',
     'log.Fatal IS os.Exit(1)'),
    ('TRIAGE-B pure-decorator allowlist emptied (34 false flags return)',
     '                if _nm in PURE_DECORATORS:', '                if _nm in ():',
     'dataclass decorator is a PURE transformer'),
    ('TRIAGE-B allowlist bypassed entirely (every decorator is pure -> @register goes quiet)',
     '                if _nm in PURE_DECORATORS:', '                if True:',
     'bare @register is ALSO a bare Name'),
    ('TRIAGE-C hash def-exclusion removed (a def hash( is a nondeterminism marker again)',
     '(?<!def[ \\t])', '', 'DEFINES a hash method'),
    ('R20-F1 shebang skip reverted to excluding R (a shebang reads as the description)',
     '    if s.startswith("#!"):', '    if s.startswith("#!") and lang != "r":',
     'interpreter directive', BX),
    ('R20-F2 javascript removed from the // branch again',
     '(lang in ("cpp", "go", "rust", "javascript") and s.startswith("//"))',
     '(lang in ("cpp", "go", "rust") and s.startswith("//"))',
     '// comments had no route', BX),
    ('R20-F2 javascript import/require no longer structural (scan breaks before the block)',
     '    if lang == "javascript" and (\n            s.startswith(("import ", "export "))',
     '    if False and (\n            s.startswith(("import ", "export "))',
     'BROKE at an import', BX),
    ('R20-O2 the not-a-docstring divergence is silently reported as a plain missing docstring',
     '            if _seen:', '            if False:', 'is reported as such'),
    ('R20 6E-F2 nothing-executed banner removed', 'if recs and not _ran_exec:',
     'if False:', 'NOTHING was executed', R),
    ('R20 6E-F2 banner prints even when the gate RAN (a false nothing-executed claim)',
     'if recs and not _ran_exec:', 'if recs:', 'NEGATIVE ARM: when the gate DID run', R),
    ('R20 6E-F1 the coverage explainer removed', 'if _part:', 'if False:',
     'explained as COVERAGE', R),
    ('R20 6E-F1 the checks-that-ran count HARDCODED instead of derived',
     '        return f"{min(v)}" if min(v) == max(v) else f"{min(v)}-{max(v)}"',
     '        return "2-3"',
     'derived from the records', R),
    ('R19 doc_behavior coverage un-declared (824 patterns go back to U1)',
     '    "doc_behavior":         LANES,', '    "doc_behavior":         ("python",),',
     'MATRIX doc_behavior x cpp'),
    ('R19 doc_behavior answers for a lane with NO slot defined (claims cobol has no description)',
     '    if lane not in LANES:', '    if False:', 'NO slot defined'),
    ('R19 doc_behavior treats a MISSING description as present (fail arm dies)',
     '    if not claim:', '    if False:', 'NEGATIVE ARM'),
    ('R19 doc_behavior reports skip for everything (present arm becomes vacuous)',
     '        claim = _BPI.extract_claim_text(text, lane)', '        claim = "x"',
     'NEGATIVE ARM'),
    ('R18 setTimeout(string) PATTERN gutted', '(r"\\bset(?:Timeout|Interval)\\s*\\(\\s*[\'\\"]"', '(r"XX18A"', 'setTimeout with a STRING'),
    ('R18 vsprintf PATTERN gutted', r'(r"\bvs?printf\s*\(", "vsprintf")', r'(r"XX18B", "vsprintf")', 'vsprintf'),
    ('R18 tmpnam PATTERN gutted', r'(r"\btmpnam\s*\(", "tmpnam — predictable temp name")', r'(r"XX18C", "tmpnam — predictable temp name")', 'tmpnam'),
    ('R18 crypto/des rule gutted', '(r"crypto/des", "crypto/des — weak cipher")', '(r"XX18D", "crypto/des — weak cipher")', 'crypto/des'),
    ('R18 crypto/rc4 rule gutted', '(r"crypto/rc4", "crypto/rc4 — weak cipher")', '(r"XX18E", "crypto/rc4 — weak cipher")', 'crypto/rc4'),
    ('R18 rust process::Command back to FULLY-QUALIFIED only (use-alias walks past again)',
     '(r"(?:std::)?process::Command", "process::Command")',
     '(r"std::process::Command", "process::Command")', 'use std::process'),
    ('R18 rust glob-import PATTERN gutted', r'(r"use\s+std::process::\*\s*;[\s\S]*?\bCommand::new\s*\(",', r'(r"XX18F",', 'GLOB import'),
    ('R18 cpp system narrowing reverted (hw.system(42) false-flags again)',
     '(r"(?<![.\\w])(?<!->)system\\s*\\(", "system()")', '(r"\\bsystem\\s*\\(", "system()")',
     'METHOD on an object'),
    ('R18 cpp system narrowed TOO FAR (a real system() call goes quiet)',
     '(r"(?<![.\\w])(?<!->)system\\s*\\(", "system()")', '(r"XX18G", "system()")',
     'REAL system() call'),
    ('R17-F1 child_process rule back to a bare substring (a path MENTION flags again)',
     '(r"[\'\\"](?:node:)?child_process[\'\\"]", "child_process")',
     '(r"child_process", "child_process")', 'MENTIONS child_process'),
    ('R17-F1 os/exec rule back to a bare substring (a wrapper package flags again)',
     '(r"[\'\\"]os/exec[\'\\"]", "os/exec")', '(r"os/exec", "os/exec")', 'wrapper package'),
    ('R17-F1 node: prefix dropped (a real require("node:child_process") goes quiet)',
     '(?:node:)?child_process', 'child_process', 'node:child_process'),
    ('R17-F1 SEEDED back to pass 1 only (random.seed("42") flagged as unseeded)',
     '_seeded = SEEDED.search(code) or (_sok and any(',
     '_seeded = SEEDED.search(code) or (False and any(',
     'random.seed'),
    # DECLARED UNKILLABLE, same discipline as the alignment guard: 4Q measured that no rule
    # in any table can begin its match at whitespace, so no fixture can make this guard change
    # a verdict today. It closes the fragility 4Q found (a blanked literal becomes spaces, so
    # code[i]==lit[i]==' ' reads as code) for any FUTURE rule that starts with \s. Honestly
    # unmeasured, and marked as such rather than left looking like a passing test.
    ('R17 provenance line removed from the rendered page (a report cannot be traced to its tool)',
     "w(f\"\u00b7 produced by `{cell(header.get('tool', 'UNKNOWN'), 40)}` md5 \"",
     "w(f\"\u00b7 x \"",
     'PROVENANCE positive arm', R),
    ('R17 provenance md5 DEFAULTS to blank instead of saying UNKNOWN out loud',
     "header.get('tool_md5', 'UNKNOWN \u2014 pre-provenance run')",
     "header.get('tool_md5', '')",
     'PROVENANCE negative arm', R),
    ('R17 ABS_PATH root set back to the 6 roots someone thought of (/etc/passwd goes quiet)',
     'home|Users|srv|opt|var|tmp|etc|usr|bin|sbin|lib|lib64|dev|proc|sys|run|root',
     'home|Users|srv|opt|var|tmp',
     '/etc/passwd'),
    ('R17 ABS_PATH anchor dropped: any "/word" matches again (16 false positives return)',
     'r"[\'\\"](?!/dev/(?:null|zero|urandom|random)[\'\\"])(/(?:" + _FS_ROOT + r")(?:/[^\'\\"]*)?)[\'\\"]"',
     'r"[\'\\"](?!/dev/(?:null|zero|urandom|random)[\'\\"])(/[A-Za-z][^\'\\"]*)[\'\\"]"',
     'route template'),
    ('R17 /dev carve-out widened to all of /dev (/dev/sda1 goes quiet)',
     '/dev/(?:null|zero|urandom|random)', '/dev/(?:[a-z0-9]*)', '/dev/sda1'),
    # ===== ROUND 17: the DEAD-BY-CONSTRUCTION engine fix =====
    ('R17 two-pass removed entirely (back to code-only: six rules die again)',
     '           if re.search(pat, code) or (lit_ok and _starts_in_code(pat))]',
     '           if re.search(pat, code)]',
     'createElement'),
    ('R17 starts-in-code guard removed (pass 2 matches anywhere: eval INSIDE a string revives)',
     '            if i < len(code) and code[i] == lit[i] and not lit[i].isspace():',
     '            if True:',
     'STRING is not a finding'),
    # DECLARED UNKILLABLE, not decoration-by-accident: the alignment census measured 0 of
    # 1514 library files where len(lit) != len(code), so no fixture can make this guard fire
    # under the CURRENT strippers. It is insurance against a future stripper that stops
    # blanking in place, and it is honestly unmeasured today. Left in the list, marked.
    # ===== ROUND 16: every broadened table row, one mutant each =====
    ('R16 r system2 PATTERN gutted', r'(r"\bsystem2?\s*\(", "system()/system2()")',
     r'(r"XXR16A", "system()/system2()")', 'system2'),
    ('R16 cpp strcat PATTERN gutted', r'(r"\bstrcat\s*\(", "strcat")',
     r'(r"XXR16C", "strcat")', 'strcat'),
    ('R16 cpp scanf PATTERN gutted', r'(r"\bs?scanf\s*\([^)]*%\s*(?:s|\[)", "unbounded scanf %s")',
     r'(r"XXR16D", "unbounded scanf %s")', 'scanf'),
    ('R16 nondet os.urandom PATTERN gutted', r'(r"\bos\.urandom\s*\(", "os.urandom")',
     r'(r"XXR16E", "os.urandom")', 'urandom'),
 # ⛔ ROUND 20: the bare `(?:debug_)?assert` fragment was duplicated by C4's _C4_HEAD.
 ("R16 rust debug_assert! false-POSITIVE fix reverted (a real assertion called missing)",
  '    "rust": r"\\b(?:debug_)?assert(?:_eq|_ne)?!",',
  '    "rust": r"\\bassert(?:_eq|_ne)?!",',
  'debug_assert'),
    ('6E-R15-F3 JS template scanner removed (backtick falls back to a plain quote)',
     '            if lane == "javascript" and c == "`":\n',
     '            if False:\n',
     'does NOT close the template'),
    ('6E-R15-F3 interpolated code BLANKED instead of kept (the opposite false pass)',
     '                    seg.append(ch); j += 1\n',
     '                    seg.append(" "); j += 1\n',
     'code INSIDE ${...} still runs'),
    ('6E-R15 decorator handling removed (a decorated def is a silent import side effect)',
     '            for _dec in n.decorator_list:\n',
     '            for _dec in []:\n',
     'DECORATED def runs register'),
    ('6E-R15 subprocess row removed from the dangerous table',
     '        (r"\\bsubprocess\\.(?:Popen|call|check_call|check_output|run)\\s*\\(",\n',
     '        (r"XXNEVERMATCHXX",\n',
     'subprocess.Popen is the same primitive'),
    ('6E-R15 the `from os import system` alias row removed',
     '        (r"^\\s*from\\s+os\\s+import\\s+[^\\n]*\\b(?:system|popen)\\b",\n',
     '        (r"XXNEVERMATCH2XX",\n',
     'walked past the dotted regex'),
    ('6E-R15 os.exec* row removed',
     '        (r"\\bos\\.exec[lv][pe]{0,2}\\s*\\(", "os.exec*"),\n',
     '        (r"XXNEVERMATCH3XX", "os.exec*"),\n',
     'os.execv is process execution'),
    ('6E-D3 tool-defect lane disabled (a code-less unverifiable reaches nobody)',
     '        "needs_tool_fix": bool(unclaimed),\n',
     '        "needs_tool_fix": False,\n',
     'is a TOOL DEFECT, not'),
    ('6E-D3 tool-defect lane fires on EVERYTHING (every pattern becomes a tool bug)',
     '        "needs_tool_fix": bool(unclaimed),\n',
     '        "needs_tool_fix": True,\n',
     'a clean record raises no tool defect'),
    ('4Q-R9-F1 the FINDING rule is deleted (flag/fail absorbed by another lane)',
     '        if _st in FINDING_STATUSES:\n            review = True',
     '        if False:\n            review = True',
     'BY THE FINDING RULE'),
    ('4Q-R7 the U3 rule is deleted (does any lane absorb it silently?)',
     '        elif _sub == "U3":\n            pathology = True',
     '        elif False:\n            pathology = True',
     'claimed by its OWN routing rule'),
    ('Ver-5 the implementation rule is deleted',
     '            impl = True ',
     '            impl = False ',
     'needs IMPLEMENTATION, not a human'),
    ('6E-D3-Q2 needs_human_judgement counts a TOOL DEFECT as human work',
     '        "needs_human_judgement": review or pathology,\n',
     '        "needs_human_judgement": review or pathology or bool(unclaimed),\n',
     'EXCLUDES a tool defect'),
    ('4Q-R7 the routed invariant always claims routed',
     '    out["routed"] = review or pathology or impl or out["needs_tool_fix"]\n',
     '    out["routed"] = True\n',
     'a clean record needs NO routing'),
    ('6E-D3-Q3 the coverage axis reports MEASURED instead of unverified',
     '    out["unverified"] = "%d/%d" % (out["checks_unmeasured"], len(checks))\n',
     '    out["unverified"] = "%d/%d" % (out["checks_measured"], len(checks))\n',
     'stated as UNVERIFIED'),
    ('6E-D3 caller/router disagreement no longer raises',
     '    if derived != set(subclasses):\n',
     '    if False:\n',
     'disagree with the check details RAISES'),
    ('4Q-R8 undeclared status no longer raises in triage_fields',
     '        raise KeyError("triage_fields: undeclared status %r -- add it to STATUSES and to "\n',
     '        pass\n    if False:\n        raise KeyError("triage_fields: undeclared status %r -- add it to STATUSES and to "\n',
     'RAISES in triage_fields'),
    ('4Q-R8 undeclared status no longer raises in verdict_for',
     '        raise KeyError("undeclared status %r -- add it to STATUSES and to STATUS_VERDICT, "\n',
     '        pass\n    if False:\n        raise KeyError("undeclared status %r -- add it to STATUSES and to STATUS_VERDICT, "\n',
     'RAISES in verdict_for'),
    ('4Q-R8-F2 a stale verdict name returns to an emitted string',
     '"than lost to a silent NO_FINDING."',
     '"than lost to a silent PASS."',
     'still uses the old verdict name'),
    ('4Q-R8-F1 the routing partition loses a status (import-time guard)',
     'CLEAN_STATUSES = ("pass", "skip")',
     'CLEAN_STATUSES = ("pass",)',
     'partition covers STATUSES exactly'),
 ('4Q-R7-O1 checks_skipped removed from the counters',
  '        "checks_skipped": sum(1 for c in checks if c[1] in SKIPPED_STATUSES),\n',
  '        "checks_skipped": 0,\n',
  'measured + unmeasured + skipped'),
 ('Ver-1 the clean verdict reverts to PASS',
  '    return "NO_FINDING"\n',
  '    return "PASS"\n',
  'NO_FINDING, not PASS'),
 ('Ver-7 evidence truncated with no marker',
  '    return text if len(text) <= limit else text[:limit - len(mark)] + mark\n',
  '    return text[:limit]\n',
  'MARKED as truncated'),
 ('4Q-R6 strip failure reverts to NO_STRIPPER for python',
  '    return "PARSE_FAIL" if lane == "python" else "NO_STRIPPER"\n',
  '    return "NO_STRIPPER"\n',
  '4Q-R6 unparseable PYTHON'),
 ("4Q-S1 '#' dropped from the JS separator class",
  '    r"(?:^|[^\\w$.#])(return|typeof|case|delete|void|instanceof|in|of|new|do|else|yield|await)"\n',
  '    r"(?:^|[^\\w$.])(return|typeof|case|delete|void|instanceof|in|of|new|do|else|yield|await)"\n',
  "INSIDE the window"),
 ("4Q-S1 '#' dropped from the boundary guard",
  '    if m.start(1) == 0 and lo > 0 and (text[lo - 1].isalnum() or text[lo - 1] in "_$.#"):\n',
  '    if m.start(1) == 0 and lo > 0 and (text[lo - 1].isalnum() or text[lo - 1] in "_$."):\n',
  'PRIVATE FIELD'),
 ('6E: a COVERED cell stops measuring (rule tables never match)',
  '           if re.search(pat, code) or (lit_ok and _starts_in_code(pat))]\n',
  '           if False]\n',
  'MATRIX+ dangerous_primitives'),
 ('6E: hollow stops flagging a file with no assertions',
  '        return ("hollow", "flag", f"no assertion construct found in CODE (looked for /{pat}/)")\n',
  '        return ("hollow", "pass", f"no assertion construct found in CODE (looked for /{pat}/)")\n',
  'MATRIX+ hollow'),
 ('4Q-F1-NEW-2 byte raw-string prefix no longer recognised',
  '                _rp = i + 1 if (c == "b" and i + 1 < n and text[i + 1] == "r") else i\n',
  '                _rp = i + 1 if (False) else i\n',
  'BYTE raw string'),
 ("4Q-F1-NEW the '.' property-access guard removed",
  '    if m.start(1) == 0 and lo > 0 and (text[lo - 1].isalnum() or text[lo - 1] in "_$.#"):\n',
  '    if m.start(1) == 0 and lo > 0 and (text[lo - 1].isalnum() or text[lo - 1] in "_$#"):\n',
  'PROPERTY ACCESS'),
 # ---- 6E's trap: U1 quietly converted to PASS. These are the exact edits a well-meaning
 # future contributor would make. Every one must break the matrix probe.
 # ⛔ ROUND 20. The mutant that stood here targeted the NON_PYTHON_AST early-return in
 # check_deps -- the text C6 replaced. It would now print SKIPPED (anchor matched 0), which
 # is visible but defends nothing. These seven take its place: three LOOSEN the rules (a
 # dependency stops being seen) and four TIGHTEN them (the standard library starts being
 # flagged). Both directions matter -- a deps rule that flags <vector> would mark most of
 # 1,150 non-python patterns and look strict while being useless.
 # ⛔ ROUND 20, 4Q's five measured defects. Each fix was a real finding with a
 # discriminating input; without a mutant a fix is just a line I happen to trust.
 ('4Q-R20 F2/F4: deps reads strings again (prose becomes an import)',
  '    code, ok = strip_noncode(text, lane, keep_strings=False)\n    if not ok:\n        return ("deps", "unverifiable",',
  '    code, ok = strip_noncode(text, lane, keep_strings=True)\n    if not ok:\n        return ("deps", "unverifiable",',
  '4Q-R20 F'),
 # ⛔ The grouped-import restore. Without this line a real third-party import in go's
 # IDIOMATIC grouped form is invisible — the regression 6E's corpus caught within
 # minutes of the F2/F4 fix landing, and that my own check had missed.
 ("C6 go: the grouped-import RESTORE line is dropped (idiomatic imports go blind)",
  '    paths |= set(re.findall(r\'^[ \\t]*(?:[\\w.]+[ \\t]+)?"([^"]+)"[ \\t]*(?://.*)?$\', code, re.M))',
  '    paths |= set()',
  'GROUPED import'),
 ('4Q-R20 F1: the POSIX header family drops out of the standard set',
  'arpa/inet.h netdb.h netinet/in.h netinet/tcp.h sys/socket.h sys/un.h sys/select.h',
  'XXR20nothing',
  '4Q-R20 F1'),
 ('4Q-R20 F5: rust stops accepting a crate-relative `use ::crate`',
  '    cs = set(re.findall(r"\\buse\\s+(?:::)?([A-Za-z_][A-Za-z0-9_]*)\\s*(?:::|;)", code))',
  '    cs = set(re.findall(r"\\buse\\s+([A-Za-z_][A-Za-z0-9_]*)\\s*(?:::|;)", code))',
  '4Q-R20 F5'),
 ('4Q-R20 F3: string literals re-enter the literal-only set (python folds foreign strings)',
  '      \\b\\d+(?:\\.\\d+)?(?:[uUlLfF]+)?\\b        # numeric literal, C/Rust suffixes allowed',
  '      "(?:[^"\\\\]|\\\\.)*"\n    | \\b\\d+(?:\\.\\d+)?(?:[uUlLfF]+)?\\b        # numeric literal',
  '4Q-R20 F3'),
 ('C4 THE POLARITY IS INVERTED (every good guard becomes vacuous and back)',
  '        vacuous = (val is True) if pol == "assert" else (val is False)',
  '        vacuous = (val is False) if pol == "assert" else (val is True)',
  'C4-'),
 # ⛔ ROUND 20: this SURVIVED at first — for any expression containing an identifier
 # _c4_fold already fails with NameError, so the guard looked redundant. It is NOT:
 # the two disagree on identifier-free expressions python CAN evaluate
 # (`"abc"[0] == 'a'`, `[1,2][0] == 1`), and folding those would judge cpp/go/rust/r/js
 # source by PYTHON semantics. The SUBSCRIPT probes are what defend it.
 ("C4 the literal-only test is dropped (foreign source folded by python semantics)",
  '        if not _c4_literal_only(expr):\n            live += 1; continue',
  '        if False:\n            live += 1; continue',
  'SUBSCRIPT'),
 ('C4 the rust assert!/assert_eq! head is dropped',
  '    "rust": re.compile(r"\\b(?:debug_)?assert(_eq|_ne)?!\\s*(?=[\\(\\[])"),',
  '    "rust": re.compile(r"\\bXXR20assert(_eq|_ne)?!\\s*(?=[\\(\\[])"),',
  'assert_nonvacuous x rust'),
 ("C4 R's TRUE stops folding to a python True",
  '    e = re.sub(r"\\b(?:true|TRUE)\\b", "True", e)',
  '    e = re.sub(r"\\bXXR20true\\b", "True", e)',
  'assert_nonvacuous x r'),
 ("C6 THE TRAP: non-python deps gets a helpful pass-fallback",
  '    if lane != "python":\n        return _deps_nonpython(text, lane)',
  '    if lane != "python":\n        return ("deps", "pass", "nothing to classify")',
  "MATRIX+ deps x cpp"),
 ("C6 go: a remote module path stops counting as third-party",
  '    return paths, {p for p in paths if "." in p.split("/")[0]}',
  '    return paths, set()',
  "MATRIX+ deps x go"),
 # ⛔ ROUND 20, MEASURED. A mutant stood here flipping C6's `keep_strings=True` to
 # False. It SURVIVED -- and the cause is not an undefended fix, it is a REDUNDANCY.
 # Two independent mechanisms preserve a go/js import line: keep_strings=True never
 # strips it, AND _IMPORT_LINE re-appends it afterwards (round 2, F5). Measured on
 # `import "github.com/pkg/errors"`: with keep_strings=False the original line is
 # blanked but the RESTORED copy is still there, so extraction is unaffected. No
 # SINGLE edit can make that probe go red -- which is exactly what "survived" meant.
 # The equivalent mutant is removed; this one attacks the OTHER arm instead, so the
 # restore is not left undefended.
 # ⛔ ROUND 20, AFTER 4Q's F2/F4 FIX: the frag was 'TEMPLATE-LITERAL' and now misses,
 # because keep_strings=False STRIPS the template prose before extraction ever runs.
 # The shape test's remaining unique job is the Node #subpath case, so the frag names
 # that. The two guards overlap by design; only the non-overlapping part can be a frag.
 ("C6 js: the npm-specifier shape test removed (#subpath becomes a dependency)",
  '        if not _NPM_SPECIFIER.match(base):     # not a package name at all -> not a dependency\n            continue',
  '        if False:                              # not a package name at all -> not a dependency\n            continue',
  'SUBPATH import'),
 ("C6 the go import-line RESTORE is dropped from _IMPORT_LINE",
  '    "go": re.compile(r\'^\\s*import\\s\'),',
  '    "go": re.compile(r\'^\\s*(XXR21never)\'),',
  'AGREE go single-line'),
 ("C6 rust: the std/crate/self allowlist emptied (use std:: starts flagging)",
  '_RUST_LOCAL_ROOTS = frozenset({"std", "core", "alloc", "crate", "self", "super"})',
  '_RUST_LOCAL_ROOTS = frozenset()',
  "C6-rust is SILENT"),
 ("C6 cpp: the standard-header set stops exempting (<vector> starts flagging)",
  '    return hs, {h for h in hs if h not in _CPP_STD_HEADERS}',
  '    return hs, set(hs)',
  "C6-cpp is SILENT"),
 ("C6 js: the node builtin set stops exempting (require fs starts flagging)",
  '        if base.split("/")[0] not in _NODE_BUILTINS:',
  '        if True:',
  "C6-javascript is SILENT"),
 ("C6 r: the base-package set stops exempting (stats:: starts flagging)",
  '    return ps, {x for x in ps if x not in _R_BASE_PKGS}',
  '    return ps, set(ps)',
  "C6-r is SILENT"),
 ("THE TRAP: doc_behavior returns pass for a lane with no slot instead of unverifiable",
  '        return ("doc_behavior", "unverifiable",\n                _u("NO_DOC_SLOT", f"no description slot is defined for lane \'{lane}\'"))',
  '        return ("doc_behavior", "pass", "assumed fine")',
  "NO slot defined"),
 # ⛔ ROUND 20: C4 replaced assert_nonvacuous's NON_PYTHON_AST return, so this guard lost
 # its subject. The RULE it defends -- an unverifiable return must carry a reason code --
 # is unchanged; moved to importable, which is still python-only.
 ("THE TRAP: an unverifiable return loses its reason code",
  '        return ("importable", "unverifiable",\n                _u("NON_PYTHON_AST", f"decidable on the python AST only; lane is \'{lane}\'"))',
  '        return ("importable", "unverifiable",\n                f"decidable on the python AST only; lane is \'{lane}\'")',
  'MATRIX importable x cpp'),
 # ⛔ ROUND 20: assert_nonvacuous is now LEGITIMATELY all-lanes (C4), and the MATRIX+
 # positive arm is what earns that declaration. The guard -- declaring coverage you do
 # not have must break the matrix -- moves to importable, the last python-only check.
 ("coverage table overclaims: python-only checks declared for all lanes",
  '    "importable":           ("python",),    # python AST only',
  '    "importable":           LANES,',
  'MATRIX importable x cpp'),
 ("the empty-lane row is dropped from the matrix (fake exhaustiveness)",
  '        for _lane in list(LANES) + ["cobol"]:',
  '        for _lane in list(LANES):',
  "MATRIX is exhaustive"),
 # ---- 4Q round 3
 ("F1 rust raw-string branch gutted",
  '            if lane == "rust" and c in "rb":\n',
  '            if lane == "rust" and False:\n',
  "raw string"),
 ("F3 js regex keyword position reverted",
  '                    prev_sig in "=(,:[!&|?{};+*%~^" or _js_regex_after_kw(text, i)):',
  '                    prev_sig in "=(,:[!&|?{};+*%~^"):',
  "regex after `return`"),
 ("F2/F5 import-line scanner reverted to blind find()",
  '            if ln.startswith(tok, k):\n                break',
  '            if False:\n                break',
  "REAL // comment on an import line"),
 ("F5 string tracking removed from the import scanner",
  '            if q:\n',
  '            if False:\n',
  "import path containing //"),
 ("F2 block-comment arm of the scanner removed",
  '            if lane != "r" and ln.startswith("/*", k):',
  '            if False and ln.startswith("/*", k):',
  "/* */ comment on a restored #include"),
 ("F4 KNOWN_FINDINGS lane key reverted to stem",
  "    hit = KNOWN_FINDINGS.get((stem, lane))",
  "    hit = KNOWN_FINDINGS.get(stem)",
  "KNOWN_FINDING"),
 ("seed detection removed",
  "        if ok and _seeded:", "        if False:",
  "SEEDED random is not nondeterminism"),
 ("assert-False marker treated as vacuous",
  "        (markers if not const else dead).append(a.lineno)",
  "        dead.append(a.lineno)",
  "FAILURE-PATH MARKER"),
 ("unknown lane silently passes",
  '        return (name, "unverifiable", _u("NO_RULE_TABLE", f"no {name} rule table for lane \'{lane}\'"), [])\n',
  '        return (name, "pass", "no rule table", [])\n',
  "unknown lane is UNVERIFIABLE not pass"),
 ("__main__ guard exemption removed",
  "        if isinstance(n, ast.If) and _is_main_guard(n.test):",
  "        if isinstance(n, ast.If):",
  "NON-guard if block is not exempt"),
 ("third-party detection removed",
  "    third = sorted(m for m in mods if m not in _STDLIB and not m.startswith(\"_\"))",
  "    third = []",
  "third-party import is flagged"),
 ("exact-duplicate detection removed",
  "        if len(group) > 1:", "        if False:",
  "duplicate: exact pair is caught"),
 ("verdict precedence: fail no longer wins",
  'STATUS_VERDICT = {"fail": "FAIL", "flag": "FLAG"}',
  'STATUS_VERDICT = {"flag": "FLAG", "fail": "FAIL"}',
  "fail beats flag"),
 ("comment stripping removed",
  '    if lane in ("cpp", "go", "rust", "javascript", "r"):', '    if False:',
  "COMMENT"),
    ('go import lines not restored',
     '        return stripped + "\\n" + _import_lines(text, lane, stripped), True',
     '        return stripped, True',
     'non-python lane really is scanned'),
 ("SEEDED no longer requires an argument",
  '_ARG = r"\\s*\\(\\s*[^)\\s]"', '_ARG = r"\\s*\\("',
  "bare random.seed()"),
 ("seedable filter back to substring match",
  "            left = [p for p in pats if p not in SEEDABLE_PATS]",
  '            left = [p for p in pats if "random" not in p]',
  "random_device"),
 ("__main__ guard operator check removed",
  "    if not isinstance(t.ops[0], ast.Eq):\n        return False", "    if False:\n        return False",
  "INVERTED __name__ guard"),
 ("guard orelse no longer inspected",
  "            for sub in n.orelse:\n                side.append(sub.lineno)",
  "            pass",
  "elif of a main guard"),
 ("TYPE_CHECKING imports counted again",
  '            if "TYPE_CHECKING" in names:', "            if False:",
  "TYPE_CHECKING-only import"),
 ("identifier normalisation removed",
  '            toks.append("ID")', "            toks.append(t)",
  "RENAMED copy-paste"),
 ("sub-floor reported as pass again",
  '                result[p] = ("skip", f"only {len(sig[p])} distinctive shingle(s) after "',
  '                result[p] = ("pass", f"only {len(sig[p])} distinctive shingle(s) after "',
  "sub-floor file is SKIP"),
 ("empty rule table passes again",
  "    if not table[lane]:", "    if False:",
  "EMPTY rule table"),
 ("norm_source strips any AE1. line again",
  '        if "AE1." in s and re.match(r\'^\\s*(#|//|/\\*|--|;)\', s):',
  '        if "AE1." in s:',
  "keeps a CODE line containing AE1."),
 ("native declaration ignored",
  "        elif stem in native.get(lane, ()):", "        elif False:",
  "DECLARED native is native"),
 ("rust treated as source-requiring again (191 false orphans)",
  "        elif lane in SOURCE_REQUIRED_LANES:", "        elif True:",
  "STANDALONE, not twin_orphan"),
 ("multi_source never set",
  "            out[f] = (\"twin\", stem, len(src_stems[stem]) > 1)",
  "            out[f] = (\"twin\", stem, False)",
  "flagged multi_source"),
 ("near-dup advisory promoted back to a verdict-changing flag",
  '        return ("duplicate", "skip",', '        return ("duplicate", "flag",',
  "ADVISORY does not change the verdict"),
 ("document-frequency filter removed",
  "        sig = {q: {g for g in sh[q] if df[g] <= cutoff} for q in ps}",
  "        sig = {q: set(sh[q]) for q in ps}",
  "DF filter POSITIVE ARM"),
 ("known findings silently dropped",
  '    hit = KNOWN_FINDINGS.get((stem, lane))', '    hit = None',
  "KNOWN finding is flagged"),
 ("rust lifetime handling removed (4Q F1, was LIVE)",
  '                if not is_char:', '                if False:',
  "LIFETIME is not a string opener"),
 ("cpp raw-string handling removed (4Q F2)",
  '            if lane == "cpp" and c == "R" and i + 1 < n and text[i + 1] == \'"\':',
  "            if False:",
  "RAW STRING with embedded quotes"),
 ("js regex-literal handling removed (4Q F4)",
  '            if lane == "javascript" and c == "/" and (',
  '            if False and (',
  "REGEX LITERAL containing quotes does not swallow"),
 ("abs_path back to raw text (4Q F5)",
  # ⛔ ROUND 20: this anchor was ONE line and matched TWICE once C6's _deps_nonpython
  # added an identical call, so the mutant printed SKIPPED and the guard went dark. A
  # SKIPPED mutant is not a pass -- it is a defence that stopped defending. Anchored past
  # the shared line onto the check's own name.
  '    code, ok = strip_noncode(text, lane, keep_strings=True)\n    if not ok:\n        return ("hardcoded_abs_path", "unverifiable",',
  '    code, ok = (text, True)\n    if not ok:\n        return ("hardcoded_abs_path", "unverifiable",',
  "quoted path inside a COMMENT"),
 ("index_parity substring fallback restored (4Q D3)",
  "        if str(p.relative_to(ROOT)) in txt:",
  "        if str(p.relative_to(ROOT)) in txt or p.name in txt:",
  "SUBSTRING of a listed file"),
 ("norm_source strips *-prefixed AE1 lines again (4Q D2)",
  "if \"AE1.\" in s and re.match(r'^\\s*(#|//|/\\*|--|;)', s):",
  "if \"AE1.\" in s and re.match(r'^\\s*(#|//|/\\*|\\*|--|;)', s):",
  "*-prefixed CODE line containing AE1."),
    # ---- the TWO-AXIS verdict (Illia 2026-08-30). New code is unmutated code.
    ('2AXIS coverage_for always says FULL (the gap disappears entirely)',
     '    return "PARTIAL" if measured else "NONE"', '    return "FULL"',
     'NO record can hide an unmeasured check'),
    ('2AXIS NONE collapsed into PARTIAL (nothing-measured looks partly-measured)',
     '    return "PARTIAL" if measured else "NONE"', '    return "PARTIAL"',
     'reserved for a record where NOTHING'),
    ('2AXIS unverifiable put back on the FINDING axis (the ORIGINAL defect)',
     'STATUS_VERDICT = {"fail": "FAIL", "flag": "FLAG"}',
     'STATUS_VERDICT = {"fail": "FAIL", "flag": "FLAG", "unverifiable": "UNVERIFIABLE"}',
     'is not called UNVERIFIABLE'),
    ('2AXIS verdict drops its coverage half (a consumer reading  loses the gap)',
     '    return "%s/%s" % (finding_for(checks), coverage_for(checks))',
     '    return "%s" % (finding_for(checks),)',
     'gap is inside the verdict STRING'),
    ('2AXIS the exit-2 coverage guard is disarmed',
     '    blocking = [r for r in records if axes_of(r)[1] != "FULL"]',
     '    blocking = []',
     'EXIT-GUARD'),
    ('2AXIS the exit-2 guard fires ALWAYS (a constant is not a guard)',
     '    return (2 if blocking and not acknowledged else 0), blocking',
     '    return 2, blocking',
     'EXIT-GUARD'),
    ('2AXIS a MISSING coverage axis defaults to FULL (absent axis reads as covered)',
     '    return a.get("finding"), a.get("coverage")',
     '    return a.get("finding"), a.get("coverage", "FULL")',
     'EXIT-GUARD'),
    ('2AXIS the top-level `finding` SEAM is reintroduced (6E reader path 2)',
     '                "axes": {"finding": finding_for(checks),',
     '                "finding": finding_for(checks), "axes": {"finding": finding_for(checks),',
     '6E-2AXIS path 2'),
    ('2AXIS renderer sums NONE into PARTIAL again',
     '_part = [r for r in recs if _coverage(r) == "PARTIAL"]',
     '_part = [r for r in recs if _coverage(r) != "FULL"]',
     'PARTIAL and NONE are reported as DIFFERENT facts', R),
    ('2AXIS renderer stops asserting that nothing hides its gap',
     '    if not hidden:', '    if False:',
     'NO record can hide an unmeasured check', R),
    # ---- WAIVERS. The whole mechanism exists to stop a waiver acting like a pass.
    ('WAIVER validation disabled (an unsigned, unreferenced waiver loads)',
     '        missing = [k for k in WAIVER_REQUIRED if not str(w.get(k) or "").strip()]',
     '        missing = []',
     'REFUSES TO LOAD'),
    ('WAIVER ⛔ a waived finding is rewritten to PASS (the exact failure it must prevent)',
     '                c["waived"] = {"owner"',
     '                c["status"] = "pass"; c["waived"] = {"owner"',
     'STILL A FINDING'),
    ('WAIVER the sha pin is ignored (a stale waiver absorbs a changed file)',
     '                if live != w["file_sha256"]:', '                if False:',
     'STALE waiver'),
    ('WAIVER orphan tracking removed (a waiver protecting nothing goes unreported)',
     '    orphan = [w for w in waivers if id(w) not in matched]', '    orphan = []',
     'ORPHAN waiver'),
    ('WAIVER applies to NON-finding checks (annotate something never found)',
     '            if c.get("status") not in FINDING_STATUSES:', '            if False:',
     'NEGATIVE ARM'),
    ('WAIVER renderer drops the WAIVED table (finding accepted AND invisible)',
     '    if _waived_rows:', '    if False:',
     'WAIVED section itself', R),
    ('2AXIS the coverage HEADLINE is removed (6E reader path 1)',
     '    w(f"> ## \u26d4 {_not_full} of {len(recs)} patterns were NOT fully measured")',
     '    pass',
     '6E-2AXIS path 1', R),
    ('WAIVER renderer reads the header one level too deep (the bug found 2026-08-30: '
     'renders "0 waivers loaded" beside real waived rows)',
     '_wv = header.get("waivers") or {}',
     '_wv = (header.get("run") or {}).get("waivers") or {}',
     'STALE', R),

    # ---- ROUND 21: the _IMPORT_LINE <-> DEPS_EXTRACT agreement fixes ----
    # ---- RETIRED 2026-09-02, with the measurement, NOT because it was inconvenient ----
    # 'R21 go _IMPORT_LINE gets its string-blind bare quote back (the csv_validator FP)'
    # old: '    "go": re.compile(r'^\\s*import\\s'),'
    # new: '    "go": re.compile(r'^\\s*(import\\s|")'),'
    # It SURVIVED the 2026-09-02 run and it is a genuine EQUIVALENT MUTANT, not a gap.
    # Round 22 made _import_lines decide on the LEXED view, and the lexer blanks string
    # DELIMITERS as well as string bodies. A go grouped-import body line is `\t"fmt"` --
    # in the lexed view its leading quote is a space. So `^\s*(import\s|")` cannot match
    # anything the original `^\s*import\s` did not already match: the mutation is
    # unobservable BY CONSTRUCTION, not merely unprobed.
    # DO NOT re-add it to buy back a KILLED count. If the lexed-view design is ever
    # reverted, this mutant becomes live again and must come back with it.
    ('R22 the restore decides on the ORIGINAL text again (every string defect returns)',
     '        if _i in _fallback:\n            vw = ln',
     '        if True:\n            vw = ln',
     'library() inside a STRING'),
    ('R21 _deps_go loses the alias prefix (idiomatic aliased grouped imports go blind)',
     'r\'^[ \\t]*(?:[\\w.]+[ \\t]+)?"([^"]+)"[ \\t]*(?://.*)?$\'',
     'r\'^[ \\t]*"([^"]+)"[ \\t]*(?://.*)?$\'',
     'AGREE go ALIASED'),
    ('R21 R restore is re-anchored to the line start (requireNamespace in a guard is dropped)',
     '    "r": re.compile(r\'^.*\\b(library|requireNamespace|require)\\s*\\(\'),',
     '    "r": re.compile(r\'^\\s*(library|require)\\s*\\(\'),',
     'AGREE r requireNamespace inside'),
    ('R21 js _IMPORT_LINE loses dynamic import( (the restore drops it before the extractor)',
     '    "javascript": re.compile(r\'^\\s*(import\\s|const\\s+\\w+\\s*=\\s*require|.*\\b(?:require|import)\\s*\\()\'),',
     '    "javascript": re.compile(r\'^\\s*(import\\s|const\\s+\\w+\\s*=\\s*require|.*\\brequire\\s*\\()\'),',
     'AGREE javascript DYNAMIC'),
    ('R21 _deps_js loses the dynamic import() capture',
     '    ms |= set(re.findall(r"""\\bimport\\s*\\(\\s*["\']([^"\']+)["\']""", code))',
     '    ms |= set()',
     'AGREE javascript DYNAMIC'),
    ('R22 the retracted cpp quote-form rule is re-added WITH the slash test',
     '    hs = set(re.findall(r"#\\s*include\\s*<([^>]+)>", code))',
     '    hs = set(re.findall(r"#\\s*include\\s*<([^>]+)>", code))\n    hs |= {h for h in re.findall(r\'#\\s*include\\s*"([^"]+)"\', code) if "/" in h}',
     'QUOTE-form third-party is NOT read'),
    ('R22 the retracted cpp quote-form rule is re-added with NO slash test',
     '    hs = set(re.findall(r"#\\s*include\\s*<([^>]+)>", code))',
     '    hs = set(re.findall(r"#\\s*include\\s*<([^>]+)>", code))\n    hs |= set(re.findall(r\'#\\s*include\\s*"([^"]+)"\', code))',
     'QUOTE-form bare local header stays silent'),
    ('R22 python import_module accepts ANY bare name (a local def is read as importlib)',
     '                     or (isinstance(f, ast.Name) and f.id in il_funcs))',
     '                     or (isinstance(f, ast.Name) and f.id is not None))',
     'a LOCAL def import_module'),
    ('R22 python import_module accepts ANY attribute owner (loader.import_module counts)',
     '            named = ((isinstance(f, ast.Attribute) and f.attr == "import_module"\n                      and isinstance(f.value, ast.Name) and f.value.id in il_mods)',
     '            named = ((isinstance(f, ast.Attribute) and f.attr == "import_module"\n                      and isinstance(f.value, ast.Name))',
     'UNRELATED module'),

    # ---- ROUND 22: the lexed-view restore and its fallback ----
    ('R22 the lexer-lost-the-plot fallback is removed (a malformed literal hides every import below)',
     '    _fallback = set()\n    for _i in range(len(src) - 1, -1, -1):',
     '    _fallback = set()\n    for _i in range(0, -1, -1):',
     'MALFORMED literal'),
    ('R22 go: the block detector no longer sees a commented `import (` line',
     "            if re.match(r'^import\\s*\\($', st):\n                in_block = True",
     "            if re.match(r'^XXR22never\\($', st):\n                in_block = True",
     'inline comment on the `import (` line'),
]
def run():
    r = subprocess.run([PY_, P, "--self-test"], capture_output=True, text=True,
                       cwd=ROOT)
    out = r.stdout + r.stderr
    fails = [l.strip() for l in out.splitlines() if l.strip().startswith("FAILED:")]
    broken = ("Traceback" in out or "SyntaxError" in out
              or "probe(s)," not in out)   # no summary => the suite never ran
    return fails, broken

def count_oracle():
    """D1: the summary count is the one line proving the suite RAN. Check it against an
    INDEPENDENT count of the probe lines actually printed -- an arithmetic guess drifted
    off by 2 and nobody noticed (4Q round 3)."""
    r = subprocess.run([PY_, P, "--self-test"], capture_output=True, text=True,
                       cwd=ROOT)
    out = r.stdout + r.stderr
    lines = sum(1 for l in out.splitlines()
                if l.startswith("  ok  ") or l.startswith("  FAIL  "))
    claimed = None
    for l in out.splitlines():
        if "probe(s)," in l:
            claimed = int(l.split()[0])
    return claimed, lines

_cl, _ln = count_oracle()
print("count oracle: claims %s, printed %d probe lines -> %s"
      % (_cl, _ln, "AGREE" if _cl == _ln else "*** DISAGREE ***"))
if _cl != _ln:
    print("*** SELF-TEST MISCOUNTS ITSELF — ABORTING ***"); sys.exit(1)

f, c = run()
print("control: failures=%d crashed=%s" % (len(f), c))
if f or c:
    print("*** CONTROL NOT CLEAN — ABORTING ***")
    print("    broken=True means the suite did not RUN (SyntaxError,"
          " traceback, or no summary line) — every mutant would score for free.")
    sys.exit(1)

# ⛔ The renderer is a SEPARATE FILE and mutants aimed at it silently SKIPPED -- an anchor
# that matches 0 measures nothing. A mutant may now name its target as a 5th element.
# ⛔ A HARNESS KILLED MID-MUTANT LEAVES A MUTATED PRODUCTION FILE ON DISK. A 2-minute
# timeout did exactly that on 2026-08-30: the restore never ran, the NEXT run copied the
# mutated file as its own baseline, and the control came back with 15 failures. I nearly
# committed a tool with a deliberately broken verdict_for. Restore is now unconditional --
# it runs on timeout, Ctrl-C, and crash, not only on the happy path.
import atexit, signal
def _restore_all():
    for _t, _b in ((P, BAK), (R, RBAK), (BX, BXBAK)):
        try:
            shutil.copy(_b, _t)
        except Exception as _e:
            print("*** RESTORE FAILED for %s: %s ***" % (_t, _e))
atexit.register(_restore_all)
for _sig in (signal.SIGTERM, signal.SIGINT):
    signal.signal(_sig, lambda *_a: sys.exit("*** killed -- restoring originals ***"))

for _m in MUTANTS:
    label, old, new, frag = _m[0], _m[1], _m[2], _m[3]
    tgt  = _m[4] if len(_m) > 4 else P
    bak  = {R: RBAK, BX: BXBAK}.get(tgt, BAK)
    tbase = {R: rbase, BX: bxbase}.get(tgt, base)
    s = open(bak).read()
    n = s.count(old)
    if n != 1:
        print("\n%-45s SKIPPED (anchor matched %d)" % (label, n)); continue
    mut = s.replace(old, new, 1)
    try:
        ast.parse(mut)                     # a mutant that cannot parse is not a result
    except SyntaxError as e:
        print("\n%-45s SKIPPED (mutant does not parse: %s)" % (label, e)); continue
    open(tgt,"w").write(mut)
    fails, crashed = run()
    hit = [x for x in fails if frag in x]
    if hit or crashed:
        verdict = "KILLED"
    elif fails:
        # Something DID die -- just not the probe this mutant names. That is a defect in the
        # mutant's search fragment, not evidence the fix is undefended. Never call it SURVIVED.
        verdict = "KILLED-BY-OTHER (frag %r missed; fix the frag)" % frag
    else:
        verdict = "*** SURVIVED — DECORATION ***"
    print("\n%-45s %s" % (label, verdict))
    print("   failures=%d crashed=%s" % (len(fails), crashed))
    for x in fails[:2]: print("     ", x[:100])
    shutil.copy(bak, tgt)
    assert hashlib.md5(open(tgt,"rb").read()).hexdigest() == tbase, "RESTORE FAILED " + label

print("\nrestored tool:", hashlib.md5(open(P,"rb").read()).hexdigest() == base)
print("restored renderer:", hashlib.md5(open(R,"rb").read()).hexdigest() == rbase)
print("restored ruler:", hashlib.md5(open(BX,"rb").read()).hexdigest() == bxbase)
