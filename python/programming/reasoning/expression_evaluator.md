# expression evaluator

**Language:** Python · **Sphere:** programming · **Category:** Reasoning

## What it does

Simple Expression Evaluator with Variables

This module provides a complete expression evaluator that supports:
- Basic arithmetic operations (+, -, *, /, %, **)
- Parentheses for grouping
- Variables with assignment and lookup
- Integer and floating-point numbers

## Guarantee

When it runs, expression evaluator guarantees got == expected; ev.evaluate('x = 10') == 10; ev.evaluate('y = 5') == 5 (proven by run).

**Checkable constraints:**

- `got == expected`
- `type(got) is type(expected)`
- `ev.evaluate('x = 10') == 10`
- `ev.evaluate('y = 5') == 5`
- `ev.evaluate('x + y') == 15`
- `ev.evaluate('z = x * y') == 50`
- `ev.evaluate('z') == 50`
- `ev.evaluate('x = -7') == -7`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
