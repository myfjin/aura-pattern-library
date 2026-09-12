"""
Hoeffding Tree (VFDT) Lite — a streaming decision stump with a Hoeffding-bound split
test.

WHAT IT DOES: Accumulates class counts on each side of every candidate split as data
streams in. After n samples, the true information gain of a split is within
ε = √(R²·ln(1/δ) / 2n) of its observed gain (Hoeffding bound). Splits as soon as the
best candidate's observed gain beats the runner-up by more than ε — provably the true
best with prob ≥ 1−δ.

WHEN TO USE: You need to train a decision tree on a stream where data arrives one
sample at a time and you can't store it all.

GUARANTEES: Split decision is statistically justified (Hoeffding bound). Streaming
stump matches batch-trained stump within 3% accuracy.

NOT: A full VFDT. Only builds a single stump (one split). Does not handle categorical
features or missing values.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"