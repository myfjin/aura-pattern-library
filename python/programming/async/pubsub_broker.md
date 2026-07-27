# pubsub broker

**Language:** Python · **Sphere:** programming · **Category:** Async

## What it does

A simple pub-sub message broker implementation with wildcard topic matching.

## Guarantee

When it runs, pubsub broker guarantees total == 6; inbox['sports'] == [('news/sports', 'football')]; ('news/sports', 'football') in inbox['news'] (proven by run).

**Checkable constraints:**

- `inbox['sports'] == [('news/sports', 'football')]`
- `('news/sports', 'football') in inbox['news']`
- `('news/politics', 'election') in inbox['news']`
- `not any((t.startswith('weather') for t, _ in inbox['news']))`
- `inbox['weather'] == [('weather/local', 'sunny')]`
- `('news/technology', 'gadget') in inbox['news']`
- `not any((t == 'news/technology' for t, _ in inbox['sports']))`
- `n_sports_msgs == 1`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
