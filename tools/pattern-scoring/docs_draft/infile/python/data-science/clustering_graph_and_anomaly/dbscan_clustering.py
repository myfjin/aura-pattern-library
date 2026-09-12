"""
DBSCAN Clustering — find clusters of any shape, and spot the outliers.

WHAT IT DOES: K-means forces clusters into spheres; DBSCAN doesn't care. It groups
points that are close together (within eps distance) and have at least min_pts
neighbors. Points in sparse regions are labeled as noise. The algorithm grows clusters
from dense points, merging overlapping regions — like oil drops on water coalescing.

WHEN TO USE: Clusters have irregular shapes, density varies, or you need to identify
outliers (noise points). Common in geospatial clustering, anomaly detection, and any
domain where "round clusters" is a bad assumption.

GUARANTEES: On two planted Gaussian clusters (σ=0.3, centers 6 units apart) with 5
uniform noise points, DBSCAN finds exactly 2 clusters and at least 3 noise points.
All cluster labels are valid (≥ -1).

NOT: A production DBSCAN implementation. Uses brute-force O(n²) neighbor search —
no spatial index. Does not handle variable density clusters (the limitation of
global eps).
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
