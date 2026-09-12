# CARD: exponential_backoff (GO batch 1 — compact format)
FILE: go/system-administration/sysadmin/exponential_backoff.go
BASELINE (verified 2026-07-21): exponential_backoff PASS
ENTRY: exponentialBackoff(operation, maxAttempts, baseDelayMs) · line 18 · demo line 41
RUN: `cd playground/go && go run system-administration/sysadmin/exponential_backoff.go`
PASTES: compile-verified in scratch 2026-07-21 — every attack runs and lands as predicted.
RESET: `git checkout pristine-full -- system-administration/sysadmin/exponential_backoff.go`

PASTE-ATTACKS — one at a time, just above `fmt.Println("exponential_backoff PASS")` (line 79).
1. ```go
	ok2, d2, n2 := exponentialBackoff(func() bool { return false }, 3, 1<<62)
	fmt.Println("overflow base:", ok2, d2, n2)
   ```
   int overflow — the go-native kill class: waitMs = base×2^(attempt-1) silently wraps;
   1<<62 ms × time.Millisecond = EXACTLY 0 in Duration arithmetic. My prediction: returns
   INSTANTLY with ~0ms delays where the contract implies centuries of backoff. The backoff
   silently VANISHES — a recovering resource gets hammered at full speed.
2. ```go
	ok3, d3, n3 := exponentialBackoff(func() bool { return false }, 3, -10)
	fmt.Println("neg base:", ok3, d3, n3)
   ```
   negative baseDelay — B5: Sleep(negative) returns immediately → same silent no-backoff,
   reachable from a plain config typo. No guard, no error.
3. ```go
	ok4, d4, n4 := exponentialBackoff(func() bool { return true }, 0, 5)
	fmt.Println("zero attempts:", ok4, d4, n4)
   ```
   maxAttempts=0 — E009 degenerate: loop never runs → returns (false, [], 0). An op that
   would succeed reports failure-in-0-attempts. Declared anywhere? No.

THREE-WAY-RULE NOTE: the self-test measures delays with `delays[1] > delays[0]*0.8` —
0.8× tolerance means "growing" barely; also delays include the OPERATION's own runtime
(measured wall-clock between attempts, not the sleep itself). Flag-grade observation.

FREE-PLAY: your garbage after mine. Attacks on the flakyOp initializer are no-ops —
attack the exponentialBackoff CALL with hostile parameters.
