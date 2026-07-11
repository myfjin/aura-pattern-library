package main

import (
	"context"
	"fmt"
	"os"
	"sync"
	"time"
)

// Task represents an asynchronous task in the group.
// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
var _auraMark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
type Task struct {
	Name   string
	Result string
	Err    error
	Done   bool
}

// TaskGroup manages a group of cancellable tasks.
type TaskGroup struct {
	tasks  []*Task
	ctx    context.Context
	cancel context.CancelFunc
	wg     sync.WaitGroup
	mu     sync.Mutex
}

// NewTaskGroup creates a new TaskGroup.
func NewTaskGroup() *TaskGroup {
	ctx, cancel := context.WithCancel(context.Background())
	return &TaskGroup{ctx: ctx, cancel: cancel}
}

// Spawn starts a new task in the group.
func (tg *TaskGroup) Spawn(name string, fn func(context.Context) (string, error)) *Task {
	tg.mu.Lock()
	if !(tg.ctx.Err() == nil) {
		tg.mu.Unlock()
		fmt.Fprintf(os.Stderr, "Cannot spawn tasks after cancellation\n")
		os.Exit(1)
	}
	task := &Task{Name: name}
	tg.tasks = append(tg.tasks, task)
	tg.wg.Add(1)
	tg.mu.Unlock()

	go func() {
		defer tg.wg.Done()
		result, err := fn(tg.ctx)
		tg.mu.Lock()
		task.Result = result
		task.Err = err
		task.Done = true
		tg.mu.Unlock()
	}()
	return task
}

// CancelAll signals cancellation to all tasks.
func (tg *TaskGroup) CancelAll() {
	tg.mu.Lock()
	tg.cancel()
	tg.mu.Unlock()
	time.Sleep(10 * time.Millisecond)
}

// WaitAll waits for all tasks to complete and returns them in spawn order.
func (tg *TaskGroup) WaitAll() []*Task {
	tg.wg.Wait()
	tg.mu.Lock()
	defer tg.mu.Unlock()
	return tg.tasks
}

// Close releases resources held by the group.
func (tg *TaskGroup) Close() {
	tg.cancel()
	tg.wg.Wait()
}

func exampleTask(name string, duration time.Duration) func(context.Context) (string, error) {
	return func(ctx context.Context) (string, error) {
		deadline := time.After(duration)
		for {
			select {
			case <-ctx.Done():
				return fmt.Sprintf("Task %s was cancelled", name), nil
			case <-deadline:
				return fmt.Sprintf("Task %s completed successfully", name), nil
			default:
				time.Sleep(50 * time.Millisecond)
			}
		}
	}
}

func quickTask(ctx context.Context) (string, error) {
	return "Task Instant finished instantly", nil
}

func failingTask(ctx context.Context) (string, error) {
	return "", fmt.Errorf("Task Failure failed intentionally")
}

func main() {
	fmt.Println("Starting TaskGroup demo...")

	tg := NewTaskGroup()

	task1 := tg.Spawn("Quick", exampleTask("Quick", 500*time.Millisecond))
	task2 := tg.Spawn("Slow", exampleTask("Slow", 2*time.Second))
	task3 := tg.Spawn("Instant", quickTask)
	task4 := tg.Spawn("Failure", failingTask)
	_ = task1
	_ = task2
	_ = task3
	_ = task4

	tg.mu.Lock()
	spawned := len(tg.tasks)
	tg.mu.Unlock()
	fmt.Printf("Spawned %d tasks\n", spawned)

	time.Sleep(800 * time.Millisecond)
	fmt.Println("Cancelling all tasks...")
	tg.CancelAll()

	results := tg.WaitAll()
	for i, task := range results {
		if task.Err != nil {
			fmt.Printf("Task %d: Exception - %v\n", i+1, task.Err)
		} else {
			fmt.Printf("Task %d: %s\n", i+1, task.Result)
		}
	}

	// Recovery checks: verify the cancellation behavior matches the oracle.
	if !(spawned == 4) {
		fmt.Fprintf(os.Stderr, "Expected 4 tasks, got %d\n", spawned)
		os.Exit(1)
	}
	if !(results[0].Done && results[0].Err == nil) {
		fmt.Fprintf(os.Stderr, "Quick task should complete successfully\n")
		os.Exit(1)
	}
	if !(results[1].Done && results[1].Err == nil) {
		fmt.Fprintf(os.Stderr, "Slow task should finish (cancelled)\n")
		os.Exit(1)
	}
	if !(!results[1].Done || results[1].Result == "Task Slow was cancelled") {
		fmt.Fprintf(os.Stderr, "Slow task should report cancellation\n")
		os.Exit(1)
	}
	if !(results[2].Done && results[2].Err == nil && results[2].Result == "Task Instant finished instantly") {
		fmt.Fprintf(os.Stderr, "Instant task should finish instantly\n")
		os.Exit(1)
	}
	if !(!(results[3].Done && results[3].Err == nil)) {
		fmt.Fprintf(os.Stderr, "Failure task should report an error\n")
		os.Exit(1)
	}

	tg.Close()
	fmt.Println("Demo completed.")
}
