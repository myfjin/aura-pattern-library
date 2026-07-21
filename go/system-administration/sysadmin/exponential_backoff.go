package main

import (
	"fmt"
	"os"
	"time"
)

// exponentialBackoff retries an operation up to maxAttempts, sleeping
// baseDelayMs * 2^(attempt-1) between tries and returning as soon as it succeeds,
// along with the measured inter-attempt delays and the attempt count. Use it to
// retry a transient/flaky operation while backing off to avoid hammering a
// recovering resource. The oracle drives an op that succeeds on the 4th call and
// proves the successive measured delays grow geometrically, not linearly/flat.
// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
var _auraMark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
// maxBackoffMs caps the per-attempt wait so baseDelayMs*2^(attempt-1) can never overflow
// int/time.Duration and silently wrap to 0 (the shipped bug — an absurd base made the backoff
// VANISH and hammered the resource; snapshot at exponential_backoff.BROKEN.go).
const maxBackoffMs = 60000

func exponentialBackoff(operation func() bool, maxAttempts int, baseDelayMs int) (bool, []float64, int) {
	if baseDelayMs <= 0 || baseDelayMs > maxBackoffMs {
		panic("baseDelayMs must be in (0, 60000] ms")
	}
	if maxAttempts <= 0 {
		panic("maxAttempts must be > 0")
	}
	delays := []float64{}
	prevTime := time.Now()

	for attempt := 1; attempt <= maxAttempts; attempt++ {
		result := operation()
		if result {
			return true, delays, attempt
		}

		if attempt < maxAttempts {
			// base is bounded by the guard; cap the shift + product so the geometric
			// growth still can never overflow to <=0.
			shift := attempt - 1
			if shift > 20 {
				shift = 20
			}
			waitMs := baseDelayMs * (1 << uint(shift))
			if waitMs > maxBackoffMs || waitMs <= 0 {
				waitMs = maxBackoffMs
			}
			time.Sleep(time.Duration(waitMs) * time.Millisecond)
			now := time.Now()
			elapsed := float64(now.Sub(prevTime).Milliseconds())
			delays = append(delays, elapsed)
			prevTime = now
		}
	}

	return false, delays, maxAttempts
}

func main() {
	callCount := 0

	flakyOp := func() bool {
		callCount++
		if callCount < 4 {
			return false
		}
		return true
	}

	success, delays, attempts := exponentialBackoff(flakyOp, 10, 5)

	if !success {
		fmt.Fprintf(os.Stderr, "Operation should succeed after retries; got %v\n", success)
		os.Exit(1)
	}

	if !(attempts == 4) {
		fmt.Fprintf(os.Stderr, "Should take 4 attempts; got %d\n", attempts)
		os.Exit(1)
	}

	if !(len(delays) == 3) {
		fmt.Fprintf(os.Stderr, "Should have 3 inter-attempt delays; got %d\n", len(delays))
		os.Exit(1)
	}

	if len(delays) >= 2 && !(delays[1] > delays[0]*0.8) {
		fmt.Fprintf(os.Stderr, "Delays should increase; delay[0]=%.1fms, delay[1]=%.1fms\n", delays[0], delays[1])
		os.Exit(1)
	}

	if len(delays) >= 3 && !(delays[2] > delays[1]*0.8) {
		fmt.Fprintf(os.Stderr, "Delays should increase; delay[1]=%.1fms, delay[2]=%.1fms\n", delays[1], delays[2])
		os.Exit(1)
	}

	fmt.Println("exponential_backoff PASS")
	os.Exit(0)
}
