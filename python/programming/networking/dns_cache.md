# dns cache

**Language:** Python · **Sphere:** programming · **Category:** Networking

## What it does

LRU DNS cache with per-record TTL expiry and negative caching.

Use as a bounded resolver cache keyed by (name, record_type): positive records
expire at their own TTL, "does-not-exist" answers are cached negatively for 30s,
and when capacity is reached the least-recently-used entry is evicted. Guarantees
(proven by self-test on a fake clock): a record lives up to its TTL and is gone
just past it while a longer-TTL peer still answers; (name, type) are independent
keys; negative entries answer None for 30s then become re-askable; clear_expired
returns the exact number removed; and LRU eviction drops the untouched entry, not
a recently-looked-up one.

## Guarantee

When it runs, dns cache guarantees cache.size() == 3; removed == 4; lru.size() == 3 (proven by run).

**Checkable constraints:**

- `cache.size() == 3`
- `cache.lookup('example.com', 'A').value == '93.184.216.34'`
- `cache.lookup('example.com', 'AAAA').value == '2606::1946'`
- `cache.lookup('example.com', 'MX') is None`
- `cache.lookup('nonexistent.com', 'A') is None`
- `cache.lookup('example.com', 'A') is not None`
- `cache.lookup('example.com', 'A') is None`
- `cache.lookup('google.com', 'A') is not None`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
