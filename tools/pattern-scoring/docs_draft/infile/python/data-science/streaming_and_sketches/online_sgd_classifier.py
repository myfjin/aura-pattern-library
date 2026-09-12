"""
Online SGD Classifier — train a model on data that doesn't fit in memory.

WHAT IT DOES: Instead of loading the entire dataset and iterating, process one sample
at a time, updating weights incrementally. This pattern implements logistic regression
trained via online SGD (single pass over the data) and compares it to batch SGD
(multiple epochs). On separable data, the online version achieves >70% accuracy in
a single pass.

WHEN TO USE: Data is too large to fit in memory, or you need to update models
continuously as new data arrives (online learning). Common in ad targeting,
recommendation systems, and real-time fraud detection.

GUARANTEES: Online accuracy > 70% on separable data. Online loss within 3x of batch
loss (trained with 5x fewer epochs). Both converge to reasonable decision boundaries.

NOT: A production online learner. No learning rate scheduling, no regularization,
no feature scaling. The comparison to batch SGD is illustrative, not rigorous.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
