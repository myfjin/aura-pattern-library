# CARD: deadline_ttl (GO batch 1 — compact format)
FILE: go/system-administration/sysadmin/deadline_ttl.go
BASELINE (verified 2026-07-21): ✓ deadline_ttl passed
ENTRY: NewDeadlineChecker(clockFn) · SetDeadline/IsExpired/Remaining · demo starts line 37
RUN: `cd playground/go && go run system-administration/sysadmin/deadline_ttl.go`
PASTES: compile-verified in scratch 2026-07-21 — every attack runs and lands as predicted.
RESET: `git checkout pristine-full -- system-administration/sysadmin/deadline_ttl.go`

PASTE-ATTACKS — one at a time, just above the final print (line 99);
run · read against the three-way rule · reset · next.
1. ```go
	z := 0.0
	nanD := checker.SetDeadline(z / z)
	fmt.Println("NaN ttl -> expired:", checker.IsExpired(nanD), "remaining:", checker.Remaining(nanD))
   ```
   NaN TTL — E008: `clock >= NaN` is ALWAYS false in float-land → my prediction: an
   IMMORTAL LEASE (never expires, remaining NaN, no error). Does a lease that can
   never expire count as silent-wrong for TTL logic? Your call.
2. ```go
	negD := checker.SetDeadline(-50.0)
	fmt.Println("neg ttl -> expired:", checker.IsExpired(negD), "remaining:", checker.Remaining(negD))
   ```
   negative TTL — B5: born-expired. Defensible IF declared (nothing declares it);
   the question is whether callers passing a computed-negative TTL get told.
3. ```go
	inf := 1.0
	infD := checker.SetDeadline(inf / z)   // needs z from attack 1, or use 1e308*10
	fmt.Println("+Inf ttl -> expired:", checker.IsExpired(infD))
   ```
   +Inf TTL — boundary: never-expires might be a FEATURE (no deadline) or a hole.

FREE-PLAY: after the paste-attacks, 1-2 shots of YOUR OWN — your garbage, not mine.
Go note: unused variables are compile errors — print everything you create.
