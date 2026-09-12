# CARD: circuit_breaker (GO batch 1 — compact format)
FILE: go/programming/resilience/circuit_breaker.go
BASELINE (verified 2026-07-21): circuit_breaker ... 8 calls exact — PASS
ENTRY: circuitBreaker struct · call(fn) line 66 · demo (fake clock) line 151
RUN: `cd playground/go && go run programming/resilience/circuit_breaker.go`
PASTES: compile-verified in scratch 2026-07-21 — every attack runs and lands as predicted.
RESET: `git checkout pristine-full -- programming/resilience/circuit_breaker.go`
CLAIM UNDER TEST: "3 failures trip OPEN; OPEN never invokes the service"

PASTE-ATTACKS — one at a time, just above the final print (line 257).
`clock`, `now` and `connectionError` are in scope there.
1. ```go
	mix := &circuitBreaker{failureThreshold: 3, recoveryTimeout: 5.0,
		expectedError: func(err error) bool { return err != nil },
		name: "mix", state: closed, now: clock}
	fail := func() (string, error) { return "", &connectionError{msg: "x"} }
	okf := func() (string, error) { return "ok", nil }
	_, _ = mix.call(fail); _, _ = mix.call(okf); _, _ = mix.call(fail)
	_, _ = mix.call(okf); _, _ = mix.call(fail)
	fmt.Println("fail,ok,fail,ok,fail ->", mix.state, "count:", mix.failureCount)
   ```
   THE DEEP ONE — R13 state-sequence: success in CLOSED never resets failureCount
   (executeClosed line 110 has no reset; only transitionToClosed does). My prediction:
   OPEN after 3 NON-consecutive failures across a 40%-failure flaky service. Is the
   contract "3 failures" cumulative-forever or consecutive? Industry breakers say
   consecutive (or windowed). Your ruling decides kill vs flag.
2. ```go
	hot := &circuitBreaker{failureThreshold: 1, recoveryTimeout: -1.0,
		expectedError: func(err error) bool { return err != nil },
		name: "hot", state: closed, now: clock}
	svcCalls := 0
	dead := func() (string, error) { svcCalls++; return "", &connectionError{msg: "x"} }
	for i := 0; i < 5; i++ { _, _ = hot.call(dead) }
	fmt.Println("neg timeout -> state:", hot.state, "service invoked:", svcCalls, "of 5")
   ```
   B5 negative recoveryTimeout — shouldAttemptReset is instantly true forever → every
   "OPEN" call goes half-open and INVOKES the dead service. My prediction: 5/5 invoked —
   "OPEN never invokes the service" silently false from one config typo. No guard.
3. ```go
	stuck := &circuitBreaker{failureThreshold: 1, recoveryTimeout: 5.0,
		expectedError: func(err error) bool { _, ok := err.(*connectionError); return ok },
		name: "stuck", state: halfOpen, now: clock}
	_, _ = stuck.call(func() (string, error) { return "", &typeError{msg: "odd"} })
	fmt.Println("unexpected err in HALF_OPEN ->", stuck.state)
   ```
   boundary — an UNEXPECTED error type during half-open probe: executeHalfOpen line 121
   neither re-opens nor closes → parked in HALF_OPEN, probing (invoking!) on every call
   while the storm lasts. Declared nowhere.

FREE-PLAY: your garbage after mine — threshold 0 and threshold -1 constructions are
untouched; nothing validates them.
