# trace collector

**Language:** Python · **Sphere:** programming · **Category:** Monitoring

**Signature:** `(node: Dict[str, Any], indent: int) → None`

## What it does

Minimal distributed-tracing collector: spans, traces, and their tree.

Use to model an operation as a tree of timed spans: a Collector creates spans
(each with an id, parent, attributes, and status) grouped into traces, and
rebuilds the parent/child hierarchy on demand. A span's finish() stamps an end
time and sets "ok" only if still unset — it never overwrites an error status.
Guarantees (proven by self-test): separate operations stay isolated as distinct
traces; the reconstructed tree has the exact root/children shape (no phantom
descendants); attributes and error status survive; durations are non-negative;
and an unknown trace_id passed to create_span creates that trace explicitly.

## Guarantee

When it runs, trace collector guarantees n_traces == 2; root_span.trace_id != second_root.trace_id; len(tree['roots']) == 1 (proven by run).

**Checkable constraints:**

- `n_traces == 2`
- `root_span.trace_id != second_root.trace_id`
- `len(tree['roots']) == 1`
- `root_node['span'].name == 'HTTP GET /api/users'`
- `child_names == ['Call external API', 'SELECT users']`
- `all((c['children'] == [] for c in root_node['children']))`
- `root_node['span'].attributes['http.method'] == 'GET'`
- `by_name['SELECT users'].attributes['db.type'] == 'sql'`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
