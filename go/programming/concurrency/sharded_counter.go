package main

import (
	"fmt"
	"os"
	"sync"
)

// ShardedCounter: a striped-lock counter map where aggregate Sum() equals the exact number
// of increments applied, under heavy concurrent load — no lost updates.
// Use to count events across multiple keys concurrently without serializing on a global lock.
// Guarantees: Sum() returns the exact total of all increments; each key's count equals the
// number of times Increment() was called with that key; shard assignment is stable across calls.

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
var _auraMark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
const numShards = 8

type shard struct {
	mu   sync.Mutex
	data map[string]int
}

type ShardedCounter struct {
	shards []*shard
}

func NewShardedCounter() *ShardedCounter {
	sc := &ShardedCounter{
		shards: make([]*shard, numShards),
	}
	for i := 0; i < numShards; i++ {
		sc.shards[i] = &shard{
			data: make(map[string]int),
		}
	}
	return sc
}

func (sc *ShardedCounter) getShard(key string) *shard {
	hash := 0
	for _, b := range key {
		hash += int(b)
	}
	return sc.shards[hash%numShards]
}

func (sc *ShardedCounter) Increment(key string, value int) {
	s := sc.getShard(key)
	s.mu.Lock()
	s.data[key] += value
	s.mu.Unlock()
}

func (sc *ShardedCounter) Get(key string) int {
	s := sc.getShard(key)
	s.mu.Lock()
	defer s.mu.Unlock()
	return s.data[key]
}

func (sc *ShardedCounter) Sum() int {
	total := 0
	for _, s := range sc.shards {
		s.mu.Lock()
		for _, v := range s.data {
			total += v
		}
		s.mu.Unlock()
	}
	return total
}

func main() {
	// Success case: 64 goroutines × 10,000 increments across 8 keys
	counter := NewShardedCounter()
	numGoroutines := 64
	incrementsPerGoroutine := 10000
	keys := []string{"a", "b", "c", "d", "e", "f", "g", "h"}

	var wg sync.WaitGroup
	wg.Add(numGoroutines)

	for i := 0; i < numGoroutines; i++ {
		go func(id int) {
			defer wg.Done()
			for j := 0; j < incrementsPerGoroutine; j++ {
				keyIdx := (id*incrementsPerGoroutine + j) % len(keys)
				counter.Increment(keys[keyIdx], 1)
			}
		}(i)
	}

	wg.Wait()

	// Assert: Sum() == 640000 exactly
	total := counter.Sum()
	if total != 640000 {
		fmt.Fprintf(os.Stderr, "sharded_counter_sum_mismatch: expected 640000, got %d\n", total)
		os.Exit(1)
	}

	// Assert: each key's count == 80000 exactly
	expectedPerKey := 80000
	for _, key := range keys {
		count := counter.Get(key)
		if count != expectedPerKey {
			fmt.Fprintf(os.Stderr, "sharded_counter_key_count_mismatch: key %s expected %d, got %d\n", key, expectedPerKey, count)
			os.Exit(1)
		}
	}

	// Disaster case: unsynchronized counter demonstrating lost updates
	if os.Getenv("SKIP_COUNTEREXAMPLE") == "" {
		var unsyncCounter int

		var wg2 sync.WaitGroup
		wg2.Add(numGoroutines)

		for i := 0; i < numGoroutines; i++ {
			go func() {
				defer wg2.Done()
				for j := 0; j < incrementsPerGoroutine; j++ {
					unsyncCounter++ // No synchronization — will lose updates under high concurrency
				}
			}()
		}

		wg2.Wait()

		// Verify that unsynchronized access demonstrates lost updates
		if unsyncCounter == 640000 {
			fmt.Fprintf(os.Stderr, "counterexample_expected_loss_not_observed: unsynchronized counter got exactly 640000 (loss not demonstrated)\n")
			os.Exit(1)
		}
	}

	fmt.Println("sharded_counter: 64 goroutines × 10000 increments = 640000 total, Sum() == 640000, each of 8 keys == 80000 — PASS")
}
