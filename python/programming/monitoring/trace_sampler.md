# trace sampler

**Language:** Python · **Sphere:** programming · **Category:** Monitoring

**Signature:** `(sampler_type: str) → Sampler`

## What it does

Distributed Tracing Sampler Module

This module provides a complete implementation of a distributed tracing sampler
with support for rate limiting, priority traces, and adaptive sampling.

## Guarantee

When it runs, trace sampler guarantees first == 5; second == 5; all((on.should_sample(_ctx(i)).decision == SamplingDecision.SAMPLE for i in range(50))) (proven by run).

**Checkable constraints:**

- `all((on.should_sample(_ctx(i)).decision == SamplingDecision.SAMPLE for i in range(50)))`
- `all((off.should_sample(_ctx(i)).decision == SamplingDecision.DROP for i in range(50)))`
- `all((ProbabilisticSampler(1.0).should_sample(_ctx(i)).decision == SamplingDecision.SAMPLE for i in range(50)))`
- `all((ProbabilisticSampler(0.0).should_sample(_ctx(i)).decision == SamplingDecision.DROP for i in range(50)))`
- `140 <= hits <= 260`
- `first == 5`
- `second == 5`
- `pr.should_sample(_ctx(1, priority=True)).decision == SamplingDecision.SAMPLE`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
