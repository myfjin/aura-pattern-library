package main

import (
	"errors"
	"fmt"
	"os"
	"sync"
	"time"
)

// SemaphorePool manages a fixed number of permits.
// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
var _auraMark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
type SemaphorePool struct {
	permits   int
	semaphore chan struct{}
	mu        sync.Mutex
	acquired  int
}

// NewSemaphorePool creates a pool with the given number of permits.
func NewSemaphorePool(permits int) (*SemaphorePool, error) {
	if permits <= 0 {
		return nil, errors.New("permits must be positive")
	}
	return &SemaphorePool{
		permits:   permits,
		semaphore: make(chan struct{}, permits),
	}, nil
}

// Permits returns the total number of permits.
func (p *SemaphorePool) Permits() int {
	return p.permits
}

// AvailablePermits returns the number of currently available permits.
func (p *SemaphorePool) AvailablePermits() int {
	p.mu.Lock()
	defer p.mu.Unlock()
	return p.permits - p.acquired
}

// Acquire tries to take a permit with an optional timeout.
func (p *SemaphorePool) Acquire(timeout time.Duration) bool {
	if timeout <= 0 {
		select {
		case p.semaphore <- struct{}{}:
			p.mu.Lock()
			p.acquired++
			p.mu.Unlock()
			return true
		default:
			return false
		}
	}
	select {
	case p.semaphore <- struct{}{}:
		p.mu.Lock()
		p.acquired++
		p.mu.Unlock()
		return true
	case <-time.After(timeout):
		return false
	}
}

// Release returns a permit to the pool.
func (p *SemaphorePool) Release() {
	p.mu.Lock()
	if p.acquired > 0 {
		p.acquired--
	}
	p.mu.Unlock()
	select {
	case <-p.semaphore:
	default:
	}
}

// Bulkhead limits concurrent access to a resource.
type Bulkhead struct {
	name             string
	semaphorePool    *SemaphorePool
	mu               sync.Mutex
	totalRequests    int
	rejectedRequests int
}

// NewBulkhead creates a bulkhead with the given concurrency limit.
func NewBulkhead(name string, maxConcurrent int) (*Bulkhead, error) {
	pool, err := NewSemaphorePool(maxConcurrent)
	if err != nil {
		return nil, err
	}
	return &Bulkhead{
		name:          name,
		semaphorePool: pool,
	}, nil
}

// MaxConcurrent returns the maximum concurrent operations allowed.
func (b *Bulkhead) MaxConcurrent() int {
	return b.semaphorePool.Permits()
}

// AvailableConcurrent returns the number of available slots.
func (b *Bulkhead) AvailableConcurrent() int {
	return b.semaphorePool.AvailablePermits()
}

// TotalRequests returns the total number of requests processed.
func (b *Bulkhead) TotalRequests() int {
	b.mu.Lock()
	defer b.mu.Unlock()
	return b.totalRequests
}

// RejectedRequests returns the number of rejected requests.
func (b *Bulkhead) RejectedRequests() int {
	b.mu.Lock()
	defer b.mu.Unlock()
	return b.rejectedRequests
}

// Execute runs a function within the bulkhead isolation.
func (b *Bulkhead) Execute(
	fn func() (interface{}, error),
	timeout time.Duration,
	fallback func() (interface{}, error),
) (interface{}, error) {
	b.mu.Lock()
	b.totalRequests++
	b.mu.Unlock()

	if !b.semaphorePool.Acquire(timeout) {
		b.mu.Lock()
		b.rejectedRequests++
		b.mu.Unlock()
		if fallback != nil {
			return fallback()
		}
		return nil, errors.New("bulkhead timeout acquiring permit")
	}

	defer b.semaphorePool.Release()
	return fn()
}

// IsolatedExecutor manages multiple named bulkheads.
type IsolatedExecutor struct {
	mu        sync.Mutex
	bulkheads map[string]*Bulkhead
}

// NewIsolatedExecutor creates an executor.
func NewIsolatedExecutor() *IsolatedExecutor {
	return &IsolatedExecutor{
		bulkheads: make(map[string]*Bulkhead),
	}
}

// CreateBulkhead registers a new bulkhead.
func (e *IsolatedExecutor) CreateBulkhead(name string, maxConcurrent int) (*Bulkhead, error) {
	e.mu.Lock()
	defer e.mu.Unlock()
	if _, exists := e.bulkheads[name]; exists {
		return nil, fmt.Errorf("bulkhead '%s' already exists", name)
	}
	bulkhead, err := NewBulkhead(name, maxConcurrent)
	if err != nil {
		return nil, err
	}
	e.bulkheads[name] = bulkhead
	return bulkhead, nil
}

// GetBulkhead returns an existing bulkhead or nil.
func (e *IsolatedExecutor) GetBulkhead(name string) *Bulkhead {
	e.mu.Lock()
	defer e.mu.Unlock()
	return e.bulkheads[name]
}

// RemoveBulkhead removes a bulkhead.
func (e *IsolatedExecutor) RemoveBulkhead(name string) bool {
	e.mu.Lock()
	defer e.mu.Unlock()
	if _, exists := e.bulkheads[name]; exists {
		delete(e.bulkheads, name)
		return true
	}
	return false
}

// BulkheadStats returns statistics for all bulkheads.
func (e *IsolatedExecutor) BulkheadStats() map[string]map[string]int {
	e.mu.Lock()
	defer e.mu.Unlock()
	stats := make(map[string]map[string]int)
	for name, b := range e.bulkheads {
		stats[name] = map[string]int{
			"max_concurrent":       b.MaxConcurrent(),
			"available_concurrent": b.AvailableConcurrent(),
			"total_requests":       b.TotalRequests(),
			"rejected_requests":    b.RejectedRequests(),
		}
	}
	return stats
}

func demoWorkerTask(taskID int, duration time.Duration) (interface{}, error) {
	time.Sleep(duration)
	return fmt.Sprintf("Task %d completed", taskID), nil
}

func demoFallback() (interface{}, error) {
	return "FALLBACK_EXECUTED", nil
}

func main() {
	fmt.Println("Bulkhead Pattern Isolator Demo")
	fmt.Println("===============================")

	executor := NewIsolatedExecutor()
	apiBulkhead, err := executor.CreateBulkhead("api", 3)
	if !(err == nil) {
		fmt.Fprintf(os.Stderr, "create api bulkhead: %v\n", err)
		os.Exit(1)
	}
	dbBulkhead, err := executor.CreateBulkhead("database", 2)
	if !(err == nil) {
		fmt.Fprintf(os.Stderr, "create db bulkhead: %v\n", err)
		os.Exit(1)
	}

	fmt.Printf("Created bulkhead 'api' with max concurrent: %d\n", apiBulkhead.MaxConcurrent())
	fmt.Printf("Created bulkhead 'database' with max concurrent: %d\n", dbBulkhead.MaxConcurrent())
	fmt.Println()

	fmt.Println("Submitting 5 tasks to API bulkhead (capacity 3)...")
	var apiWg sync.WaitGroup
	for i := 0; i < 5; i++ {
		apiWg.Add(1)
		go func(id int) {
			defer apiWg.Done()
			_, _ = apiBulkhead.Execute(
				func() (interface{}, error) { return demoWorkerTask(id, 200*time.Millisecond) },
				0,
				demoFallback,
			)
		}(i)
	}

	fmt.Println("Submitting 4 tasks to database bulkhead (capacity 2)...")
	var dbWg sync.WaitGroup
	for i := 0; i < 4; i++ {
		dbWg.Add(1)
		go func(id int) {
			defer dbWg.Done()
			_, _ = dbBulkhead.Execute(
				func() (interface{}, error) { return demoWorkerTask(id+100, 300*time.Millisecond) },
				0,
				demoFallback,
			)
		}(i)
	}

	apiWg.Wait()
	dbWg.Wait()

	fmt.Println("\nFinal Statistics:")
	fmt.Println("-----------------")
	for name, bulkheadStats := range executor.BulkheadStats() {
		fmt.Printf("Bulkhead '%s':\n", name)
		for statName, value := range bulkheadStats {
			fmt.Printf("  %s: %d\n", statName, value)
		}
		fmt.Println()
	}

	fmt.Println("Testing timeout behavior...")
	// Fill the API bulkhead with long tasks.
	var blockWg sync.WaitGroup
	for i := 0; i < 3; i++ {
		blockWg.Add(1)
		go func(id int) {
			defer blockWg.Done()
			_, _ = apiBulkhead.Execute(
				func() (interface{}, error) { return demoWorkerTask(id, 5*time.Second) },
				0,
				nil,
			)
		}(i)
	}
	time.Sleep(50 * time.Millisecond)
	res, err := apiBulkhead.Execute(
		func() (interface{}, error) { return demoWorkerTask(999, 100*time.Millisecond) },
		100*time.Millisecond,
		demoFallback,
	)
	if err != nil {
		fmt.Printf("Timeout error as expected: %v\n", err)
	} else {
		fmt.Printf("Timeout test result: %v\n", res)
	}
	blockWg.Wait()

	fmt.Println("\nDemo completed successfully!")
}
