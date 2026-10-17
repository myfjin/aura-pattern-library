# `library_verify.py` — the library's CI

The gate. If this prints GREEN, the library **is what it claims to be**: signed, watermarked, catalogued, counted, internally consistent. If this prints RED, something lies about the tree and must be fixed before any commit lands.

**It does not grade any pattern.** For that, see [`library_audit.md`](library_audit.md) and [`polyglot.md`](polyglot.md).

---

## What question does it answer?

> *"Is this tree a trustworthy copy of the signed library — or has something drifted, broken, or been smuggled in?"*

It is the **entry criterion** for every change. The library's whole claim is one sentence (*"this is what it says it is"*); `library_verify.py` is the mechanism that makes that sentence checkable.

---

## Dependencies

- **Python ≥ 3.10**
- **[folder-nature](https://github.com/myfjin/folder-nature)** — signing + mark primitives. Install in a venv:
  ```bash
  python3 -m venv .venv && .venv/bin/pip install folder-nature
  .venv/bin/python library_verify.py
  ```
- Under `--gate`: `python3`, `Rscript`, `node`, `g++`, `go`, `rustc`. Any missing toolchain turns the run **RED** (loud per-language SKIP), never silently green.

---

## CLI

```
library_verify.py [--pubkey PATH] [--gate] [--self-test]
```

| Flag | Default | Effect |
|---|---|---|
| `--pubkey` | `aura-signing.pub` | public key to verify Ed25519 signatures against |
| `--gate` | off | also compile+run every file; slow, requires full toolchain |
| `--self-test` | off | run only the vacuous-check proofs (prove the gate can still go RED) |

Exit code 0 = GREEN, 1 = RED.

---

## The eight check classes

| | Check | What it proves |
|---|---|---|
| (a) | signature + manifest integrity per subtree | the tree matches its signed hash |
| (b) | every file carries a valid master-0 watermark | nothing unmarked slipped in |
| (c) | `CATALOG.md` ID set == on-disk ID set | the catalog is honest about what ships |
| (d) | `--gate` only: compile/run every file exit 0 | every pattern's self-test holds |
| (e) | quarantine IDs absent from all shippable trees | nothing REJECTed by the assert-linter ships |
| (f) | twin integrity: no cpp/go twin whose source is quarantined or missing (unless declared NATIVE in MANIFEST) | orphan twins fail; native twins are a deliberate declaration |
| (g) | **self-test**: quarantine checks proven non-vacuous on every run | a check that cannot fail is worse than no check |
| (h) | twin contract divergence equals the number MANIFEST declares | the known gap is tracked, not hidden |

---

## The three ruler versions

- **RULER v2** (2026-07-27) — **the NATIVE LANE.** A cpp/go file does not have to be a conversion twin of a python/r pattern; a sphere can be harvested natively in a compiled language (Go concurrency sphere has no meaningful python source). A native pattern must be **declared** in `MANIFEST.json["native_patterns"]`. Declared → exempt from source-ID requirement. Undeclared and sourceless → RED. **Silence still fails.**
- **RULER v3** (2026-07-28) — **the QUARANTINE LEDGERS.** The old check used `(_quarantine).glob("*.py")`, which held no files (sources are deleted, not stored); the check passed trivially for months. Fixed to read the real ledgers (`_quarantine/QUARANTINE.md`, `QUARANTINE.jsonl`, `MANIFEST.json["quarantine"]`) and to prove on every run that the checks can still go RED.
- **RULER v3.1** (2026-07-28) — **TWIN CONTRACT DIVERGENCE.** 125 cpp twins ship without the `_aura_validate_*` input contract their python sources now carry. This is NOT scored as a defect (no cpp attack lane exists yet). It is **declared** in `MANIFEST.json["twin_contract_divergence"]` and goes RED only when the number MOVES — in either direction. A rise means twins shipped behind; a fall means twins caught up.

---

## What a GREEN run looks like

```
[python/programming    ] signature: authentic + unaltered
                         watermark: all valid
[python/data-science   ] signature: authentic + unaltered
                         watermark: all valid
…
[catalog               ] 1085 pattern rows — unique IDs: 1074 on disk, 1074 listed — OK
[native lane           ] 60 pattern(s) declared native — cpp:50, go:10
[quarantine            ] 5 record(s) read from 2 ledger(s) — 4 source-wide, 0 lang-scoped
[twin contract         ] 128 twin file(s) whose source carries an input contract they do not (cpp:128, go:0, rust:0) — declared 128
[census                ] 0 mismatch(es) against disk — OK
------------------------------------------------------------
GREEN — the Grand Library is what it claims.
```

The numbers move every time patterns land. The RULES do not.

---

## When to run it

- **Before every commit** that touches any file inside a signed subtree (`python/`, `cpp/`, `rust/`, `go/`, `javascript/`, `r/`). Any edit changes the sha; the sha is signed; an edit without a re-sign leaves the tree RED.
- **After every ingest** (via `ingest.py`, `ingest_cpp_native.py`, `ingest_go.py`).
- **Before every release.** With `--gate` for the full compile/run matrix.
- **Weekly, scheduled**, on `master` HEAD. A failure here that was not caught by the pre-commit path is a process bug worth noticing.

---

## When RED means something

| Symptom | Likely cause |
|---|---|
| `signature: FAILED` on one subtree | you edited a file in that subtree without re-signing |
| `watermark: invalid` | watermark was moved, re-stamped, or deleted (never do this) |
| `catalog mismatch` | you added/removed a pattern on disk without regenerating `CATALOG.md` |
| `(e) quarantine ID in shippable tree` | a REJECTed source made it back into a lane |
| `(f) orphan twin` | a cpp/go file has no python/r source and is not declared NATIVE |
| `twin contract divergence moved` | twins shipped behind sources (number up) OR caught up (number down) — update `MANIFEST.json["twin_contract_divergence"]` to match |
| `census mismatch` | `languages_present` in MANIFEST disagrees with the actual file count — one of them is wrong |

**RED = stop and report. Never force. Never --skip-verify.**

---

## Related

- [`library_audit.md`](library_audit.md) — the second layer: grades individual patterns.
- [`polyglot.md`](polyglot.md) — language-agnostic health across all six lanes.
- [`.claude/skills/library-operations/SKILL.md`](https://github.com) — the operator-side skill.
