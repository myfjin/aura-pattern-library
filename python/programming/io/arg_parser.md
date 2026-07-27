# arg parser

**Language:** Python · **Sphere:** programming · **Category:** Io

## What it does

A small argparse-style command-line parser (options + positionals).

Use when you want an argparse-like surface without the dependency: define
options (short/long, store / store_true / store_false, nargs 1 / N / '*') and
positional arguments, then parse an argv list into a dict, with -h/--help
generated. Guarantees (proven by self-test): option values are consumed and
never double-counted as positionals; an unset store_true defaults False (an
unset store_false defaults True); defaults are applied; variadic tails and
nargs='*' options resolve exactly; and a missing required option/positional or
an unknown flag is refused with the offending name in the error.

## Guarantee

When it runs, arg parser guarantees sum((int(x) for x in r['numbers'])) == 6; r['format'] == 'json'; r['input_file'] == 'data.txt' (proven by run).

**Checkable constraints:**

- `r['format'] == 'json'`
- `r['input_file'] == 'data.txt'`
- `r['multiplier'] == ['2'] or r['multiplier'] == '2'`
- `r['verbose'] is False`
- `r['output'] == 'output.txt'`
- `r['format'] == 'xml'`
- `r['verbose'] is True`
- `r['input_file'] == 'input.txt'`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
