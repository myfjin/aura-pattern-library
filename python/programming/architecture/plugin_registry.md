# plugin registry

**Language:** Python · **Sphere:** programming · **Category:** Architecture

**Signature:** `() → None`

## What it does

Plugin registry with lazy loading, dependency management, and entry point discovery.

## Guarantee

When it runs, plugin registry guarantees n_loaded == 3; sorted(registry.list_plugins()) == ['database', 'logger', 'webserver']; sorted(order) == ['database', 'logger', 'webserver'] (proven by run).

**Checkable constraints:**

- `sorted(registry.list_plugins()) == ['database', 'logger', 'webserver']`
- `sorted(order) == ['database', 'logger', 'webserver']`
- `order.index('logger') < order.index('database') < order.index('webserver')`
- `inst is None or not inst.is_loaded()`
- `webserver.is_loaded()`
- `registry.get_plugin('logger').is_loaded()`
- `registry.get_plugin('database').is_loaded()`
- `database.execute('SELECT 1') == 'Executed: SELECT 1'`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
