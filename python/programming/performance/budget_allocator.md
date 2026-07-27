# budget allocator

**Language:** Python · **Sphere:** programming · **Category:** Performance

## What it does

Request Collapser Module

This module implements a request collapser that batches identical requests
within a time window to reduce backend load. It deduplicates concurrent
requests and executes them as a single backend call.

## Guarantee

When it runs, budget allocator guarantees results[0]['user_id'] == 123 and results[0]['call_no'] == 1; calls['n'] == 4; c._get_request_key((1,), {'b': 2, 'a': 3}) == '1|a:3|b:2' (proven by run).

**Checkable constraints:**

- `c._get_request_key((1,), {'b': 2, 'a': 3}) == '1|a:3|b:2'`
- `calls['n'] == 1`
- `len(results) == 5`
- `all((r == results[0] for r in results))`
- `results[0]['user_id'] == 123 and results[0]['call_no'] == 1`
- `calls['n'] == 4`
- `[r['user_id'] for r in r2] == [123, 456, 789]`
- `len(failures) == 2`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
