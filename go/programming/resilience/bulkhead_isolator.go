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
// A zero or negative timeout means try once without blocking.
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

// Name returns the bulkhead identifier.
func (b *Bulkhead) Name() string {
	return b.name
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
// If acquisition fails and a fallback is provided, it runs the fallback.
// Otherwise it returns a timeout error.
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
		return nil, fmt.Errorf("bulkhead %s timeout acquiring permit", b.name)
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

// futureResult carries the outcome of a submitted task.
type futureResult struct {
	value interface{}
	err   error
}

// Submit runs a task asynchronously inside the named bulkhead and returns a channel
// that yields exactly one result. The returned channel is buffered so the goroutine
// does not block after the receiver stops reading, and it is closed after the result
// is delivered.
func (e *IsolatedExecutor) Submit(
	bulkheadName string,
	fn func() (interface{}, error),
	timeout time.Duration,
	fallback func() (interface{}, error),
) <-chan futureResult {
	ch := make(chan futureResult, 1)
	go func() {
		bulkhead := e.GetBulkhead(bulkheadName)
		if bulkhead == nil {
			ch <- futureResult{nil, fmt.Errorf("bulkhead '%s' not found", bulkheadName)}
			close(ch)
			return
		}
		value, err := bulkhead.Execute(fn, timeout, fallback)
		ch <- futureResult{value, err}
		close(ch)
	}()
	return ch
}

// readFutureResult blocks until the future channel delivers a result.
func readFutureResult(ch <-chan futureResult, timeout time.Duration) (interface{}, error) {
	select {
	case res := <-ch:
		return res.value, res.err
	case <-time.After(timeout):
		return nil, errors.New("future result timeout")
	}
}

func tracked(kind string, duration time.Duration, meter map[string]int, meterLock *sync.Mutex) func() (interface{}, error) {
	return func() (interface{}, error) {
		meterLock.Lock()
		meter[kind]++
		if meter[kind] > meter[kind+"_max"] {
			meter[kind+"_max"] = meter[kind]
		}
		meterLock.Unlock()
		time.Sleep(duration)
		meterLock.Lock()
		meter[kind]--
		meterLock.Unlock()
		return kind + "-done", nil
	}
}

func holderFunc(hold chan struct{}) func() (interface{}, error) {
	return func() (interface{}, error) {
		select {
		case <-hold:
			return "held", nil
		case <-time.After(3 * time.Second):
			return "held", nil
		}
	}
}

func assert(cond bool, format string, args ...interface{}) {
	if !cond {
		fmt.Fprintf(os.Stderr, format+"\n", args...)
		os.Exit(1)
	}
}

func main() {
	executor := NewIsolatedExecutor()
	api, err := executor.CreateBulkhead("api", 3)
	assert(err == nil, "create api bulkhead: %v", err)
	_, err = executor.CreateBulkhead("database", 2)
	assert(err == nil, "create database bulkhead: %v", err)

	meter := map[string]int{"api": 0, "api_max": 0, "db": 0, "db_max": 0}
	var meterLock sync.Mutex

	// Oracle uses a 5.0s timeout for task acquisition and future result waits.
	resultTimeout := 5 * time.Second
	if !(resultTimeout >= 5*time.Second) {
		fmt.Fprintf(os.Stderr, "result timeout must be at least 5s\n")
		os.Exit(1)
	}

	// 6 api tasks (cap 3) + 4 db tasks (cap 2). Generous 5s timeout so all run eventually;
	// the CEILING is what we assert.
	var apiFutures []<-chan futureResult
	var dbFutures []<-chan futureResult
	for i := 0; i < 6; i++ {
		apiFutures = append(apiFutures, executor.Submit("api", tracked("api", 100*time.Millisecond, meter, &meterLock), resultTimeout, nil))
	}
	for i := 0; i < 4; i++ {
		dbFutures = append(dbFutures, executor.Submit("database", tracked("db", 100*time.Millisecond, meter, &meterLock), resultTimeout, nil))
	}

	results := make([]string, 0, 10)
	for _, f := range apiFutures {
		v, err := readFutureResult(f, resultTimeout)
		assert(err == nil, "api task error: %v", err)
		results = append(results, v.(string))
	}
	for _, f := range dbFutures {
		v, err := readFutureResult(f, resultTimeout)
		assert(err == nil, "db task error: %v", err)
		results = append(results, v.(string))
	}

	assert(count(results, "api-done") == 6, "all api tasks must complete: %v", results)
	assert(count(results, "db-done") == 4, "all db tasks must complete: %v", results)
	assert(meter["api_max"] <= 3, "api bulkhead (cap 3) reached %d concurrent", meter["api_max"])
	assert(meter["db_max"] <= 2, "db bulkhead (cap 2) reached %d concurrent — ISOLATION BROKEN", meter["db_max"])
	assert(meter["api_max"] >= 2, "api tasks never actually overlapped (test too weak)")

	stats := executor.BulkheadStats()
	assert(stats["api"]["total_requests"] == 6, "api stats: %v", stats["api"])
	assert(stats["database"]["total_requests"] == 4, "db stats: %v", stats["database"])
	assert(stats["api"]["rejected_requests"] == 0, "api rejected: %v", stats["api"])

	// SATURATION: hold all 3 api permits, then a 50ms-timeout call must take the fallback.
	hold := make(chan struct{})
	holders := make([]<-chan futureResult, 3)
	for i := 0; i < 3; i++ {
		holders[i] = executor.Submit("api", holderFunc(hold), 5*time.Second, nil)
	}
	time.Sleep(200 * time.Millisecond) // let the holders occupy the permits

	result, err := api.Execute(
		func() (interface{}, error) { return "should not run", nil },
		50*time.Millisecond,
		func() (interface{}, error) { return "FALLBACK", nil },
	)
	assert(err == nil, "saturated execute should not error: %v", err)
	assert(result == "FALLBACK", "saturated bulkhead must fall back, got %q", result)
	assert(executor.BulkheadStats()["api"]["rejected_requests"] == 1, "rejection not counted")

	close(hold)
	for i, h := range holders {
		v, err := readFutureResult(h, 5*time.Second)
		assert(err == nil, "holder %d error: %v", i, err)
		assert(v == "held", "holder %d result: %v", i, v)
	}

	// Unknown bulkhead refused; duplicate creation refused.
	ch := executor.Submit("ghost", func() (interface{}, error) { return nil, nil }, 0, nil)
	_, err = readFutureResult(ch, 1*time.Second)
	assert(err != nil, "unknown bulkhead accepted")

	_, err = executor.CreateBulkhead("api", 3)
	assert(err != nil, "duplicate bulkhead accepted")

	fmt.Printf("bulkhead_isolator: ceilings held (api %d<=3, db %d<=2), 10/10 completed, saturation -> fallback + rejection counted -- PASS\n",
		meter["api_max"], meter["db_max"])
}

func count(slice []string, target string) int {
	c := 0
	for _, s := range slice {
		if s == target {
			c++
		}
	}
	return c
}
