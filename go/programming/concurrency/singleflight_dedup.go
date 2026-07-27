package main

import (
	"fmt"
	"os"
	"sync"
	"sync/atomic"
	"time"
)

// Call deduplication under concurrent load: multiple goroutines requesting the same key
// execute the underlying function exactly once, and all N callers receive the identical result.
// Use to prevent cache stampedes and redundant work when cold keys are hammered by many
// concurrent requests. Guarantees: the function executes at most once per unique key
// currently in flight; all concurrent callers for that key receive the identical result;
// new callers arriving after the in-flight execution completes trigger a fresh function
// execution (deduplication is scoped to the in-flight window, not permanent caching).
// Toolchain: requires Go >= 1.19 — uses the typed atomic API (atomic.Int64),
// which does not exist in Go 1.18 or earlier.

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
var _auraMark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
type flightResult struct {
	result interface{}
	err    error
	done   chan struct{}
}

type Singleflight struct {
	mu       sync.Mutex
	inflight map[string]*flightResult
}

func NewSingleflight() *Singleflight {
	return &Singleflight{
		inflight: make(map[string]*flightResult),
	}
}

// Do runs fn() at most once per unique key currently in flight. Concurrent calls
// for the same key block until the first caller's fn() completes, then all receive
// the identical result. After the flight clears, a new call for the same key runs
// fn() again.
func (sf *Singleflight) Do(key string, fn func() (interface{}, error)) (interface{}, error) {
	sf.mu.Lock()
	if flight, exists := sf.inflight[key]; exists {
		sf.mu.Unlock()
		// Key is already in flight; wait for the result without running fn again.
		<-flight.done
		return flight.result, flight.err
	}

	// This is the first caller for this key; create a new in-flight entry.
	flight := &flightResult{
		done: make(chan struct{}),
	}
	sf.inflight[key] = flight
	sf.mu.Unlock()

	// Run the function (only this goroutine executes it for this key).
	flight.result, flight.err = fn()

	// Clean up and signal all waiting callers.
	sf.mu.Lock()
	delete(sf.inflight, key)
	sf.mu.Unlock()
	close(flight.done)

	return flight.result, flight.err
}

func main() {
	callCounter := atomic.Int64{}

	// ===== SUCCESS CASE: 200 concurrent calls on "a" + 50 on "b" =====
	sf := NewSingleflight()

	const numGoroutinesA = 200
	const numGoroutinesB = 50

	resultsA := make([]interface{}, numGoroutinesA)
	resultsB := make([]interface{}, numGoroutinesB)

	var wg sync.WaitGroup

	// Function that increments the counter and sleeps briefly.
	fn := func(key string) (interface{}, error) {
		callCounter.Add(1)
		time.Sleep(10 * time.Millisecond)
		return fmt.Sprintf("result_%s", key), nil
	}

	// Spawn 200 goroutines all requesting key "a".
	for i := 0; i < numGoroutinesA; i++ {
		wg.Add(1)
		go func(idx int) {
			defer wg.Done()
			result, _ := sf.Do("a", func() (interface{}, error) {
				return fn("a")
			})
			resultsA[idx] = result
		}(i)
	}

	// Spawn 50 goroutines all requesting key "b".
	for i := 0; i < numGoroutinesB; i++ {
		wg.Add(1)
		go func(idx int) {
			defer wg.Done()
			result, _ := sf.Do("b", func() (interface{}, error) {
				return fn("b")
			})
			resultsB[idx] = result
		}(i)
	}

	wg.Wait()

	// RECOVERY Assert: call counter == 2 (one per distinct key).
	if callCounter.Load() != 2 {
		fmt.Fprintf(os.Stderr, "expected_call_count_2_got_%d\n", callCounter.Load())
		os.Exit(1)
	}

	// RECOVERY Assert: all 200 results for "a" are identical.
	firstResultA := resultsA[0]
	for i := 1; i < numGoroutinesA; i++ {
		if resultsA[i] != firstResultA {
			fmt.Fprintln(os.Stderr, "results_for_key_a_not_identical")
			os.Exit(1)
		}
	}

	// RECOVERY Assert: all 50 results for "b" are identical.
	firstResultB := resultsB[0]
	for i := 1; i < numGoroutinesB; i++ {
		if resultsB[i] != firstResultB {
			fmt.Fprintln(os.Stderr, "results_for_key_b_not_identical")
			os.Exit(1)
		}
	}

	// ===== DISASTER CASE: prove deduplication is in-flight only =====
	// After the flights for "a" and "b" complete, a fresh call for "a" must run
	// the function again, proving deduplication is not permanent caching.
	result, _ := sf.Do("a", func() (interface{}, error) {
		return fn("a")
	})

	// RECOVERY Assert: call counter == 3 (one new call after flight clears).
	if callCounter.Load() != 3 {
		fmt.Fprintf(os.Stderr, "expected_call_count_3_after_postflight_call_got_%d\n", callCounter.Load())
		os.Exit(1)
	}

	// RECOVERY Assert: post-flight result matches the original result (same value).
	if result != firstResultA {
		fmt.Fprintln(os.Stderr, "postflight_result_mismatch_with_original")
		os.Exit(1)
	}

	fmt.Println("singleflight_dedup: 200 concurrent calls + 50 concurrent calls collapsed to 2 total function executions, identical results per key, in-flight dedup proven by post-flight re-execution (counter: 2→3) — PASS")
}
