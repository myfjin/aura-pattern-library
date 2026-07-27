# tokenizer ast evaluator

**Language:** Rust · **Sphere:** rust · **Category:** composed-systems

**Signature:** `(s: &str) → Vec<Token>`

## What it does

composes: tokenize-arithmetic + parse-to-ast-with-precedence + evaluate

## Guarantee

When it runs, tokenizer ast evaluator guarantees assert_eq!(result, 14, "Correct precedence: 2 + 3*4 = 14") (proven by rustc-run).

**Checkable constraints:**

- `assert_eq!(result, 14, "Correct precedence: 2 + 3*4 = 14")`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
