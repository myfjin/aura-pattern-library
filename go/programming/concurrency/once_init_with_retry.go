package main

import (
	"fmt"
	"os"
	"sync"
	"sync/atomic"
)

// Lazy initialization that caches only successful results, retries after failures.
// Unlike sync.Once which caches a failed initialization permanently, this pattern
// lets the next caller retry after a transient failure. Guarantees at most one
// concurrent initialization attempt at any moment.
// Use when one-time initialization may fail transiently and later callers should
// have a chance to retry (e.g., connecting to a dependency that might be temporarily down).
// Guarantees: at most one initialization attempt runs at a time; only successful
// results are cached forever; after success, the cached result is always returned;
// failed attempts allow retry by the next caller; all concurrent callers waiting
// for the same initialization observe the final result atomically.

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
var _auraMark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
type OnceInitWithRetry struct {
	mu       sync.Mutex
	cond     *sync.Cond
	result   interface{}
	err      error
	success  bool
	inFlight bool

	// Observability: total attempts started and peak concurrent depth
	attempts              int32
	concurrent            int32
	maxObservedConcurrent int32
}

func NewOnceInitWithRetry() *OnceInitWithRetry {
	o := &OnceInitWithRetry{}
	o.cond = sync.NewCond(&o.mu)
	return o
}

func (o *OnceInitWithRetry) Do(fn func() (interface{}, error)) (interface{}, error) {
	o.mu.Lock()
	defer o.mu.Unlock()

	// Loop until we either have a successful result or successfully claim the attempt lock.
	for {
		// If we already have a successful result, return it.
		if o.success {
			return o.result, nil
		}

		// If no attempt is in flight, we can start one.
		if !o.inFlight {
			o.inFlight = true
			atomic.AddInt32(&o.attempts, 1)
			break  // Exit loop to run the attempt
		}

		// An attempt is in flight; wait for it to complete.
		o.cond.Wait()
		// Loop back to re-check the condition (success or not, inFlight or not)
	}

	// Run the attempt outside the lock.
	o.mu.Unlock()

	// Track concurrent execution depth.
	conc := atomic.AddInt32(&o.concurrent, 1)
	for {
		curr := atomic.LoadInt32(&o.maxObservedConcurrent)
		if conc <= curr {
			break
		}
		if atomic.CompareAndSwapInt32(&o.maxObservedConcurrent, curr, conc) {
			break
		}
	}

	result, err := fn()

	atomic.AddInt32(&o.concurrent, -1)

	// Re-acquire the lock to finalize the attempt.
	o.mu.Lock()

	if err == nil {
		o.success = true
		o.result = result
	} else {
		o.err = err
	}

	o.inFlight = false
	o.cond.Broadcast()

	if err == nil {
		return result, nil
	}
	return nil, err
}

func (o *OnceInitWithRetry) Stats() (totalAttempts, maxConc int32) {
	return atomic.LoadInt32(&o.attempts), atomic.LoadInt32(&o.maxObservedConcurrent)
}

func main() {
	// Part 1: Success case - init succeeds on first attempt
	{
		var successfulInits int32
		o1 := NewOnceInitWithRetry()

		initFn1 := func() (interface{}, error) {
			atomic.AddInt32(&successfulInits, 1)
			return "success", nil
		}

		var wg sync.WaitGroup
		var results [100]interface{}
		var errors [100]error
		for i := 0; i < 100; i++ {
			wg.Add(1)
			go func(idx int) {
				defer wg.Done()
				results[idx], errors[idx] = o1.Do(initFn1)
			}(i)
		}
		wg.Wait()

		// Assert 1: successful inits == 1 exactly
		if atomic.LoadInt32(&successfulInits) != 1 {
			fmt.Fprintf(os.Stderr, "part 1 assert 1: successful inits expected 1, got %d\n", atomic.LoadInt32(&successfulInits))
			os.Exit(1)
		}

		// Assert 3: max concurrent depth == 1 exactly
		_, maxConc := o1.Stats()
		if maxConc != 1 {
			fmt.Fprintf(os.Stderr, "part 1 assert 3: max concurrent depth expected 1, got %d\n", maxConc)
			os.Exit(1)
		}

		// Assert 4: identical pointer for all non-nil results (must be exactly 1 distinct pointer)
		distinctPointers := make(map[interface{}]bool)
		for i := 0; i < 100; i++ {
			if errors[i] != nil {
				fmt.Fprintf(os.Stderr, "part 1 assert 4: caller %d got unexpected error: %v\n", i, errors[i])
				os.Exit(1)
			}
			if results[i] == nil {
				fmt.Fprintf(os.Stderr, "part 1 assert 4: caller %d got nil result\n", i)
				os.Exit(1)
			}
			distinctPointers[results[i]] = true
		}
		if len(distinctPointers) != 1 {
			fmt.Fprintf(os.Stderr, "part 1 assert 4: expected 1 distinct pointer, got %d\n", len(distinctPointers))
			os.Exit(1)
		}

		// Assert 6: no torn results (every caller must have either (result, nil) or (nil, error))
		tornCount := 0
		for i := 0; i < 100; i++ {
			hasResult := results[i] != nil
			hasError := errors[i] != nil
			if (hasResult && hasError) || (!hasResult && !hasError) {
				tornCount++
			}
		}
		if tornCount != 0 {
			fmt.Fprintf(os.Stderr, "part 1 assert 6: torn results count expected 0, got %d\n", tornCount)
			os.Exit(1)
		}

		fmt.Println("part 1 success: successful_inits=1, max_concurrent_attempts=1, distinct_pointers=1, torn_results=0 — PASS")
	}

	// Part 2: Disaster case - first two attempts fail, concurrent callers per wave
	{
		var attemptCounter int32
		var successCount int32
		var failureCount int32
		o2 := NewOnceInitWithRetry()

		initFn2 := func() (interface{}, error) {
			current := atomic.AddInt32(&attemptCounter, 1)
			if current <= 2 {
				atomic.AddInt32(&failureCount, 1)
				return nil, fmt.Errorf("transient failure")
			}
			atomic.AddInt32(&successCount, 1)
			return "recovered", nil
		}

		// Wave 1: 100 concurrent callers
		var wg sync.WaitGroup
		var wave1Results [100]interface{}
		var wave1Errors [100]error
		for i := 0; i < 100; i++ {
			wg.Add(1)
			go func(idx int) {
				defer wg.Done()
				wave1Results[idx], wave1Errors[idx] = o2.Do(initFn2)
			}(i)
		}
		wg.Wait()

		// Wave 2: 100 concurrent callers
		var wave2Results [100]interface{}
		var wave2Errors [100]error
		for i := 0; i < 100; i++ {
			wg.Add(1)
			go func(idx int) {
				defer wg.Done()
				wave2Results[idx], wave2Errors[idx] = o2.Do(initFn2)
			}(i)
		}
		wg.Wait()

		// Wave 3: 100 concurrent callers (may include successful results)
		var wave3Results [100]interface{}
		var wave3Errors [100]error
		for i := 0; i < 100; i++ {
			wg.Add(1)
			go func(idx int) {
				defer wg.Done()
				wave3Results[idx], wave3Errors[idx] = o2.Do(initFn2)
			}(i)
		}
		wg.Wait()

		attempts, maxConc := o2.Stats()
		successes := atomic.LoadInt32(&successCount)
		failures := atomic.LoadInt32(&failureCount)

		// Assert 2: attempts == failures + successes exactly (every attempt outcome was recorded)
		if attempts != failures+successes {
			fmt.Fprintf(os.Stderr, "part 2 assert 2: attempts (%d) must equal failures (%d) + successes (%d) = %d\n", attempts, failures, successes, failures+successes)
			os.Exit(1)
		}

		// Assert 1: successful inits == 1 exactly
		if successes != 1 {
			fmt.Fprintf(os.Stderr, "part 2 assert 1: successful inits expected 1, got %d\n", successes)
			os.Exit(1)
		}

		// Assert 3: max concurrent depth == 1 exactly
		if maxConc != 1 {
			fmt.Fprintf(os.Stderr, "part 2 assert 3: max concurrent depth expected 1, got %d\n", maxConc)
			os.Exit(1)
		}

		// Assert 6: no torn results across all waves
		allResults := append(append(wave1Results[:], wave2Results[:]...), wave3Results[:]...)
		allErrors := append(append(wave1Errors[:], wave2Errors[:]...), wave3Errors[:]...)
		tornCount := 0
		for i := 0; i < 300; i++ {
			hasResult := allResults[i] != nil
			hasError := allErrors[i] != nil
			if (hasResult && hasError) || (!hasResult && !hasError) {
				tornCount++
			}
		}
		if tornCount != 0 {
			fmt.Fprintf(os.Stderr, "part 2 assert 6: torn results count expected 0, got %d\n", tornCount)
			os.Exit(1)
		}

		// Assert 4: all non-nil results must be identical pointer (count of distinct non-nil pointers == 1)
		successPointers := make(map[interface{}]bool)
		for i := 0; i < 300; i++ {
			if allResults[i] != nil {
				successPointers[allResults[i]] = true
			}
		}
		if len(successPointers) != 1 {
			fmt.Fprintf(os.Stderr, "part 2 assert 4: distinct success pointers expected exactly 1, got %d\n", len(successPointers))
			os.Exit(1)
		}

		// Assert 5: after first success, 100 more concurrent calls add zero attempts
		attemptsBeforeCachedWave := atomic.LoadInt32(&o2.attempts)
		var cachedWaveResults [100]interface{}
		var cachedWaveErrors [100]error
		for i := 0; i < 100; i++ {
			wg.Add(1)
			go func(idx int) {
				defer wg.Done()
				cachedWaveResults[idx], cachedWaveErrors[idx] = o2.Do(initFn2)
			}(i)
		}
		wg.Wait()
		attemptsAfterCachedWave := atomic.LoadInt32(&o2.attempts)

		if attemptsBeforeCachedWave != attemptsAfterCachedWave {
			fmt.Fprintf(os.Stderr, "part 2 assert 5: cached wave should add 0 attempts, added %d\n", attemptsAfterCachedWave-attemptsBeforeCachedWave)
			os.Exit(1)
		}

		// Assert 4 (cached wave): every one of the 100 post-success callers must receive the
		// SAME instance the earlier waves saw — a cache that hands out a fresh instance would
		// satisfy "zero new attempts" and still be broken.
		cachedDistinct := 0
		for i := 0; i < 100; i++ {
			if cachedWaveErrors[i] != nil || cachedWaveResults[i] == nil {
				fmt.Fprintf(os.Stderr, "part 2 assert 4b: cached caller %d got err=%v result=%v, expected the cached instance\n", i, cachedWaveErrors[i], cachedWaveResults[i])
				os.Exit(1)
			}
			if !successPointers[cachedWaveResults[i]] {
				cachedDistinct++
			}
		}
		if cachedDistinct != 0 {
			fmt.Fprintf(os.Stderr, "part 2 assert 4b: %d cached callers received an instance other than the one initialized\n", cachedDistinct)
			os.Exit(1)
		}

		fmt.Printf("part 2 disaster: attempts=%d (failures=%d + successes=%d), max_concurrent_attempts=1, distinct_pointers=%d, torn_results=0, cached_wave_zero_attempts=true — PASS\n", attempts, failures, successes, len(successPointers))
	}

	fmt.Println("once_init_with_retry: successes=1, attempts=failures+successes, max_concurrent_attempts=1, all_success_pointers_identical, torn_results=0, cached_wave_zero_new_attempts — PASS")
}
