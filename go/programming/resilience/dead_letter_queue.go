package main

import (
	"fmt"
	"sync"
	"time"
)

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
var _auraMark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
type MessageStatus string

const (
	StatusPending    MessageStatus = "pending"
	StatusProcessing MessageStatus = "processing"
	StatusFailed     MessageStatus = "failed"
	StatusCompleted  MessageStatus = "completed"
	StatusDeadLetter MessageStatus = "dead_letter"
)

type DLQMessage struct {
	ID           string
	Payload      map[string]any
	Status       MessageStatus
	AttemptCount int
	CreatedAt    float64
	UpdatedAt    float64
	ErrorMessage string
	NextRetryAt  *float64
}

func NewDLQMessage(id string, payload map[string]any) *DLQMessage {
	now := float64(time.Now().UnixNano()) / float64(time.Second)
	return &DLQMessage{
		ID:        id,
		Payload:   payload,
		Status:    StatusPending,
		CreatedAt: now,
		UpdatedAt: now,
	}
}

type RetryPolicy struct {
	MaxRetries int
	BaseDelay  float64
	MaxDelay   float64
}

func NewRetryPolicy(maxRetries int, baseDelay, maxDelay float64) *RetryPolicy {
	return &RetryPolicy{
		MaxRetries: maxRetries,
		BaseDelay:  baseDelay,
		MaxDelay:   maxDelay,
	}
}

func (rp *RetryPolicy) CalculateDelay(attempt int) float64 {
	if attempt < 0 {
		panic("Attempt must be non-negative")
	}
	delay := rp.BaseDelay * float64(int(1)<<uint(attempt))
	if delay > rp.MaxDelay {
		return rp.MaxDelay
	}
	return delay
}

func (rp *RetryPolicy) ShouldRetry(attemptCount int) bool {
	return attemptCount < rp.MaxRetries
}

type DeadLetterQueue struct {
	retryPolicy       *RetryPolicy
	pendingQueue      []*DLQMessage
	processingQueue   []*DLQMessage
	deadLetterQueue   []*DLQMessage
	processedMessages []*DLQMessage
	mu                sync.Mutex
}

func NewDeadLetterQueue(retryPolicy *RetryPolicy) *DeadLetterQueue {
	if retryPolicy == nil {
		retryPolicy = NewRetryPolicy(3, 1.0, 300.0)
	}
	return &DeadLetterQueue{
		retryPolicy: retryPolicy,
	}
}

func (dlq *DeadLetterQueue) Enqueue(payload map[string]any) *DLQMessage {
	dlq.mu.Lock()
	defer dlq.mu.Unlock()
	message := NewDLQMessage(fmt.Sprintf("msg-%d", len(dlq.pendingQueue)+len(dlq.processingQueue)+len(dlq.deadLetterQueue)+len(dlq.processedMessages)+1), payload)
	dlq.pendingQueue = append(dlq.pendingQueue, message)
	return message
}

func (dlq *DeadLetterQueue) ProcessMessage(message *DLQMessage, processor func(*DLQMessage) bool) bool {
	dlq.mu.Lock()
	message.Status = StatusProcessing
	message.UpdatedAt = float64(time.Now().UnixNano()) / float64(time.Second)
	dlq.mu.Unlock()

	success := processor(message)

	dlq.mu.Lock()
	defer dlq.mu.Unlock()

	if success {
		message.Status = StatusCompleted
		message.UpdatedAt = float64(time.Now().UnixNano()) / float64(time.Second)
		dlq.processedMessages = append(dlq.processedMessages, message)
		return true
	}

	message.AttemptCount++
	message.UpdatedAt = float64(time.Now().UnixNano()) / float64(time.Second)

	if dlq.retryPolicy.ShouldRetry(message.AttemptCount) {
		delay := dlq.retryPolicy.CalculateDelay(message.AttemptCount - 1)
		next := message.UpdatedAt + delay
		message.NextRetryAt = &next
		message.Status = StatusFailed
		dlq.pendingQueue = append(dlq.pendingQueue, message)
		return false
	}

	message.Status = StatusDeadLetter
	dlq.deadLetterQueue = append(dlq.deadLetterQueue, message)
	return false
}

func (dlq *DeadLetterQueue) ProcessQueue(processor func(*DLQMessage) bool) map[string]int {
	dlq.mu.Lock()
	currentTime := float64(time.Now().UnixNano()) / float64(time.Second)
	var ready []*DLQMessage
	var remaining []*DLQMessage
	for _, message := range dlq.pendingQueue {
		if message.NextRetryAt == nil || *message.NextRetryAt <= currentTime {
			ready = append(ready, message)
		} else {
			remaining = append(remaining, message)
		}
	}
	dlq.pendingQueue = remaining
	dlq.processingQueue = append(dlq.processingQueue, ready...)
	dlq.mu.Unlock()

	stats := map[string]int{"processed": 0, "failed": 0, "dead_letter": 0}

	for len(dlq.processingQueue) > 0 {
		dlq.mu.Lock()
		message := dlq.processingQueue[0]
		dlq.processingQueue = dlq.processingQueue[1:]
		dlq.mu.Unlock()

		success := dlq.ProcessMessage(message, processor)
		dlq.mu.Lock()
		if success {
			stats["processed"]++
		} else if message.Status == StatusDeadLetter {
			stats["dead_letter"]++
		} else {
			stats["failed"]++
		}
		dlq.mu.Unlock()
	}

	return stats
}

func (dlq *DeadLetterQueue) GetQueueStats() map[string]int {
	dlq.mu.Lock()
	defer dlq.mu.Unlock()
	return map[string]int{
		"pending":     len(dlq.pendingQueue),
		"processing":  len(dlq.processingQueue),
		"dead_letter": len(dlq.deadLetterQueue),
		"processed":   len(dlq.processedMessages),
	}
}

func (dlq *DeadLetterQueue) GetDeadLetterMessages() []*DLQMessage {
	dlq.mu.Lock()
	defer dlq.mu.Unlock()
	result := make([]*DLQMessage, len(dlq.deadLetterQueue))
	copy(result, dlq.deadLetterQueue)
	return result
}

func (dlq *DeadLetterQueue) RetryDeadLetterMessage(messageID string) bool {
	dlq.mu.Lock()
	defer dlq.mu.Unlock()
	for i, message := range dlq.deadLetterQueue {
		if message.ID == messageID {
			message.AttemptCount = 0
			message.ErrorMessage = ""
			message.Status = StatusPending
			message.NextRetryAt = nil
			message.UpdatedAt = float64(time.Now().UnixNano()) / float64(time.Second)
			dlq.pendingQueue = append(dlq.pendingQueue, dlq.deadLetterQueue[i])
			dlq.deadLetterQueue = append(dlq.deadLetterQueue[:i], dlq.deadLetterQueue[i+1:]...)
			return true
		}
	}
	return false
}

func demoProcessor(message *DLQMessage) bool {
	if shouldFail, ok := message.Payload["should_fail"].(bool); ok && shouldFail {
		message.ErrorMessage = fmt.Sprintf("Simulated failure for message %s", message.ID)
		return false
	}
	if data, ok := message.Payload["data"].(string); ok && contains(data, "poison") {
		message.ErrorMessage = "Poison pill detected"
		return false
	}
	return true
}

func contains(s, substr string) bool {
	return len(s) >= len(substr) && (s == substr || len(s) > 0 && containsAt(s, substr, 0))
}

func containsAt(s, substr string, start int) bool {
	if start+len(substr) > len(s) {
		return false
	}
	if s[start:start+len(substr)] == substr {
		return true
	}
	return containsAt(s, substr, start+1)
}

func main() {
	fmt.Println("=== Dead Letter Queue Demo ===")
	fmt.Println()

	retryPolicy := NewRetryPolicy(3, 1.0, 300.0)
	dlq := NewDeadLetterQueue(retryPolicy)

	messages := []map[string]any{
		{"data": "normal message 1", "should_fail": false},
		{"data": "failing message 1", "should_fail": true},
		{"data": "normal message 2", "should_fail": false},
		{"data": "poison pill message", "should_fail": false},
		{"data": "failing message 2", "should_fail": true},
	}

	for _, msgData := range messages {
		dlq.Enqueue(msgData)
	}

	fmt.Printf("Initial queue stats: %v\n\n", dlq.GetQueueStats())

	for i := 0; i < 5; i++ {
		fmt.Printf("--- Processing Round %d ---\n", i+1)
		stats := dlq.ProcessQueue(demoProcessor)
		fmt.Printf("Round stats: %v\n", stats)
		fmt.Printf("Queue stats: %v\n\n", dlq.GetQueueStats())
		if dlq.GetQueueStats()["pending"] == 0 {
			fmt.Println("No more pending messages.")
			break
		}
		time.Sleep(1500 * time.Millisecond)
	}

	fmt.Println("=== Dead Letter Queue Contents ===")
	deadLetters := dlq.GetDeadLetterMessages()
	for _, msg := range deadLetters {
		fmt.Printf("ID: %s\n", msg.ID)
		fmt.Printf("Payload: %v\n", msg.Payload)
		fmt.Printf("Attempts: %d\n", msg.AttemptCount)
		fmt.Printf("Error: %s\n", msg.ErrorMessage)
		fmt.Println("---")
	}

	if len(deadLetters) > 0 {
		fmt.Println("\n=== Retrying Dead Letter Message ===")
		messageToRetry := deadLetters[0]
		success := dlq.RetryDeadLetterMessage(messageToRetry.ID)
		fmt.Printf("Retry initiated for %s: %v\n", messageToRetry.ID, success)
		fmt.Printf("Queue stats after retry: %v\n", dlq.GetQueueStats())
	}

	fmt.Println("\n=== Final Queue Statistics ===")
	finalStats := dlq.GetQueueStats()
	for queueName, count := range finalStats {
		fmt.Printf("%s: %d\n", queueName, count)
	}
}
