# dotenv parse

**Language:** Python · **Sphere:** system-administration · **Category:** Wave 9 · Config management

**Signature:** `(filepath: str) → ?`

## What it does

Dotenv parser: parse .env files correctly, handle special chars, reject malformed.
Failure simulated: malformed key=value lines; special characters; unquoted values.
Asserts: exact parsed key/value; malformed line rejected with line number; valid .env loads.

## Guarantee

When it runs, dotenv parse guarantees result['HOST'] == 'localhost'; result['PORT'] == '8080'; result['DEBUG'] == 'true' (weak-grade: directional, proven by run).

**Checkable constraints:**

- `result['HOST'] == 'localhost'`
- `result['PORT'] == '8080'`
- `result['DEBUG'] == 'true'`
- `result['MESSAGE'] == 'hello world'`
- `result['PATH'] == '/usr/bin'`
- `result['SINGLE'] == 'single quoted'`
- `result['KEY1'] == 'value1'`
- `result['KEY2'] == 'value2'`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** unreviewed

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** `def parse_dotenv(filepath):`
**Valid input:** `filepath` points to a `.env` file with `KEY=VALUE` lines, comments (`#`), and blank lines.
**Core:** Line-by-line dotenv parser. Strips lines, skips comments/blanks, splits on the first `=`, strips whitespace, and removes matching surrounding single/double quotes.
**Assert:** Simple key-values, quoted values, comments/blanks, missing `=`, empty key, and exact line-number reporting all behave as expected.
**⚠️ Defect:** Does not handle inline comments (`KEY=val # comment` would include the comment in the value), escaped quotes, variable expansion (`$OTHER`), or multiline values. Quote stripping is naive and can mangle values like `"say "hello""`.

---
*△ AURA Pattern Library — © Reality Optimizer*
