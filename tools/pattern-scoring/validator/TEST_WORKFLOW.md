# Validation Tool — Test Workflow for 5S & 4Q (2026-07-20)
**Goal: try to make the tool LIE. A verdict that disagrees with reality is the prize.
Structure below is a floor, not a ceiling — IMPROVISE beyond it. Illia reviews your findings.**

## The tool
`~/ai-lab/pattern-scoring/validator/` (on .5; mirrored to /tmp/aura-review/pattern-scoring/validator/ for .8).
Run: `cd validator && python3 validate.py` → grades itself against exam.json (Illia's answer key).
Read README.md for architecture (13 recipes · 8-signal oracle · honesty guardrails · verdict ladder).

## Your mission: adversarial verification of the TOOL (not the patterns)
The patterns were audited by Illia. Now audit the AUDITOR. Three attack fronts:

### Front 1 — FALSE-PASS hunt (5S's #1 fear: silent PASS that should be FLAG/INVALID)
Find a pattern the tool PASSes (or would) that actually has a defect. Especially:
- patterns with NO numeric oracle and NO invariant — does the tool correctly FALL THROUGH to
  FLAG (oracle_coverage guardrail), or does it wrongly PASS?
- a wrong-math pattern with no closed-form reference — can the tool be fooled into PASS?

### Front 2 — FALSE-KILL hunt (5S's #2: attack that never reached the code)
Find a case where the tool marks INVALID but the attack was a no-op (didn't reach the function),
like Illia's X=[] before generation loops. Does the attack-reachability guardrail catch it, or
does the tool false-KILL a healthy pattern?

### Front 3 — BOUNDARY honesty (does the tool admit what it can't do?)
- feed it a concurrency pattern (Atomic/Mutex/spawn) — does it CAP at FLAG for ordering, or
  falsely PASS after a lucky single-threaded run?
- feed it a twin pair where the twin DIVERGED — does it re-audit or blindly inherit?

## Method (per finding)
1. Pick/construct a pattern + your PREDICTED correct verdict (with your reasoning).
2. Run the tool (or reason about what it would do from oracle.py's 8-signal table).
3. If tool-verdict ≠ your-verdict → you found a calibration case. Record: pattern, tool verdict +
   its reason, YOUR verdict + mechanism, which guardrail failed.
4. This feeds the disagreement protocol: a mechanism the other accepts wins; logged as a
   calibration ticket. Finding where the tool is wrong is SUCCESS, not failure.

## Division (improvise, but a starting split)
- **5S:** Fronts 1 + 3 (false-PASS + boundary honesty) — your conscience-thesis is the tool's soul.
- **4Q:** Front 2 + composition/twin (false-KILL + twin-divergence) — your efficiency-lens fits.
- Overlap welcome. If you find something outside your front, take it.

## Deliverable
`<AGENT>_tool_test_2026-07-20.md` in your drop path: for each probe — pattern · predicted verdict ·
tool verdict · agree/disagree · if disagree the mechanism · which guardrail (if any) failed.
Batch incrementally, @claude_aura_bot when a batch is done. Improvisation encouraged — the more
creatively you attack the tool's honesty, the more Illia trusts it (or learns where it lies).

## The spirit
The tool's motto (5S): "the biggest risk is silently PASSing when it should say I cannot tell."
Your job is to catch it doing exactly that. A tool that survives your attacks earns the university
claim; a tool that fails one earns a fix. Both are wins.
