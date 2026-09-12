"""
Missing Value Imputation Pattern.

Replaces None/NaN values with statistical estimates (mean, median, mode) or
creates binary missing-indicator columns. Core idea: preserve sample count while
reconstructing plausible values from complete records; track missingness separately.

When to use: handling incomplete datasets before analysis, preserving row count,
understanding missing-data patterns, tree-based models that benefit from missingness signals.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

from typing import List, Tuple, Optional
import statistics


class MissingValueImputer:
    """Impute missing values using mean/median/mode + missing indicators."""

    def __init__(self, strategy: str = "mean"):
        """
        Args:
            strategy: 'mean', 'median', or 'mode'
        """
        self.strategy = strategy
        self.fill_values: dict = {}
        self.missing_indices: dict = {}

    def fit(self, data: List[Optional[float]]) -> "MissingValueImputer":
        """Learn imputation value from non-missing data."""
        non_missing = [x for x in data if x is not None]
        if not non_missing:
            raise ValueError("All values missing, cannot impute")

        if self.strategy == "mean":
            self.fill_values["value"] = statistics.mean(non_missing)
        elif self.strategy == "median":
            self.fill_values["value"] = statistics.median(non_missing)
        elif self.strategy == "mode":
            self.fill_values["value"] = statistics.mode(non_missing)
        else:
            raise ValueError(f"Unknown strategy: {self.strategy}")

        return self

    def transform(self, data: List[Optional[float]]) -> Tuple[List[float], List[int]]:
        """
        Impute missing values, return (imputed_data, missing_indicator).
        missing_indicator[i] = 1 if original was None, else 0.
        """
        imputed = []
        indicators = []
        fill_val = self.fill_values["value"]

        for x in data:
            if x is None:
                imputed.append(fill_val)
                indicators.append(1)
            else:
                imputed.append(x)
                indicators.append(0)

        return imputed, indicators

    def fit_transform(
        self, data: List[Optional[float]]
    ) -> Tuple[List[float], List[int]]:
        """Fit and transform in one step."""
        return self.fit(data).transform(data)


if __name__ == "__main__":
    import random

    random.seed(42)

    # Synthetic data: values with planted structure, some missing
    # True mean ~50, add missingness
    data_with_missing = [48.0, None, 52.0, 49.0, None, 51.0, 50.0, None, 53.0]

    imputer_mean = MissingValueImputer(strategy="mean")
    imputed, indicators = imputer_mean.fit_transform(data_with_missing)

    # Verify structure
    assert len(imputed) == len(data_with_missing), "Length mismatch"
    assert len(indicators) == len(data_with_missing), "Indicator length mismatch"

    # Verify no Nones remain
    assert all(x is not None for x in imputed), "Imputation failed: None remains"

    # Verify missing indicator: should be 1 where original was None
    assert indicators == [0, 1, 0, 0, 1, 0, 0, 1, 0], f"Indicator mismatch: {indicators}"

    # Verify imputed value is the mean of non-missing
    non_missing_vals = [48.0, 52.0, 49.0, 51.0, 50.0, 53.0]
    expected_mean = statistics.mean(non_missing_vals)
    assert abs(imputer_mean.fill_values["value"] - expected_mean) < 1e-6

    # Verify all missing positions are filled with mean
    for i, ind in enumerate(indicators):
        if ind == 1:
            assert imputed[i] == expected_mean, f"Imputed value at {i} is wrong"

    # Test median imputation
    imputer_median = MissingValueImputer(strategy="median")
    imputed_med, _ = imputer_median.fit_transform(data_with_missing)
    expected_median = statistics.median(non_missing_vals)
    for i, ind in enumerate(indicators):
        if ind == 1:
            assert imputed_med[i] == expected_median

    print("missing_value_imputation.py: PASS")
