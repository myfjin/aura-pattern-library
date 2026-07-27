# http router

**Language:** Python · **Sphere:** programming · **Category:** Networking

**Signature:** `(message: str) → Callable[[Request], Response]`

## What it does

HTTP Request Multiplexer Module

A lightweight HTTP request multiplexer that routes requests based on path and method,
with support for middleware chains and parameterized routes.

## Guarantee

When it runs, http router guarantees r.status_code == 200 and r.body == 'user:123'; r.status_code == 201 and r.body == 'created'; r.status_code == 404 (proven by run).

**Checkable constraints:**

- `(r.status_code, r.body) == (200, 'home')`
- `r.status_code == 200 and r.body == 'user:123'`
- `r.status_code == 201 and r.body == 'created'`
- `(r.status_code, r.body) == (200, 'OK')`
- `r.status_code in (404, 405)`
- `r.status_code == 404`
- `r.status_code == 401 and r.body == 'Unauthorized'`
- `seen == ['probe']`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
