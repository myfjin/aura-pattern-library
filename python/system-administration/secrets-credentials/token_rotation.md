# token rotation

**Language:** Python · **Sphere:** system-administration · **Category:** Wave 10 · Secrets & credentials

**Signature:** `(token_file: str, max_tokens: int) → ?`

## What it does

Token rotation: keep only N most recent tokens, discard oldest on overflow.
Failure simulated: add 100 tokens with cap=5; assert only 5 remain and oldest are gone.
Defended outcome: file holds exactly N tokens; accessing beyond cap returns None.

## Guarantee

When it runs, token rotation guarantees final_count == 5; token_ids == expected_ids; 'token_000' not in token_ids (proven by run).

**Checkable constraints:**

- `final_count == 5`
- `token_ids == expected_ids`
- `'token_000' not in token_ids`
- `'token_050' not in token_ids`
- `file_size < 500`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
