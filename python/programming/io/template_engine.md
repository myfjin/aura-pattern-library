# template engine

**Language:** Python · **Sphere:** programming · **Category:** Io

## What it does

A minimal regex-based string template engine.

Use for lightweight text templating without a full engine: `{{ var }}`
substitution, `{{ var | default }}` fallbacks, dotted paths (`{{ user.name }}`)
into nested dicts, and `{% for x in list %}...{% endfor %}` loops (including
nested loops). Rendering does loops first, then variables. Guarantees (proven by
self-test): substitution/defaults/nesting/loops produce exact output; a default
fires only when the variable is missing; loop variables are scoped per iteration
and do not leak to the outer context; empty or non-iterable loop targets render
nothing; a non-str template or non-Context context raises TypeError.

## Guarantee

When it runs, template engine guarantees int(engine.render('{{ n }}', Context({'n': 42}))) == 42; engine.render('Hello {{ name }}!', Context({'name': 'World'})) == 'Hello World!'; engine.render('Hello {{ name | Guest }}!', Context({})) == 'Hello Guest!' (proven by run).

**Checkable constraints:**

- `engine.render('Hello {{ name }}!', Context({'name': 'World'})) == 'Hello World!'`
- `int(engine.render('{{ n }}', Context({'n': 42}))) == 42`
- `engine.render('Hello {{ name | Guest }}!', Context({})) == 'Hello Guest!'`
- `engine.render('Hello {{ name | Guest }}!', Context({'name': 'Zed'})) == 'Hello Zed!'`
- `out == 'User: Alice, Age: 30'`
- `out == 'Items: apple, banana, cherry, '`
- `out == 'Alice=30;Bob=25;'`
- `engine.render('A{% for x in xs %}X{% endfor %}B', Context({'xs': []})) == 'AB'`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
