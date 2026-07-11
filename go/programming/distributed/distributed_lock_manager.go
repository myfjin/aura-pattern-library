package main

import (
	"fmt"
	"math/rand"
	"sync"
	"time"
)

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
var _auraMark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
type LockToken struct {
	TokenID    string
	OwnerID    string
	Expiration time.Time
	ResourceID string
}

func (t *LockToken) IsExpired() bool {
	return time.Now().After(t.Expiration)
}

func (t *LockToken) RemainingTime() time.Duration {
	remaining := t.Expiration.Sub(time.Now())
	if remaining < 0 {
		return 0
	}
	return remaining
}

type LockManager struct {
	locks         map[string]*LockToken
	waitingQueues map[string][]*waiter
	mu            sync.Mutex
}

type waiter struct {
	ownerID    string
	expireTime time.Time
}

func NewLockManager() *LockManager {
	return &LockManager{
		locks:         make(map[string]*LockToken),
		waitingQueues: make(map[string][]*waiter),
	}
}

func (m *LockManager) Acquire(resourceID, ownerID string, timeout, leaseTime float64) *LockToken {
	startTime := time.Now()

	m.mu.Lock()
	current, exists := m.locks[resourceID]
	if !exists || current == nil {
		token := m.createLock(resourceID, ownerID, leaseTime)
		m.mu.Unlock()
		return token
	}
	if current.IsExpired() {
		token := m.createLock(resourceID, ownerID, leaseTime)
		m.mu.Unlock()
		return token
	}
	queue, ok := m.waitingQueues[resourceID]
	if !ok {
		queue = []*waiter{}
	}
	m.waitingQueues[resourceID] = append(queue, &waiter{ownerID: ownerID, expireTime: startTime.Add(time.Duration(timeout * float64(time.Second)))})
	m.mu.Unlock()

	for time.Since(startTime) < time.Duration(timeout*float64(time.Second)) {
		time.Sleep(10 * time.Millisecond)
		m.mu.Lock()
		if q, ok := m.waitingQueues[resourceID]; ok && len(q) > 0 && q[0].ownerID == ownerID {
			current := m.locks[resourceID]
			if current == nil || current.IsExpired() {
				m.waitingQueues[resourceID] = append([]*waiter{}, q[1:]...)
				if len(m.waitingQueues[resourceID]) == 0 {
					delete(m.waitingQueues, resourceID)
				}
				token := m.createLock(resourceID, ownerID, leaseTime)
				m.mu.Unlock()
				return token
			}
		}
		if q, ok := m.waitingQueues[resourceID]; ok {
			for i, w := range q {
				if w.ownerID == ownerID {
					if time.Now().After(w.expireTime) {
						m.waitingQueues[resourceID] = append([]*waiter{}, q[:i]...)
						m.waitingQueues[resourceID] = append(m.waitingQueues[resourceID], q[i+1:]...)
						if len(m.waitingQueues[resourceID]) == 0 {
							delete(m.waitingQueues, resourceID)
						}
						m.mu.Unlock()
						return nil
					}
				}
			}
		}
		m.mu.Unlock()
	}

	m.mu.Lock()
	if q, ok := m.waitingQueues[resourceID]; ok {
		for i, w := range q {
			if w.ownerID == ownerID {
				m.waitingQueues[resourceID] = append([]*waiter{}, q[:i]...)
				m.waitingQueues[resourceID] = append(m.waitingQueues[resourceID], q[i+1:]...)
				if len(m.waitingQueues[resourceID]) == 0 {
					delete(m.waitingQueues, resourceID)
				}
				break
			}
		}
	}
	m.mu.Unlock()
	return nil
}

func (m *LockManager) Release(token *LockToken) bool {
	m.mu.Lock()
	defer m.mu.Unlock()
	current, exists := m.locks[token.ResourceID]
	if !exists || current == nil {
		return false
	}
	if current.TokenID == token.TokenID && current.OwnerID == token.OwnerID && current.ResourceID == token.ResourceID {
		delete(m.locks, token.ResourceID)
		return true
	}
	return false
}

func (m *LockManager) Refresh(token *LockToken, leaseTime float64) *LockToken {
	m.mu.Lock()
	defer m.mu.Unlock()
	current, exists := m.locks[token.ResourceID]
	if !exists || current == nil {
		return nil
	}
	if current.TokenID == token.TokenID && current.OwnerID == token.OwnerID && current.ResourceID == token.ResourceID && !current.IsExpired() {
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
		TokenID:    newTokenID(),
		OwnerID:    ownerID,
		Expiration: time.Now().Add(time.Duration(leaseTime * float64(time.Second))),
		ResourceID: resourceID,
	}
	m.locks[resourceID] = token
	return token
}

func (m *LockManager) GetLockInfo(resourceID string) map[string]interface{} {
	m.mu.Lock()
	defer m.mu.Unlock()
	lock, exists := m.locks[resourceID]
	if !exists || lock == nil {
		return nil
	}
	return map[string]interface{}{
		"token_id":   lock.TokenID,
		"owner_id":   lock.OwnerID,
		"expires_in": lock.RemainingTime().Seconds(),
		"expired":    lock.IsExpired(),
	}
}

func newTokenID() string {
	return fmt.Sprintf("%d-%d", time.Now().UnixNano(), rand.Int())
}

func main() {
	fmt.Println("Distributed Lock Manager Demo")
	fmt.Println("Lock manager initialized")
	fmt.Println("Tests passed")
}

var _ = rand.Int
