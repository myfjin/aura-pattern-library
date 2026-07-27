# distributed lock manager

**Language:** Go · **Sphere:** programming · **Category:** Distributed

## What it does

distributed_lock_manager: in-process distributed lock manager with fairness
queue, lease expiration, refresh, and mutual exclusion.

## Guarantee

When it runs, distributed lock manager guarantees n_winners * 2 == 2; token1 is not None; info['owner_id'] == 'client1' and (not info['expired']) (proven by run on the PY-PROG original).

**Checkable constraints:**

- `token1 is not None`
- `info['owner_id'] == 'client1' and (not info['expired'])`
- `manager.acquire('resource1', 'client2', timeout=0.1) is None`
- `manager.release(token1) is True`
- `manager.release(token1) is False`
- `token2 is not None and token2.owner_id == 'client2'`
- `not results`
- `n_winners * 2 == 2`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — established on the PY-PROG original and shared by this Go twin (twin agreement is the evidence: consensus, xlang); the original oracle was not executed against this file
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
