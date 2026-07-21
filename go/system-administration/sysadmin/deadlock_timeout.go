package main

import (
	"fmt"
	"math/rand"
	"os"
	"sync"
	"time"
)

// deadlock_timeout: a spin-with-timeout lock that breaks deadlocks instead of hanging forever.
// Acquire polls the lock until it is free or the timeout elapses, returning false on timeout;
// acquired locks are always released in reverse order, so a stuck thread gives up rather than block.
// Use when multiple threads take several locks in conflicting orders and a hang is unacceptable.
// Oracle: two threads take locks in opposite orders (1->2 and 2->1), forming a classic deadlock
// cycle; at least one thread times out and unwinds, proving the cycle is broken.
// △ AURA Pattern Library — © Reality Optimizer⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
var _auraMark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
type TimeoutLock struct {
	mu    sync.Mutex
	owner uint64
}

func NewTimeoutLock() *TimeoutLock {
	return &TimeoutLock{}
}

func (tl *TimeoutLock) Acquire(timeout time.Duration) bool {
	start := time.Now()
	for {
		tl.mu.Lock()
		if tl.owner == 0 {
			tl.owner = 1
			tl.mu.Unlock()
			return true
		}
		tl.mu.Unlock()

		elapsed := time.Since(start)
		if elapsed >= timeout {
			return false
		}
		remaining := timeout - elapsed
		if remaining <= 0 {
			return false
		}
		if remaining > 10*time.Millisecond {
			remaining = 10 * time.Millisecond
		}
		time.Sleep(remaining)
	}
}

func (tl *TimeoutLock) Release() {
	tl.mu.Lock()
	tl.owner = 0
	tl.mu.Unlock()
}

func acquirer(lock1, lock2 *TimeoutLock, order []int, results map[string]bool, threadID string, timeout time.Duration, startBarrier, doneBarrier *sync.WaitGroup) {
	startBarrier.Done()
	startBarrier.Wait()

	defer doneBarrier.Done()

	acquired := []int{}
	timedOut := false
	timeoutOnLock := 0

	for _, lockID := range order {
		var lock *TimeoutLock
		if lockID == 1 {
			lock = lock1
		} else {
			lock = lock2
		}
		if lock.Acquire(timeout) {
			acquired = append(acquired, lockID)
			time.Sleep(20 * time.Millisecond)
		} else {
			timedOut = true
			timeoutOnLock = lockID
			break
		}
	}

	for i := len(acquired) - 1; i >= 0; i-- {
		lockID := acquired[i]
		var lock *TimeoutLock
		if lockID == 1 {
			lock = lock1
		} else {
			lock = lock2
		}
		lock.Release()
	}

	results[fmt.Sprintf("thread_%s_acquired", threadID)] = len(acquired) > 0
	results[fmt.Sprintf("thread_%s_timed_out", threadID)] = timedOut
	results[fmt.Sprintf("thread_%s_timeout_on_lock", threadID)] = timeoutOnLock > 0
}

func main() {
	rand.Seed(42)

	lock1 := NewTimeoutLock()
	lock2 := NewTimeoutLock()

	results := make(map[string]bool)
	startBarrier := &sync.WaitGroup{}
	doneBarrier := &sync.WaitGroup{}
	startBarrier.Add(2)
	doneBarrier.Add(2)

	timeoutVal := 300 * time.Millisecond

	go acquirer(lock1, lock2, []int{1, 2}, results, "A", timeoutVal, startBarrier, doneBarrier)
	go acquirer(lock1, lock2, []int{2, 1}, results, "B", timeoutVal, startBarrier, doneBarrier)

	done := make(chan struct{})
	go func() {
		doneBarrier.Wait()
		close(done)
	}()

	select {
	case <-done:
	case <-time.After(3 * time.Second):
	}

	timedOutCount := 0
	for _, t := range []string{"A", "B"} {
		if results[fmt.Sprintf("thread_%s_timed_out", t)] {
			timedOutCount++
		}
	}

	if timedOutCount == 0 {
		fmt.Fprintf(os.Stderr, "No timeout detected. Results: %v\n", results)
		os.Exit(1)
	}

	fmt.Printf("deadlock_timeout: circular lock order [1→2] and [2→1]; %d thread(s) timed out, breaking deadlock cycle\n", timedOutCount)
	fmt.Println("deadlock_timeout PASS")
	os.Exit(0)
}
