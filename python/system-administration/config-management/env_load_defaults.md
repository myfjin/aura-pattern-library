# env load defaults

**Language:** Python · **Sphere:** system-administration · **Category:** Wave 9 · Config management

**Signature:** `(required_vars: List[str], optional_defaults: None) → ?`

## What it does

Environment variable loading with defaults: load env vars, fill missing with defaults.
Failure simulated: required env var missing, no default provided.
Asserts: exact env var name in error; valid defaults apply; valid required vars load.

## Guarantee

When it runs, env load defaults guarantees result['REQ_VAR'] == 'required_value'; result['ANOTHER_REQ'] == 'another_value'; result['OPT_VAR'] == 'default_opt' (weak-grade: directional, proven by run).

**Checkable constraints:**

- `result['REQ_VAR'] == 'required_value'`
- `result['ANOTHER_REQ'] == 'another_value'`
- `result['OPT_VAR'] == 'default_opt'`
- `result['ANOTHER_OPT'] == 'default_another'`
- `result['OPT_VAR'] == 'present_opt'`
- `result['ANOTHER_OPT'] == 'default_another'`
- `'MISSING_REQ' in str(e)`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** unreviewed

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** `def env_load_defaults(required_vars, optional_defaults=None):`
**Valid input:** `required_vars` is a list of environment-variable names; `optional_defaults` is a dict of name → default value.
**Core:** Loads required environment variables, raising `KeyError` with the exact missing name if absent; fills optional variables from the environment or their defaults.
**Assert:** Required vars load, missing required raises with the var name, optional defaults apply, and present optional vars override defaults.
**⚠️ Defect:** Modifies the process-global `os.environ` in its own tests by popping keys, which is not isolated. There is no type conversion or validation beyond presence; every value is returned as a string.

---
*△ AURA Pattern Library — © Reality Optimizer*
