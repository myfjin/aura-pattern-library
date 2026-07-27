# csrf double submit

**Language:** Rust · **Sphere:** rust · **Category:** security-crypto

**Signature:** `(cookie: &str, form: &str) → bool`

## What it does

CSRF double-submit check — cookie token must equal form token AND both be present.
Core idea: a state-changing request is accepted only if the token in the cookie matches
the token submitted in the form/header. THE ONE LAW: the check must reject not just a
MISMATCH but also the EMPTY/MISSING case — a naive `cookie == form` accepts "" == "" and
hands the attacker a bypass (no cookie, no form → both empty → "match"). We reject it.
When to use: form submissions, state-changing POSTs, stateless CSRF defense.

## Guarantee

When it runs, csrf double submit guarantees assert!(csrf_ok(token, token), "matching present tokens accepted") (none-grade: proven by rustc-run).

**Checkable constraints:**

- `assert!(csrf_ok(token, token), "matching present tokens accepted")`
- `assert!(!csrf_ok(token, "attacker-token"), "mismatched tokens rejected")`
- `assert!(!csrf_ok(token, ""), "missing form token rejected")`
- `assert!(!csrf_ok("", token), "missing cookie rejected")`
- `assert!(!csrf_ok("", ""), "both-empty (no auth) must be rejected, not treated as a match")`
- `assert!(!csrf_ok(token, "abc123def45"), "truncated token rejected")`
- `assert!(!csrf_ok(token, " abc123def456"), "altered token rejected")`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** none (no checkable constraint)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
