"""
Difference-in-Differences (DiD) — did the treatment actually work?

WHAT IT DOES: Two groups (treated and control) observed before and after a policy
change. You can't just compare after vs before (time trends confound) or treated vs
control (groups may differ). DiD subtracts both: (treated_after - treated_before) -
(control_after - control_before). The key assumption: parallel trends — without
treatment, both groups would have changed the same way.

WHEN TO USE: You have pre/post data for both a treated and a control group, and you
believe the parallel trends assumption is reasonable. Classic use: policy evaluation,
program evaluation, pricing changes.

GUARANTEES: DiD estimate within 3 units of the true treatment effect. Pre-period DiD
(no treatment yet) returns ~0. Same-group DiD (control vs itself) returns ~0. The
parallel trends assumption is planted and verified.

NOT: A general causal inference tool. Only works when parallel trends holds. Does
not handle multiple time periods, staggered adoption, or non-parallel trends.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
