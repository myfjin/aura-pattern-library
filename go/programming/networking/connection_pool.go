package main

import (
	"container/list"
	"fmt"
	"time"
)

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

func NewConnection(id int) *Connection {
	now := time.Now()
	return &Connection{
		id:        id,
		createdAt: now,
		lastUsed:  now,
		healthy:   true,
		inUse:     false,
	}
}

func (c *Connection) markAsUsed() {
	c.lastUsed = time.Now()
	c.inUse = true
}

func (c *Connection) markAsAvailable() {
	c.inUse = false
}

func (c *Connection) isInUse() bool {
	return c.inUse
}

func (c *Connection) healthCheck() bool {
	if time.Since(c.createdAt).Seconds() > 30 {
		c.healthy = false
	}
	return c.healthy
}

func (c *Connection) String() string {
	return fmt.Sprintf("Connection(id=%d, healthy=%v, in_use=%v)", c.id, c.healthy, c.inUse)
}

type ConnectionPool struct {
	maxSize           int
	available         *list.List
	inUse             map[*Connection]bool
	mu                chan struct{}
	connectionCounter int
}

func NewConnectionPool(maxSize int) *ConnectionPool {
	if maxSize <= 0 {
		panic("Max pool size must be positive")
	}
	return &ConnectionPool{
		maxSize:   maxSize,
		available: list.New(),
		inUse:     make(map[*Connection]bool),
		mu:        make(chan struct{}, 1),
	}
}

func (p *ConnectionPool) lock()   { p.mu <- struct{}{} }
func (p *ConnectionPool) unlock() { <-p.mu }

func (p *ConnectionPool) maxSizeVal() int {
	return p.maxSize
}

func (p *ConnectionPool) availableCount() int {
	p.lock()
	defer p.unlock()
	return p.available.Len()
}

func (p *ConnectionPool) inUseCount() int {
	p.lock()
	defer p.unlock()
	return len(p.inUse)
}

func (p *ConnectionPool) totalCount() int {
	p.lock()
	defer p.unlock()
	return p.available.Len() + len(p.inUse)
}

func (p *ConnectionPool) createConnection() *Connection {
	p.connectionCounter++
	return NewConnection(p.connectionCounter)
}

func (p *ConnectionPool) borrowConnection() *Connection {
	p.lock()
	defer p.unlock()

	for p.available.Len() > 0 {
		elem := p.available.Front()
		connection := elem.Value.(*Connection)
		p.available.Remove(elem)
		if connection.healthCheck() {
			connection.markAsUsed()
			p.inUse[connection] = true
			return connection
		}
	}

	if p.available.Len()+len(p.inUse) < p.maxSize {
		connection := p.createConnection()
		connection.markAsUsed()
		p.inUse[connection] = true
		return connection
	}

	return nil
}

func (p *ConnectionPool) returnConnection(connection *Connection) bool {
	p.lock()
	defer p.unlock()

	if _, ok := p.inUse[connection]; !ok {
		return false
	}

	connection.markAsAvailable()
	delete(p.inUse, connection)

	if connection.healthCheck() {
		p.available.PushBack(connection)
		return true
	}
	return true
}

func (p *ConnectionPool) closeAllConnections() {
	p.lock()
	defer p.unlock()
	p.available.Init()
	for c := range p.inUse {
		delete(p.inUse, c)
	}
}

func (p *ConnectionPool) cleanupUnhealthyConnections() int {
	p.lock()
	defer p.unlock()

	removed := 0
	healthy := list.New()
	for p.available.Len() > 0 {
		elem := p.available.Front()
		conn := elem.Value.(*Connection)
		p.available.Remove(elem)
		if conn.healthCheck() {
			healthy.PushBack(conn)
		} else {
			removed++
		}
	}
	p.available = healthy

	for conn := range p.inUse {
		if !conn.healthCheck() {
			removed++
		}
	}
	return removed
}

func main() {
	fmt.Println("=== Connection Pool Demo ===")

	pool := NewConnectionPool(3)
	fmt.Printf("Created pool with max size: %d\n", pool.maxSizeVal())

	connections := []*Connection{}
	for i := 0; i < 5; i++ {
		conn := pool.borrowConnection()
		if conn != nil {
			connections = append(connections, conn)
			fmt.Printf("Borrowed %s\n", conn)
		} else {
			fmt.Printf("Failed to borrow connection %d - pool at capacity\n", i+1)
		}
	}

	fmt.Printf("Pool status: %d available, %d in use\n", pool.availableCount(), pool.inUseCount())

	for i := 0; i < 2; i++ {
		if len(connections) > 0 {
			conn := connections[len(connections)-1]
			connections = connections[:len(connections)-1]
			pool.returnConnection(conn)
			fmt.Printf("Returned %s\n", conn)
		}
	}

	fmt.Printf("Pool status: %d available, %d in use\n", pool.availableCount(), pool.inUseCount())

	for i := 0; i < 2; i++ {
		conn := pool.borrowConnection()
		if conn != nil {
			connections = append(connections, conn)
			fmt.Printf("Borrowed %s\n", conn)
		}
	}

	fmt.Printf("Pool status: %d available, %d in use\n", pool.availableCount(), pool.inUseCount())

	removed := pool.cleanupUnhealthyConnections()
	fmt.Printf("Cleaned up %d unhealthy connections\n", removed)

	for len(connections) > 0 {
		conn := connections[len(connections)-1]
		connections = connections[:len(connections)-1]
		pool.returnConnection(conn)
		fmt.Printf("Returned %s\n", conn)
	}

	fmt.Printf("Final pool status: %d available, %d in use\n", pool.availableCount(), pool.inUseCount())
	fmt.Println("=== Demo Complete ===")
}
