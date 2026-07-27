# retry with budget

**Language:** Rust · **Sphere:** rust · **Category:** concurrency-resilience

**Signature:** `() → u64`

## What it does

retry_with_budget — retry budget guard; amplification capped, measured over seeds.

Core idea: retry logic with a fixed budget (max retries, max amplification). Each retry
costs budget. THE ONE LAW: run a series of flaky operations with retry budget, measure
the amplification (total attempts / initial requests), then assert amplification is
capped and doesn't exceed budget — an unguarded retry would amplify without bound.
When to use: rate limiting, preventing amplification attacks, backoff-bounded retry.

## Guarantee

When it runs, retry with budget guarantees assert!(amplification <= tight_cap + 1e-9, "amplification {:.4}x exceeded the global-budget cap {:.4}x", amplification, tight_cap); assert!(total_attempts <= initial_requests + max_retries, "total attempts {total_attempts} exceeded initial+budget {}", initial_requests + max_retries); assert!(budget.retries_used > 0, "no retries used (too lucky)") (weak-grade: proven by rustc-run).

**Checkable constraints:**

- `assert!(amplification <= tight_cap + 1e-9, "amplification {:.4}x exceeded the global-budget cap {:.4}x", amplification, tight_cap)`
- `assert!(total_attempts <= initial_requests + max_retries, "total attempts {total_attempts} exceeded initial+budget {}", initial_requests + max_retries)`
- `assert!(budget.retries_used > 0, "no retries used (too lucky)")`
- `assert_eq!(budget.retries_used, budget.max_retries, "budget should be exhausted")`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
