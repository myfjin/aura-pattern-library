# cli args parser

**Language:** Rust · **Sphere:** rust · **Category:** parsing-protocols

**Signature:** `(argv: &[&str]) → Result<Args, ParseError>`

## What it does

cli_args_parser — from-scratch getopt: short/long flags, =values, -- boundary.

Core idea: parse command-line arguments from scratch, handling short/long flags, values,
and -- to stop flag parsing. THE ONE LAW: plant argv with mixed flags, values, and the --
boundary, parse it, and assert every flag/value/positional is captured exactly, including
combined short flags (-abc) and --key=value — a naive split would fail on both.
(The parser is intentionally lenient — it does not reject unknown flags.)
When to use: CLI tools, configuration loading, argument validation.

## Guarantee

When it runs, cli args parser guarantees assert_eq!(parsed1.flags.len(), 3); assert_eq!(parsed1.flags[0].0, "v"); assert_eq!(parsed1.flags[1].0, "config") (proven by rustc-run).

**Checkable constraints:**

- `assert_eq!(parsed1.flags.len(), 3)`
- `assert_eq!(parsed1.flags[0].0, "v")`
- `assert_eq!(parsed1.flags[1].0, "config")`
- `assert_eq!(parsed1.flags[1].1, Some("/etc/app.conf".to_string()))`
- `assert_eq!(parsed1.flags[2].0, "n")`
- `assert_eq!(parsed1.flags[2].1, Some("100".to_string()))`
- `assert_eq!(parsed2.positional, vec!["file1", "file2"])`
- `assert_eq!(parsed3.flags.len(), 4)`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
