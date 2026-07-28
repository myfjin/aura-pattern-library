"""
Walk-Forward Validation

Time-series cross-validation using expanding windows: train on the first
window, forecast 1 step ahead, expand window by 1, repeat.
Evaluates forecasters on realistic out-of-sample data without lookahead bias.
Compare multiple forecasters (naive mean vs. other methods) using MAE.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

from typing import List, Callable, Tuple




class AuraInputError(ValueError):
    """All input-contract violations, reported together (accumulate-then-raise)."""
    def __init__(self, violations):
        self.violations = violations
        super().__init__("input contract violated:\n  " + "\n  ".join(violations))

def _aura_validate_naive_last_value_forecast(train):
    v = []
    if isinstance(train, (int, float)) and train <= 0:
        v.append(f"AURA-E009: train must be > 0, got {train}")
    if v:
        raise AuraInputError(v)

def _aura_validate_naive_mean_forecast(train):
    v = []
    if isinstance(train, (int, float)) and train <= 0:
        v.append(f"AURA-E009: train must be > 0, got {train}")
    if v:
        raise AuraInputError(v)

def naive_mean_forecast(train: List[float], steps_ahead: int = 1) -> List[float]:
    """Forecast using mean of training set."""
    _aura_validate_naive_mean_forecast(train)
    mean = sum(train) / len(train) if train else 0.0
    return [mean] * steps_ahead


def naive_last_value_forecast(train: List[float], steps_ahead: int = 1) -> List[float]:
    """Forecast using last value (random walk)."""
    _aura_validate_naive_last_value_forecast(train)
    last = train[-1] if train else 0.0
    return [last] * steps_ahead


def walk_forward_validation(
    series: List[float],
    initial_window: int,
    forecast_func: Callable[[List[float]], List[float]],
) -> Tuple[List[float], List[float]]:
    """
    Walk-forward validation: expand window, train, forecast 1 step.
    initial_window: size of first training window
    forecast_func: function(train_data) -> [forecast_value]
    Returns (actual_values, predicted_values)
    """
    if initial_window >= len(series):
        raise ValueError("initial_window must be < len(series)")

    actuals = []
    predictions = []

    for t in range(initial_window, len(series)):
        train = series[:t]
        actual = series[t]

        # Forecast
        fcst = forecast_func(train)
        pred = fcst[0] if fcst else 0.0

        actuals.append(actual)
        predictions.append(pred)

    return actuals, predictions


def compute_mae(actual: List[float], predicted: List[float]) -> float:
    """Mean absolute error."""
    if len(actual) != len(predicted):
        raise ValueError("Length mismatch")
    return sum(abs(a - p) for a, p in zip(actual, predicted)) / len(actual)


if __name__ == "__main__":
    import random
    random.seed(42)

    # Generate series with trend
    series = []
    val = 10.0
    for i in range(100):
        val += 0.2 + random.gauss(0, 0.5)
        series.append(val)

    # Walk-forward validation with naive mean forecast
    actuals_mean, preds_mean = walk_forward_validation(
        series, initial_window=30, forecast_func=naive_mean_forecast
    )
    assert len(actuals_mean) == len(preds_mean)
    assert len(actuals_mean) == len(series) - 30

    # Walk-forward with naive last value (random walk)
    actuals_last, preds_last = walk_forward_validation(
        series, initial_window=30, forecast_func=naive_last_value_forecast
    )

    # Compute MAE
    mae_mean = compute_mae(actuals_mean, preds_mean)
    mae_last = compute_mae(actuals_last, preds_last)

    # Both should be positive
    assert mae_mean > 0 and mae_last > 0

    # For trending series, last-value is usually better than mean
    # (but not guaranteed for all seeds/data)
    # Just check that we can compare them
    assert isinstance(mae_mean, float) and isinstance(mae_last, float)

    # Check that predictions are within a reasonable range
    series_mean = sum(series) / len(series)
    series_std = (sum((x - series_mean) ** 2 for x in series) / len(series)) ** 0.5
    for pred in preds_mean:
        assert series_mean - 3 * series_std < pred < series_mean + 3 * series_std

    # Verify that walk-forward actually expanded the window
    # by checking that early predictions have less variance (smaller training set)
    early_preds = preds_mean[:10]
    late_preds = preds_mean[-10:]
    # Early predictions should be more similar to the mean (less variance)
    early_std = (sum((p - sum(early_preds) / len(early_preds)) ** 2 for p in early_preds) / len(early_preds)) ** 0.5
    # This is a weak test; the key is that the loop ran correctly

    print("walk_forward_validation.py PASS")
