# service registry

**Language:** Python · **Sphere:** programming · **Category:** Distributed

## What it does

In-memory service-discovery registry with heartbeat-based health and TTL.

Use when instances register themselves and clients look them up by name and an
optional set of tags: each instance must heartbeat within its TTL to stay
discoverable, and a background thread reaps the silent ones. Lookups return only
healthy instances. Guarantees (proven by self-test): name+tag lookup is exact
(tags matched as a subset); an instance that stops heartbeating disappears once
its TTL lapses while a heartbeated peer survives; deregister returns honestly and
removes immediately.

## Guarantee

When it runs, service registry guarantees len(found) == 2 and found[0].port == 8080; {s.service_id for s in registry.find('web-server')} == {web_id, web2_id}; len(registry.find('database')) == 1 (proven by run).

**Checkable constraints:**

- `{s.service_id for s in registry.find('web-server')} == {web_id, web2_id}`
- `len(registry.find('database')) == 1`
- `registry.find('ghost-service') == []`
- `[s.service_id for s in prod_web] == [web_id]`
- `registry.find('web-server', {'production', 'frontend'}) != []`
- `registry.find('web-server', {'production', 'backend'}) == []`
- `len(found) == 2 and found[0].port == 8080`
- `registry.heartbeat(web_id) is True`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
