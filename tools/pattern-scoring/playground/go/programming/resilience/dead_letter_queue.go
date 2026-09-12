// dead_letter_queue: retry handler with exponential backoff and poison-pill detection.
package main

import (
	"fmt"
	"os"
	"strings"
	"time"
)

// MessageStatus enumerates possible message statuses.
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

// DLQMessage represents a message in the dead-letter queue system.
type DLQMessage struct {
	ID           string
	Payload      map[string]interface{}
	Status       MessageStatus
	AttemptCount int
	CreatedAt    time.Time
	UpdatedAt    time.Time
	ErrorMessage string
	NextRetryAt  *time.Time
}

// NewDLQMessage creates a pending message.
func NewDLQMessage(id string, payload map[string]interface{}) *DLQMessage {
	now := clock.Now()
	return &DLQMessage{
		ID:           id,
		Payload:      payload,
		Status:       StatusPending,
		AttemptCount: 0,
		CreatedAt:    now,
		UpdatedAt:    now,
	}
}

// RetryPolicy defines exponential backoff for message processing.
type RetryPolicy struct {
	MaxRetries int
	BaseDelay  float64
	MaxDelay   float64
}

// NewRetryPolicy creates a retry policy.
func NewRetryPolicy(maxRetries int, baseDelay, maxDelay float64) *RetryPolicy {
	return &RetryPolicy{MaxRetries: maxRetries, BaseDelay: baseDelay, MaxDelay: maxDelay}
}

// CalculateDelay returns the backoff delay for the 0-indexed attempt.
func (rp *RetryPolicy) CalculateDelay(attempt int) float64 {
	if attempt < 0 {
		panic("Attempt must be non-negative")
	}
	delay := rp.BaseDelay
	for i := 0; i < attempt; i++ {
		delay *= 2
		if delay > rp.MaxDelay {
			return rp.MaxDelay
		}
	}
	return delay
}

// ShouldRetry reports whether another attempt is allowed.
func (rp *RetryPolicy) ShouldRetry(attemptCount int) bool {
	return attemptCount < rp.MaxRetries
}

// Processor is a function that processes a message and returns success.
type Processor func(*DLQMessage) bool

// DeadLetterQueue handles pending/processing/dead-letter queues.
type DeadLetterQueue struct {
	RetryPolicy       *RetryPolicy
	PendingQueue      []*DLQMessage
	ProcessingQueue   []*DLQMessage
	DeadLetterQueue   []*DLQMessage
	ProcessedMessages []*DLQMessage
}

// NewDeadLetterQueue creates a DLQ with the given retry policy.
func NewDeadLetterQueue(retryPolicy *RetryPolicy) *DeadLetterQueue {
	if retryPolicy == nil {
		retryPolicy = NewRetryPolicy(3, 1.0, 300.0)
	}
	return &DeadLetterQueue{RetryPolicy: retryPolicy}
}

// Enqueue adds a payload to the pending queue and returns the created message.
func (dlq *DeadLetterQueue) Enqueue(payload map[string]interface{}) *DLQMessage {
	id := nextID()
	msg := NewDLQMessage(id, payload)
	dlq.PendingQueue = append(dlq.PendingQueue, msg)
	return msg
}

// ProcessMessage processes a single message with retries.
func (dlq *DeadLetterQueue) ProcessMessage(message *DLQMessage, processor Processor) bool {
	message.Status = StatusProcessing
	message.UpdatedAt = clock.Now()

	success := processor(message)

	if success {
		message.Status = StatusCompleted
		message.UpdatedAt = clock.Now()
		dlq.ProcessedMessages = append(dlq.ProcessedMessages, message)
		return true
	}

	message.ErrorMessage = "Processor returned False"
	message.AttemptCount++
	message.UpdatedAt = clock.Now()

	if dlq.RetryPolicy.ShouldRetry(message.AttemptCount) {
		delay := dlq.RetryPolicy.CalculateDelay(message.AttemptCount - 1)
		retryAt := clock.Now().Add(time.Duration(delay * float64(time.Second)))
		message.NextRetryAt = &retryAt
		message.Status = StatusFailed
		dlq.PendingQueue = append(dlq.PendingQueue, message)
	} else {
		message.Status = StatusDeadLetter
		dlq.DeadLetterQueue = append(dlq.DeadLetterQueue, message)
	}
	return false
}

// ProcessQueue processes all ready pending messages.
func (dlq *DeadLetterQueue) ProcessQueue(processor Processor) map[string]int {
	stats := map[string]int{"processed": 0, "failed": 0, "dead_letter": 0}

	now := clock.Now()
	ready := make([]*DLQMessage, 0)
	remaining := make([]*DLQMessage, 0)
	for _, msg := range dlq.PendingQueue {
		if msg.NextRetryAt == nil || !msg.NextRetryAt.After(now) {
			ready = append(ready, msg)
		} else {
			remaining = append(remaining, msg)
		}
	}
	dlq.PendingQueue = remaining
	dlq.ProcessingQueue = append(dlq.ProcessingQueue, ready...)

	for len(dlq.ProcessingQueue) > 0 {
		message := dlq.ProcessingQueue[0]
		dlq.ProcessingQueue = dlq.ProcessingQueue[1:]
		success := dlq.ProcessMessage(message, processor)
		if success {
			stats["processed"]++
		} else if message.Status == StatusDeadLetter {
			stats["dead_letter"]++
		} else {
			stats["failed"]++
		}
	}

	return stats
}

// GetQueueStats returns counts for all queues.
func (dlq *DeadLetterQueue) GetQueueStats() map[string]int {
	return map[string]int{
		"pending":     len(dlq.PendingQueue),
		"processing":  len(dlq.ProcessingQueue),
		"dead_letter": len(dlq.DeadLetterQueue),
		"processed":   len(dlq.ProcessedMessages),
	}
}

// GetDeadLetterMessages returns a copy of the dead-letter queue.
func (dlq *DeadLetterQueue) GetDeadLetterMessages() []*DLQMessage {
	out := make([]*DLQMessage, len(dlq.DeadLetterQueue))
	copy(out, dlq.DeadLetterQueue)
	return out
}

// RetryDeadLetterMessage moves a dead-letter message back to pending.
func (dlq *DeadLetterQueue) RetryDeadLetterMessage(messageID string) bool {
	for i, msg := range dlq.DeadLetterQueue {
		if msg.ID == messageID {
			msg.AttemptCount = 0
			msg.ErrorMessage = ""
			msg.Status = StatusPending
			msg.NextRetryAt = nil
			msg.UpdatedAt = clock.Now()
			dlq.PendingQueue = append(dlq.PendingQueue, dlq.DeadLetterQueue[i])
			dlq.DeadLetterQueue = append(dlq.DeadLetterQueue[:i], dlq.DeadLetterQueue[i+1:]...)
			return true
		}
	}
	return false
}

// ---- deterministic helpers replacing stdlib/runtime behavior ----

var (
	idCounter int
	clock     = &fakeClock{now: time.Unix(70000, 0)}
)

type fakeClock struct {
	now time.Time
}

func (fc *fakeClock) Now() time.Time { return fc.now }
func (fc *fakeClock) Add(d time.Duration) time.Time {
	fc.now = fc.now.Add(d)
	return fc.now
}

func nextID() string {
	idCounter++
	return fmt.Sprintf("msg-%04d", idCounter)
}

func main() {
	idCounter = 0
	clock.now = time.Unix(70000, 0)

	dlq := NewDeadLetterQueue(NewRetryPolicy(3, 1.0, 300.0))
	for _, payload := range []map[string]interface{}{
		{"data": "good 1", "should_fail": false},
		{"data": "bad", "should_fail": true},
		{"data": "good 2", "should_fail": false},
	} {
		dlq.Enqueue(payload)
	}
	if !(dlq.GetQueueStats()["pending"] == 3 && dlq.GetQueueStats()["processing"] == 0 &&
		dlq.GetQueueStats()["dead_letter"] == 0 && dlq.GetQueueStats()["processed"] == 0) {
		fmt.Fprintf(os.Stderr, "initial queue stats wrong: %v\n", dlq.GetQueueStats())
		os.Exit(1)
	}

	processor := func(message *DLQMessage) bool {
		if shouldFail, _ := message.Payload["should_fail"].(bool); shouldFail {
			message.ErrorMessage = "simulated failure"
			return false
		}
		return true
	}

	// Round 1: two good messages process; bad one schedules a retry.
	dlq.ProcessQueue(processor)
	s := dlq.GetQueueStats()
	if !(s["processed"] == 2) {
		fmt.Fprintf(os.Stderr, "2 good messages must process, got %d\n", s["processed"])
		os.Exit(1)
	}
	if !(s["dead_letter"] == 0) {
		fmt.Fprintln(os.Stderr, "message dead-lettered before exhausting retries")
		os.Exit(1)
	}
	if !(s["pending"] == 1) {
		fmt.Fprintf(os.Stderr, "failing message must be re-queued as pending, got %d\n", s["pending"])
		os.Exit(1)
	}

	// Backoff must be honored: processing before the delay must not retry.
	attemptsBefore := dlq.PendingQueue[0].AttemptCount
	dlq.ProcessQueue(processor) // too early
	if !(dlq.PendingQueue[0].AttemptCount == attemptsBefore) {
		fmt.Fprintln(os.Stderr, "message retried before its backoff delay elapsed")
		os.Exit(1)
	}

	// Advance the clock through retries until exhaustion.
	rounds := 0
	for dlq.GetQueueStats()["pending"] > 0 && rounds < 10 {
		clock.now = clock.now.Add(300 * time.Second)
		dlq.ProcessQueue(processor)
		rounds++
	}
	s = dlq.GetQueueStats()
	if !(s["dead_letter"] == 1) {
		fmt.Fprintf(os.Stderr, "exhausted message must be dead-lettered: %v\n", s)
		os.Exit(1)
	}
	if !(s["pending"] == 0 && s["processed"] == 2) {
		fmt.Fprintf(os.Stderr, "expected pending=0 processed=2, got %v\n", s)
		os.Exit(1)
	}

	dead := dlq.GetDeadLetterMessages()
	if !(len(dead) == 1) {
		fmt.Fprintf(os.Stderr, "expected exactly 1 dead letter, got %d\n", len(dead))
		os.Exit(1)
	}
	if !(dead[0].Payload["data"] == "bad") {
		fmt.Fprintf(os.Stderr, "dead letter payload wrong: %v\n", dead[0].Payload)
		os.Exit(1)
	}
	if !(dead[0].AttemptCount == 3) {
		fmt.Fprintf(os.Stderr, "must record max_retries=3 attempts, got %d\n", dead[0].AttemptCount)
		os.Exit(1)
	}
	if !(dead[0].ErrorMessage != "") {
		fmt.Fprintln(os.Stderr, "dead letter must carry an error message")
		os.Exit(1)
	}

	// Manual resurrection.
	if !(dlq.RetryDeadLetterMessage(dead[0].ID) == true) {
		fmt.Fprintln(os.Stderr, "retry dead-letter message failed")
		os.Exit(1)
	}
	if !(dlq.RetryDeadLetterMessage("ghost") == false) {
		fmt.Fprintln(os.Stderr, "retry ghost message should fail")
		os.Exit(1)
	}
	if !(dlq.GetQueueStats()["pending"] == 1) {
		fmt.Fprintf(os.Stderr, "expected 1 pending after resurrection, got %d\n", dlq.GetQueueStats()["pending"])
		os.Exit(1)
	}
	dlq.ProcessQueue(func(*DLQMessage) bool { return true })
	s = dlq.GetQueueStats()
	if !(s["pending"] == 0 && s["processing"] == 0 && s["dead_letter"] == 0 && s["processed"] == 3) {
		fmt.Fprintf(os.Stderr, "resurrected message did not complete: %v\n", s)
		os.Exit(1)
	}

	// Backoff arithmetic is exponential and capped.
	rp := NewRetryPolicy(5, 1.0, 4.0)
	delays := []float64{rp.CalculateDelay(0), rp.CalculateDelay(1), rp.CalculateDelay(2), rp.CalculateDelay(3)}
	if !(delays[0] == 1.0 && delays[1] == 2.0 && delays[2] == 4.0 && delays[3] == 4.0) {
		fmt.Fprintf(os.Stderr, "backoff must double then cap at max_delay (0-indexed attempts): %v\n", delays)
		os.Exit(1)
	}
	if !(rp.ShouldRetry(4) && !rp.ShouldRetry(5)) {
		fmt.Fprintln(os.Stderr, "retry boundary wrong")
		os.Exit(1)
	}

	fmt.Println("dead_letter_queue: 2 good processed, poison retried 3x then " +
		"dead-lettered with history, backoff respected, resurrection 3/3 — PASS")
}

// suppress unused import lint for strings until used.
var _ = strings.NewReader
