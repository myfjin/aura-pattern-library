package main

import (
	"fmt"
	"os"
	"sync"
	"time"
)

// Circuit breaker: wraps calls with stateful failure detection. CLOSED lets calls
// through and counts failures; at the threshold it trips OPEN and short-circuits
// (failing fast without calling); after a recovery timeout it goes HALF_OPEN to probe,
// closing on success or re-opening on failure. Use to stop hammering a failing
// dependency. Guarantees (self-test): 3 failures trip OPEN, OPEN never invokes the
// service, half-open success closes+resets while failure re-opens, call counts exact.
// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
var _auraMark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
type circuitState string

const (
	closed   circuitState = "CLOSED"
	open     circuitState = "OPEN"
	halfOpen circuitState = "HALF_OPEN"
)

type connectionError struct {
	msg string
}

func (e *connectionError) Error() string { return e.msg }

type typeError struct {
	msg string
}

func (e *typeError) Error() string { return e.msg }

// circuitBreaker prevents cascading failures by wrapping calls with stateful
// failure detection. It mirrors the Python implementation: CLOSED allows calls,
// OPEN short-circuits them, and HALF_OPEN probes recovery.
type circuitBreaker struct {
	failureThreshold int
	recoveryTimeout  float64
	expectedError    func(error) bool
	name             string

	state           circuitState
	failureCount    int
	lastFailureTime *float64
	mu              sync.Mutex
	now             func() float64
}

func newCircuitBreaker(threshold int, recovery float64, name string) *circuitBreaker {
	return &circuitBreaker{
		failureThreshold: threshold,
		recoveryTimeout:  recovery,
		expectedError:    func(err error) bool { return err != nil },
		name:             name,
		state:            closed,
		now:              func() float64 { return float64(time.Now().UnixNano()) / 1e9 },
	}
}

func (cb *circuitBreaker) call(fn func() (string, error)) (string, error) {
	cb.mu.Lock()
	defer cb.mu.Unlock()

	if cb.state == open {
		if cb.shouldAttemptReset() {
			cb.transitionToHalfOpen()
		} else {
			return "", fmt.Errorf("circuit '%s' is OPEN", cb.name)
		}
	}

	if cb.state == halfOpen {
		return cb.executeHalfOpen(fn)
	}
	return cb.executeClosed(fn)
}

func (cb *circuitBreaker) shouldAttemptReset() bool {
	if cb.lastFailureTime == nil {
		return false
	}
	return cb.now()-*cb.lastFailureTime >= cb.recoveryTimeout
}

func (cb *circuitBreaker) transitionToHalfOpen() {
	cb.state = halfOpen
	fmt.Printf("[CircuitBreaker %s] Transitioned to HALF_OPEN\n", cb.name)
}

func (cb *circuitBreaker) transitionToOpen() {
	cb.state = open
	now := cb.now()
	cb.lastFailureTime = &now
	fmt.Printf("[CircuitBreaker %s] Transitioned to OPEN\n", cb.name)
}

func (cb *circuitBreaker) transitionToClosed() {
	cb.state = closed
	cb.failureCount = 0
	cb.lastFailureTime = nil
	fmt.Printf("[CircuitBreaker %s] Transitioned to CLOSED\n", cb.name)
}

func (cb *circuitBreaker) executeClosed(fn func() (string, error)) (string, error) {
	result, err := fn()
	if err != nil {
		if cb.expectedError(err) {
			cb.handleFailure()
		}
		return "", err
	}
	// A success in CLOSED resets the failure run — the threshold counts CONSECUTIVE
	// failures, not cumulative-forever. Without this reset a 50%-healthy service tripped
	// permanently OPEN (the shipped bug; snapshot at circuit_breaker.BROKEN.go).
	cb.failureCount = 0
	return result, nil
}

func (cb *circuitBreaker) executeHalfOpen(fn func() (string, error)) (string, error) {
	result, err := fn()
	if err != nil {
		if cb.expectedError(err) {
			cb.transitionToOpen()
		}
		return "", err
	}
	cb.transitionToClosed()
	return result, nil
}

func (cb *circuitBreaker) handleFailure() {
	cb.failureCount++
	now := cb.now()
	cb.lastFailureTime = &now
	fmt.Printf("[CircuitBreaker %s] Failure %d/%d\n", cb.name, cb.failureCount, cb.failureThreshold)
	if cb.failureCount >= cb.failureThreshold {
		cb.transitionToOpen()
	}
}

func (cb *circuitBreaker) isClosed() bool   { return cb.state == closed }
func (cb *circuitBreaker) isOpen() bool     { return cb.state == open }
func (cb *circuitBreaker) isHalfOpen() bool { return cb.state == halfOpen }
func (cb *circuitBreaker) String() string {
	return fmt.Sprintf("CircuitBreaker(name=%s, state=%s, failures=%d/%d)",
		cb.name, cb.state, cb.failureCount, cb.failureThreshold)
}

func main() {
	// Self-test on a fake clock: full lifecycle CLOSED→OPEN→HALF_OPEN→
	// (CLOSED on success | OPEN on failure), fail-fast without calling.
	now := 40000.0
	clock := func() float64 { return now }

	breaker := &circuitBreaker{
		failureThreshold: 3,
		recoveryTimeout:  5.0,
		expectedError:    func(err error) bool { return err != nil },
		name:             "test",
		state:            closed,
		now:              clock,
	}

	calls := 0
	service := func(fail bool) (string, error) {
		calls++
		if fail {
			return "", &connectionError{msg: "down"}
		}
		return "ok", nil
	}

	// CLOSED: successes flow through, failures count.
	result, err := breaker.call(func() (string, error) { return service(false) })
	if !(result == "ok" && breaker.isClosed()) {
		fmt.Fprintf(os.Stderr, "expected ok and closed, got %q, closed=%v, err=%v\n", result, breaker.isClosed(), err)
		os.Exit(1)
	}
	for i := 0; i < 3; i++ {
		_, _ = breaker.call(func() (string, error) { return service(true) })
	}
	if !(breaker.state == open) {
		fmt.Fprintf(os.Stderr, "3 failures at threshold 3 must OPEN, state %s\n", breaker.state)
		os.Exit(1)
	}
	if !(breaker.failureCount == 3) {
		fmt.Fprintf(os.Stderr, "expected 3 failures, got %d\n", breaker.failureCount)
		os.Exit(1)
	}

	// OPEN: fail-fast — the service is NOT called.
	before := calls
	_, err = breaker.call(func() (string, error) { return service(false) })
	if err == nil {
		fmt.Fprintln(os.Stderr, "OPEN breaker executed the call")
		os.Exit(1)
	}
	if !(calls == before) {
		fmt.Fprintf(os.Stderr, "OPEN breaker still invoked the service: calls %d vs before %d\n", calls, before)
		os.Exit(1)
	}

	// HALF_OPEN after recovery timeout; a FAILURE re-opens immediately.
	now += 5.1
	_, _ = breaker.call(func() (string, error) { return service(true) })
	if !(breaker.state == open) { // 5.1s elapsed
		fmt.Fprintln(os.Stderr, "failed half-open probe must re-OPEN")
		os.Exit(1)
	}

	// HALF_OPEN again; a SUCCESS closes and resets the failure count.
	now += 5.1
	result, err = breaker.call(func() (string, error) { return service(false) })
	if !(result == "ok") {
		fmt.Fprintf(os.Stderr, "expected ok from half-open success, got %q, err=%v\n", result, err)
		os.Exit(1)
	}
	if !(breaker.state == closed) { // 5.1s elapsed
		fmt.Fprintln(os.Stderr, "successful half-open probe must CLOSE")
		os.Exit(1)
	}
	if !(breaker.failureCount == 0) {
		fmt.Fprintf(os.Stderr, "failure count must reset on close, got %d\n", breaker.failureCount)
		os.Exit(1)
	}

	// After closing, the breaker needs a fresh threshold of failures.
	for i := 0; i < 2; i++ {
		_, _ = breaker.call(func() (string, error) { return service(true) })
	}
	if !(breaker.state == closed) { // 2 failures below threshold
		fmt.Fprintln(os.Stderr, "breaker opened below the threshold after reset")
		os.Exit(1)
	}
	if !(calls == 8) {
		fmt.Fprintf(os.Stderr, "service must have run exactly 8 times, ran %d\n", calls)
		os.Exit(1)
	}

	// Unexpected exception types pass through without tripping the breaker.
	plain := &circuitBreaker{
		failureThreshold: 1,
		recoveryTimeout:  30.0,
		expectedError:    func(err error) bool { _, ok := err.(*connectionError); return ok },
		name:             "default",
		state:            closed,
		now:              clock,
	}
	_, _ = plain.call(func() (string, error) { return "", &typeError{msg: "not counted"} })
	if !(plain.state == closed) {
		fmt.Fprintf(os.Stderr, "non-expected exception tripped the breaker, state %s\n", plain.state)
		os.Exit(1)
	}

	fmt.Println("circuit_breaker: 3 fails→OPEN, fail-fast verified (no call), " +
		"half-open fail re-OPENs / success CLOSES+resets, 8 calls exact — PASS")
}
