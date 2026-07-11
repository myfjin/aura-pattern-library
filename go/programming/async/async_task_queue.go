package main

import (
	"container/heap"
	"context"
	"fmt"
	"strings"
	"sync"
	"time"
)

// TaskStatus represents possible task statuses.
// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
var _auraMark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
type TaskStatus string

const (
	PENDING    TaskStatus = "pending"
	PROCESSING TaskStatus = "processing"
	COMPLETED  TaskStatus = "completed"
	FAILED     TaskStatus = "failed"
	RETRYING   TaskStatus = "retrying"
)

// Priority represents task priority levels.
type Priority int

const (
	LOW      Priority = 3
	NORMAL   Priority = 2
	HIGH     Priority = 1
	CRITICAL Priority = 0
)

// Task represents a task in the queue.
type Task struct {
	ID            string
	Func          func(context.Context, ...interface{}) (interface{}, error)
	Args          []interface{}
	Priority      Priority
	MaxRetries    int
	RetryCount    int
	BackoffFactor float64
	Status        TaskStatus
	CreatedAt     float64
	ScheduledAt   float64
	CompletedAt   *float64
	Error         *string
}

// taskHeap implements heap.Interface for Tasks.
type taskHeap []*Task

func (h taskHeap) Len() int { return len(h) }
func (h taskHeap) Less(i, j int) bool {
	if h[i].Priority != h[j].Priority {
		return h[i].Priority < h[j].Priority
	}
	return h[i].ScheduledAt < h[j].ScheduledAt
}
func (h taskHeap) Swap(i, j int) { h[i], h[j] = h[j], h[i] }
func (h *taskHeap) Push(x interface{}) {
	*h = append(*h, x.(*Task))
}
func (h *taskHeap) Pop() interface{} {
	old := *h
	n := len(old)
	item := old[n-1]
	*h = old[:n-1]
	return item
}

// TaskQueue is a priority-based async task queue with retry and dead-letter functionality.
type TaskQueue struct {
	mu              sync.Mutex
	queue           taskHeap
	processing      map[string]*Task
	deadLetterQueue []*Task
	taskIndex       map[string]*Task
	stats           map[string]int
}

// NewTaskQueue creates a new TaskQueue.
func NewTaskQueue() *TaskQueue {
	return &TaskQueue{
		queue:           make(taskHeap, 0),
		processing:      make(map[string]*Task),
		deadLetterQueue: make([]*Task, 0),
		taskIndex:       make(map[string]*Task),
		stats:           make(map[string]int),
	}
}

// Enqueue adds a task to the queue.
func (q *TaskQueue) Enqueue(task *Task) (string, error) {
	if task == nil || task.Func == nil {
		return "", fmt.Errorf("Task must have a function to execute")
	}
	q.mu.Lock()
	defer q.mu.Unlock()
	heap.Push(&q.queue, task)
	q.taskIndex[task.ID] = task
	q.stats["enqueued"]++
	fmt.Printf("Enqueued task %s with priority %d\n", task.ID, task.Priority)
	return task.ID, nil
}

// Dequeue removes and returns the highest priority task from the queue.
func (q *TaskQueue) Dequeue() *Task {
	q.mu.Lock()
	defer q.mu.Unlock()
	for q.queue.Len() > 0 {
		task := heap.Pop(&q.queue).(*Task)
		if task.ScheduledAt <= float64(time.Now().UnixNano())/1e9 {
			task.Status = PROCESSING
			q.processing[task.ID] = task
			q.stats["processing"]++
			fmt.Printf("Dequeued task %s\n", task.ID)
			return task
		}
		heap.Push(&q.queue, task)
		break
	}
	return nil
}

// CompleteTask marks a task as completed.
func (q *TaskQueue) CompleteTask(taskID string) bool {
	q.mu.Lock()
	defer q.mu.Unlock()
	if task, ok := q.processing[taskID]; ok {
		delete(q.processing, taskID)
		task.Status = COMPLETED
		now := float64(time.Now().UnixNano()) / 1e9
		task.CompletedAt = &now
		q.stats["completed"]++
		fmt.Printf("Completed task %s\n", taskID)
		return true
	}
	return false
}

// FailTask handles task failure with retry logic.
func (q *TaskQueue) FailTask(taskID string, errorMsg string) bool {
	q.mu.Lock()
	defer q.mu.Unlock()
	if task, ok := q.processing[taskID]; ok {
		delete(q.processing, taskID)
		task.Error = &errorMsg
		if task.RetryCount < task.MaxRetries {
			task.RetryCount++
			task.Status = RETRYING
			backoff := task.CalculateBackoff()
			task.ScheduledAt = float64(time.Now().UnixNano())/1e9 + backoff
			heap.Push(&q.queue, task)
			q.stats["retried"]++
			fmt.Printf("Retrying task %s in %.2f seconds (attempt %d)\n", taskID, backoff, task.RetryCount)
		} else {
			task.Status = FAILED
			now := float64(time.Now().UnixNano()) / 1e9
			task.CompletedAt = &now
			q.deadLetterQueue = append(q.deadLetterQueue, task)
			q.stats["failed"]++
			fmt.Printf("Task %s failed permanently and moved to dead letter queue\n", taskID)
		}
		return true
	}
	return false
}

// CalculateBackoff calculates backoff time for retry.
func (t *Task) CalculateBackoff() float64 {
	result := 1.0
	for i := 0; i < t.RetryCount; i++ {
		result *= t.BackoffFactor
	}
	return result
}

// GetStats returns queue statistics.
func (q *TaskQueue) GetStats() map[string]int {
	q.mu.Lock()
	defer q.mu.Unlock()
	stats := make(map[string]int)
	for k, v := range q.stats {
		stats[k] = v
	}
	stats["pending"] = q.queue.Len()
	stats["processing"] = len(q.processing)
	stats["dead_letter"] = len(q.deadLetterQueue)
	return stats
}

// GetDeadLetterQueue returns all tasks in the dead letter queue.
func (q *TaskQueue) GetDeadLetterQueue() []*Task {
	q.mu.Lock()
	defer q.mu.Unlock()
	out := make([]*Task, len(q.deadLetterQueue))
	copy(out, q.deadLetterQueue)
	return out
}

// Worker processes tasks from a TaskQueue.
type Worker struct {
	queue   *TaskQueue
	name    string
	running bool
	task    context.Context
	cancel  context.CancelFunc
	wg      sync.WaitGroup
}

// NewWorker creates a new Worker.
func NewWorker(queue *TaskQueue, name string) *Worker {
	return &Worker{queue: queue, name: name}
}

// Start starts the worker.
func (w *Worker) Start() {
	if w.running {
		return
	}
	w.running = true
	ctx, cancel := context.WithCancel(context.Background())
	w.task = ctx
	w.cancel = cancel
	w.wg.Add(1)
	go w.run()
	fmt.Printf("%s started\n", w.name)
}

// Stop stops the worker.
func (w *Worker) Stop() {
	if !w.running {
		return
	}
	w.running = false
	if w.cancel != nil {
		w.cancel()
	}
	w.wg.Wait()
	fmt.Printf("%s stopped\n", w.name)
}

func (w *Worker) run() {
	defer w.wg.Done()
	for w.running {
		select {
		case <-w.task.Done():
			return
		default:
		}
		task := w.queue.Dequeue()
		if task != nil {
			w.processTask(task)
		} else {
			time.Sleep(100 * time.Millisecond)
		}
	}
}

func (w *Worker) processTask(task *Task) {
	ctx, cancel := context.WithTimeout(context.Background(), 5*time.Second)
	defer cancel()
	fmt.Printf("%s processing task %s\n", w.name, task.ID)
	result, err := task.Func(ctx, task.Args...)
	if err != nil {
		fmt.Printf("%s failed task %s: %v\n", w.name, task.ID, err)
		w.queue.FailTask(task.ID, err.Error())
		return
	}
	w.queue.CompleteTask(task.ID)
	fmt.Printf("%s completed task %s with result: %v\n", w.name, task.ID, result)
}

// demoTaskSuccess succeeds after sleeping.
func demoTaskSuccess(ctx context.Context, args ...interface{}) (interface{}, error) {
	name := "task"
	if len(args) > 0 {
		if s, ok := args[0].(string); ok {
			name = s
		}
	}
	select {
	case <-time.After(100 * time.Millisecond):
	case <-ctx.Done():
		return nil, ctx.Err()
	}
	return fmt.Sprintf("Success: %s", name), nil
}

// demoTaskFailure fails after sleeping.
func demoTaskFailure(ctx context.Context, args ...interface{}) (interface{}, error) {
	name := "task"
	if len(args) > 0 {
		if s, ok := args[0].(string); ok {
			name = s
		}
	}
	select {
	case <-time.After(100 * time.Millisecond):
	case <-ctx.Done():
		return nil, ctx.Err()
	}
	return nil, fmt.Errorf("Intentional failure for %s", name)
}

// generateID creates a simple unique task ID.
var taskIDCounter int
var taskIDMu sync.Mutex

func generateID() string {
	taskIDMu.Lock()
	defer taskIDMu.Unlock()
	taskIDCounter++
	return fmt.Sprintf("task-%d-%d", time.Now().UnixNano(), taskIDCounter)
}

// NewTask creates a new Task.
func NewTask(fn func(context.Context, ...interface{}) (interface{}, error), args []interface{}, priority Priority, maxRetries int) *Task {
	now := float64(time.Now().UnixNano()) / 1e9
	return &Task{
		ID:            generateID(),
		Func:          fn,
		Args:          args,
		Priority:      priority,
		MaxRetries:    maxRetries,
		RetryCount:    0,
		BackoffFactor: 2.0,
		Status:        PENDING,
		CreatedAt:     now,
		ScheduledAt:   now,
	}
}

func main() {
	fmt.Println("=== Async Task Queue Demo ===")
	fmt.Println()

	queue := NewTaskQueue()
	worker := NewWorker(queue, "DemoWorker")
	worker.Start()

	tasks := []*Task{}

	for i := 0; i < 3; i++ {
		task := NewTask(demoTaskSuccess, []interface{}{fmt.Sprintf("High Priority Task %d", i)}, HIGH, 2)
		tasks = append(tasks, task)
		queue.Enqueue(task)
	}

	for i := 0; i < 5; i++ {
		var fn func(context.Context, ...interface{}) (interface{}, error)
		if i%2 == 0 {
			fn = demoTaskSuccess
		} else {
			fn = demoTaskFailure
		}
		task := NewTask(fn, []interface{}{fmt.Sprintf("Normal Task %d", i)}, NORMAL, 3)
		tasks = append(tasks, task)
		queue.Enqueue(task)
	}

	for i := 0; i < 2; i++ {
		task := NewTask(demoTaskSuccess, []interface{}{fmt.Sprintf("Low Priority Task %d", i)}, LOW, 1)
		tasks = append(tasks, task)
		queue.Enqueue(task)
	}

	fmt.Printf("Enqueued %d tasks\n\n", len(tasks))

	time.Sleep(5 * time.Second)

	stats := queue.GetStats()
	fmt.Println("=== Processing Statistics ===")
	for key, value := range stats {
		fmt.Printf("%s: %d\n", capitalize(key), value)
	}

	dlq := queue.GetDeadLetterQueue()
	if len(dlq) > 0 {
		fmt.Println("\n=== Dead Letter Queue ===")
		for _, task := range dlq {
			var errStr string
			if task.Error != nil {
				errStr = *task.Error
			}
			fmt.Printf("Task %s: %s\n", task.ID, errStr)
		}
	}

	worker.Stop()
	fmt.Println("\n=== Demo Complete ===")
}

func capitalize(s string) string {
	if s == "" {
		return ""
	}
	return strings.ToUpper(s[:1]) + s[1:]
}
