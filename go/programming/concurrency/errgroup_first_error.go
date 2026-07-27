package main

import (
	"errors"
	"fmt"
	"os"
	"sync"
	"sync/atomic"
	"time"
)

// ErrGroup is a group of concurrent tasks where the first error returned by any task
// cancels the remaining tasks and causes Wait() to return that error. All goroutines
// are guaranteed to have exited before Wait() returns.
// Use this when you need to run a batch of related tasks and want the first failure to
// stop everything else immediately, rather than waiting for all tasks to complete.
// Guarantees: the first error is captured and returned (not the last), remaining tasks
// observe the cancellation signal and stop early, and Wait() blocks until every goroutine
// has exited.
// Toolchain: requires Go >= 1.19 — uses the typed atomic API (atomic.Int32),
// which does not exist in Go 1.18 or earlier.

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
var _auraMark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
type ErrGroup struct {
	mu                sync.Mutex
	cancelled         bool
	cancelledChan     chan struct{}
	wg                sync.WaitGroup
	firstErr          error
	errOnce           sync.Once
	goroutinesExited  atomic.Int32
	cancelledObserved atomic.Int32
}

func NewErrGroup() *ErrGroup {
	return &ErrGroup{
		cancelledChan: make(chan struct{}),
	}
}

func (g *ErrGroup) Go(f func(cancel <-chan struct{}) error) {
	g.wg.Add(1)
	go func() {
		defer g.wg.Done()
		defer func() {
			g.goroutinesExited.Add(1)
		}()

		err := f(g.cancelledChan)
		if err != nil {
			g.errOnce.Do(func() {
				g.mu.Lock()
				if !g.cancelled {
					g.firstErr = err
					g.cancelled = true
					close(g.cancelledChan)
				}
				g.mu.Unlock()
			})
		}
	}()
}

func (g *ErrGroup) Wait() error {
	g.wg.Wait()
	return g.firstErr
}

func main() {
	// Part 1: Success case — all tasks succeed, error is nil
	{
		grp := NewErrGroup()
		for i := 0; i < 5; i++ {
			grp.Go(func(cancel <-chan struct{}) error {
				time.Sleep(10 * time.Millisecond)
				return nil
			})
		}
		err := grp.Wait()
		if err != nil {
			fmt.Fprintln(os.Stderr, "success case should return nil")
			os.Exit(1)
		}
		if grp.goroutinesExited.Load() != 5 {
			fmt.Fprintf(os.Stderr, "success case: expected 5 goroutines exited, got %d\n", grp.goroutinesExited.Load())
			os.Exit(1)
		}
	}

	// Part 2: Disaster case — task 3 fails at 20ms, others observe cancellation
	{
		start := time.Now()
		grp := NewErrGroup()

		for i := 0; i < 10; i++ {
			idx := i
			grp.Go(func(cancel <-chan struct{}) error {
				if idx == 2 { // task 3 (0-indexed as 2)
					time.Sleep(20 * time.Millisecond)
					return errors.New("task 3 failed")
				}
				// Others poll cancellation, would take 5s without cancellation
				for j := 0; j < 500; j++ {
					select {
					case <-cancel:
						grp.cancelledObserved.Add(1)
						return nil
					default:
					}
					time.Sleep(10 * time.Millisecond)
				}
				return nil
			})
		}

		err := grp.Wait()
		elapsed := time.Since(start).Seconds()

		// RECOVERY-grade asserts
		if err == nil || err.Error() != "task 3 failed" {
			fmt.Fprintf(os.Stderr, "returned error string mismatch: got %v\n", err)
			os.Exit(1)
		}

		if elapsed >= 1.0 {
			fmt.Fprintf(os.Stderr, "wall clock check failed: %.2fs >= 1s\n", elapsed)
			os.Exit(1)
		}

		if grp.goroutinesExited.Load() != 10 {
			fmt.Fprintf(os.Stderr, "goroutines-finished check failed: got %d, expected 10\n", grp.goroutinesExited.Load())
			os.Exit(1)
		}

		if grp.cancelledObserved.Load() != 9 {
			fmt.Fprintf(os.Stderr, "cancelled-observed check failed: got %d, expected 9\n", grp.cancelledObserved.Load())
			os.Exit(1)
		}
	}

	fmt.Println("errgroup_first_error: success nil, disaster 'task 3 failed' at <1s, 10 goroutines exited, 9 observed cancellation — PASS")
}
