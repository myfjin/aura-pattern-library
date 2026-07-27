# layered merge

**Language:** Python · **Sphere:** system-administration · **Category:** Wave 9 · Config management

**Signature:** `(layers: List[dict], required_keys: None) → ?`

## What it does

Layered config merge: merge multiple config sources with precedence (later = higher).
Failure simulated: required key missing across all layers; wrong precedence applied.
Asserts: exact missing key name in error; exact winning value per layer order.

## Guarantee

When it runs, layered merge guarantees result['port'] == 9090; result['timeout'] == 30; result['port'] == 3000 (proven by run).

**Checkable constraints:**

- `result['host'] == 'localhost'`
- `result['port'] == 9090`
- `result['debug'] == True`
- `result['timeout'] == 30`
- `result['port'] == 3000`
- `result['host'] == 'localhost'`
- `result['port'] == 9090`
- `'missing_key' in str(e)`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** `def layered_merge(layers, required_keys=None):`
**Valid input:** `layers` is a list of dicts; `required_keys` is a list of keys that must exist in the merged result.
**Core:** Merges config layers in order, with later layers overriding earlier ones. Raises `KeyError` if any required key is missing from the final merged dict.
**Assert:** Later layers override earlier values; required keys present pass; missing required keys are reported by name.
**⚠️ Defect:** Merging is shallow; nested dicts are replaced rather than recursively merged. There is no type checking or conflict reporting for keys that appear in multiple layers.

---
*△ AURA Pattern Library — © Reality Optimizer*
