# `harvest_gate.py` — Phase A proposer for new patterns

Routes candidate patterns through a battery of Phase A tools and emits per-pattern verdicts into `.harvest/`. **Never writes to the signed library tree.** This is the step that happens *before* `ingest.py` touches canonical.

Where [`library_verify.py`](library_verify.md) protects the tree from drift, `harvest_gate.py` protects the tree from **bad new work landing in the first place**.

---

## What question does it answer?

> *"Does this candidate pattern deserve to enter the signed tree — and if not, exactly why?"*

The verdict ladder: `PASS` · `FLAG` · `INVALID` (Cat A: fix-known / Cat B: fix-unknown) · `SKIP` · `CONTRADICTION` · `PROPOSAL`.

A `CONTRADICTION` with Illia's frozen exam is **logged to `.harvest/contradictions/`, never auto-flied**. Humans resolve frozen-exam flips.

A `PROPOSAL` (from `invariant_mine`) is **recorded separately and never enters the grade ladder** — mining proposes, never grades. Illia's law #1.

---

## The five invariants (unchanged since v1)

1. **NEVER mutates the signed library tree.**
2. **NEVER auto-flies a frozen exam verdict** — contradictions log to `.harvest/contradictions/`.
3. **Harvest tools are IMPORTED from `~/ai-lab/pattern-scoring/validator/` (staging).** The staging tech-debt is logged; patch per claim boundary, don't vendor silently.
4. **FAIL HARD on tool-hash mismatch vs `.harvest/tool_hashes.json`.** Silent staleness is a bigger failure than a loud refusal.
5. **Twin_divergence held for Draft 2.** The twin-divergence probe lives in the suite but doesn't participate in Phase A verdicts yet.

Any run where an invariant would be violated **aborts** rather than proceeds degraded.

---

## Dependencies

- **Python ≥ 3.10**
- **Harvest tools present at the expected staging path**: `~/ai-lab/pattern-scoring/validator/`
  - `metamorphic_scan.py`
  - `chaos_scan.py`
  - `nan_domain_probe.py`
  - `invariant_mine.py`
- **Tool-hash manifest** at `.harvest/tool_hashes.json` must match the current tool files. If any tool drifts, the run aborts with `FATAL: tool hash mismatch`.

---

## CLI

```
harvest_gate.py [--run] [--self-test]
```

| Flag | Default | Effect |
|---|---|---|
| (none) | **dry-run** | print T1 count, per-tool coverage, would-run pairs. No writes. |
| `--run` | | actually invoke tools; write per-pattern results into `.harvest/`. |
| `--self-test` | | run the stale-report mutation flip proof suite and exit (13 tests). |

---

## What a dry-run looks like

```
T1 population: 122 patterns (from t1_detect_v2.py md5 352841f76c6b)
  invariant_mine: 3 target(s) via T1 ∩ ADAPTERS (linear_regression_gd, ridge_regression_normal_eq, polynomial_regression)
  nan_domain_probe: 122 target(s)
  metamorphic_scan: 85 target(s)
  chaos_scan: 18 target(s) via CHAOS_FUNCTION_TO_PID

[dry-run] would invoke 228 (tool, pattern) pair(s). No writes.
```

If any tool hash drifts, the dry-run itself refuses:

```
FATAL: tool hash mismatch vs .harvest/tool_hashes.json — silent staleness prevented.
  metamorphic_scan: recorded=a10fece84f95 current=3233bf6ebeb1
Resolution: either revert the tool or explicitly regenerate .harvest/tool_hashes.json.
```

**Resolution is manual on purpose.** A silent re-hash means a different tool silently became the authority; that is exactly what invariant 4 exists to prevent.

---

## The wired Phase A tools

| Tool | Purpose | Routing |
|---|---|---|
| **metamorphic_scan** | metamorphic-equivalence probes (same answer under equivalent transforms) | per-pattern verdict → PASS / FLAG / INVALID |
| **chaos_scan** | 9-row routing table per 6E (negative-control abort keys on a specific string; harness-FLAG → SKIP; contradiction → `.harvest/contradictions/`; etc.) | per-pattern verdict with special NEG-CONTROL rules |
| **nan_domain_probe** | NaN / domain-break detector; probes the pattern's response to boundary and out-of-domain inputs | per-pattern verdict |
| **invariant_mine** | discovers candidate invariants in the pattern | **PROPOSAL only** — never grades, recorded separately, coerced to PROPOSAL if a tool misdeclared |

Each tool has its own timeout cap. The whole-run cap for `invariant_mine` is 300s (3 adapters × 100 seeds in-process).

---

## `--self-test` — 13 tests, each with sub-cases

Not a smoke test — a **wiring-correctness proof suite**. Test 11 alone proves chaos routing with 6 subcases: negative-control abort, key-string distinguisher, contradiction, harness-FLAG override, timeout, and exit-2-with-fresh-report parse. Test 13 proves `invariant_mine` PROPOSAL wiring with the contamination-guard flip (any card with `verdict != "PROPOSAL"` is coerced to PROPOSAL — Illia's law #1).

Add a new tool to Phase A → add a `--self-test` test with both the positive arm (correctly produces the expected verdict on a planted input) and the negative arm (correctly refuses to produce it on a planted non-input). No wiring lands without both arms.

---

## Output surface

Everything written goes under `.harvest/`:

- `.harvest/manifest/<tool>/t1_manifest.json` — the frozen T1 target list (bare list, not wrapped)
- `.harvest/<tool>/<pattern>.json` — per-run verdict + evidence
- `.harvest/contradictions/<pattern>.json` — any case where a tool verdict contradicts the frozen exam
- `.harvest/proposals/<pattern>.json` — `invariant_mine` cards, in their own counter so they never pollute the grade ladder

Reading these is how a human decides what to ingest. `harvest_gate.py` never auto-ingests; it only decides what is *eligible*.

---

## When to run it

- **Before any pattern-ingest session** — the Phase A verdicts tell `ingest.py` what has passed the gate.
- **After any Phase A tool is updated** — `--self-test` to prove wiring; refuse to run until all tests pass.
- **Scheduled, weekly** — on the current pending tree, so stalled candidates get a fresh look.

---

## Known limits

- **Phase A, not Phase B.** The deeper attack recipes (R1–R15 in `recipes.py`) and the frozen-exam grader live elsewhere; harvest_gate hands off to them, does not include them.
- **Python-centric for deep probes.** `chaos_scan` and `metamorphic_scan` reach cpp/go/rust only through compiled-harness lanes which were still in progress at the time this doc landed.
- **Staging coupling.** The tools live outside the public tree (invariant 3). This is a known tech-debt entry; patch per claim boundary, don't silently vendor.

---

## Related

- [`library_verify.md`](library_verify.md) — the gate that `harvest_gate.py` sits *before*.
- [`library_audit.md`](library_audit.md) — the second-layer check that `harvest_gate.py` sits *before* on the ingest side.
- [`polyglot.md`](polyglot.md) — the health runner that confirms a candidate at least compiles and runs clean.
- [`.claude/skills/library-operations/SKILL.md`](https://github.com) — the operator-side skill (THE THREE LANES: canonical / pending / harvest workspace).
