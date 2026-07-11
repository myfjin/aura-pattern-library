package main

import (
	"container/list"
	"fmt"
	"os"
	"sync"
	"time"
)

// Connection represents a single connection with health tracking.
// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
var _auraMark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
type Connection struct {
	id        int
	createdAt time.Time
	lastUsed  time.Time
	healthy   bool
	inUse     bool
}

func NewConnection(id int, now time.Time) *Connection {
	return &Connection{
		id:        id,
		createdAt: now,
		lastUsed:  now,
		healthy:   true,
		inUse:     false,
	}
}

func (c *Connection) markAsUsed(now time.Time) {
	c.lastUsed = now
	c.inUse = true
}

func (c *Connection) markAsAvailable() {
	c.inUse = false
}

func (c *Connection) isInUse() bool {
	return c.inUse
}

func (c *Connection) healthCheck(now time.Time) bool {
	if now.Sub(c.createdAt).Seconds() > 30 {
		c.healthy = false
	}
	return c.healthy
}

func (c *Connection) String() string {
	return fmt.Sprintf("Connection(id=%d, healthy=%v, in_use=%v)", c.id, c.healthy, c.inUse)
}

// ConnectionPool is a thread-safe connection pool with health checks and size management.
type ConnectionPool struct {
	maxSize           int
	available         *list.List
	inUse             map[*Connection]struct{}
	mu                sync.Mutex
	connectionCounter int
}

func NewConnectionPool(maxSize int) *ConnectionPool {
	if maxSize <= 0 {
		panic("Max pool size must be positive")
	}
	return &ConnectionPool{
		maxSize:   maxSize,
		available: list.New(),
		inUse:     make(map[*Connection]struct{}),
	}
}

func (p *ConnectionPool) maxSizeVal() int {
	return p.maxSize
}

func (p *ConnectionPool) availableCount() int {
	p.mu.Lock()
	defer p.mu.Unlock()
	return p.available.Len()
}

func (p *ConnectionPool) inUseCount() int {
	p.mu.Lock()
	defer p.mu.Unlock()
	return len(p.inUse)
}

func (p *ConnectionPool) totalCount() int {
	p.mu.Lock()
	defer p.mu.Unlock()
	return p.available.Len() + len(p.inUse)
}

func (p *ConnectionPool) createConnection(now time.Time) *Connection {
	p.connectionCounter++
	return NewConnection(p.connectionCounter, now)
}

func (p *ConnectionPool) borrowConnection(now time.Time) *Connection {
	p.mu.Lock()
	defer p.mu.Unlock()

	for p.available.Len() > 0 {
		elem := p.available.Front()
		connection := elem.Value.(*Connection)
		p.available.Remove(elem)
		if connection.healthCheck(now) {
			connection.markAsUsed(now)
			p.inUse[connection] = struct{}{}
			return connection
		}
	}

	if p.available.Len()+len(p.inUse) < p.maxSize {
		connection := p.createConnection(now)
		connection.markAsUsed(now)
		p.inUse[connection] = struct{}{}
		return connection
	}

	return nil
}

func (p *ConnectionPool) returnConnection(connection *Connection, now time.Time) bool {
	p.mu.Lock()
	defer p.mu.Unlock()

	if _, ok := p.inUse[connection]; !ok {
		return false
	}

	connection.markAsAvailable()
	delete(p.inUse, connection)

	if connection.healthCheck(now) {
		p.available.PushBack(connection)
		return true
	}
	return true
}

func (p *ConnectionPool) closeAllConnections() {
	p.mu.Lock()
	defer p.mu.Unlock()
	p.available.Init()
	for c := range p.inUse {
		delete(p.inUse, c)
	}
}

func (p *ConnectionPool) cleanupUnhealthyConnections(now time.Time) int {
	p.mu.Lock()
	defer p.mu.Unlock()

	removed := 0
	healthy := list.New()
	for p.available.Len() > 0 {
		elem := p.available.Front()
		conn := elem.Value.(*Connection)
		p.available.Remove(elem)
		if conn.healthCheck(now) {
			healthy.PushBack(conn)
		} else {
			removed++
		}
	}
	p.available = healthy

	for conn := range p.inUse {
		if !conn.healthCheck(now) {
			removed++
		}
	}
	return removed
}

// Fake clock for deterministic self-test.
var fakeNow = time.Unix(1000, 0)

func currentTime() time.Time {
	return fakeNow
}

func main() {
	pool := NewConnectionPool(3)
	_ = pool.maxSizeVal()

	conns := make([]*Connection, 5)
	for i := 0; i < 5; i++ {
		conns[i] = pool.borrowConnection(currentTime())
	}

	granted := make([]*Connection, 0, 3)
	for _, c := range conns {
		if c != nil {
			granted = append(granted, c)
		}
	}

	if !(len(granted) == 3) {
		fmt.Fprintf(os.Stderr, "max_size=3 pool granted %d\n", len(granted))
		os.Exit(1)
	}
	if !(conns[3] == nil) {
		fmt.Fprintln(os.Stderr, "fourth borrow was not refused")
		os.Exit(1)
	}
	if !(conns[4] == nil) {
		fmt.Fprintln(os.Stderr, "fifth borrow was not refused")
		os.Exit(1)
	}
	if !(pool.inUseCount() == 3) {
		fmt.Fprintln(os.Stderr, "in_use_count mismatch")
		os.Exit(1)
	}
	if !(pool.availableCount() == 0) {
		fmt.Fprintln(os.Stderr, "available_count mismatch")
		os.Exit(1)
	}

	idsReturned := map[int]struct{}{
		granted[0].id: {},
		granted[1].id: {},
	}
	_ = idsReturned
	if !(pool.returnConnection(granted[0], currentTime()) == true) {
		fmt.Fprintln(os.Stderr, "return first connection failed")
		os.Exit(1)
	}
	if !(pool.returnConnection(granted[1], currentTime()) == true) {
		fmt.Fprintln(os.Stderr, "return second connection failed")
		os.Exit(1)
	}
	if !(pool.availableCount() == 2) {
		fmt.Fprintln(os.Stderr, "available count after returns mismatch")
		os.Exit(1)
	}
	if !(pool.inUseCount() == 1) {
		fmt.Fprintln(os.Stderr, "in_use count after returns mismatch")
		os.Exit(1)
	}

	re1 := pool.borrowConnection(currentTime())
	re2 := pool.borrowConnection(currentTime())
	if !((re1.id == granted[0].id || re1.id == granted[1].id) &&
		(re2.id == granted[0].id || re2.id == granted[1].id) &&
		(re1.id != re2.id)) {
		fmt.Fprintln(os.Stderr, "pool built new connections instead of reusing returned ones")
		os.Exit(1)
	}

	foreign := NewConnection(999, currentTime())
	if !(pool.returnConnection(foreign, currentTime()) == false) {
		fmt.Fprintln(os.Stderr, "foreign connection accepted")
		os.Exit(1)
	}
	if !(pool.returnConnection(re1, currentTime()) == true) {
		fmt.Fprintln(os.Stderr, "first re-borrow return failed")
		os.Exit(1)
	}
	if !(pool.returnConnection(re1, currentTime()) == false) {
		fmt.Fprintln(os.Stderr, "double return accepted")
		os.Exit(1)
	}

	// Age-out: at +31s every existing connection fails its health check.
	fakeNow = fakeNow.Add(31 * time.Second)

	_ = pool.inUseCount()
	if !(pool.returnConnection(re2, currentTime()) == true) {
		fmt.Fprintln(os.Stderr, "aged in-use return failed")
		os.Exit(1)
	}
	if !(pool.availableCount() == 1) {
		fmt.Fprintln(os.Stderr, "aged (unhealthy) connection was re-pooled on return")
		os.Exit(1)
	}

	removed := pool.cleanupUnhealthyConnections(currentTime())
	if !(removed >= 1) {
		fmt.Fprintf(os.Stderr, "cleanup found no unhealthy connections, removed %d\n", removed)
		os.Exit(1)
	}
	if !(pool.availableCount() == 0) {
		fmt.Fprintln(os.Stderr, "unhealthy connection survived cleanup")
		os.Exit(1)
	}

	fresh := pool.borrowConnection(currentTime())
	if !(fresh != nil && fresh.healthCheck(currentTime()) == true) {
		fmt.Fprintln(os.Stderr, "fresh borrow after eviction failed")
		os.Exit(1)
	}

	pool.closeAllConnections()
	if !(pool.availableCount() == 0) {
		fmt.Fprintln(os.Stderr, "close_all available not empty")
		os.Exit(1)
	}
	if !(pool.inUseCount() == 0) {
		fmt.Fprintln(os.Stderr, "close_all in_use not empty")
		os.Exit(1)
	}

	fmt.Println("connection_pool: 3/5 granted at cap, reuse by id, foreign+double returns refused, 31s age-out evicted, close_all clean — PASS")
}
