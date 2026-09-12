# PATTERN SHEET — ttl_cache
`python/system-administration/secrets-credentials/ttl_cache.py`
**Status: PASS-WITH-FLAG (STRONG) (Illia's audit, 2026-07-19) — core expiry correct, but size()
is a docstring-lie hiding a memory leak, and the cache silently accepts nonsense time. Fix #11.**

## What it solves
Hold a value, but only for a while. Cached DB credentials, a session token, a DNS answer —
things that must expire so stale secrets don't linger. TTL = time-to-live: set an item, and after
`ttl` ticks it's gone. **Logical clock, not wall-clock**: time only moves when YOU move it
(`clock.advance(n)`) — which makes tests deterministic and lets you simulate hours in microseconds.

## How to drive it (the manipulation guide Illia asked for)
```python
clk = LogicalClock()          # starts at now=0
c   = ttl_cache(100, clk)     # items live 100 ticks
c.set("api_key", "secret")    # stored at now=0
clk.advance(50); c.get("api_key")   # → "secret"  (age 50 ≤ 100, alive)
clk.advance(50); c.get("api_key")   # → "secret"  (age EXACTLY 100 — still alive, expiry is age>ttl)
clk.advance(1);  c.get("api_key")   # → None      (age 101 > 100, expired + deleted)
```
Basic variations to reason about:
- **advance in one big jump vs many small** → identical (only the total age matters).
- **ttl=0** → item alive only at the exact set-tick, gone at the next advance.
- **re-set the same key** → insertion_time resets; the clock for that item restarts.
- **advance backwards** (`advance(-n)`) → the clock ACCEPTS it (see failure modes — this resurrects).

## Valid inputs (the contract — to be enforced per fix #11)
| Input | Domain | Today → |
|---|---|---|
| `ttl_seconds` | > 0 | **-5 → cache born dead, silent** (every get None) |
| `clock.advance(delta)` | delta ≥ 0 (time moves forward) | negative accepted → resurrects expired items |
| expiry boundary | strict: expired when `age > ttl` | undeclared (age == ttl is still a hit) |

## Failure modes (audited by hand — a docstring-lie + a leak, in a SECRETS pattern)
| Trigger | What happens today | Meaning |
|---|---|---|
| `size()` on an expired item | **returns 1** — then `get()` it, size drops to 0 | docstring says "non-expired count" but returns raw `len`; **expiry is LAZY (only on get)** |
| write-heavy, keys never re-read | expired entries **never freed** → unbounded memory | the leak the size()-lie conceals; serious for cached secrets |
| `advance(-600)` after expiry | dead item returns to life (`get → "secret"`) | negative age = "alive"; real-world analog: NTP clock correction |
| `ttl = -5` | cache holds nothing, no error | nonsense config silently accepted |

**The teaching point (Part C gold):** the code's `get()` is correct, so every quick test passes.
The lie is in `size()` and in what the cache does when NOT accessed — a bug you only see by
reading the docstring's claim against the code's `return len(self.cache)`, exactly what a machine
gate (which trusts the green asserts) cannot do.

## Worked example (real run)
```
$ python3 python/system-administration/secrets-credentials/ttl_cache.py
ttl_cache PASS
```
The demo proves the happy path (hit at 50, miss at 150). It never calls `size()` on an expired
item — which is why the lie survived every machine gate.

## Provenance
Machine-VERIFIED (frozen ruler) · **Illia's audit 07-19: size() docstring-lie + lazy-expiry
leak + time-travel + neg-ttl, all silent → STRONG flag; fix #11** ·
evidence: `output/manual_audit_2026-07-19.csv`
