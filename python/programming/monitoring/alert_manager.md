# alert manager

**Language:** Python · **Sphere:** programming · **Category:** Monitoring

## What it does

Alert manager with rule-driven deduplication, suppression, and escalation.

Use to ingest a stream of alerts and cut noise: each alert is fingerprinted
(title+source+tags) and matched to a rule that sets a dedup window, suppression
tags, and an escalation threshold. Guarantees (proven by self-test): an
identical fingerprint inside the dedup window is folded into the existing alert
(not re-fired), but the same fingerprint past the window alerts again; a
maintenance-tagged alert is accepted but kept out of the active set; resolve
removes from active and returns honestly (double-resolve is False).

## Guarantee

When it runs, alert manager guarantees n_active_before == 3; manager.process_alert(a1) is True; manager.process_alert(dup) is False (proven by run).

**Checkable constraints:**

- `manager.process_alert(a1) is True`
- `manager.process_alert(dup) is False`
- `manager.process_alert(a3) is True`
- `manager.process_alert(again) is True`
- `manager.process_alert(supp) is True`
- `[s.title for s in suppressed] == ['Disk Warning']`
- `'Disk Warning' not in active_titles`
- `n_active_before == 3`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
