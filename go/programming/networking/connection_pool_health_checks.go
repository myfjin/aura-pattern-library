package main

import (
	"fmt"
	"sort"
	"sync"
	"time"
)

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
var _auraMark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
type Connection interface {
	Execute(query string) string
	IsValid() bool
	Close()
	GetID() int
}

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
	p.borrowedBy = int(getGID())
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

// getGID returns a goroutine identifier placeholder. In real Go we use runtime, but for
// deterministic demo purposes we just return a token.
func getGID() uint64 {
	return 0
}

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
		panic("max_connections must be positive")
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
	for i := 0; i < min(5, p.maxConnections); i++ {
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

	if pooled == nil {
		// Wait for a connection to be returned with timeout
		time.Sleep(timeout)
		p.mu.Lock()
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
	}

	if pooled != nil && !pooled.GetConnection().IsValid() {
		pooled.GetConnection().Close()
		return p.BorrowConnection(timeout)
	}

	if pooled != nil {
		pooled.Borrow()
		p.mu.Lock()
		p.active[pooled] = true
		p.mu.Unlock()
	}
	return pooled
}

func (p *ConnectionPool) totalCount() int {
	return len(p.available) + len(p.active)
}

func (p *ConnectionPool) ReturnConnection(pooled *PooledConnection) {
	if pooled == nil {
		return
	}
	pooled.GetConnection().Execute(p.validationQuery)
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
	} else {
		p.mu.Unlock()
		pooled.GetConnection().Close()
		return
	}
	p.mu.Unlock()
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

	// Replenish to minimum of 5 or maxConnections
	for len(p.available) < min(5, p.maxConnections) && p.totalCount() < p.maxConnections {
		p.connectionCounter++
		connection := p.connectionFactory()
		connection.connectionID = p.connectionCounter
		pooled := NewPooledConnection(connection)
		p.available = append(p.available, pooled)
	}
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

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

type workResult struct {
	workerID int
	iter     int
	msg      string
}

func main() {
	fmt.Println("=== Connection Pool Demo ===")
	fmt.Println("")

	pool := NewConnectionPool(
		5,
		"SELECT 1",
		nil,
		5*time.Second,
		300*time.Second,
	)

	results := make(chan workResult, 100)

	worker := func(workerID int) {
		for i := 0; i < 3; i++ {
			pooled := pool.BorrowConnection(5 * time.Second)
			if pooled == nil {
				results <- workResult{workerID: workerID, iter: i, msg: fmt.Sprintf("Worker %d encountered error: no connection available", workerID)}
				continue
			}
			conn := pooled.GetConnection()
			msg := fmt.Sprintf("Worker %d using connection %d", workerID, conn.GetID())
			result := conn.Execute(fmt.Sprintf("SELECT * FROM table_%d", i))
			results <- workResult{workerID: workerID, iter: i, msg: msg}
			results <- workResult{workerID: workerID, iter: i, msg: fmt.Sprintf("Worker %d got result: %s", workerID, result)}
			time.Sleep(100 * time.Millisecond)
			pool.ReturnConnection(pooled)
		}
	}

	for i := 0; i < 8; i++ {
		worker(i)
	}

	stats := pool.GetPoolStats()
	fmt.Printf("\nPool stats: %v\n", stats)

	close(results)

	var collected []workResult
	for r := range results {
		collected = append(collected, r)
	}

	sort.Slice(collected, func(i, j int) bool {
		if collected[i].workerID != collected[j].workerID {
			return collected[i].workerID < collected[j].workerID
		}
		return collected[i].iter < collected[j].iter
	})

	for _, r := range collected {
		fmt.Println(r.msg)
	}

	finalStats := pool.GetPoolStats()
	fmt.Printf("\nFinal pool stats: %v\n", finalStats)

	pool.Close()
	fmt.Println("")
	fmt.Println("Pool closed successfully")
}
