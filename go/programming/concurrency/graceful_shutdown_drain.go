package main

import (
	"fmt"
	"os"
	"sync"
	"sync/atomic"
	"time"
)

// Graceful shutdown of a worker pool: accepts jobs into a queue, but on Shutdown
// closes the queue to new submissions while draining all accepted-but-unprocessed jobs,
// guaranteeing every accepted job is completed before Shutdown returns.
// Use when a pool of worker goroutines must drain queued work on exit, avoiding job loss
// and the panic from closing a channel under active senders.
// Guarantees: after Shutdown, completed jobs == accepted jobs (no loss, no work left),
// and no goroutine panics with "send on closed channel" even if producers race shutdown.
// Toolchain: requires Go >= 1.19 — uses the typed atomic API (atomic.Bool, atomic.Int64),
// which does not exist in Go 1.18 or earlier.

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
var _auraMark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
type Job struct {
	id int
}

type WorkerPool struct {
	jobs         chan Job
	numWorkers   int
	shutdownOnce sync.Once
	shuttingDown atomic.Bool
	submitMu     sync.Mutex
	accepted     atomic.Int64
	completed    atomic.Int64
	workersExited atomic.Int64
	wg           sync.WaitGroup
}

func NewWorkerPool(numWorkers int, queueSize int) *WorkerPool {
	wp := &WorkerPool{
		jobs:       make(chan Job, queueSize),
		numWorkers: numWorkers,
	}
	// Start workers
	for i := 0; i < numWorkers; i++ {
		wp.wg.Add(1)
		go wp.worker()
	}
	return wp
}

func (wp *WorkerPool) worker() {
	defer func() {
		wp.workersExited.Add(1)
		wp.wg.Done()
	}()
	for range wp.jobs {
		// Process the job (minimal work)
		time.Sleep(1 * time.Millisecond)
		wp.completed.Add(1)
	}
}

func (wp *WorkerPool) Submit(job Job) bool {
	wp.submitMu.Lock()
	defer wp.submitMu.Unlock()

	// If shutdown has started, reject immediately
	if wp.shuttingDown.Load() {
		return false
	}

	// Try to send the job; if queue is full, reject
	select {
	case wp.jobs <- job:
		wp.accepted.Add(1)
		return true
	default:
		return false
	}
}

func (wp *WorkerPool) Shutdown() {
	wp.shutdownOnce.Do(func() {
		// Acquire submitMu to block new submissions
		wp.submitMu.Lock()
		wp.shuttingDown.Store(true)
		wp.submitMu.Unlock()

		// Give brief moment for in-flight submits to complete
		time.Sleep(10 * time.Millisecond)

		// Close channel so workers drain and exit
		close(wp.jobs)

		// Wait for all workers to finish
		wp.wg.Wait()
	})
}

func main() {
	var part1Accepted, part1Completed int64
	var part2Accepted, part2Completed, part2Rejected, part2Submitted int64

	// Part 1: Simple success case
	{
		wp := NewWorkerPool(4, 100)

		// Submit 100 jobs sequentially
		for i := 0; i < 100; i++ {
			ok := wp.Submit(Job{id: i})
			if !ok {
				fmt.Fprintf(os.Stderr, "submit failed unexpectedly at job %d\n", i)
				os.Exit(1)
			}
		}

		// Verify acceptance count
		part1Accepted = wp.accepted.Load()
		if part1Accepted != 100 {
			fmt.Fprintf(os.Stderr, "expected 100 accepted, got %d\n", part1Accepted)
			os.Exit(1)
		}

		// Shut down gracefully
		wp.Shutdown()

		// Verify all accepted jobs were completed
		part1Completed = wp.completed.Load()
		if part1Completed != 100 {
			fmt.Fprintf(os.Stderr, "expected 100 completed, got %d\n", part1Completed)
			os.Exit(1)
		}

		// Verify all workers exited
		if wp.workersExited.Load() != 4 {
			fmt.Fprintf(os.Stderr, "expected 4 workers exited (part 1), got %d\n", wp.workersExited.Load())
			os.Exit(1)
		}
	}

	// Part 2: Disaster case—shutdown while producer submits continuously
	{
		wp := NewWorkerPool(4, 50)

		rejectedCount := atomic.Int64{}
		attemptedCount := atomic.Int64{}
		producerDone := sync.WaitGroup{}
		producerDone.Add(1)
		part2Submitted = 500

		// Producer goroutine submitting 500 jobs
		go func() {
			defer producerDone.Done()
			for i := 0; i < 500; i++ {
				if !wp.Submit(Job{id: i}) {
					rejectedCount.Add(1)
				}
				attemptedCount.Add(1)
				time.Sleep(50 * time.Microsecond)
			}
		}()

		// Let some jobs get queued and processed
		time.Sleep(50 * time.Millisecond)

		// Trigger shutdown mid-flight (producer still running)
		wp.Shutdown()

		// Wait for producer goroutine to finish all 500 submission attempts
		producerDone.Wait()

		part2Attempted := attemptedCount.Load()
		part2Accepted = wp.accepted.Load()
		part2Completed = wp.completed.Load()
		part2Rejected = rejectedCount.Load()
		workers := wp.workersExited.Load()

		// Assertion 1: completed == accepted (no job loss)
		if part2Completed != part2Accepted {
			fmt.Fprintf(os.Stderr, "completed (%d) != accepted (%d)\n", part2Completed, part2Accepted)
			os.Exit(1)
		}

		// Assertion 2a: attempted submissions == 500 (producer ran to completion)
		if part2Attempted != 500 {
			fmt.Fprintf(os.Stderr, "attempted (%d) != 500\n", part2Attempted)
			os.Exit(1)
		}

		// Assertion 2b: accepted + rejected == attempted (all attempts accounted for)
		if part2Accepted+part2Rejected != part2Attempted {
			fmt.Fprintf(os.Stderr, "accepted+rejected (%d+%d=%d) != attempted (%d)\n", part2Accepted, part2Rejected, part2Accepted+part2Rejected, part2Attempted)
			os.Exit(1)
		}

		// Assertion 3: rejected > 0 (shutdown really refused new work)
		if part2Rejected <= 0 {
			fmt.Fprintf(os.Stderr, "expected rejected > 0, got %d\n", part2Rejected)
			os.Exit(1)
		}

		// Assertion 4: all 4 workers exited
		if workers != 4 {
			fmt.Fprintf(os.Stderr, "expected 4 workers exited (part 2), got %d\n", workers)
			os.Exit(1)
		}
	}

	fmt.Printf("%d accepted→%d completed (success), %d→%d accepted+%d completed+%d rejected (disaster), 8 workers exited — PASS\n",
		part1Accepted, part1Completed, part2Submitted, part2Accepted, part2Completed, part2Rejected)
}
