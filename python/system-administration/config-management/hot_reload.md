# hot reload

**Language:** Python · **Sphere:** system-administration · **Category:** Wave 9 · Config management

**Signature:** `(key: str) → ?`

## What it does

Hot reload config: reload config without restart, new value visible after reload, old before.
Failure simulated: old value persists after reload; new value not visible after reload.
Asserts: old value accessible before reload; new value visible after reload (exact values).

## Guarantee

When it runs, hot reload guarantees cfg.get('port') == 8080; old_port == 8080; new_port == 9090 (proven by run).

**Checkable constraints:**

- `cfg.get('port') == 8080`
- `cfg.get('debug') == False`
- `old_port == 8080`
- `new_port != old_port`
- `new_port == 9090`
- `new_debug == True`
- `cfg.get('port') != 8080`
- `cfg.get('port') == 3000`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** `class HotConfig:`, `def __init__(self, filepath):`, `def reload(self):`, `def get(self, key):`
**Valid input:** `filepath` is a JSON config file; keys requested via `get` exist in the current config.
**Core:** Loads a JSON config at init and on explicit `reload`; caches values in memory; `get` reads from the cache.
**Assert:** Initial values load; after modifying the file and calling `reload`, new values are visible; a third reload also works.
**⚠️ Defect:** `reload` is manual, not automatic or file-watch-driven, so stale config is used until someone calls it. There is no error handling for a malformed JSON file during reload; a bad reload would crash the caller.

---
*△ AURA Pattern Library — © Reality Optimizer*
