package main

import (
	"container/heap"
	"context"
	"fmt"
	"math"
	"os"
	"sort"
	"sync"
	"time"
)

// TaskStatus represents possible task statuses.
// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
var _auraMark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
type TaskStatus string

const (
	Pending    TaskStatus = "pending"
	Processing TaskStatus = "processing"
	Completed  TaskStatus = "completed"
	Failed     TaskStatus = "failed"
	Retrying   TaskStatus = "retrying"
)

// Priority represents task priority levels.
type Priority int

const (
	Low      Priority = 3
	Normal   Priority = 2
	High     Priority = 1
	Critical Priority = 0
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

// taskHeap implements heap.Interface for *Task.
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

func nowSeconds() float64 {
	return float64(time.Now().UnixNano()) / 1e9
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
	fmt.Printf("Enqueued task %s with priority %s\n", task.ID, priorityName(task.Priority))
	return task.ID, nil
}

// Dequeue removes and returns the highest priority ready task from the queue.
func (q *TaskQueue) Dequeue() *Task {
	q.mu.Lock()
	defer q.mu.Unlock()
	for q.queue.Len() > 0 {
		task := heap.Pop(&q.queue).(*Task)
		if task.ScheduledAt <= nowSeconds() {
			task.Status = Processing
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
		task.Status = Completed
		n := nowSeconds()
		task.CompletedAt = &n
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
			task.Status = Retrying
			backoff := task.CalculateBackoff()
			task.ScheduledAt = nowSeconds() + backoff
			heap.Push(&q.queue, task)
			q.stats["retried"]++
			fmt.Printf("Retrying task %s in %.2f seconds (attempt %d)\n", taskID, backoff, task.RetryCount)
		} else {
			task.Status = Failed
			n := nowSeconds()
			task.CompletedAt = &n
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
	return math.Pow(t.BackoffFactor, float64(t.RetryCount))
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

// GetStatsSortedKeys returns sorted keys of statistics for deterministic printing.
func (q *TaskQueue) GetStatsSortedKeys() []string {
	stats := q.GetStats()
	keys := make([]string, 0, len(stats))
	for k := range stats {
		keys = append(keys, k)
	}
	sort.Strings(keys)
	return keys
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
	cancel  context.CancelFunc
	wg      sync.WaitGroup
	mu      sync.Mutex
}

// NewWorker creates a new Worker.
func NewWorker(queue *TaskQueue, name string) *Worker {
	return &Worker{queue: queue, name: name}
}

// Start starts the worker.
func (w *Worker) Start() {
	w.mu.Lock()
	defer w.mu.Unlock()
	if w.running {
		return
	}
	w.running = true
	ctx, cancel := context.WithCancel(context.Background())
	w.cancel = cancel
	w.wg.Add(1)
	go w.run(ctx)
	fmt.Printf("%s started\n", w.name)
}

// Stop stops the worker.
func (w *Worker) Stop() {
	w.mu.Lock()
	if !w.running {
		w.mu.Unlock()
		return
	}
	w.running = false
	cancel := w.cancel
	w.mu.Unlock()
	if cancel != nil {
		cancel()
	}
	w.wg.Wait()
	fmt.Printf("%s stopped\n", w.name)
}

func (w *Worker) run(ctx context.Context) {
	defer w.wg.Done()
	for {
		select {
		case <-ctx.Done():
			return
		default:
		}
		task := w.queue.Dequeue()
		if task != nil {
			w.processTask(task)
		} else {
			select {
			case <-ctx.Done():
				return
			case <-time.After(100 * time.Millisecond):
			}
		}
	}
}

func (w *Worker) processTask(task *Task) {
	ctx, cancel := context.WithTimeout(context.Background(), 5*time.Second)
	defer cancel()
	fmt.Printf("%s processing task %s\n", w.name, task.ID)
	result, err := task.Func(ctx, task.Args...)
	if err != nil {
		errorMsg := err.Error()
		fmt.Printf("%s failed task %s: %s\n", w.name, task.ID, errorMsg)
		w.queue.FailTask(task.ID, errorMsg)
		return
	}
	w.queue.CompleteTask(task.ID)
	fmt.Printf("%s completed task %s with result: %v\n", w.name, task.ID, result)
}

func priorityName(p Priority) string {
	switch p {
	case Critical:
		return "CRITICAL"
	case High:
		return "HIGH"
	case Normal:
		return "NORMAL"
	case Low:
		return "LOW"
	default:
		return "UNKNOWN"
	}
}

var (
	idCounter int
	idMu      sync.Mutex
)

func generateID() string {
	idMu.Lock()
	defer idMu.Unlock()
	idCounter++
	return fmt.Sprintf("task-%d", idCounter)
}

// NewTask creates a new Task with default fields.
func NewTask(fn func(context.Context, ...interface{}) (interface{}, error), args []interface{}, priority Priority, maxRetries int) *Task {
	n := nowSeconds()
	return &Task{
		ID:            generateID(),
		Func:          fn,
		Args:          args,
		Priority:      priority,
		MaxRetries:    maxRetries,
		RetryCount:    0,
		BackoffFactor: 2.0,
		Status:        Pending,
		CreatedAt:     n,
		ScheduledAt:   n,
	}
}

// Demo task functions.
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

func main() {
	// 1. Priority order, queue driven by hand.
	q := NewTaskQueue()
	tLow := NewTask(demoTaskSuccess, []interface{}{"low"}, Low, 3)
	tHigh := NewTask(demoTaskSuccess, []interface{}{"high"}, High, 3)
	tNorm := NewTask(demoTaskSuccess, []interface{}{"norm"}, Normal, 3)
	for _, t := range []*Task{tLow, tHigh, tNorm} {
		if _, err := q.Enqueue(t); err != nil {
			fmt.Fprintf(os.Stderr, "enqueue error: %v\n", err)
			os.Exit(1)
		}
	}

	var order []string
	for i := 0; i < 3; i++ {
		t := q.Dequeue()
		if t == nil {
			fmt.Fprintln(os.Stderr, "ASSERT FAILED: expected a task from non-empty queue")
			os.Exit(1)
		}
		if s, ok := t.Args[0].(string); ok {
			order = append(order, s)
		} else {
			order = append(order, "")
		}
	}
	if !(len(order) == 3 && order[0] == "high" && order[1] == "norm" && order[2] == "low") {
		fmt.Fprintf(os.Stderr, "ASSERT FAILED: priority dequeue order wrong: %v\n", order)
		os.Exit(1)
	}
	if q.Dequeue() != nil {
		fmt.Fprintln(os.Stderr, "ASSERT FAILED: empty queue dequeued something")
		os.Exit(1)
	}

	// complete_task: honest bookkeeping.
	if q.CompleteTask(tHigh.ID) != true {
		fmt.Fprintln(os.Stderr, "ASSERT FAILED: complete high should succeed")
		os.Exit(1)
	}
	if q.CompleteTask(tHigh.ID) != false {
		fmt.Fprintln(os.Stderr, "ASSERT FAILED: double complete reported success")
		os.Exit(1)
	}
	if q.CompleteTask("ghost") != false {
		fmt.Fprintln(os.Stderr, "ASSERT FAILED: complete ghost should fail")
		os.Exit(1)
	}
	q.CompleteTask(tNorm.ID)
	q.CompleteTask(tLow.ID)
	stats := q.GetStats()
	if !(stats["completed"] == 3 && stats["processing"] == 0) {
		fmt.Fprintf(os.Stderr, "ASSERT FAILED: expected completed==3 and processing==0, got %v\n", stats)
		os.Exit(1)
	}

	// 2. RETRY: a failed task is rescheduled with backoff -- NOT immediately
	// dequeuable -- and lands in the DLQ only after max_retries.
	flaky := NewTask(demoTaskFailure, []interface{}{"flaky"}, Normal, 1)
	if _, err := q.Enqueue(flaky); err != nil {
		fmt.Fprintf(os.Stderr, "enqueue error: %v\n", err)
		os.Exit(1)
	}
	got := q.Dequeue()
	if got == nil || got.ID != flaky.ID {
		fmt.Fprintln(os.Stderr, "ASSERT FAILED: dequeued task should be flaky")
		os.Exit(1)
	}
	if q.FailTask(flaky.ID, "boom-1") != true {
		fmt.Fprintln(os.Stderr, "ASSERT FAILED: fail_task should succeed")
		os.Exit(1)
	}
	stats = q.GetStats()
	if !(stats["retried"] == 1 && stats["dead_letter"] == 0) {
		fmt.Fprintf(os.Stderr, "ASSERT FAILED: expected retried==1 dead_letter==0, got %v\n", stats)
		os.Exit(1)
	}
	if q.Dequeue() != nil {
		fmt.Fprintln(os.Stderr, "ASSERT FAILED: retrying task was dequeuable BEFORE its backoff elapsed")
		os.Exit(1)
	}
	// Make it due now, fail again -> exhausted -> DLQ with the error recorded.
	flaky.ScheduledAt = nowSeconds() - 1
	heapTask := q.Dequeue()
	if heapTask == nil || heapTask.ID != flaky.ID {
		fmt.Fprintln(os.Stderr, "ASSERT FAILED: expected flaky task after making it due")
		os.Exit(1)
	}
	q.FailTask(flaky.ID, "boom-2")
	dlq := q.GetDeadLetterQueue()
	if !(len(dlq) == 1 && dlq[0].ID == flaky.ID) {
		fmt.Fprintln(os.Stderr, "ASSERT FAILED: exhausted task not in DLQ")
		os.Exit(1)
	}
	if !(dlq[0].Error != nil && *dlq[0].Error == "boom-2" && dlq[0].Status == Failed) {
		fmt.Fprintln(os.Stderr, "ASSERT FAILED: DLQ task error/status mismatch")
		os.Exit(1)
	}
	if dlq[0].RetryCount != 1 {
		fmt.Fprintf(os.Stderr, "ASSERT FAILED: expected retry_count==1, got %d\n", dlq[0].RetryCount)
		os.Exit(1)
	}

	// 3. Integration: a real worker drains 3 successes + 1 permanent failure.
	wq := NewTaskQueue()
	worker := NewWorker(wq, "TestWorker")
	worker.Start()
	for i := 0; i < 3; i++ {
		if _, err := wq.Enqueue(NewTask(demoTaskSuccess, []interface{}{fmt.Sprintf("ok-%d", i)}, High, 0)); err != nil {
			fmt.Fprintf(os.Stderr, "enqueue error: %v\n", err)
			os.Exit(1)
		}
	}
	if _, err := wq.Enqueue(NewTask(demoTaskFailure, []interface{}{"dead"}, High, 0)); err != nil {
		fmt.Fprintf(os.Stderr, "enqueue error: %v\n", err)
		os.Exit(1)
	}
	for i := 0; i < 80; i++ {
		wqs := wq.GetStats()
		if wqs["completed"] == 3 && wqs["failed"] == 1 {
			break
		}
		time.Sleep(100 * time.Millisecond)
	}
	worker.Stop()
	stats = wq.GetStats()
	if stats["completed"] != 3 {
		fmt.Fprintf(os.Stderr, "ASSERT FAILED: worker must complete 3 tasks, stats: %v\n", stats)
		os.Exit(1)
	}
	if !(stats["failed"] == 1 && stats["dead_letter"] == 1) {
		fmt.Fprintf(os.Stderr, "ASSERT FAILED: failure not dead-lettered: %v\n", stats)
		os.Exit(1)
	}
	if !(stats["pending"] == 0 && stats["processing"] == 0) {
		fmt.Fprintf(os.Stderr, "ASSERT FAILED: queue not drained: %v\n", stats)
		os.Exit(1)
	}

	fmt.Println("async_task_queue: dequeue high->norm->low, backoff blocks early retry, " +
		"exhaustion -> DLQ (boom-2, 1 retry), worker drained 3+1 exact -- PASS")
}
