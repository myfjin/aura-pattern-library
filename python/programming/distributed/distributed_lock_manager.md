# distributed lock manager

**Language:** Python · **Sphere:** programming · **Category:** Distributed

## What it does

In-process distributed lock manager with lease expiry and a fairness queue.

Use when several owners contend for named resources and you need mutual
exclusion plus automatic recovery if a holder dies: locks carry a lease that
lapses on its own, and blocked waiters are served first-come-first-served.
Guarantees (proven by self-test): only one owner holds a resource at a time; a
released lock hands off to exactly one waiter; an expired lease is reacquirable;
refresh extends a live lease past its original expiry; release/refresh with a
foreign or stale token is refused.

## Guarantee

When it runs, distributed lock manager guarantees n_winners * 2 == 2; token1 is not None; info['owner_id'] == 'client1' and (not info['expired']) (proven by run).

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
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
