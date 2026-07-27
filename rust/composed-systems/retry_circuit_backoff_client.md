# retry circuit backoff client

**Language:** Rust · **Sphere:** rust · **Category:** composed-systems

**Signature:** `(code: usize) → Status`

## What it does

composes: status-classify + exponential-backoff-schedule + circuit-breaker-open-after-K + exact-attempt-timeline

## Guarantee

When it runs, retry circuit backoff client guarantees assert_eq!(attempts.len(), 3, "Circuit stops after 3 failures (K=3)"); assert_eq!(attempts[0].1, 500, "First attempt got 500"); assert_eq!(attempts[1].1, 503, "Second attempt got 503") (proven by rustc-run).

**Checkable constraints:**

- `assert_eq!(attempts.len(), 3, "Circuit stops after 3 failures (K=3)")`
- `assert_eq!(attempts[0].1, 500, "First attempt got 500")`
- `assert_eq!(attempts[1].1, 503, "Second attempt got 503")`
- `assert_eq!(attempts[2].1, 500, "Third attempt got 500 (circuit opens)")`
- `assert!(circuit_open, "Circuit breaker is open after K failures")`
- `assert!(backoff_ms > 100, "Backoff increased from exponential retries")`
- `assert!(no_circuit.len() <= 4, "Circuit breaker limits attempts")`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
