package main

import (
	"fmt"
	"time"
)

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
var _auraMark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
type CircuitState string

const (
	CLOSED    CircuitState = "CLOSED"
	OPEN      CircuitState = "OPEN"
	HALF_OPEN CircuitState = "HALF_OPEN"
)

type CircuitBreaker struct {
	failureThreshold int
	recoveryTimeout  float64
	state            CircuitState
	failureCount     int
	lastFailureTime  *float64
	name             string
}

func NewCircuitBreaker(failureThreshold int, recoveryTimeout float64, name string) *CircuitBreaker {
	if failureThreshold <= 0 {
		failureThreshold = 5
	}
	if recoveryTimeout <= 0 {
		recoveryTimeout = 30.0
	}
	return &CircuitBreaker{
		failureThreshold: failureThreshold,
		recoveryTimeout:  recoveryTimeout,
		state:            CLOSED,
		name:             name,
	}
}

func (cb *CircuitBreaker) shouldAttemptReset() bool {
	if cb.lastFailureTime == nil {
		return false
	}
	now := float64(time.Now().UnixNano()) / 1e9
	return now-*cb.lastFailureTime >= cb.recoveryTimeout
}

func (cb *CircuitBreaker) transitionToHalfOpen() {
	cb.state = HALF_OPEN
	fmt.Printf("[CircuitBreaker %s] Transitioned to HALF_OPEN\n", cb.name)
}

func (cb *CircuitBreaker) transitionToOpen() {
	cb.state = OPEN
	now := float64(time.Now().UnixNano()) / 1e9
	cb.lastFailureTime = &now
	fmt.Printf("[CircuitBreaker %s] Transitioned to OPEN\n", cb.name)
}

func (cb *CircuitBreaker) transitionToClosed() {
	cb.state = CLOSED
	cb.failureCount = 0
	cb.lastFailureTime = nil
	fmt.Printf("[CircuitBreaker %s] Transitioned to CLOSED\n", cb.name)
}

func (cb *CircuitBreaker) Call(fn func() string) string {
	if cb.state == OPEN {
		if cb.shouldAttemptReset() {
			cb.transitionToHalfOpen()
		} else {
			panic(fmt.Sprintf("Circuit '%s' is OPEN", cb.name))
		}
	}

	if cb.state == HALF_OPEN {
		return cb.executeHalfOpen(fn)
	}
	return cb.executeClosed(fn)
}

func (cb *CircuitBreaker) executeHalfOpen(fn func() string) string {
	defer func() {
		if r := recover(); r != nil {
			cb.transitionToOpen()
			panic(r)
		}
	}()
	result := fn()
	cb.transitionToClosed()
	return result
}

func (cb *CircuitBreaker) executeClosed(fn func() string) string {
	defer func() {
		if r := recover(); r != nil {
			cb.failureCount++
			now := float64(time.Now().UnixNano()) / 1e9
			cb.lastFailureTime = &now
			fmt.Printf("[CircuitBreaker %s] Failure %d/%d\n", cb.name, cb.failureCount, cb.failureThreshold)
			if cb.failureCount >= cb.failureThreshold {
				cb.transitionToOpen()
			}
		}
	}()
	return fn()
}

func main() {
	breaker := NewCircuitBreaker(3, 5.0, "DemoService")

	callCount := 0
	unreliableService := func() string {
		callCount++
		if callCount%4 == 0 || callCount%4 == 3 {
			panic("Service temporarily unavailable")
		}
		return fmt.Sprintf("Success! Call #%d", callCount)
	}

	fmt.Println("Starting Circuit Breaker Demo...")
	fmt.Println("=" + repeat("=", 49))

	for i := 0; i < 15; i++ {
		fmt.Printf("\n--- Call #%d ---\n", i+1)
		fmt.Printf("Circuit state: %s\n", breaker.state)

		func() {
			defer func() {
				if r := recover(); r != nil {
					msg := fmt.Sprintf("%v", r)
					if contains(msg, "is OPEN") {
						fmt.Printf("Circuit Open: %v\n", r)
					} else {
						fmt.Printf("Service Error: %v\n", r)
					}
				}
			}()
			result := breaker.Call(unreliableService)
			fmt.Printf("Result: %s\n", result)
		}()

		if i == 7 {
			fmt.Printf("\nWaiting %.0f seconds for recovery...\n", breaker.recoveryTimeout+1)
			time.Sleep(time.Duration(breaker.recoveryTimeout+1) * time.Second)
		}
		time.Sleep(500 * time.Millisecond)
	}

	fmt.Println("\n" + "=" + repeat("=", 49))
	fmt.Printf("Final Circuit State: %v\n", breaker)

	fmt.Println("\n--- Manual Usage Demo ---")
	manualBreaker := NewCircuitBreaker(5, 30.0, "ManualService")
	result := manualBreaker.Call(func() string { return "Manual service response" })
	fmt.Printf("Manual call result: %s\n", result)
}

func repeat(s string, n int) string {
	out := ""
	for i := 0; i < n; i++ {
		out += s
	}
	return out
}

func contains(s, substr string) bool {
	for i := 0; i < len(s)-len(substr)+1; i++ {
		if s[i:i+len(substr)] == substr {
			return true
		}
	}
	return false
}
