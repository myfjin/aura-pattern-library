# Library Fix Request — full-sweep findings, 2026-07-18

**For a NEW session. Launch:**
`cd ~/ai-lab && claude --model claude-fable-5 "Read pattern-scoring/fix_request_2026-07-18/FIX_REQUEST.md and execute it."`

**Origin:** during manual-audit prep (session with Illia, 07-18) a full deterministic sweep of
`~/aura-pattern-library` (1,399 patterns) found the defects below. This doc is the complete,
self-contained work order. Machine-readable lists: `defect_lists.json` (same dir).
When done, Illia returns to the audit session and the manual approval cycle starts on clean material.

## Ruler used (frozen for this sweep — keep it)
Claim = the first real comment/docstring block above code (python: `ast.get_docstring`;
cpp/rust/go/r: first comment block, skipping watermark lines / `use`/`import`/`package`/`#include`).
Nothing there → MISSING. The audit sheet `pattern-scoring/manual_audit_prep/DESCRIPTIONS_SHEET.csv`
was already rebuilt under this ruler on 07-18 (old broken sheet kept at `DESCRIPTIONS_SHEET.csv.bak-0718`).

## What was verified CLEAN (no work needed — do not "improve")
- Watermarks: 1,399/1,399 carry the AURA mark.
- Duplicates: 0 (normalized-source sha256 across all languages).
- Python syntax: 676/676 parse.
- assert_linter (all 676 python): **REJECT 0** — no hollow-assert gutting. (WARN 359 = advisory, see §4.)
- TODO/FIXME/HACK markers: 0 real (5 grep hits are all test data / hex-comment false positives).
- Oracle forms + 66 evidence cards: no watermark garbage.
- Determinism (all 676 python, 3 runs, varying PYTHONHASHSEED): OK 675 · REJECT 0 — one NOTE, see §5.

## THE WORK

### 1. Write descriptions for 191 patterns that have NONE (blocking the manual audit)
`defect_lists.json → "missing"` — 69 cpp · 49 rust · 39 go · 34 python.
These files have no top-level description at all; under Illia's rule ("no description I can
understand = pattern GONE") they can't even enter his gate.
Per file:
- Read the code. Write a description block **above the code, below the watermark lines**:
  what it does · when to use it · what it guarantees (the oracle/disaster it survives) —
  3–6 plain-language lines. Format: python = module docstring; cpp = `/* … */`; rust/go = `//` block
  (go: place above the description-worthy decl or as file-top comment after package if needed —
  prefer file-top); r = `#` block.
- The description must be TRUE to the code — this library's law: the name is a claim, the
  docstring is a claim. No adjacent-but-wrong summaries. When unsure, describe less, not more.
- **Illia's ruling (07-18): these 191 descriptions are DRAFTS for his manual gate, not final.**
  He will personally review each during the audit — plausible-but-adjacent summaries (the
  docstring-lie) is exactly what he'll hunt there, and he decides which of the 191 earn a
  definition and a chance to exist vs GONE. Write accordingly: honest drafts, no salesmanship,
  and if a pattern's purpose is genuinely unclear from its code, SAY SO in a line the reviewer
  will see (e.g. "UNCLEAR: …") instead of inventing a confident claim.
- Python note: 34 files have helper-class docstrings but no MODULE docstring — add the module one.

### 2. Expand 29 title-only descriptions (`"short"` in json)
Claims under 40 chars, e.g. "Missing Value Imputation Pattern." — a title, not a description.
Same treatment as §1: extend in-file to what/when/guarantees. 19 cpp · 5 go · 3 python · 2 rust.

### 3. Fix 14 decl-style descriptions (`"declstyle"` in json)
First comment describes a type ("TaskStatus represents possible task statuses.") not the pattern.
Add a real file-top description; keep the decl comment where it is.

### 4. DO NOT touch the 359 assert-WARN files (explicitly out of scope)
`assert_linter_full.txt` has the full tagged list (mostly `directional`-tier asserts).
REJECT count is 0 — nothing is gutted. Strengthening 359 oracles en masse is exactly the kind of
mass edit that broke things before (a rail scoped too wide breaks what it protects). If anyone
wants this lane, it's a separate later project with per-file oracle re-runs, gated on Illia.

### 5. Determinism: ONE file to fix (result: OK 675 · NOTE 1 · REJECT 0)
`python/data-science/rankings_and_information_retrieval/inverted_index_search.py` —
all asserts pass but **stdout varies across runs with different PYTHONHASHSEED** (full log:
`determinism_results.txt`). Almost certainly set/dict iteration order leaking into printed output.
Fix: sort before printing (or seed the structure), keep asserts untouched, then re-verify:
`python3 ~/ai-lab/tools/determinism_check.py <file>` → must be OK.

## AFTER EDITING — the signature law (non-negotiable)
Every edited file changes sha → its signature goes stale. Finish with:
1. Re-sign each touched language subtree:
   `~/aura-pattern-library/.venv/bin/python` +
   `from folder_nature.mark import signing; seed = signing.read_private_key(Path.home()/".config/folder-nature/aura-signing.key"); signing.sign_directory(<lib>/<lang>, "AURA Pattern Library", seed)`
   (same primitive `ingest.py` uses; watermark stamps survive comment edits — do NOT re-stamp).
2. `cd ~/aura-pattern-library && .venv/bin/python library_verify.py` → must end GREEN
   ("the Grand Library is what it claims"). RED = stop, report, don't force.
3. Rebuild the audit sheet under the same ruler so Illia's Part A feed is fresh:
   the rebuild script logic is documented above; verify `claim_missing` count drops 191 → 0
   and short(<40) drops 29 → 0.
4. Re-run the testbed sanity: `python3 ~/ai-lab/pattern-scoring/testbed/driver.py` → expect 13/13.
5. Write a completion report `fix_request_2026-07-18/COMPLETION_REPORT.md`: files touched,
   before/after counts, library_verify + testbed output tails. Illia's audit session reads it first.

## Verification law for the fixing session
Show real output for every claim (pre-flight: read board → show proof → then claim).
Descriptions are claims about code — the writer must have READ the code it describes.
Batch by sphere (cpp → rust → go → python), library_verify after each sphere, not once at the end.
