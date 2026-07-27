# csv to json

**Language:** Python · **Sphere:** programming · **Category:** Io

## What it does

CSV to JSON converter module with type inference, nested key support, and streaming.

## Guarantee

When it runs, csv to json guarantees john['age'] == 30 and isinstance(john['age'], int); john['salary'] == 75000.5 and isinstance(john['salary'], float); sum((r['age'] for r in rows)) == 100 (proven by run).

**Checkable constraints:**

- `len(rows) == 3`
- `john['name'] == 'John Doe'`
- `john['age'] == 30 and isinstance(john['age'], int)`
- `john['salary'] == 75000.5 and isinstance(john['salary'], float)`
- `john['employment']['status'] is True`
- `john['department'] == {'name': 'Engineering', 'budget': 500000}`
- `rows[1]['employment']['status'] is False`
- `sum((r['age'] for r in rows)) == 100`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
