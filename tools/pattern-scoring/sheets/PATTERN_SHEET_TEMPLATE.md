# PATTERN SHEET — <pattern name>
*The teaching page: everything a student needs to USE this pattern, not just run it.*
*Layer 4 of the definition stack: ① description (in-file) ② error catalog ③ input contract ④ this.*

## What it solves
<the problem, in plain words — when would a person reach for this>

## Valid inputs (the contract)
| Input | Domain | Violating it → |
|---|---|---|
| <param> | <valid range/type, from docstring + audit> | AURA-E### |

## How inputs shape the output
<per input: what turning this knob does to the result — direction, sensitivity, edge behavior.
This is the section students learn from.>

## Worked example (real run, not invented)
```
<actual command + actual output from the audited baseline>
```
**Reading the output:** <what each printed number MEANS for the problem being solved>

## Failure modes (from the error catalog)
| Trigger | What happens today | Meaning |
|---|---|---|
| <attack> | <observed error, E-code> | <plain words> |

## Provenance
Machine-VERIFIED <date> · cross-model reviewed <date> · Illia's audit: <verdict, date> ·
sheet material generated during manual audit (evidence in `output/manual_audit_<date>.csv`)
