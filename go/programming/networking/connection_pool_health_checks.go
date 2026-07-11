package main

import (
	"fmt"
	"os"
	"sync"
	"time"
)

// Connection abstracts a database-style connection.
// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
var _auraMark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
type Connection interface {
	Execute(query string) string
	IsValid() bool
	Close()
	GetID() int
	GetLastUsed() time.Time
	SetActive(bool)
}

// MockDatabaseConnection is a concrete connection for self-testing.
type MockDatabaseConnection struct {
	connectionID int
	createdAt    time.Time
	lastUsed     time.Time
	isActive     bool
	isClosed     bool
}

func NewMockDatabaseConnection(id int) *MockDatabaseConnection {
	now := time.Now()
	return &MockDatabaseConnection{
		connectionID: id,
		createdAt:    now,
		lastUsed:     now,
		isActive:     true,
		isClosed:     false,
	}
}

func (m *MockDatabaseConnection) Execute(query string) string {
	if m.isClosed {
		panic("Connection is closed")
	}
	m.lastUsed = time.Now()
	time.Sleep(10 * time.Millisecond)
	return fmt.Sprintf("Executed: %s", query)
}

func (m *MockDatabaseConnection) IsValid() bool {
	return !m.isClosed && m.isActive
}

func (m *MockDatabaseConnection) Close() {
	m.isClosed = true
}

func (m *MockDatabaseConnection) GetID() int {
	return m.connectionID
}

func (m *MockDatabaseConnection) GetLastUsed() time.Time {
	return m.lastUsed
}

func (m *MockDatabaseConnection) SetActive(active bool) {
	m.isActive = active
}

// PooledConnection wraps a connection with borrowing metadata.
type PooledConnection struct {
	connection *MockDatabaseConnection
	borrowedAt *time.Time
	borrowedBy int
}

func NewPooledConnection(connection *MockDatabaseConnection) *PooledConnection {
	return &PooledConnection{
		connection: connection,
		borrowedBy: -1,
	}
}

func (p *PooledConnection) Borrow() {
	now := time.Now()
	p.borrowedAt = &now
}

func (p *PooledConnection) Release() {
	p.borrowedAt = nil
	p.borrowedBy = -1
}

func (p *PooledConnection) IsBorrowed() bool {
	return p.borrowedAt != nil
}

func (p *PooledConnection) GetConnection() *MockDatabaseConnection {
	return p.connection
}

// ConnectionPool manages a pool of connections with background health checks.
type ConnectionPool struct {
	maxConnections      int
	validationQuery     string
	connectionFactory   func() *MockDatabaseConnection
	healthCheckInterval time.Duration
	maxIdleTime         time.Duration
	available           []*PooledConnection
	active              map[*PooledConnection]bool
	mu                  sync.Mutex
	closed              bool
	connectionCounter   int
	stopHealthCheck     chan struct{}
}

func NewConnectionPool(maxConnections int, validationQuery string, connectionFactory func() *MockDatabaseConnection, healthCheckInterval, maxIdleTime time.Duration) *ConnectionPool {
	if maxConnections <= 0 {
		fmt.Fprintln(os.Stderr, "max_connections must be positive")
		os.Exit(1)
	}
	if connectionFactory == nil {
		connectionFactory = defaultConnectionFactory
	}
	pool := &ConnectionPool{
		maxConnections:      maxConnections,
		validationQuery:     validationQuery,
		connectionFactory:   connectionFactory,
		healthCheckInterval: healthCheckInterval,
		maxIdleTime:         maxIdleTime,
		available:           make([]*PooledConnection, 0),
		active:              make(map[*PooledConnection]bool),
		stopHealthCheck:     make(chan struct{}),
	}
	pool.initializePool()
	go pool.healthCheckWorker()
	return pool
}

func defaultConnectionFactory() *MockDatabaseConnection {
	return NewMockDatabaseConnection(0)
}

func (p *ConnectionPool) initializePool() {
	for i := 0; i < minInt(5, p.maxConnections); i++ {
		p.createAndAddConnection()
	}
}

func (p *ConnectionPool) createAndAddConnection() {
	p.connectionCounter++
	connection := p.connectionFactory()
	connection.connectionID = p.connectionCounter
	pooled := NewPooledConnection(connection)
	if len(p.available) < p.maxConnections {
		p.available = append(p.available, pooled)
	}
}

func (p *ConnectionPool) BorrowConnection(timeout time.Duration) *PooledConnection {
	deadline := time.Now().Add(timeout)
	for {
		p.mu.Lock()
		if p.closed {
			p.mu.Unlock()
			panic("Connection pool is closed")
		}

		var pooled *PooledConnection
		if len(p.available) > 0 {
			pooled = p.available[0]
			p.available = p.available[1:]
		} else if p.totalCount() < p.maxConnections {
			p.connectionCounter++
			connection := p.connectionFactory()
			connection.connectionID = p.connectionCounter
			pooled = NewPooledConnection(connection)
		}
		p.mu.Unlock()

		if pooled != nil {
			if !pooled.GetConnection().IsValid() {
				pooled.GetConnection().Close()
				continue
			}
			pooled.Borrow()
			p.mu.Lock()
			p.active[pooled] = true
			p.mu.Unlock()
			return pooled
		}

		if time.Now().After(deadline) {
			panic("timed out waiting for connection")
		}
		time.Sleep(5 * time.Millisecond)
	}
}

func (p *ConnectionPool) totalCount() int {
	return len(p.available) + len(p.active)
}

func (p *ConnectionPool) ReturnConnection(pooled *PooledConnection) {
	if pooled == nil {
		return
	}
	pooled.Release()
	p.mu.Lock()
	delete(p.active, pooled)
	if p.closed {
		p.mu.Unlock()
		pooled.GetConnection().Close()
		return
	}
	if len(p.available) < p.maxConnections {
		p.available = append(p.available, pooled)
		p.mu.Unlock()
		return
	}
	p.mu.Unlock()
	pooled.GetConnection().Close()
}

func (p *ConnectionPool) healthCheckWorker() {
	ticker := time.NewTicker(p.healthCheckInterval)
	defer ticker.Stop()
	for {
		select {
		case <-ticker.C:
			p.performHealthCheck()
		case <-p.stopHealthCheck:
			return
		}
	}
}

func (p *ConnectionPool) performHealthCheck() {
	p.mu.Lock()
	defer p.mu.Unlock()
	if p.closed {
		return
	}
	healthy := make([]*PooledConnection, 0, len(p.available))
	for _, pooled := range p.available {
		if pooled.GetConnection().IsValid() {
			healthy = append(healthy, pooled)
		} else {
			pooled.GetConnection().Close()
		}
	}
	p.available = healthy

	for len(p.available) < minInt(5, p.maxConnections) && p.totalCount() < p.maxConnections {
		p.connectionCounter++
		connection := p.connectionFactory()
		connection.connectionID = p.connectionCounter
		pooled := NewPooledConnection(connection)
		p.available = append(p.available, pooled)
	}
}

func (p *ConnectionPool) GetConnection(timeout time.Duration, fn func(Connection)) {
	pooled := p.BorrowConnection(timeout)
	conn := pooled.GetConnection()
	defer p.ReturnConnection(pooled)
	fn(conn)
}

func (p *ConnectionPool) GetPoolStats() map[string]interface{} {
	p.mu.Lock()
	defer p.mu.Unlock()
	return map[string]interface{}{
		"available_connections": len(p.available),
		"active_connections":    len(p.active),
		"max_connections":       p.maxConnections,
		"is_closed":             p.closed,
	}
}

func (p *ConnectionPool) Close() {
	p.mu.Lock()
	p.closed = true
	close(p.stopHealthCheck)
	for _, pooled := range p.available {
		pooled.GetConnection().Close()
	}
	p.available = nil
	for pooled := range p.active {
		pooled.GetConnection().Close()
	}
	p.active = make(map[*PooledConnection]bool)
	p.mu.Unlock()
}

func minInt(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func main() {
	pool := NewConnectionPool(5, "SELECT 1", nil, 3600*time.Second, 300*time.Second)

	// Borrow/return bookkeeping is exact.
	c1 := pool.BorrowConnection(2 * time.Second)
	c2 := pool.BorrowConnection(2 * time.Second)
	stats := pool.GetPoolStats()
	if !(stats["active_connections"] == 2) {
		fmt.Fprintf(os.Stderr, "2 borrows -> active %v\n", stats["active_connections"])
		os.Exit(1)
	}
	if !(stats["max_connections"] == 5) {
		fmt.Fprintf(os.Stderr, "max_connections mismatch: %v\n", stats["max_connections"])
		os.Exit(1)
	}
	pool.ReturnConnection(c1)
	pool.ReturnConnection(c2)
	if !(pool.GetPoolStats()["active_connections"] == 0) {
		fmt.Fprintln(os.Stderr, "returns not accounted")
		os.Exit(1)
	}

	// Context manager auto-returns even on exceptions.
	pool.GetConnection(2*time.Second, func(conn Connection) {
		if !conn.IsValid() {
			fmt.Fprintln(os.Stderr, "connection not valid")
			os.Exit(1)
		}
		result := conn.Execute("SELECT 1")
		if !(result != "") {
			fmt.Fprintln(os.Stderr, "execute returned empty")
			os.Exit(1)
		}
		if !(pool.GetPoolStats()["active_connections"] == 1) {
			fmt.Fprintf(os.Stderr, "active during CM: %v\n", pool.GetPoolStats()["active_connections"])
			os.Exit(1)
		}
	})
	if !(pool.GetPoolStats()["active_connections"] == 0) {
		fmt.Fprintln(os.Stderr, "context manager leaked")
		os.Exit(1)
	}

	leaked := false
	func() {
		defer func() {
			if r := recover(); r != nil {
				leaked = r == "boom"
			}
		}()
		pool.GetConnection(2*time.Second, func(conn Connection) {
			panic("boom")
		})
	}()
	if !leaked {
		fmt.Fprintln(os.Stderr, "expected panic from CM body")
		os.Exit(1)
	}
	if !(pool.GetPoolStats()["active_connections"] == 0) {
		fmt.Fprintln(os.Stderr, "connection leaked when the body raised")
		os.Exit(1)
	}

	// Contention test: 8 threads x 5 checkouts against 5 connections.
	errors := make([]string, 0)
	done := 0
	var lock sync.Mutex
	var wg sync.WaitGroup

	worker := func(workerID int) {
		defer wg.Done()
		for i := 0; i < 5; i++ {
			func() {
				defer func() {
					if r := recover(); r != nil {
						lock.Lock()
						errors = append(errors, fmt.Sprintf("w%d/%d: %v", workerID, i, r))
						lock.Unlock()
					}
				}()
				pool.GetConnection(10*time.Second, func(conn Connection) {
					conn.Execute(fmt.Sprintf("SELECT %d", workerID))
				})
				lock.Lock()
				done++
				lock.Unlock()
			}()
		}
	}

	for i := 0; i < 8; i++ {
		wg.Add(1)
		go worker(i)
	}
	wg.Wait()

	if !(len(errors) == 0) {
		sample := errors
		if len(sample) > 3 {
			sample = sample[:3]
		}
		fmt.Fprintf(os.Stderr, "checkouts failed under contention: %v\n", sample)
		os.Exit(1)
	}
	if !(done == 40) {
		fmt.Fprintf(os.Stderr, "8x5 checkouts must complete 40, got %d\n", done)
		os.Exit(1)
	}
	final := pool.GetPoolStats()
	if !(final["active_connections"] == 0) {
		fmt.Fprintf(os.Stderr, "%v connections leaked after the storm\n", final["active_connections"])
		os.Exit(1)
	}
	if !(final["available_connections"].(int) <= 5) {
		fmt.Fprintln(os.Stderr, "pool grew past max_connections")
		os.Exit(1)
	}

	// close(): pool refuses further borrows.
	pool.Close()
	if !(pool.GetPoolStats()["is_closed"] == true) {
		fmt.Fprintln(os.Stderr, "pool not marked closed")
		os.Exit(1)
	}
	recovered := false
	func() {
		defer func() {
			if r := recover(); r != nil {
				recovered = true
			}
		}()
		pool.BorrowConnection(500 * time.Millisecond)
	}()
	if !recovered {
		fmt.Fprintln(os.Stderr, "closed pool lent a connection")
		os.Exit(1)
	}

	fmt.Println("connection_pool_health_checks: bookkeeping exact, CM auto-return (incl. on raise), 40/40 contended checkouts no leaks, closed refuses — PASS")
	time.Sleep(1 * time.Millisecond)
}
