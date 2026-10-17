# Tool docs — map

The library ships two layers of tooling. Together they answer two different questions.

| Layer | Lives at | Answers |
|---|---|---|
| **1 — Library gate** | repo root | *Is this library what it claims to be?* — signed, watermarked, catalogued, counted, consistent. |
| **2 — Pattern validation** | `tools/pattern-scoring/validator/` | *Is any individual pattern worth something?* — compiles, runs clean, survives attack recipes, holds its invariants. |

A green Layer 1 does not grade a pattern. A green Layer 2 does not prove the tree is signed. Each needs the other; neither replaces it.

---

## This directory

**Priority-1 docs (this page's siblings):**

- [`library_verify.md`](library_verify.md) — the Layer-1 gate (library CI). 8 check classes.
- [`library_audit.md`](library_audit.md) — Layer-1 second pass. 12 check classes; 5 verdicts.
- [`polyglot.md`](polyglot.md) — Layer-2 multi-language health runner.
- [`harvest_gate.md`](harvest_gate.md) — Phase A proposer for new patterns. 5 strict invariants.

Follow-up pages will cover `audit_report.py`, `build_patterns_index.py`, the ingest flow, and the rest of the Layer-2 validator family (`sweep`, `full_sweep`, `executor`, `chaos_scan`, `metamorphic_scan`, `nan_domain_probe`, `invariant_mine`, `recipes` R1–R15).

---

## Install

All Layer-1 tools except `build_patterns_index.py` depend on **[folder-nature](https://github.com/myfjin/folder-nature)** for signing + mark primitives. Install it in a venv:

```bash
cd ~/aura-pattern-library
python3 -m venv .venv
.venv/bin/pip install folder-nature
.venv/bin/python library_verify.py   # should print GREEN
```

Layer-2 validators (`polyglot.py` etc.) need the toolchains of whatever languages they are asked to check. On a Debian/Ubuntu host:

```bash
sudo apt install -y gcc g++ clang rustc golang r-base nodejs
```

Any missing toolchain is reported as a loud per-language SKIP that turns the run RED — the tool never silently passes a language it could not run.

---

## Which tool, when

**Daily / before every PR that touches a pattern:**
- `library_verify.py` — proves the tree still signs cleanly after your edit. See [`library_verify.md`](library_verify.md).

**Before shipping a release:**
- `library_verify.py --gate` — adds compile/run of every pattern across all six languages.
- `library_audit.py` — second-layer check across the 12 classes. See [`library_audit.md`](library_audit.md).
- `polyglot.py` — language-agnostic health confirmation. See [`polyglot.md`](polyglot.md).

**When proposing a new pattern for ingest:**
- `harvest_gate.py` — Phase A triage: metamorphic + NaN + chaos + invariant_mine. See [`harvest_gate.md`](harvest_gate.md). It **never writes to the signed tree**; it writes decisions to `.harvest/`.

**When investigating a specific pattern's health:**
- Call `polyglot.selftest(relpath)` directly — one pattern, one card: `BASELINE-OK` / `COMPILE-FAIL` / `RUNTIME-FAIL` / `TIMEOUT`.

---

## The verdict discipline (both layers)

The tooling never conflates *"could not measure"* with *"ok"*. Every tool returns one of these states:

| State | Meaning |
|---|---|
| `pass` / `BASELINE-OK` / GREEN | measured, and it is fine |
| `fail` / RED | measured and wrong (deterministic defect) |
| `flag` | measured something suspicious; evidence attached, judgement needed |
| `unverifiable` | could not measure (no implementation, toolchain missing, hang) |
| `skip` | genuinely not applicable (`detail` field says which) |

**A missing toolchain never scores as pass.** A hung run never scores as pass. These are the vacuous-fixture traps that `library_verify.py` and `library_audit.py` were graduated against (see each tool's doc).

---

## Related

- [`.claude/skills/library-operations/SKILL.md`](https://github.com) — operator-side skill: the three lanes, the one law (edit→re-sign→verify), the per-language description slot, the two toolchains that touch the library (never confuse them).
- [`CONTRIBUTING.md`](../../CONTRIBUTING.md) — DCO, the pattern-library-specific Testing section.
- [`SECURITY.md`](../../SECURITY.md) — scope + the signing-key boundary.
