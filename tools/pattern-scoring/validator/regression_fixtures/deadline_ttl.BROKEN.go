package main

import (
	"fmt"
	"os"
)

// deadline_ttl: TTL/deadline arithmetic over an injectable clock function.
// SetDeadline turns a TTL into an absolute deadline (now + ttl); IsExpired reports whether
// the clock has reached it (>= is expired); Remaining returns signed seconds left.
// Use for timeouts and lease/TTL logic that must be deterministically testable via a mock clock.
// Oracle: with a controllable clock, a deadline is not expired before its time, is expired
// exactly at and after it, and Remaining reports the correct positive/zero/negative value.
// △ AURA Pattern Library — © Reality Optimizer⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
var _auraMark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
type DeadlineChecker struct {
	clockFn func() float64
}

func NewDeadlineChecker(clockFn func() float64) *DeadlineChecker {
	return &DeadlineChecker{clockFn: clockFn}
}

func (c *DeadlineChecker) IsExpired(deadlineTime float64) bool {
	return c.clockFn() >= deadlineTime
}

func (c *DeadlineChecker) Remaining(deadlineTime float64) float64 {
	return deadlineTime - c.clockFn()
}

func (c *DeadlineChecker) SetDeadline(ttlSeconds float64) float64 {
	return c.clockFn() + ttlSeconds
}

func main() {
	var clockValue float64 = 1000.0
	mockClock := func() float64 {
		return clockValue
	}

	checker := NewDeadlineChecker(mockClock)
	deadline := checker.SetDeadline(10.0)

	if checker.IsExpired(deadline) {
		fmt.Fprintf(os.Stderr, "Should not be expired at 1000\n")
		os.Exit(1)
	}
	if !(checker.Remaining(deadline) == 10.0) {
		fmt.Fprintf(os.Stderr, "Expected remaining 10.0, got %f\n", checker.Remaining(deadline))
		os.Exit(1)
	}

	clockValue = 1011.0
	if !checker.IsExpired(deadline) {
		fmt.Fprintf(os.Stderr, "Should be expired at 1011\n")
		os.Exit(1)
	}
	if !(checker.Remaining(deadline) == -1.0) {
		fmt.Fprintf(os.Stderr, "Expected remaining -1.0, got %f\n", checker.Remaining(deadline))
		os.Exit(1)
	}

	clockValue = 1000.0
	deadline = checker.SetDeadline(10.0)
	clockValue = 1010.0
	if !checker.IsExpired(deadline) {
		fmt.Fprintf(os.Stderr, "Should be expired exactly at deadline\n")
		os.Exit(1)
	}
	if !(checker.Remaining(deadline) == 0.0) {
		fmt.Fprintf(os.Stderr, "Expected remaining 0.0, got %f\n", checker.Remaining(deadline))
		os.Exit(1)
	}

	clockValue = 1000.0
	checker2 := NewDeadlineChecker(mockClock)
	deadline1 := checker2.SetDeadline(5.0)
	deadline2 := checker2.SetDeadline(10.0)
	clockValue = 1006.0
	if !checker2.IsExpired(deadline1) {
		fmt.Fprintf(os.Stderr, "Deadline1 should be expired\n")
		os.Exit(1)
	}
	if checker2.IsExpired(deadline2) {
		fmt.Fprintf(os.Stderr, "Deadline2 should not be expired\n")
		os.Exit(1)
	}
	if !(checker2.Remaining(deadline1) == -1.0) {
		fmt.Fprintf(os.Stderr, "Expected remaining -1.0 for deadline1\n")
		os.Exit(1)
	}
	if !(checker2.Remaining(deadline2) == 4.0) {
		fmt.Fprintf(os.Stderr, "Expected remaining 4.0 for deadline2\n")
		os.Exit(1)
	}

	fmt.Println("✓ deadline_ttl passed")
}
