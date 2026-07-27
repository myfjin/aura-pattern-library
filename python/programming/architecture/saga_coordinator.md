# saga coordinator

**Language:** Python · **Sphere:** programming · **Category:** Architecture

## What it does

Saga Pattern Coordinator Module

This module implements the Saga pattern for distributed transactions,
providing forward execution and backward compensation on failure.

## Guarantee

When it runs, saga coordinator guarantees n_executed == 3; ok is False; saga.status == SagaStatus.FAILED (proven by run).

**Checkable constraints:**

- `ok is False`
- `saga.status == SagaStatus.FAILED`
- `trace == ['do:A', 'do:B', 'undo:B', 'undo:A']`
- `saga.context.get('A_compensated') is True`
- `saga.context.get('B_compensated') is True`
- `saga.context.get('C_compensated') is None`
- `saga.context.get('D') is None`
- `ok is True and good.status == SagaStatus.COMPLETED`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
