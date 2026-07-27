# event logger

**Language:** Python · **Sphere:** programming · **Category:** Monitoring

## What it does

Structured event logger with rotation capabilities.

This module provides a complete logging solution that outputs structured
events in JSONL format with automatic log rotation based on file size.

## Guarantee

When it runs, event logger guarantees err['error_code'] == 500 and isinstance(err['error_code'], int); warn['available_gb'] == 2.5; len(written) == 4 (proven by run).

**Checkable constraints:**

- `len(written) == 4`
- `all((w['level'] != 'DEBUG' for w in written))`
- `err['error_code'] == 500 and isinstance(err['error_code'], int)`
- `warn['available_gb'] == 2.5`
- `all(('timestamp' in w for w in written))`
- `inc.should_log({'message': 'an ERROR happened'}) is True`
- `inc.should_log({'message': 'all fine'}) is False`
- `exc.should_log({'message': 'heartbeat ok'}) is False`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
