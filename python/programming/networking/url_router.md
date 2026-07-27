# url router

**Language:** Python · **Sphere:** programming · **Category:** Networking

## What it does

URL router with `{param}` path patterns and reverse URL building.

Use to map URL paths to handlers: register routes (via add_route or the @route
decorator) whose patterns embed `{name}` segments that match anything except '/',
match() returns the handler plus a dict of extracted params, and build_url()
reconstructs a URL from a named route's arguments. Guarantees (proven by
self-test): params are extracted exactly; unknown, partial, or over-long paths
return (None, {}) honestly; reverse building is exact and returns None for an
unknown name; and build->match is a round-trip identity on the params.

## Guarantee

When it runs, url router guarantees int(params['user_id']) + int(params['post_id']) == 1245; handler is not None and params == {} and (handler() == 'home'); params == {'user_id': '123'} (proven by run).

**Checkable constraints:**

- `handler is not None and params == {} and (handler() == 'home')`
- `params == {'user_id': '123'}`
- `handler(**params) == 'user 123'`
- `params == {'user_id': '456', 'post_id': '789'}`
- `handler(**params) == 'post 789 by 456'`
- `int(params['user_id']) + int(params['post_id']) == 1245`
- `params == {'query': 'python'} and handler(**params) == 'results for python'`
- `handler is None`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
