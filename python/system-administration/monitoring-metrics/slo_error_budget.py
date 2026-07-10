#!/usr/bin/env python3
"""slo_error_budget: track error budget against SLO."""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
import sys

class SLOErrorBudget:
    """Track error budget for service level objective."""
    def __init__(self, slo_percent=99.9, period_seconds=2592000):
        """
        slo_percent: target availability (e.g., 99.9 = 99.9% uptime)
        period_seconds: measurement period (default 30 days)
        """
        self.slo_percent = slo_percent
        self.period_seconds = period_seconds
        self.requests_total = 0
        self.requests_failed = 0

    def request_success(self, count=1):
        """Record successful requests."""
        self.requests_total += count

    def request_failure(self, count=1):
        """Record failed requests."""
        self.requests_total += count
        self.requests_failed += count

    def success_rate_percent(self):
        """Get current success rate as percentage."""
        if self.requests_total == 0:
            return 100.0
        return (self.requests_total - self.requests_failed) / self.requests_total * 100.0

    def error_budget_consumed_percent(self):
        """Get percentage of error budget consumed."""
        allowed_failures = self.requests_total * (100.0 - self.slo_percent) / 100.0
        if self.requests_total == 0:
            return 0.0
        return self.requests_failed / allowed_failures * 100.0 if allowed_failures > 0 else 0.0

    def remaining_budget_requests(self):
        """Calculate remaining budget in number of requests."""
        allowed_failures = self.requests_total * (100.0 - self.slo_percent) / 100.0
        return int(max(0, allowed_failures - self.requests_failed))

    def over_budget(self):
        """Check if error budget is exceeded."""
        # Allow small floating point tolerance for equality
        allowed_failures = self.requests_total * (100.0 - self.slo_percent) / 100.0
        return self.requests_failed > (allowed_failures + 0.01)

def test_slo_error_budget():
    """Test: track budget, verify calculations, detect breach."""
    # Test 1: 99.9% SLO (0.1% error budget)
    slo = SLOErrorBudget(slo_percent=99.9)

    # 1 million requests
    slo.request_success(999000)
    slo.request_failure(1000)

    success_rate = slo.success_rate_percent()
    assert success_rate == 99.9, f"Success rate should be 99.9%, got {success_rate}%"

    # Allowed budget: 1M * 0.1% = 1000 failures
    # Actual failures: 1000
    assert not slo.over_budget(), "Should not be over budget at exactly SLO"

    # Add one more failure
    slo.request_failure(1)
    assert slo.over_budget(), "Should be over budget after 1001 failures"

    # Test 2: 99% SLO (1% error budget)
    slo99 = SLOErrorBudget(slo_percent=99.0)

    slo99.request_success(990)
    slo99.request_failure(10)

    # 1000 requests, 1% allowed = 10 allowed failures
    success = slo99.success_rate_percent()
    assert success == 99.0, f"Should be 99.0%, got {success}%"

    budget_consumed = slo99.error_budget_consumed_percent()
    assert budget_consumed == 100.0, f"Budget consumed should be 100%, got {budget_consumed}%"

    # Test 3: safety margin
    slo95 = SLOErrorBudget(slo_percent=95.0)

    # 1000 requests, 5% allowed = 50 allowed failures
    slo95.request_success(950)
    slo95.request_failure(50)

    remaining = slo95.remaining_budget_requests()
    assert remaining == 0, f"Should have 0 remaining budget, got {remaining}"

    # Test 4: well within budget
    slo999 = SLOErrorBudget(slo_percent=99.99)

    # 10000 requests, 0.01% allowed = 1 failure
    slo999.request_success(9999)
    slo999.request_failure(1)

    assert not slo999.over_budget(), "Should be within budget"

    remaining_999 = slo999.remaining_budget_requests()
    assert remaining_999 == 0, f"At SLO boundary, remaining should be 0, got {remaining_999}"

    # Test 5: half budget consumed
    slo_half = SLOErrorBudget(slo_percent=99.0)

    # 1000 requests, 1% allowed = 10 allowed failures
    slo_half.request_success(995)
    slo_half.request_failure(5)

    budget_consumed_half = slo_half.error_budget_consumed_percent()
    assert budget_consumed_half == 50.0, f"Budget consumed should be 50%, got {budget_consumed_half}%"

    remaining_half = slo_half.remaining_budget_requests()
    assert remaining_half == 5, f"Should have 5 remaining failures, got {remaining_half}"

    # Test 6: zero requests
    slo_empty = SLOErrorBudget(slo_percent=99.0)

    assert slo_empty.success_rate_percent() == 100.0, "Empty SLO should show 100% success"
    assert not slo_empty.over_budget(), "Empty SLO should not be over budget"

if __name__ == "__main__":
    test_slo_error_budget()
    print("✓ slo_error_budget passed")
