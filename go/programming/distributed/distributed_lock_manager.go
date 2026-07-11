// distributed_lock_manager: in-process distributed lock manager with fairness
// queue, lease expiration, refresh, and mutual exclusion.
package main

import (
	"fmt"
	"math/rand"
	"os"
	"sync"
	"time"
)

// LockToken represents a held lock with expiration and ownership.
// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
var _auraMark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
type LockToken struct {
	TokenID    string
	OwnerID    string
	Expiration time.Time
	ResourceID string
}

// IsExpired reports whether the token has expired.
func (t *LockToken) IsExpired() bool {
	return time.Now().After(t.Expiration)
}

// RemainingTime returns seconds left before expiration.
func (t *LockToken) RemainingTime() float64 {
	remaining := t.Expiration.Sub(time.Now()).Seconds()
	if remaining < 0 {
		return 0
	}
	return remaining
}

// LockManager implements a distributed lock manager.
type LockManager struct {
	locks   map[string]*LockToken
	waiting map[string][]*waiter
	mu      sync.Mutex
}

type waiter struct {
	ownerID    string
	expireTime time.Time
}

// NewLockManager creates a lock manager.
func NewLockManager() *LockManager {
	return &LockManager{
		locks:   make(map[string]*LockToken),
		waiting: make(map[string][]*waiter),
	}
}

// Acquire tries to obtain a lock for resourceID as ownerID.
func (m *LockManager) Acquire(resourceID, ownerID string, timeout, leaseTime float64) *LockToken {
	startTime := time.Now()

	m.mu.Lock()
	if existing, ok := m.locks[resourceID]; !ok || existing == nil {
		tok := m.createLock(resourceID, ownerID, leaseTime)
		m.mu.Unlock()
		return tok
	}
	if existing := m.locks[resourceID]; existing != nil && existing.IsExpired() {
		tok := m.createLock(resourceID, ownerID, leaseTime)
		m.mu.Unlock()
		return tok
	}
	if _, ok := m.waiting[resourceID]; !ok {
		m.waiting[resourceID] = []*waiter{}
	}
	m.waiting[resourceID] = append(m.waiting[resourceID], &waiter{
		ownerID:    ownerID,
		expireTime: startTime.Add(time.Duration(timeout * float64(time.Second))),
	})
	m.mu.Unlock()

	for time.Since(startTime).Seconds() < timeout {
		time.Sleep(10 * time.Millisecond)
		m.mu.Lock()
		queue := m.waiting[resourceID]
		if len(queue) > 0 && queue[0].ownerID == ownerID {
			existing := m.locks[resourceID]
			if existing == nil || existing.IsExpired() {
				m.waiting[resourceID] = queue[1:]
				if len(m.waiting[resourceID]) == 0 {
					delete(m.waiting, resourceID)
				}
				tok := m.createLock(resourceID, ownerID, leaseTime)
				m.mu.Unlock()
				return tok
			}
		}
		for i, w := range m.waiting[resourceID] {
			if w.ownerID == ownerID {
				if time.Now().After(w.expireTime) {
					m.waiting[resourceID] = append(m.waiting[resourceID][:i], m.waiting[resourceID][i+1:]...)
					if len(m.waiting[resourceID]) == 0 {
						delete(m.waiting, resourceID)
					}
					m.mu.Unlock()
					return nil
				}
				break
			}
		}
		m.mu.Unlock()
	}

	m.mu.Lock()
	for i, w := range m.waiting[resourceID] {
		if w.ownerID == ownerID {
			m.waiting[resourceID] = append(m.waiting[resourceID][:i], m.waiting[resourceID][i+1:]...)
			if len(m.waiting[resourceID]) == 0 {
				delete(m.waiting, resourceID)
			}
			break
		}
	}
	m.mu.Unlock()
	return nil
}

// Release frees the lock identified by token.
func (m *LockManager) Release(token *LockToken) bool {
	m.mu.Lock()
	defer m.mu.Unlock()
	current, ok := m.locks[token.ResourceID]
	if !ok || current == nil {
		return false
	}
	if current.TokenID == token.TokenID && current.OwnerID == token.OwnerID && current.ResourceID == token.ResourceID {
		delete(m.locks, token.ResourceID)
		return true
	}
	return false
}

// Refresh extends an existing lock's lease.
func (m *LockManager) Refresh(token *LockToken, leaseTime float64) *LockToken {
	m.mu.Lock()
	defer m.mu.Unlock()
	current, ok := m.locks[token.ResourceID]
	if !ok || current == nil {
		return nil
	}
	if current.TokenID == token.TokenID && current.OwnerID == token.OwnerID &&
		current.ResourceID == token.ResourceID && !current.IsExpired() {
		newToken := &LockToken{
			TokenID:    current.TokenID,
			OwnerID:    current.OwnerID,
			Expiration: time.Now().Add(time.Duration(leaseTime * float64(time.Second))),
			ResourceID: current.ResourceID,
		}
		m.locks[token.ResourceID] = newToken
		return newToken
	}
	return nil
}

func (m *LockManager) createLock(resourceID, ownerID string, leaseTime float64) *LockToken {
	token := &LockToken{
		TokenID:    fmt.Sprintf("token-%d-%s", time.Now().UnixNano(), randomString(8)),
		OwnerID:    ownerID,
		Expiration: time.Now().Add(time.Duration(leaseTime * float64(time.Second))),
		ResourceID: resourceID,
	}
	m.locks[resourceID] = token
	return token
}

func randomString(n int) string {
	const letters = "abcdefghijklmnopqrstuvwxyz0123456789"
	b := make([]byte, n)
	for i := range b {
		b[i] = letters[rand.Intn(len(letters))]
	}
	return string(b)
}

// LockInfo returns a snapshot of lock state.
type LockInfo struct {
	TokenID   string
	OwnerID   string
	ExpiresIn float64
	Expired   bool
}

// GetLockInfo returns info about a resource's lock, or nil if none.
func (m *LockManager) GetLockInfo(resourceID string) *LockInfo {
	m.mu.Lock()
	defer m.mu.Unlock()
	lock, ok := m.locks[resourceID]
	if !ok || lock == nil {
		return nil
	}
	return &LockInfo{
		TokenID:   lock.TokenID,
		OwnerID:   lock.OwnerID,
		ExpiresIn: lock.RemainingTime(),
		Expired:   lock.IsExpired(),
	}
}

func main() {
	rand.Seed(time.Now().UnixNano())
	manager := NewLockManager()

	token1 := manager.Acquire("resource1", "client1", 10.0, 5.0)
	if token1 == nil {
		fmt.Fprintf(os.Stderr, "first acquire failed\n")
		os.Exit(1)
	}
	info := manager.GetLockInfo("resource1")
	if info == nil {
		fmt.Fprintf(os.Stderr, "lock info missing\n")
		os.Exit(1)
	}
	if !(info.OwnerID == "client1" && !info.Expired) {
		fmt.Fprintf(os.Stderr, "lock info mismatch: owner=%s expired=%v\n", info.OwnerID, info.Expired)
		os.Exit(1)
	}
	if manager.Acquire("resource1", "client2", 0.1, 5.0) != nil {
		fmt.Fprintf(os.Stderr, "second client acquired a HELD lock — mutual exclusion broken\n")
		os.Exit(1)
	}

	if !manager.Release(token1) {
		fmt.Fprintf(os.Stderr, "honest release refused\n")
		os.Exit(1)
	}
	if manager.Release(token1) {
		fmt.Fprintf(os.Stderr, "double release reported success\n")
		os.Exit(1)
	}

	token2 := manager.Acquire("resource1", "client2", 0.1, 5.0)
	if token2 == nil {
		fmt.Fprintf(os.Stderr, "after-release acquire failed\n")
		os.Exit(1)
	}
	if token2.OwnerID != "client2" {
		fmt.Fprintf(os.Stderr, "after-release wrong owner: %s\n", token2.OwnerID)
		os.Exit(1)
	}
	manager.Release(token2)

	t1 := manager.Acquire("resource2", "client1", 10.0, 10.0)
	if t1 == nil {
		fmt.Fprintf(os.Stderr, "resource2 initial acquire failed\n")
		os.Exit(1)
	}
	results := make(map[string]*LockToken)
	var wg sync.WaitGroup
	tryAcquire := func(clientID string) {
		defer wg.Done()
		tok := manager.Acquire("resource2", clientID, 3.0, 10.0)
		results[clientID] = tok
	}
	wg.Add(2)
	go tryAcquire("client2")
	go tryAcquire("client3")
	time.Sleep(300 * time.Millisecond)
	if len(results) > 0 {
		fmt.Fprintf(os.Stderr, "a waiter acquired while the lock was held: %v\n", results)
		os.Exit(1)
	}
	manager.Release(t1)
	wg.Wait()
	nWinners := 0
	for _, tok := range results {
		if tok != nil {
			nWinners++
		}
	}
	if nWinners != 1 {
		fmt.Fprintf(os.Stderr, "exactly one waiter must win the handoff, got %d: %v\n", nWinners, results)
		os.Exit(1)
	}
	var winner string
	for c, tok := range results {
		if tok != nil {
			winner = c
			break
		}
	}
	manager.Release(results[winner])

	manager.Acquire("resource3", "client1", 10.0, 0.3)
	if manager.Acquire("resource3", "client2", 0.05, 5.0) != nil {
		fmt.Fprintf(os.Stderr, "expired-lock acquire succeeded too early\n")
		os.Exit(1)
	}
	time.Sleep(500 * time.Millisecond)
	expiredInfo := manager.GetLockInfo("resource3")
	if expiredInfo == nil || !expiredInfo.Expired {
		fmt.Fprintf(os.Stderr, "lease did not expire\n")
		os.Exit(1)
	}
	stolen := manager.Acquire("resource3", "client2", 0.5, 5.0)
	if stolen == nil {
		fmt.Fprintf(os.Stderr, "expired lock not reacquirable\n")
		os.Exit(1)
	}
	manager.Release(stolen)

	tok := manager.Acquire("resource4", "client1", 10.0, 0.4)
	if tok == nil {
		fmt.Fprintf(os.Stderr, "resource4 acquire failed\n")
		os.Exit(1)
	}
	time.Sleep(200 * time.Millisecond)
	refreshed := manager.Refresh(tok, 2.0)
	if refreshed == nil {
		fmt.Fprintf(os.Stderr, "refresh of a live lock failed\n")
		os.Exit(1)
	}
	time.Sleep(400 * time.Millisecond)
	if manager.Acquire("resource4", "client2", 0.05, 5.0) != nil {
		fmt.Fprintf(os.Stderr, "lock lapsed despite the refresh\n")
		os.Exit(1)
	}
	refreshInfo := manager.GetLockInfo("resource4")
	if refreshInfo == nil || refreshInfo.ExpiresIn <= 0.5 {
		fmt.Fprintf(os.Stderr, "refresh did not extend lease past 0.5s: %v\n", refreshInfo)
		os.Exit(1)
	}

	fmt.Println("distributed_lock_manager: exclusion held, 1/2 waiters won handoff, " +
		"0.3s lease expired+stolen, refresh outlived original lease — PASS")
}
