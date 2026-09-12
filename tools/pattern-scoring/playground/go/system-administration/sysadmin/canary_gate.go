package main

import (
	"fmt"
	"os"
)

// CanaryGate gradually shifts traffic to a new version and rolls back if the
// error rate exceeds a threshold.
// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
var _auraMark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
type CanaryGate struct {
	ErrorThreshold float64
	CanaryTraffic  float64
	canaryErrors   int
	canaryTotal    int
	stableErrors   int
	stableTotal    int
}

// NewCanaryGate creates a gate with the given error-rate threshold.
func NewCanaryGate(errorThreshold float64) *CanaryGate {
	return &CanaryGate{ErrorThreshold: errorThreshold}
}

// IncreaseCanaryTraffic raises the canary traffic percentage by percent (capped at 100).
func (g *CanaryGate) IncreaseCanaryTraffic(percent float64) {
	g.CanaryTraffic += percent
	if g.CanaryTraffic > 100.0 {
		g.CanaryTraffic = 100.0
	}
}

// RecordCanaryRequest records a canary result (success == true means no error).
func (g *CanaryGate) RecordCanaryRequest(success bool) {
	g.canaryTotal++
	if !success {
		g.canaryErrors++
	}
}

// RecordStableRequest records a stable-version result.
func (g *CanaryGate) RecordStableRequest(success bool) {
	g.stableTotal++
	if !success {
		g.stableErrors++
	}
}

// GetCanaryErrorRate returns the current canary error rate.
func (g *CanaryGate) GetCanaryErrorRate() float64 {
	if g.canaryTotal == 0 {
		return 0.0
	}
	return float64(g.canaryErrors) / float64(g.canaryTotal)
}

// IsHealthy reports whether the canary error rate is within the threshold.
func (g *CanaryGate) IsHealthy() bool {
	return g.GetCanaryErrorRate() <= g.ErrorThreshold
}

// ShouldRollback returns true when the error rate exceeds the threshold.
func (g *CanaryGate) ShouldRollback() bool {
	return !g.IsHealthy()
}

// ResetCanaryTraffic resets canary traffic to zero (manual rollback action).
func (g *CanaryGate) ResetCanaryTraffic() {
	g.CanaryTraffic = 0.0
}

func assertf(cond bool, format string, args ...interface{}) {
	if !cond {
		fmt.Fprintf(os.Stderr, format+"\n", args...)
		os.Exit(1)
	}
}

func main() {
	// test_canary_starts_at_zero
	gate := NewCanaryGate(0.05)
	assertf(gate.CanaryTraffic == 0.0, "canary should start at zero traffic")

	// test_increase_canary_traffic
	gate2 := NewCanaryGate(0.05)
	gate2.IncreaseCanaryTraffic(10.0)
	assertf(gate2.CanaryTraffic == 10.0, "expected 10.0, got %f", gate2.CanaryTraffic)
	gate2.IncreaseCanaryTraffic(20.0)
	assertf(gate2.CanaryTraffic == 30.0, "expected 30.0, got %f", gate2.CanaryTraffic)
	gate2.IncreaseCanaryTraffic(100.0)
	assertf(gate2.CanaryTraffic == 100.0, "expected cap at 100.0, got %f", gate2.CanaryTraffic)

	// test_healthy_canary_continues
	gate3 := NewCanaryGate(0.05)
	gate3.IncreaseCanaryTraffic(50.0)
	for i := 0; i < 100; i++ {
		gate3.RecordCanaryRequest(i != 50)
	}
	assertf(gate3.GetCanaryErrorRate() == 0.01, "expected 0.01, got %f", gate3.GetCanaryErrorRate())
	assertf(gate3.IsHealthy(), "1%% error rate should be healthy")
	assertf(!gate3.ShouldRollback(), "should not rollback")

	// test_unhealthy_canary_triggers_rollback
	gate4 := NewCanaryGate(0.05)
	gate4.IncreaseCanaryTraffic(50.0)
	for i := 0; i < 100; i++ {
		gate4.RecordCanaryRequest(i >= 10)
	}
	errorRate := gate4.GetCanaryErrorRate()
	assertf(errorRate == 0.1, "expected 0.1, got %f", errorRate)
	assertf(!gate4.IsHealthy(), "error rate 10%% should be unhealthy")
	assertf(gate4.ShouldRollback(), "should trigger rollback")

	// test_error_rate_at_threshold
	gate5 := NewCanaryGate(0.05)
	gate5.IncreaseCanaryTraffic(50.0)
	for i := 0; i < 100; i++ {
		gate5.RecordCanaryRequest(i >= 5)
	}
	assertf(gate5.GetCanaryErrorRate() == 0.05, "expected 0.05, got %f", gate5.GetCanaryErrorRate())
	assertf(gate5.IsHealthy(), "at threshold should pass")

	// test_rollback_clears_canary
	gate6 := NewCanaryGate(0.05)
	gate6.IncreaseCanaryTraffic(50.0)
	for i := 0; i < 100; i++ {
		gate6.RecordCanaryRequest(false)
	}
	assertf(gate6.ShouldRollback(), "should rollback")
	gate6.ResetCanaryTraffic()
	assertf(gate6.CanaryTraffic == 0.0, "canary traffic should be reset")

	// test_gradual_ramp_up
	gate7 := NewCanaryGate(0.02)
	gate7.IncreaseCanaryTraffic(50.0)
	for i := 0; i < 100; i++ {
		gate7.RecordCanaryRequest(true)
	}
	for i := 0; i < 100; i++ {
		gate7.RecordCanaryRequest(i >= 10)
	}
	assertf(gate7.GetCanaryErrorRate() > 0.02, "expected error rate > 0.02, got %f", gate7.GetCanaryErrorRate())
	assertf(gate7.ShouldRollback(), "should detect error spike")

	fmt.Println("✓ canary_gate passed")
}
