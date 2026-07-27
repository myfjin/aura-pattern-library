# dns resolve check

**Language:** Python · **Sphere:** system-administration · **Category:** Wave 8 · Network reachability & health

**Signature:** `(hostname: str, timeout_sec: float) → ?`

## What it does

dns_resolve_check: resolve a hostname; return resolved IP or None if DNS fails.
Failure simulated: resolve localhost (succeeds), resolve guaranteed-bogus name (fails).
Recovery asserted: localhost resolves to 127.0.0.1 or ::1; bogus name fails; no internet access needed.

## Guarantee

When it runs, dns resolve check guarantees localhost_ip is not None; localhost_ip == '127.0.0.1'; loopback_ip == '127.0.0.1' (weak-grade: directional, proven by run).

**Checkable constraints:**

- `localhost_ip is not None`
- `localhost_ip == '127.0.0.1'`
- `loopback_ip == '127.0.0.1'`
- `bogus_ip is None`
- `localhost_ip is not None and bogus_ip is None`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
