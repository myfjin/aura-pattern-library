"""
Stratified Randomization — better experiments through smarter randomization.

WHAT IT DOES: Simple randomization can leave your treatment and control groups
imbalanced on important covariates by chance. Stratified randomization splits the
data into strata (e.g. by age group or gender) and randomizes within each stratum,
ensuring balance. This pattern demonstrates that stratified randomization produces
better covariate balance and lower estimator variance than simple randomization.

WHEN TO USE: You have a known covariate that affects the outcome, and you want to
ensure balance across treatment groups. Common in clinical trials, A/B tests with
known confounders, and any experiment where covariate balance matters.

GUARANTEES: Stratified randomization achieves better covariate balance (lower
|mean(X|T=1) - mean(X|T=0)|) than simple randomization. Stratified randomization
achieves lower ATE estimator variance. Both results hold over 50 replications.

NOT: A general experimental design tool. Only handles median-split stratification.
Does not handle multiple strata, unequal stratum sizes, or post-stratification.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
