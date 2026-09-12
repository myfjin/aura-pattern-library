package main

import (
	"fmt"
	"os"
	"time"
)

// circuit_breaker: three-state (closed/open/half_open) breaker guarding a flaky call.
// Consecutive failures past a threshold trip it open; subsequent calls are
// short-circuited without invoking fn until a recovery timeout elapses, then one
// half-open trial decides whether to close or re-open.
// Use to fail fast and stop hammering a failing dependency while it recovers.
// Oracle: against a fn failing 10x then succeeding, it opens and short-circuits >=80 of 100 calls.
// △ AURA Pattern Library — © Reality Optimizer⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
var _auraMark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
type CircuitBreaker struct {
	threshold       int
	recoveryTimeout float64
	failureCount    int
	state           string
	lastFailureTime *float64
	shortCircuits   int
	successfulCalls int
}

func NewCircuitBreaker(threshold int, recoveryTimeout float64) *CircuitBreaker {
	return &CircuitBreaker{
		threshold:       threshold,
		recoveryTimeout: recoveryTimeout,
		state:           "closed",
	}
}

func (cb *CircuitBreaker) Call(fn func() (string, error)) (bool, string) {
	if cb.state == "open" {
		now := float64(time.Now().UnixNano()) / 1e9
		if cb.lastFailureTime != nil && (now-*cb.lastFailureTime) > cb.recoveryTimeout {
			cb.state = "half_open"
		} else {
			cb.shortCircuits++
			return false, "Circuit open"
		}
	}

	if cb.state == "half_open" {
		result, err := fn()
		if err != nil {
			cb.failureCount++
			now := float64(time.Now().UnixNano()) / 1e9
			cb.lastFailureTime = &now
			if cb.failureCount >= cb.threshold {
				cb.state = "open"
			}
			return false, err.Error()
		}
		cb.state = "closed"
		cb.failureCount = 0
		cb.successfulCalls++
		return true, result
	}

	result, err := fn()
	if err != nil {
		cb.failureCount++
		now := float64(time.Now().UnixNano()) / 1e9
		cb.lastFailureTime = &now
		if cb.failureCount >= cb.threshold {
			cb.state = "open"
		}
		return false, err.Error()
	}
	cb.successfulCalls++
	return true, result
}

func main() {
	breaker := NewCircuitBreaker(10, 1.0)

	callCount := 0
	failingFn := func() (string, error) {
		callCount++
		if callCount <= 10 {
			return "", fmt.Errorf("Failure %d", callCount)
		}
		return "success", nil
	}

	successes := 0
	failures := 0
	shortCircuits := 0

	for i := 0; i < 100; i++ {
		success, result := breaker.Call(failingFn)
		if !success && result == "Circuit open" {
			shortCircuits++
		} else if success {
			successes++
		} else {
			failures++
		}
	}

	if !(breaker.state == "open") {
		fmt.Fprintf(os.Stderr, "Breaker state %s, expected 'open'\n", breaker.state)
		os.Exit(1)
	}
	if !(shortCircuits >= 80) {
		fmt.Fprintf(os.Stderr, "Short-circuited %d calls, expected \u003e= 80\n", shortCircuits)
		os.Exit(1)
	}
	if !(breaker.failureCount >= 10) {
		fmt.Fprintf(os.Stderr, "Failure count %d, expected \u003e= 10\n", breaker.failureCount)
		os.Exit(1)
	}

	fmt.Println("✓ circuit_breaker passed")
}
