# state machine

**Language:** Python · **Sphere:** programming · **Category:** Architecture

## What it does

Simple State Machine Engine

This module provides a complete state machine implementation with support for
states, transitions, guards, actions, and entry/exit hooks.

## Guarantee

When it runs, state machine guarantees sm.get_current_state() == expected; events.count('enter:on') == 2 and events.count('exit:off') == 2; guard_calls['n'] == 2 (proven by run).

**Checkable constraints:**

- `sm.get_current_state() == 'off'`
- `sm.trigger(event) is True`
- `sm.get_current_state() == expected`
- `events[0] == 'exit:off' and events[1] == 'enter:on'`
- `'handler:power_on:off' in events`
- `events.count('enter:on') == 2 and events.count('exit:off') == 2`
- `guard_calls['n'] == 2`
- `sm.trigger('power_on') is False`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
