# trace span collector

**Language:** Python · **Sphere:** programming · **Category:** Monitoring

**Signature:** `(collector: SpanCollector, name: str, parent_context: Optional[SpanContext]) → ?`

## What it does

Distributed Tracing Span Collector Module

This module provides a complete implementation of a distributed tracing system
with span collection, parent-child relationships, baggage propagation, and sampling.

## Guarantee

When it runs, trace span collector guarantees by_name['child1'].tags['db.rows'] == 10; child2.get_baggage_item('user_id') == '12345'; len(traces) == 1 (proven by run).

**Checkable constraints:**

- `child2.get_baggage_item('user_id') == '12345'`
- `len(traces) == 1`
- `len(trace.spans) == 4`
- `set(by_name) == {'parent', 'child1', 'grandchild', 'child2'}`
- `by_name['parent'].context.parent_span_id is None`
- `by_name['child1'].context.parent_span_id == by_name['parent'].context.span_id`
- `by_name['child2'].context.parent_span_id == by_name['parent'].context.span_id`
- `by_name['grandchild'].context.parent_span_id == by_name['child1'].context.span_id`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
