#!/usr/bin/env python3
"""library-verify — the Grand Library's CI (multi-language).

Green means the library is what it claims:
  (a) every populated subtree: Ed25519 signature valid + catalog/manifest integrity
  (b) every file carries a valid master-0 watermark with the right mark
  (c) master CATALOG.md ID set == on-disk ID set
  (d) [--gate] every file compiles/runs exit 0 (python3/Rscript/node/g++/go/rustc);
      a missing toolchain is a LOUD per-language SKIP that turns the run RED, and a file
      that HANGS is INCONCLUSIVE — also RED. Neither is ever counted as validated
  (e) quarantine IDs absent from all shippable trees
  (f) twin integrity: no cpp/go twin whose source ID is quarantined or missing,
      UNLESS it is explicitly declared NATIVE in MANIFEST.json (see below)
  (g) self-test: the quarantine checks are PROVEN non-vacuous on every run (--self-test
      to run it alone); a check that cannot fail is worse than no check
  (h) twin contract divergence == the number MANIFEST.json declares it to be

RULER v2 — 2026-07-27, the NATIVE LANE (versioned change, Illia's yes).
Until now (f) assumed every cpp/go file is a CONVERSION TWIN of a python/r pattern. That was
true when written and is no longer: a sphere can be harvested natively in a compiled language
(the Go concurrency sphere has no meaningful python source — goroutine scheduling and sync.Mutex
do not survive translation). The rule is NOT relaxed: an orphan twin still goes RED. A native
pattern must be DECLARED, in MANIFEST.json:

    "native_patterns": { "go": ["fan_in_multiplexer", ...], "cpp": [...] }

Declared -> exempt from the source-ID requirement. Undeclared and sourceless -> RED, as before.
The declaration is the point: a native pattern is a deliberate statement, never an inference
from a missing file. Silence still fails.

RULER v3 — 2026-07-28, the QUARANTINE LEDGERS (bug fix, no relaxation).
(e) and (f) built their ID set with `(_quarantine).glob("*.py")`. That directory holds no .py
files — the held-out sources were deleted, not stored — so the set was ALWAYS EMPTY and both
checks passed trivially for months. They never blocked anything. A vacuous check that prints
GREEN is the exact failure class this library exists to prevent, so the fix comes in two parts:
read the real ledgers, and prove on every run that the checks can still go RED (see self_test).

The ledgers, all three of them:
    _quarantine/QUARANTINE.md   — held-out SOURCES (assert-linter REJECTs)
    QUARANTINE.jsonl            — structured records, one JSON object per line
    MANIFEST.json["quarantine"] — the manifest's mirror of the .md list; a disagreement
                                  between the two is a ledger split and goes RED

SCOPE is part of the record. A source quarantine condemns the ID everywhere, twins included.
A twin quarantine (`"lang": "cpp"` — twin invalidated by source_sha256 drift) condemns THAT
TREE ONLY: the python source drifted because it was FIXED, and a ruler that punishes the repair
is a broken ruler. Anything unscoped fails closed to source-wide.

RULER v3.1 — 2026-07-28, TWIN CONTRACT DIVERGENCE (a declared number, not a verdict).
The 2026-07-21 retrofit (7497d40) gave 119 python sources an `_aura_validate_*` input contract
and deliberately excluded the compiled lanes. So 125 cpp twin files now reject nothing their
sources reject. Nothing in the tree could see that — the same blindness that let the quarantine
glob run empty for weeks.

This is NOT scored as a defect. No cpp attack lane exists yet, so it is unknown which of those
twins actually accept the attacks their sources now refuse; C++ typing kills whole classes for
free, and the library's own measured base rate for NaN/domain flags is ~15% real. Declaring 125
patterns broken on that evidence would be the opposite failure to a vacuous green: a loud check
that is wrong. So the number is DECLARED in MANIFEST.json and RED only when it MOVES — in either
direction. A rise means twins shipped behind their sources; a fall means twins were fixed and the
manifest still claims otherwise. Both are claims about the library that stopped being true.

RULER v3.2 — 2026-08-04, THE GATE REAPS ITS CHILDREN + "I COULD NOT MEASURE THIS".
Two fixes, both defects rather than enhancements.

(1) All six `subprocess.run(..., timeout=)` calls killed only the DIRECT child. `go run` execs its
compiled binary as a grandchild, so on timeout the runner died and the binary kept spinning at
100% CPU. Six of those once cooked this laptop; the same shape burned 18 hours at 92°C on .8.
Every spawn now goes through `_run()`: `start_new_session=True`, and `killpg` on timeout. The
self-test proves it with a fixture that ACTUALLY orphans — it first demonstrates the leak under
the old semantics, because a reaper never observed to reap is not a reaper.
Also fixed alongside: the gate compiled every cpp and rust file to ONE fixed path (`/tmp/_apl_x`),
so a failed compile left a stale binary exactly where the next file's run would look.

(2) run_gate had no way to say "I could not measure this" as distinct from "I measured it and it
is wrong". A hang used to raise TimeoutExpired and crash the verifier outright. There are now four
outcomes — ok / fail / skip / inconclusive — routed through the pure `gate_outcome()`, which FAILS
CLOSED: any verdict it does not recognise is inconclusive, never a pass.

Requires `folder-nature>=0.2` (falls back to the v-next checkout on sys.path).
"""
import argparse, json, os, re, shutil, signal, subprocess, sys, tempfile, time
from pathlib import Path

try:
    from folder_nature.mark import signing
    from folder_nature.mark.watermark import verify_file
except ModuleNotFoundError:
    sys.path.insert(0, str(Path.home() / "Projects/folder-nature"))
    from folder_nature.mark import signing
    from folder_nature.mark.watermark import verify_file

ROOT = Path(__file__).resolve().parent
SIGNED_SUBTREES = ["python/programming", "python/data-science", "python/system-administration", "r", "cpp", "rust", "go", "javascript"]
GATE = {".py": ["python3"], ".R": ["Rscript"], ".js": ["node"]}   # cpp/go/rust handled specially
SRC_EXT = (".py", ".R", ".cpp", ".go", ".rs", ".js")

# Ledgers that MUST exist and MUST parse to at least one record. Emptying the quarantine is a
# deliberate act: you remove the ledger from this tuple in code, where it is reviewed. Silence
# — a deleted ledger, a parser that reads zero — fails, exactly as the native lane fails.
QUARANTINE_LEDGERS = ("_quarantine/QUARANTINE.md", "QUARANTINE.jsonl")
SOURCE_LANGS = {"python", "r", "javascript"}             # a quarantine here condemns twins too
_MD_ENTRY = re.compile(r"^\s*[-*]\s+`([^`]+)`")

# (h) An input contract is recognised by the retrofit's own markers. A twin that grows one by
# some other name reads as divergent — deliberately: the marker IS the declaration.
CONTRACT_MARKS = ("_aura_validate_", "AuraInputError", "aura_validate")
TWIN_LANES = (("cpp", ".cpp"), ("go", ".go"), ("rust", ".rs"))


class GateTimeout(Exception):
    """Raised after a hung gate's process GROUP has been reaped."""


def _reap(proc) -> None:
    """SIGKILL the process GROUP, not the process. Never raises — the caller is already failing."""
    try:
        os.killpg(os.getpgid(proc.pid), signal.SIGKILL)
    except (ProcessLookupError, PermissionError, OSError):
        pass
    try:
        proc.communicate(timeout=5)
    except Exception:
        try:
            proc.kill()
        except Exception:
            pass


def _run(cmd, timeout: int, cwd=None) -> int:
    """Run cmd in its OWN SESSION and reap the WHOLE GROUP on timeout. Returns the returncode.

    `subprocess.run(timeout=)` kills only the DIRECT child. `go run` compiles to a temp binary and
    execs it as a grandchild; a python pattern may spawn anything. On timeout the runner dies and
    the grandchild keeps spinning at 100% CPU — six of those once cooked this laptop, and the same
    shape burned 18 hours at 92°C on .8. start_new_session makes the child a group leader so its
    descendants share its pgid, and killpg takes the whole family.
    """
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                            cwd=cwd, start_new_session=True)
    try:
        proc.communicate(timeout=timeout)
        return proc.returncode
    except subprocess.TimeoutExpired:
        _reap(proc)
        raise GateTimeout(f"{cmd[0]} exceeded {timeout}s")


def gate_outcome(verdict: str):
    """Map a run_gate verdict to (kind, detail). Pure, so the self-test can prove that nothing
    except a literal 'ok' can ever be bucketed as a pass.

    ⛔ FAILS CLOSED: an unrecognised verdict is INCONCLUSIVE, never a pass. A future verdict
    string added to run_gate and forgotten here must go RED, not silently green.
    """
    if verdict == "ok":
        return ("pass", None)
    if verdict == "fail":
        return ("fail", None)
    if verdict.startswith("skip:"):
        return ("skip", verdict[5:])
    if verdict.startswith("inconclusive:"):
        return ("inconclusive", verdict.split(":", 1)[1])
    return ("inconclusive", f"unrecognised gate verdict {verdict!r}")


_GATE_TMP = None


def _gate_tmp() -> Path:
    """Per-run scratch for compiled binaries. The old code reused a single fixed /tmp path for
    every cpp and rust file in the library — one name, 570 files, and a stale binary left behind
    by a failed compile sitting exactly where the next run looks."""
    global _GATE_TMP
    if _GATE_TMP is None:
        _GATE_TMP = Path(tempfile.mkdtemp(prefix="apl-gate-"))
    return _GATE_TMP


def run_gate(p: Path, timeout: int = 120) -> str:
    """Gate one file. Returns 'ok' | 'fail' | 'skip:<toolchain>' | 'inconclusive:<why>'.

    FOUR outcomes, and only one of them is a pass:
      ok           — measured, exit 0
      fail         — MEASURED AND WRONG
      skip:<tc>    — toolchain missing; nothing was measured
      inconclusive — the tool could not measure this file at all (a hang, a reaped group)

    'inconclusive' exists because there was previously no way to say "I could not tell" as
    distinct from "I checked and it is fine". Both skip and inconclusive turn the run RED. A
    verifier that cannot express its own ignorance will eventually report it as a pass.
    """
    try:
        if p.suffix in (".py", ".R", ".js"):
            runner = GATE[p.suffix][0]
            if not shutil.which(runner):
                return f"skip:{runner}"
            return "ok" if _run([runner, str(p)], timeout) == 0 else "fail"
        if p.suffix == ".cpp":
            if not shutil.which("g++"):
                return "skip:g++"
            out = _gate_tmp() / f"{p.stem}_cpp"
            try:
                if _run(["g++", "-O2", "-std=c++17", str(p), "-o", str(out)], timeout) != 0:
                    return "fail"
                return "ok" if _run([str(out)], timeout) == 0 else "fail"
            finally:
                out.unlink(missing_ok=True)
        if p.suffix == ".go":
            if not shutil.which("go"):
                return "skip:go"
            return "ok" if _run(["go", "run", str(p)], timeout) == 0 else "fail"
        if p.suffix == ".rs":
            if not shutil.which("rustc"):
                return "skip:rustc"
            out = _gate_tmp() / f"{p.stem}_rs"
            try:
                if _run(["rustc", "-O", "--edition", "2021", "-D", "warnings",
                         str(p), "-o", str(out)], timeout) != 0:
                    return "fail"
                return "ok" if _run([str(out)], timeout) == 0 else "fail"
            finally:
                out.unlink(missing_ok=True)
    except GateTimeout as e:
        return f"inconclusive:{e}"
    return "ok"


def annotation_failures(root: Path, files=None) -> list:
    """(i) Every top-level function's signature must be READABLE. Returns [(file, fn, error)].

    WHY THIS EXISTS — found 2026-08-07 by the robustness probe, not by this verifier.
    `pca_power_iteration` annotated `-> Tuple[...]` while importing the name as `TupleType`.
    Python 3.14 evaluates annotations LAZILY (PEP 649), so the module imports, the file exits 0,
    and `--gate` passed it happily. Anything that then reads `__annotations__` —
    `inspect.signature`, doc tooling, a type checker, this library's own doc generators —
    raises `NameError`. The gate asks "does it run"; a published signature that cannot be read
    is a false claim the gate is structurally blind to.

    Imports are safe here: all python patterns are `__main__`-guarded, so nothing executes.
    Modules are given unique names from their path and are never inserted into sys.modules.
    """
    import importlib.util, inspect, io, contextlib
    out = []
    for p in (files if files is not None else sorted(root.glob("python/**/*.py"))):
        if "__pycache__" in p.parts:
            continue
        modname = "aplchk_" + str(p).replace("/", "_").replace(".", "_")
        try:
            spec = importlib.util.spec_from_file_location(modname, p)
            mod = importlib.util.module_from_spec(spec)
            with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
                spec.loader.exec_module(mod)
        except Exception:
            continue          # an unimportable file is the GATE's finding, not this check's
        for name, obj in vars(mod).items():
            if not inspect.isfunction(obj) or obj.__module__ != modname:
                continue
            try:
                inspect.signature(obj)
            except NameError as e:
                out.append((p, name, str(e)))
            except Exception:
                pass          # unresolvable for other reasons is not this check's claim
    return out


def load_quarantine(root: Path):
    """Read the ACTUAL quarantine ledgers on disk. Returns (q_all, q_lang, counts, problems).

      q_all    — IDs quarantined at the SOURCE: forbidden in EVERY shippable tree, twins included.
      q_lang   — lang -> IDs quarantined in that language tree ONLY (a twin invalidated while its
                 source stayed good). See the SCOPE paragraph in the module docstring.
      counts   — ledger path -> records parsed (rejoined ones included: this counts READS, not
                 active holds, so a parser that silently reads nothing is visible).
      problems — every one of these is RED. An unreadable record is never a skip.
    """
    q_all, q_lang, counts, problems = set(), {}, {}, []

    md = root / "_quarantine" / "QUARANTINE.md"
    md_ids = set()
    if md.exists():
        for line in md.read_text(encoding="utf-8").splitlines():
            m = _MD_ENTRY.match(line)
            if not m:
                continue
            tok = m.group(1).strip()
            stem, dot, ext = tok.rpartition(".")
            if not dot:
                stem = tok
            elif f".{ext}" not in SRC_EXT:
                problems.append(f"QUARANTINE.md: entry `{tok}` has no recognised source suffix")
                continue
            md_ids.add(stem)
        counts["_quarantine/QUARANTINE.md"] = len(md_ids)
    q_all |= md_ids

    jl = root / "QUARANTINE.jsonl"
    if jl.exists():
        n = 0
        for i, line in enumerate(jl.read_text(encoding="utf-8").splitlines(), 1):
            if not line.strip():
                continue
            try:
                e = json.loads(line)
            except ValueError as exc:
                problems.append(f"QUARANTINE.jsonl:{i}: unparseable ({exc}) — an unreadable "
                                f"quarantine record is RED, never a skip")
                continue
            pid = str(e.get("id") or "").strip()
            if not pid:
                problems.append(f"QUARANTINE.jsonl:{i}: record with no id")
                continue
            n += 1
            if str(e.get("status") or "").strip().lower() == "rejoined":
                continue
            lang = str(e.get("lang") or "").strip().lower()
            if lang in SOURCE_LANGS or lang in ("", "*", "all"):
                q_all.add(pid)                       # unscoped fails closed to source-wide
            else:
                q_lang.setdefault(lang, set()).add(pid)
        counts["QUARANTINE.jsonl"] = n

    for led in QUARANTINE_LEDGERS:
        if not (root / led).exists():
            problems.append(f"declared quarantine ledger '{led}' is MISSING — an absent ledger "
                            f"reads as 'nothing quarantined', which is how (e)/(f) went vacuous")
        elif not counts.get(led):
            problems.append(f"quarantine ledger '{led}' parsed 0 records — either it was emptied "
                            f"without removing it from QUARANTINE_LEDGERS, or the parser is broken")

    try:
        mf_q = {Path(x).stem for x in (json.loads((root / "MANIFEST.json").read_text(encoding="utf-8"))
                                       .get("quarantine") or [])}
    except (OSError, ValueError) as exc:
        problems.append(f"MANIFEST.json unreadable for the quarantine list ({exc})")
        mf_q = None
    if mf_q is not None and mf_q != md_ids:
        problems.append(f"ledger split: MANIFEST.json 'quarantine' != _quarantine/QUARANTINE.md "
                        f"(manifest-only: {sorted(mf_q - md_ids)}; md-only: {sorted(md_ids - mf_q)})")
    if mf_q:
        q_all |= mf_q                                # union, so a split still blocks while it is fixed

    return q_all, q_lang, counts, problems


def _has_contract(p: Path) -> bool:
    return any(m in p.read_text(encoding="utf-8", errors="replace") for m in CONTRACT_MARKS)


def count_contract_divergence(root: Path):
    """Count twin FILES whose python/r source carries an input contract they do not.

    Files, not IDs: a stem living in two spheres is two patterns (census law), so this number
    is legitimately larger than the count of distinct sources. Returns (per-lane counts, examples).
    """
    src = {}
    for p in root.glob("python/**/*.py"):
        if "__pycache__" not in p.parts:
            src[p.stem] = _has_contract(p)
    for p in root.glob("r/**/*.R"):
        src.setdefault(p.stem, _has_contract(p))

    lanes, examples = {}, []
    for lane, ext in TWIN_LANES:
        n = 0
        for p in sorted(root.glob(f"{lane}/**/*{ext}")):
            if src.get(p.stem) and not _has_contract(p):
                n += 1
                if len(examples) < 3:
                    examples.append(str(p.relative_to(root)))
        lanes[lane] = n
    return lanes, examples


def divergence_fails(block, lanes, examples) -> list:
    """Compare the declared divergence against disk. Pure, so the self-test can drive it both ways.

    Movement in EITHER direction is RED — see RULER v3.1. The declaration is the point: this
    number may only change by a deliberate edit, never by a commit nobody noticed.
    """
    if not isinstance(block, dict):
        return ["MANIFEST.json has no 'twin_contract_divergence' block — the source/twin input-"
                "contract gap would move in silence (RULER v3.1)"]
    fails = []
    declared_lanes = block.get("lanes") or {}
    if block.get("declared") != sum(declared_lanes.values()):
        fails.append(f"MANIFEST twin_contract_divergence is internally inconsistent: "
                     f"declared {block.get('declared')} != sum of lanes {sum(declared_lanes.values())}")
    for lane, n in sorted(lanes.items()):
        d = declared_lanes.get(lane, 0)
        if d != n:
            eg = f" (e.g. {examples[0]})" if examples and n > d else ""
            fails.append(f"twin contract divergence[{lane}] {'ROSE' if n > d else 'FELL'}: "
                         f"MANIFEST declares {d}, disk has {n}{eg} — update the declaration "
                         f"deliberately, do not silence it")
    return fails


def census_mismatches(root, manifest) -> list:
    """Recompute census fields from disk; return mismatches against the manifest dict.

    Takes the manifest as a PARAMETER (not read from file) so the self-test can drive it
    with synthetic dicts without touching the real MANIFEST.json. Compares six fields:
    total_shippable, total_signed_files, unique_ids, multi_language_patterns,
    languages_present, and per-subtree languages[<key>]["files"].
    """
    if not isinstance(manifest, dict):
        return [f"manifest is not a dict (got {type(manifest).__name__})"]

    LANE_EXT = {"python": ".py", "cpp": ".cpp", "rust": ".rs", "go": ".go", "r": ".R", "javascript": ".js"}
    mismatches = []

    # Count files and stems per lane on disk
    lane_filecount = {}   # lane -> file count (not unique stems)
    lane_stems = {}       # lane -> set of stems
    for lane, ext in LANE_EXT.items():
        lane_dir = root / lane
        files = []
        if lane_dir.exists():
            for p in lane_dir.rglob("*"):
                if p.suffix == ext and "__pycache__" not in p.parts:
                    files.append(p)
        lane_filecount[lane] = len(files)
        lane_stems[lane] = {p.stem for p in files}

    # total_shippable — count of pattern files across the 6 language lanes
    disk_val = sum(lane_filecount.values())
    if manifest.get("total_shippable") != disk_val:
        mismatches.append(f"total_shippable: manifest={manifest.get('total_shippable')!r}, disk={disk_val}")

    # total_signed_files — count of pattern files under the 8 SIGNED_SUBTREES
    disk_val = 0
    for st in SIGNED_SUBTREES:
        sroot = root / st
        if not sroot.exists():
            continue
        lane = st.split("/")[0]
        ext = LANE_EXT.get(lane)
        if ext is None:
            continue
        for p in sroot.rglob("*"):
            if p.suffix == ext and "__pycache__" not in p.parts:
                disk_val += 1
    if manifest.get("total_signed_files") != disk_val:
        mismatches.append(f"total_signed_files: manifest={manifest.get('total_signed_files')!r}, disk={disk_val}")

    # unique_ids — distinct pattern basenames (stem, no extension)
    all_stems = set()
    for stems in lane_stems.values():
        all_stems |= stems
    disk_val = len(all_stems)
    if manifest.get("unique_ids") != disk_val:
        mismatches.append(f"unique_ids: manifest={manifest.get('unique_ids')!r}, disk={disk_val}")

    # multi_language_patterns — basenames appearing in 2 or more languages
    stem_langs = {}
    for lane, stems in lane_stems.items():
        for s in stems:
            stem_langs[s] = stem_langs.get(s, 0) + 1
    disk_val = sum(1 for c in stem_langs.values() if c >= 2)
    if manifest.get("multi_language_patterns") != disk_val:
        mismatches.append(f"multi_language_patterns: manifest={manifest.get('multi_language_patterns')!r}, disk={disk_val}")

    # languages_present — the language lanes that hold at least one pattern file
    disk_langs = sorted(lane for lane, n in lane_filecount.items() if n > 0)
    _mfl = manifest.get("languages_present") or []
    if isinstance(_mfl, (str, bytes)) or not isinstance(_mfl, (list, tuple, set, frozenset)):
        mismatches.append(
            f"languages_present: not a list of lanes (got {type(_mfl).__name__}: {_mfl!r})")
        _mfl = []
    elif not all(isinstance(_e, str) for _e in _mfl):
        # A list of MIXED types is valid JSON, passes the container guard, and then crashes
        # sorted() -- Python cannot order str against int/None/bytes/dict/bool.
        mismatches.append(
            f"languages_present: contains a non-string lane name ({_mfl!r})")
        _mfl = []
    mf_langs = sorted(_mfl)
    if disk_langs != mf_langs:
        mismatches.append(f"languages_present: manifest={mf_langs!r}, disk={disk_langs}")

    # per-subtree files — derive the lane set from DISK (SIGNED_SUBTREES), not the manifest.
    # A subtree with files on disk but NO entry in the manifest is a mismatch — that is how
    # a deleted lane vanishes silently when the check only iterates manifest keys.
    mf_langs_dict = manifest.get("languages") or {}
    if not isinstance(mf_langs_dict, dict):
        mismatches.append(f"languages: not a dict (got {type(mf_langs_dict).__name__})")
        mf_langs_dict = {}

    # First: every SIGNED_SUBTREE with files must have a manifest entry (exact key or sub-key).
    for st in SIGNED_SUBTREES:
        sroot = root / st
        if not sroot.exists():
            continue
        lane = st.split("/")[0]
        ext = LANE_EXT.get(lane)
        if ext is None:
            continue
        disk_count = 0
        for p in sroot.rglob("*"):
            if p.suffix == ext and "__pycache__" not in p.parts:
                disk_count += 1
        if disk_count == 0:
            continue
        has_entry = st in mf_langs_dict or any(
            isinstance(k, str) and k.startswith(st + "/") for k in mf_langs_dict)
        if not has_entry:
            mismatches.append(f"languages[{st}]: missing from manifest, disk has {disk_count} file(s)")

    # Sum invariant — keying-independent. A SIGNED_SUBTREE may be split across several
    # manifest keys (go -> go/programming + go/system-administration), so the presence test
    # above is satisfied by a surviving sibling and a deleted entry hides. The declared counts
    # must SUM to the disk total; no keying scheme can fool that.
    if mf_langs_dict:
        declared_sum = 0
        for _k, _info in mf_langs_dict.items():
            _v = _info.get("files") if isinstance(_info, dict) else _info
            # bool is an int subclass but is never a valid count; str/bytes must not be
            # coerced. Everything else defers to int(), so Decimal/Fraction are accepted the
            # same way the per-subtree != comparison accepts them.
            if isinstance(_v, (bool, str, bytes)):
                mismatches.append(f"languages[{_k}].files: not a number ({_v!r})")
                continue
            try:
                declared_sum += int(_v)
            except (ValueError, OverflowError, TypeError):
                mismatches.append(f"languages[{_k}].files: not a finite number ({_v!r})")
        disk_total = sum(lane_filecount.values())
        if declared_sum != disk_total:
            mismatches.append(
                f"languages[*].files sums to {declared_sum}, disk total is {disk_total}")

    # Second: compare per-subtree file counts for every key the manifest does declare.
    for subtree, info in mf_langs_dict.items():
        if not isinstance(subtree, str):
            mismatches.append(f"languages: non-string key {subtree!r}")
            continue
        lane = subtree.split("/")[0]
        ext = LANE_EXT.get(lane)
        if ext is None:
            mismatches.append(f"languages[{subtree}]: unknown lane '{lane}'")
            continue
        sroot = root / subtree
        if not sroot.is_dir():
            mismatches.append(f"languages[{subtree}]: declares a path that is not a directory on disk")
            continue
        disk_count = 0
        for p in sroot.rglob("*"):
            if p.suffix == ext and "__pycache__" not in p.parts:
                disk_count += 1
        mf_count = info.get("files") if isinstance(info, dict) else info
        if mf_count != disk_count:
            mismatches.append(f"languages[{subtree}].files: manifest={mf_count!r}, disk={disk_count}")

    return mismatches


def run_checks(pub, gate=False, inject_all=frozenset(), inject_lang=None,
               quiet=False, probe=False) -> list:
    """The checks. Returns the failure list.

    inject_* add IDs to the quarantine sets on top of the real ledgers — that is how self_test
    proves (e)/(f) can still fire. probe=True skips signature/watermark/catalog work so those
    injections cost a file walk, not a full verify; the quarantine logic is the SAME code path.
    """
    say = (lambda *a, **k: None) if quiet else print
    fails, disk_ids, source_ids = [], set(), set()
    skipped = {}       # toolchain -> file count (missing compiler/runner under --gate)
    inconclusive = []  # files the gate could not measure at all — never a pass, always RED

    q_all, q_lang, counts, q_problems = load_quarantine(ROOT)
    q_all = set(q_all) | set(inject_all)
    q_lang = {k: set(v) for k, v in q_lang.items()}
    for k, v in (inject_lang or {}).items():
        q_lang.setdefault(k, set()).update(v)
    fails.extend(q_problems)

    # (a)(b)(d) per signed subtree
    for st in SIGNED_SUBTREES:
        sroot = ROOT / st
        if not sroot.exists():
            continue
        if not probe:
            rep = signing.verify_directory(sroot, pub)
            say(f"[{st:22}] signature: {rep.summary()}")
            if not rep.ok:
                fails.append(f"{st}: {rep.summary()}")
        qset = q_all | q_lang.get(st.split("/")[0], set())
        bad = 0
        for p in sroot.rglob("*"):
            if p.suffix not in SRC_EXT:
                continue
            disk_ids.add(p.stem)
            if st.startswith("python") or st in ("r", "javascript"):
                source_ids.add(p.stem)
            if not probe:
                mr = verify_file(p)
                if mr.status != "authentic" or (mr.payload and not mr.payload.is_master):
                    bad += 1; fails.append(f"{p.relative_to(ROOT)}: watermark {mr.status}")
            if p.stem in qset:
                fails.append(f"{p.relative_to(ROOT)}: quarantined ID present in shippable tree")
            if gate:
                kind, detail = gate_outcome(run_gate(p))
                if kind == "fail":
                    fails.append(f"{p.relative_to(ROOT)}: GATE fail")
                elif kind == "skip":
                    skipped[detail] = skipped.get(detail, 0) + 1
                elif kind == "inconclusive":
                    inconclusive.append(f"{p.relative_to(ROOT)}: {detail}")
        if not probe:
            say(f"                         watermark: {'all valid' if not bad else f'{bad} BAD'}")

    if skipped:
        for tc, n in sorted(skipped.items()):
            say(f"!! GATE SKIPPED — toolchain '{tc}' missing: {n} file(s) NOT validated")
            fails.append(f"GATE SKIPPED: toolchain '{tc}' missing — {n} file(s) not validated")

    if gate:
        ann = annotation_failures(ROOT)
        say(f"[annotations           ] {len(ann)} unreadable signature(s)"
            + ("" if not ann else " — a published signature nobody can read is a false claim"))
        for f, fn, err in ann:
            fails.append(f"{f.relative_to(ROOT)}: {fn}() signature unreadable — {err}")

    if inconclusive:
        say(f"!! GATE INCONCLUSIVE — {len(inconclusive)} file(s) could NOT be measured "
            f"(hung and were reaped). This is not a fail and it is CERTAINLY not a pass.")
        for item in inconclusive:
            fails.append(f"GATE INCONCLUSIVE: {item}")

    # (f) twin integrity — cpp/go twin whose source ID is missing or quarantined.
    # source_ids holds python/r stems only (disk_ids would include the twin itself).
    # cpp/go are SIGNED_SUBTREES, so the loop above already gated them — no re-gate here.
    # RULER v2: natives are exempt from the source-ID requirement, but only when DECLARED.
    try:
        _mf = json.loads((ROOT / "MANIFEST.json").read_text())
        native = {k: set(v) for k, v in (_mf.get("native_patterns") or {}).items()}
    except (OSError, ValueError) as e:
        native = {}
        fails.append(f"MANIFEST.json unreadable for native_patterns ({e}) — natives cannot be verified")
    declared = sum(len(v) for v in native.values())

    for tl in ("cpp", "go"):
        nat = native.get(tl, set())
        for p in (ROOT / tl).rglob("*"):
            if p.suffix not in (".cpp", ".go"):
                continue
            # q_all only: a twin quarantined in its own lane is caught above as (e). This line is
            # the SOURCE-quarantine rule — you may not ship a twin of a pattern we pulled.
            if p.stem in q_all:
                fails.append(f"{p.relative_to(ROOT)}: twin of a quarantined pattern")
            if p.stem in nat:
                # A native must NOT also have a source — that would mean it is really a twin
                # and the declaration is hiding a coupling the ruler exists to enforce.
                if p.stem in source_ids:
                    fails.append(f"{p.relative_to(ROOT)}: declared NATIVE but a python/r source "
                                 f"of the same ID exists — it is a twin, undeclare it")
                continue
            if p.stem not in source_ids:
                fails.append(f"{p.relative_to(ROOT)}: twin with no python/r source ID "
                             f"(declare it in MANIFEST.json native_patterns if it is a native harvest)")

    # A declaration naming a file that is not on disk is a stale claim — catch it, don't ignore it.
    for tl, stems in native.items():
        on_disk = {p.stem for p in (ROOT / tl).rglob("*") if p.suffix in (".cpp", ".go")}
        for missing in sorted(stems - on_disk):
            fails.append(f"MANIFEST native_patterns[{tl}]: '{missing}' declared native but not on disk")

    if probe:
        return fails

    # (c) catalog ID parity — parity is over UNIQUE ids; the headline count is
    # ROWS (934): a stem living in two spheres is two patterns (census law),
    # so rows > unique ids. Print both so the numbers can't be misread.
    catalog = (ROOT / "CATALOG.md").read_text(encoding="utf-8")
    rows = re.findall(r"^\| `([^`]+)` \|", catalog, re.M)
    listed = set(rows)
    if listed and listed != disk_ids:
        miss = listed - disk_ids
        extra = disk_ids - listed
        if miss: fails.append(f"catalog lists {len(miss)} ID(s) not on disk")
        if extra: fails.append(f"disk has {len(extra)} ID(s) not in catalog")
    say(f"[catalog               ] {len(rows)} pattern rows — unique IDs:"
        f" {len(disk_ids)} on disk, {len(listed)} listed"
        f" — {'OK' if listed == disk_ids else 'MISMATCH'}")

    say(f"[native lane           ] {declared} pattern(s) declared native"
        f"{' — ' + ', '.join(f'{k}:{len(v)}' for k, v in sorted(native.items()) if v) if declared else ' (twin-only library)'}")

    say(f"[quarantine            ] {sum(counts.values())} record(s) read from "
        f"{len(counts)} ledger(s) — {len(q_all)} source-wide, "
        f"{sum(len(v) for v in q_lang.values())} lang-scoped"
        f"{' — ' + ', '.join(f'{k}:{len(v)}' for k, v in sorted(q_lang.items()) if v) if q_lang else ''}")

    # (h) twin contract divergence — a declared number, RED when it moves. Not a defect verdict.
    dlanes, dexamples = count_contract_divergence(ROOT)
    try:
        dblock = json.loads((ROOT / "MANIFEST.json").read_text(encoding="utf-8")).get("twin_contract_divergence")
    except (OSError, ValueError):
        dblock = None          # the MANIFEST.json failure is already reported above
    fails.extend(divergence_fails(dblock, dlanes, dexamples))
    say(f"[twin contract         ] {sum(dlanes.values())} twin file(s) whose source carries an "
        f"input contract they do not ({', '.join(f'{k}:{v}' for k, v in sorted(dlanes.items()))})"
        f" — declared {(dblock or {}).get('declared')}")

    # (j) census recomputation — manifest census fields must agree with disk
    try:
        _mf_census = json.loads((ROOT / "MANIFEST.json").read_text(encoding="utf-8"))
    except (OSError, ValueError) as e:
        _mf_census = {}
        fails.append(f"MANIFEST.json unreadable for census ({e})")
    census_mm = census_mismatches(ROOT, _mf_census)
    say(f"[census                ] {len(census_mm)} mismatch(es) against disk"
        + (" — " + census_mm[0] if census_mm else " — OK"))
    fails.extend(census_mm)

    return fails


def self_test(pub, deep=False) -> list:
    """Prove the quarantine checks are NOT vacuous. Returns the failure list.

    (e) and (f) globbed a directory that holds no .py files, so the quarantine set was always
    empty and both checks passed for every pattern ever shipped. Nothing detected it because an
    empty set is indistinguishable from a clean library — from the outside. So this test walks
    in from the inside: it feeds a known-quarantined ID into the REAL tree checks and requires
    them to go RED, and feeds a nonsense ID and requires them to stay quiet. Both halves matter —
    a check wired to always fire is as useless as one wired never to.
    """
    out = []

    def check(name, ok, got=None):
        print(f"  {'ok  ' if ok else 'FAIL'} {name}")
        if not ok:
            out.append(f"SELF-TEST '{name}' failed (got: {got!r})")

    print("[self-test             ] quarantine parser + non-vacuity probes")

    with tempfile.TemporaryDirectory() as td:
        troot = Path(td)
        (troot / "_quarantine").mkdir()
        (troot / "_quarantine" / "QUARANTINE.md").write_text(
            "# Quarantine\n\n"
            "- `alpha_pattern.py` — assert-linter REJECT\n"
            "- `beta_pattern.py` — assert-linter REJECT\n"
            "prose that is not an entry\n", encoding="utf-8")
        (troot / "QUARANTINE.jsonl").write_text(
            '{"id": "gamma_twin", "lang": "cpp", "status": "fix-to-rejoin"}\n'
            '{"id": "delta_done", "lang": "cpp", "status": "rejoined"}\n'
            '{"id": "epsilon_unscoped", "status": "held"}\n', encoding="utf-8")
        (troot / "MANIFEST.json").write_text(
            json.dumps({"quarantine": ["alpha_pattern.py", "beta_pattern.py"]}), encoding="utf-8")

        qa, ql, counts, probs = load_quarantine(troot)
        check("md entries + unscoped jsonl -> source-wide",
              qa == {"alpha_pattern", "beta_pattern", "epsilon_unscoped"}, qa)
        check("lang-scoped record stays in its lane", ql == {"cpp": {"gamma_twin"}}, ql)
        check("status 'rejoined' is not quarantined",
              "delta_done" not in qa and "delta_done" not in ql.get("cpp", set()), (qa, ql))
        check("every declared ledger reported as read",
              counts == {"_quarantine/QUARANTINE.md": 2, "QUARANTINE.jsonl": 3}, counts)
        check("clean fixture raises no problems", not probs, probs)

        (troot / "MANIFEST.json").write_text(json.dumps({"quarantine": ["alpha_pattern.py"]}),
                                             encoding="utf-8")
        check("ledger split (manifest vs md) is caught",
              any("ledger split" in p for p in load_quarantine(troot)[3]), None)

    with tempfile.TemporaryDirectory() as td:
        troot = Path(td)
        (troot / "_quarantine").mkdir()
        (troot / "_quarantine" / "QUARANTINE.md").write_text("# Quarantine\n\nnone\n", encoding="utf-8")
        (troot / "QUARANTINE.jsonl").write_text("", encoding="utf-8")
        (troot / "MANIFEST.json").write_text(json.dumps({"quarantine": []}), encoding="utf-8")
        _, _, _, probs = load_quarantine(troot)
        check("a ledger that parses 0 records is RED (THE bug)",
              sum("parsed 0 records" in p for p in probs) == 2, probs)

    with tempfile.TemporaryDirectory() as td:
        troot = Path(td)
        (troot / "MANIFEST.json").write_text(json.dumps({"quarantine": []}), encoding="utf-8")
        check("a MISSING ledger is RED, not 'nothing quarantined'",
              sum("is MISSING" in p for p in load_quarantine(troot)[3]) == 2, None)

    # --- (h) twin contract divergence: same discipline, proven on a fixture tree -------------
    with tempfile.TemporaryDirectory() as td:
        troot = Path(td)
        for rel, body in (
            ("python/ds/guarded_one.py", "def f():\n    _aura_validate_f(1)\n"),
            ("python/ds/guarded_two.py", "def g():\n    _aura_validate_g(1)\n"),
            ("python/ds/plain.py",       "def h():\n    pass\n"),
            ("cpp/ds/guarded_one.cpp",   "int main(){return 0;}\n"),              # divergent
            ("cpp/other/guarded_one.cpp", "int main(){return 0;}\n"),             # divergent (2nd sphere)
            ("cpp/ds/guarded_two.cpp",   "// aura_validate mirrored\nint main(){}\n"),  # not divergent
            ("cpp/ds/plain.cpp",         "int main(){return 0;}\n"),              # source has no contract
            ("go/ds/guarded_one.go",     "package main\nfunc main(){}\n"),        # divergent, other lane
        ):
            f = troot / rel
            f.parent.mkdir(parents=True, exist_ok=True)
            f.write_text(body, encoding="utf-8")

        lanes, examples = count_contract_divergence(troot)
        check("divergence counts FILES, not IDs (two spheres = two)",
              lanes == {"cpp": 2, "go": 1, "rust": 0}, lanes)
        check("a twin that mirrored the contract is not counted",
              all("guarded_two" not in e for e in examples), examples)
        check("declared == disk -> silent",
              divergence_fails({"declared": 3, "lanes": {"cpp": 2, "go": 1, "rust": 0}},
                               lanes, examples) == [], None)
        check("a RISE is RED",
              any("ROSE" in f for f in divergence_fails(
                  {"declared": 2, "lanes": {"cpp": 1, "go": 1, "rust": 0}}, lanes, examples)), None)
        check("a FALL is RED too (a fix that leaves a stale claim)",
              any("FELL" in f for f in divergence_fails(
                  {"declared": 4, "lanes": {"cpp": 3, "go": 1, "rust": 0}}, lanes, examples)), None)
        check("a missing declaration is RED, not 'no divergence'",
              len(divergence_fails(None, lanes, examples)) == 1, None)
        check("an internally inconsistent declaration is caught",
              any("internally inconsistent" in f for f in divergence_fails(
                  {"declared": 99, "lanes": {"cpp": 2, "go": 1, "rust": 0}}, lanes, examples)), None)

    # --- census recomputation: non-vacuity probes -------------------------------------------
    with tempfile.TemporaryDirectory() as td:
        troot = Path(td)
        for rel in (
            "python/programming/foo.py", "python/programming/bar.py",
            "python/data-science/baz.py", "python/system-administration/qux.py",
            "cpp/foo.cpp", "rust/foo.rs", "go/foo.go", "r/foo.R", "javascript/foo.js",
        ):
            f = troot / rel
            f.parent.mkdir(parents=True, exist_ok=True)
            f.write_text("pass\n", encoding="utf-8")

        correct = {
            "total_shippable": 9, "total_signed_files": 9, "unique_ids": 4,
            "multi_language_patterns": 1,
            "languages_present": ["python", "cpp", "rust", "go", "r", "javascript"],
            "languages": {
                "python/programming": {"files": 2}, "python/data-science": {"files": 1},
                "python/system-administration": {"files": 1}, "r": {"files": 1},
                "cpp": {"files": 1}, "rust": {"files": 1}, "go": {"files": 1},
                "javascript": {"files": 1},
            },
        }
        check("census: a correct manifest produces NO mismatches (silent case)",
              census_mismatches(troot, correct) == [], census_mismatches(troot, correct))

        for field in ("total_shippable", "total_signed_files", "unique_ids", "multi_language_patterns"):
            bad = dict(correct)
            bad[field] = 999
            check(f"census: wrong {field} is RED",
                  any(field in m for m in census_mismatches(troot, bad)), None)

        bad = dict(correct)
        bad["languages_present"] = ["python", "cpp", "rust", "go", "r"]
        check("census: languages_present missing a real lane is RED",
              any("languages_present" in m for m in census_mismatches(troot, bad)), None)

        bad = dict(correct)
        bad["languages_present"] = correct["languages_present"] + ["cobol"]
        check("census: languages_present listing a phantom lane is RED",
              any("languages_present" in m for m in census_mismatches(troot, bad)), None)

        bad = json.loads(json.dumps(correct))
        bad["languages"]["cpp"]["files"] = 999
        check("census: per-lane files mismatch is RED",
              any("languages[cpp]" in m for m in census_mismatches(troot, bad)), None)

        bad = json.loads(json.dumps(correct))
        del bad["languages"]["javascript"]
        check("census: a per-lane entry DELETED from the manifest is RED",
              any("languages[javascript]" in m and "missing" in m
                  for m in census_mismatches(troot, bad)), None)

        # --- classes found by red-team rounds 3-5. Each one was a live defect; these probes
        # exist so a future edit cannot silently reintroduce it. ---------------------------

        bad = json.loads(json.dumps(correct))
        bad["languages"]["python/nonexistent"] = {"files": 0}
        check("census: a phantom directory entry with files=0 is RED",
              any("python/nonexistent" in m for m in census_mismatches(troot, bad)), None)

        bad = json.loads(json.dumps(correct))
        bad["languages"]["javascript/foo.js"] = {"files": 0}
        check("census: an entry naming a FILE (not a dir) with files=0 is RED",
              any("javascript/foo.js" in m for m in census_mismatches(troot, bad)), None)

        for label, val in (("string", "hello"), ("list", [1, 2]), ("int", 42), ("bool", True)):
            bad = json.loads(json.dumps(correct))
            bad["languages"] = val
            check(f"census: languages as a truthy non-dict ({label}) is RED, not a crash",
                  any("not a dict" in m for m in census_mismatches(troot, bad)), None)

        bad = json.loads(json.dumps(correct))
        bad["languages"][None] = {"files": 1}
        check("census: a non-string key is RED, not a crash",
              any("non-string key" in m for m in census_mismatches(troot, bad)), None)

        for label, val in (("NaN", float("nan")), ("inf", float("inf"))):
            bad = json.loads(json.dumps(correct))
            bad["languages"]["cpp"] = {"files": val}
            check(f"census: files={label} is RED, not a crash",
                  any("finite" in m for m in census_mismatches(troot, bad)), None)

        # Assert the SUM INVARIANT's own message, not merely that the result is RED: the
        # per-subtree != comparison catches these independently, so an outcome-only probe
        # keeps passing when the rejection it claims to protect is deleted.
        for label, val, frag in (("str", "1", "not a number"),
                                 ("bytes", b"1", "not a number"),
                                 ("bool", True, "not a number"),
                                 ("list", [1], "not a finite number"),
                                 ("dict", {"n": 1}, "not a finite number")):
            bad = json.loads(json.dumps(correct))
            bad["languages"]["cpp"] = {"files": val}
            check(f"census: files as {label} is rejected BY THE SUM INVARIANT ({frag})",
                  any(frag in m for m in census_mismatches(troot, bad)),
                  census_mismatches(troot, bad))

        check("census: a non-dict manifest is RED, not a crash",
              any("manifest is not a dict" in m for m in census_mismatches(troot, None)), None)

        for label, val in (("True", True), ("int", 42), ("float", 1.0)):
            bad = json.loads(json.dumps(correct))
            bad["languages_present"] = val
            check(f"census: languages_present as a truthy non-iterable ({label}) is RED, "
                  "not a crash",
                  any("languages_present" in m for m in census_mismatches(troot, bad)), None)

        bad = json.loads(json.dumps(correct))
        bad["languages_present"] = "python"
        check("census: languages_present as a bare string is RED",
              any("languages_present" in m for m in census_mismatches(troot, bad)), None)

        bad = json.loads(json.dumps(correct))
        bad["languages_present"] = tuple(correct["languages_present"])
        check("census: languages_present as a tuple with correct content is SILENT",
              census_mismatches(troot, bad) == [], census_mismatches(troot, bad))

        for label, val in (("int", ["javascript", 1]), ("None", [None, "javascript"]),
                           ("dict", [{"k": 1}, "javascript"]), ("bytes", [b"js", "javascript"]),
                           ("bool", [True, "javascript"]), ("all ints", [1, 2, 3])):
            bad = json.loads(json.dumps(correct))
            bad["languages_present"] = val
            check(f"census: languages_present with a non-string element ({label}) is RED, "
                  "not a sorted() crash",
                  any("non-string lane name" in m for m in census_mismatches(troot, bad)),
                  census_mismatches(troot, bad))

        bad = json.loads(json.dumps(correct))
        bad["languages"] = {k: v["files"] for k, v in correct["languages"].items()}
        check("census: bare-int entries with correct values are SILENT",
              census_mismatches(troot, bad) == [], census_mismatches(troot, bad))

        from decimal import Decimal
        from fractions import Fraction
        for label, val in (("Decimal", Decimal(1)), ("Fraction", Fraction(1, 1))):
            bad = json.loads(json.dumps(correct))
            bad["languages"]["cpp"] = {"files": val}
            check(f"census: files as {label} with a correct value is SILENT",
                  census_mismatches(troot, bad) == [], census_mismatches(troot, bad))

        # A SIGNED_SUBTREE may be split across several manifest keys ("go" ->
        # go/programming + go/system-administration). Deleting one leaves the sibling, which
        # satisfies the presence check -- only the sum invariant catches it. The main fixture
        # declares a single "go", so this class needs its own tree.
        with tempfile.TemporaryDirectory() as td2:
            sroot = Path(td2)
            for rel in ("go/programming/a.go", "go/system-administration/b.go"):
                f = sroot / rel
                f.parent.mkdir(parents=True, exist_ok=True)
                f.write_text("pass\n", encoding="utf-8")
            split_ok = {
                "total_shippable": 2, "total_signed_files": 2, "unique_ids": 2,
                "multi_language_patterns": 0, "languages_present": ["go"],
                "languages": {"go/programming": {"files": 1},
                              "go/system-administration": {"files": 1}},
            }
            check("census: a split-subtree fixture is SILENT when correct",
                  census_mismatches(sroot, split_ok) == [],
                  census_mismatches(sroot, split_ok))
            bad = json.loads(json.dumps(split_ok))
            del bad["languages"]["go/programming"]
            check("census: deleting ONE key of a split subtree is RED (sibling hides it "
                  "from the presence check; the sum invariant catches it)",
                  any("sums to 1," in m for m in census_mismatches(sroot, bad)),
                  census_mismatches(sroot, bad))

    # --- (1)(3) the gate: orphan reaping + the inconclusive outcome ---------------------------
    if deep:
        marker = f"APL_ORPHAN_PROBE_{os.getpid()}"

        def survivors():
            r = subprocess.run(["pgrep", "-f", marker], capture_output=True, text=True)
            return [x for x in r.stdout.split() if x.strip()]

        def kill_all():
            for pid in survivors():
                try:
                    os.kill(int(pid), signal.SIGKILL)
                except (ProcessLookupError, ValueError, PermissionError):
                    pass

        with tempfile.TemporaryDirectory() as td:
            fx = Path(td) / "hang_fixture.py"
            # Mimics `go run`: the runner spawns a GRANDCHILD, then both hang. The marker lives in
            # the grandchild's argv (not the file), so pgrep finds the survivor and nothing else.
            fx.write_text(
                "import subprocess, sys, time\n"
                f"subprocess.Popen([sys.executable, '-c', "
                f"'import time; time.sleep(300)  # {marker}'])\n"
                "time.sleep(300)\n", encoding="utf-8")

            # CONTROL — the old semantics. If this does NOT leak, the fixture proves nothing and
            # a passing reaper test below would be worthless.
            old = subprocess.Popen([sys.executable, str(fx)],
                                   stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            time.sleep(1.0)
            old.kill(); old.wait()
            time.sleep(0.4)
            leaked = survivors()
            check("control: killing only the child LEAKS the grandchild (fixture really orphans)",
                  len(leaked) >= 1, leaked)
            kill_all(); time.sleep(0.2)

            # THE FIX — same fixture, through the real gate.
            verdict = run_gate(fx, timeout=2)
            time.sleep(0.4)
            left = survivors()
            check("a hung gate reports 'inconclusive', never 'ok' or 'fail'",
                  verdict.startswith("inconclusive:"), verdict)
            check("REAPED — no grandchild survives the timeout", left == [], left)
            kill_all()

        with tempfile.TemporaryDirectory() as td:
            ok_f, bad_f = Path(td) / "ok.py", Path(td) / "bad.py"
            ok_f.write_text("assert 1 == 1\n", encoding="utf-8")
            bad_f.write_text("raise SystemExit(3)\n", encoding="utf-8")
            check("gate GREEN case: a clean file is 'ok'", run_gate(ok_f, timeout=30) == "ok")
            check("gate RED case: a failing file is 'fail'", run_gate(bad_f, timeout=30) == "fail")

        # (i) unreadable signatures — RED case and GREEN case, on fixtures
        with tempfile.TemporaryDirectory() as td:
            broken = Path(td) / "broken_ann.py"
            fine = Path(td) / "fine_ann.py"
            # imported under an ALIAS but annotated with the bare name: the exact shape found in
            # pca_power_iteration. Under PEP 649 the def succeeds and the file exits 0.
            broken.write_text("from typing import List, Tuple as TupleType\n"
                              "def entry(x: List[int]) -> Tuple[int, int]:\n    return (1, 2)\n",
                              encoding="utf-8")
            fine.write_text("from typing import List, Tuple\n"
                            "def entry(x: List[int]) -> Tuple[int, int]:\n    return (1, 2)\n",
                            encoding="utf-8")
            bad = annotation_failures(Path(td), files=[broken])
            good = annotation_failures(Path(td), files=[fine])
            check("(i) RED case: an unreadable signature is caught",
                  len(bad) == 1 and "Tuple" in bad[0][2], bad)
            check("(i) GREEN case: a resolvable signature is silent", good == [], good)
            check("(i) the broken fixture still EXITS 0 — proving --gate is blind to it",
                  run_gate(broken, timeout=30) == "ok")

        # the WIRING: only a literal 'ok' may ever be bucketed as a pass
        check("only 'ok' is a pass", gate_outcome("ok")[0] == "pass")
        check("'inconclusive' is NOT a pass",
              gate_outcome("inconclusive:node exceeded 2s")[0] == "inconclusive")
        check("'skip' is NOT a pass", gate_outcome("skip:go")[0] == "skip")
        check("an UNRECOGNISED verdict fails closed to inconclusive, never pass",
              gate_outcome("okay")[0] == "inconclusive" and gate_outcome("")[0] == "inconclusive")
    else:
        print("  --   gate/orphan proof not exercised (runs under --gate or --self-test)")

    # --- non-vacuity against the real tree -------------------------------------------------
    live_all, live_lang, _, _ = load_quarantine(ROOT)
    held = live_all | {i for v in live_lang.values() for i in v}
    py = {p.stem for p in (ROOT / "python").rglob("*.py")}
    twins = sorted({p.stem for p in (ROOT / "cpp").rglob("*.cpp")} & py - held)
    if len(twins) < 2:
        out.append("SELF-TEST: fewer than 2 clean cpp twins on disk — probes cannot run")
        return out
    probe_a, probe_b = twins[0], twins[1]

    def hit(fails, stem, msg, tree=None):
        return any(msg in f and f"/{stem}." in f and (tree is None or f.startswith(tree + "/"))
                   for f in fails)

    fa = run_checks(pub, inject_all={probe_a}, quiet=True, probe=True)
    check(f"(e) fires on a source-quarantined ID ({probe_a})",
          hit(fa, probe_a, "quarantined ID present in shippable tree", "python"), None)
    check(f"(f) fires on the twin of a quarantined source ({probe_a})",
          hit(fa, probe_a, "twin of a quarantined pattern", "cpp"), None)

    fb = run_checks(pub, inject_lang={"cpp": {probe_b}}, quiet=True, probe=True)
    check(f"(e) fires on a lang-scoped quarantined twin ({probe_b})",
          hit(fb, probe_b, "quarantined ID present in shippable tree", "cpp"), None)
    check("a lang-scoped twin quarantine does NOT condemn its python source",
          not hit(fb, probe_b, "quarantined ID present in shippable tree", "python")
          and not hit(fb, probe_b, "twin of a quarantined pattern"), None)

    fc = run_checks(pub, inject_all={"__no_such_pattern_id__"}, quiet=True, probe=True)
    check("no probe -> the checks stay quiet (not wired to always fire)",
          not any("__no_such_pattern_id__" in f for f in fc), None)

    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--pubkey", default=str(ROOT / "aura-signing.pub"))
    ap.add_argument("--gate", action="store_true", help="also compile/run every file (slow)")
    ap.add_argument("--self-test", action="store_true",
                    help="run ONLY the non-vacuity self-test (it runs on every verify anyway)")
    args = ap.parse_args()
    pub = Path(args.pubkey).read_text().strip() if Path(args.pubkey).exists() else args.pubkey

    # (g) The self-test runs FIRST and on EVERY run. GREEN is not reachable without the proof
    # that (e)/(f) can still go RED — that is the whole lesson of the empty-glob bug.
    fails = self_test(pub, deep=args.self_test or args.gate)
    if args.self_test:
        print("-" * 60)
        if fails:
            print(f"RED — self-test: {len(fails)} problem(s):")
            for f in fails:
                print(f"  - {f}")
            return 1
        print("GREEN — the quarantine checks are live and can fail.")
        return 0

    fails += run_checks(pub, gate=args.gate)

    print("-" * 60)
    if fails:
        print(f"RED — {len(fails)} problem(s):")
        for f in fails[:25]:
            print(f"  - {f}")
        return 1
    print("GREEN — the Grand Library is what it claims.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
