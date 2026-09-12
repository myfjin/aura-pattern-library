# Description-writing spec (read fully before editing)

You are writing DRAFT descriptions for AURA Pattern Library files. Illia will personally
review each during a manual audit — so honesty beats polish. This library's law: **the name
is a claim, the docstring is a claim.** A plausible-but-adjacent summary is the exact defect
he hunts ("the docstring-lie"). Never invent a confident claim.

## The one law: you MUST read the code before describing it
Open each file with Read. Understand what it actually does, what scenario/oracle its asserts
survive (many are "cause the disaster, prove survival" patterns). Then write 3–6 plain-language
lines: **what it does · when to use it · what it guarantees (the oracle/disaster it survives).**
- TRUE to the code. No salesmanship, no marketing adjectives.
- If a pattern's purpose is genuinely unclear from its code, do NOT guess — write a line the
  reviewer will see, starting `UNCLEAR:` and naming what's ambiguous. Describe less, not more.

## Where the description goes, per language (match the existing convention EXACTLY)
Every file has a 3-line watermark block: `<lang-comment> △ AURA Pattern Library …⟦…⟧`, then a
zero-width line, then a `_AURA_MARK`/`_auraMark`/`_aura_mark` assignment. NEVER touch those lines.

- **python**: module docstring `"""…"""` as the VERY FIRST lines of the file, ABOVE the watermark
  comment. (If a `#!/usr/bin/env python3` shebang is line 1, put the docstring right after it.)
  Note: some files already have a helper-CLASS docstring but no MODULE docstring — add the module one at top.
- **cpp**: `/* … */` block placed immediately AFTER the `static const char *_aura_mark = "…";`
  line and BEFORE the first `#include`.
- **go**: `// …` block placed AFTER the import block and immediately BEFORE the watermark
  `// △ AURA …` line. (If the file has no imports, place it right after `package main`.)
- **rust**: `// …` block placed AFTER the `use …;` lines and BEFORE the first real code
  (`fn main`/`struct`/etc). If there are no top-level `use` lines, place it right after the
  `const _AURA_MARK …;` line.

## For `short` / `declstyle` files (they already have a weak comment)
The worklist entry gives you the current claim. Do NOT delete a real decl comment that documents
a type (e.g. `// AVLNode is a node class`) — leave it in place. ADD a proper pattern-level
description block in the language's description slot above (for go, the pattern description goes
right before the watermark, same slot as missing files). Expand title-only claims into what/when/guarantees.

## Do NOT
- Do NOT modify any code, asserts, includes, or the watermark/`_AURA_MARK` lines.
- Do NOT re-stamp or re-sign — the orchestrator handles signing after all edits.
- Do NOT reformat unrelated lines.

## Return
When done, return ONLY: a JSON object `{"done": [<files edited>], "unclear": [<files where you
wrote an UNCLEAR line>], "skipped": [<file: reason>]}`. Keep it terse.
