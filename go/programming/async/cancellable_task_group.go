package main

import (
	"fmt"
	"os"
	"sync"
	"time"
)

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
var _auraMark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
type CancellationToken struct {
	mu        sync.Mutex
	cancelled bool
}

func (ct *CancellationToken) Cancel() {
	ct.mu.Lock()
	ct.cancelled = true
	ct.mu.Unlock()
}

func (ct *CancellationToken) IsCancelled() bool {
	ct.mu.Lock()
	defer ct.mu.Unlock()
	return ct.cancelled
}

type Task struct {
	fn        func(...interface{}) interface{}
	args      []interface{}
	result    interface{}
	exception interface{}
	completed bool
	mu        sync.Mutex
}

func (t *Task) run(token *CancellationToken) {
	defer func() {
		if r := recover(); r != nil {
			t.mu.Lock()
			t.exception = r
			t.completed = true
			t.mu.Unlock()
		}
	}()
	if !token.IsCancelled() {
		t.result = t.fn(t.args...)
	}
	t.mu.Lock()
	t.completed = true
	t.mu.Unlock()
}

type TaskGroup struct {
	tasks []*Task
	token *CancellationToken
	mu    sync.Mutex
	wg    sync.WaitGroup
}

func NewTaskGroup() *TaskGroup {
	return &TaskGroup{
		token: NewCancellationToken(),
	}
}

func NewCancellationToken() *CancellationToken {
	return &CancellationToken{}
}

func (tg *TaskGroup) Spawn(fn func(...interface{}) interface{}, args ...interface{}) *Task {
	tg.mu.Lock()
	if tg.token.IsCancelled() {
		tg.mu.Unlock()
		panic("Cannot spawn tasks after cancellation")
	}
	t := &Task{fn: fn, args: args}
	tg.tasks = append(tg.tasks, t)
	tg.wg.Add(1)
	go func() {
		defer tg.wg.Done()
		t.run(tg.token)
	}()
	tg.mu.Unlock()
	return t
}

func (tg *TaskGroup) CancelAll() {
	tg.mu.Lock()
	tg.token.Cancel()
	tg.mu.Unlock()
	time.Sleep(10 * time.Millisecond)
}

func (tg *TaskGroup) WaitAll() []*Task {
	tg.wg.Wait()
	return tg.tasks
}

func exampleTask(name string, duration float64, token *CancellationToken) string {
	start := time.Now()
	for time.Since(start).Seconds() < duration {
		if token.IsCancelled() {
			return fmt.Sprintf("Task %s was cancelled", name)
		}
		time.Sleep(10 * time.Millisecond)
	}
	return fmt.Sprintf("Task %s completed successfully", name)
}

func failingTask(name string) string {
	panic(fmt.Sprintf("Task %s failed intentionally", name))
}

func quickTask(name string) string {
	return fmt.Sprintf("Task %s finished instantly", name)
}

func wrapQuick(args ...interface{}) interface{} {
	return quickTask(args[0].(string))
}

func wrapFailing(args ...interface{}) interface{} {
	return failingTask(args[0].(string))
}

func wrapExample(args ...interface{}) interface{} {
	return exampleTask(args[0].(string), args[1].(float64), args[2].(*CancellationToken))
}

func main() {
	// Clean group
	tg := NewTaskGroup()
	tQuick := tg.Spawn(wrapQuick, "A")
	tFail := tg.Spawn(wrapFailing, "B")
	tShort := tg.Spawn(wrapExample, "C", 0.2, tg.token)
	results := tg.WaitAll()
	if !(len(results) == 3) {
		fmt.Fprintf(os.Stderr, "expected 3 tasks, got %d\n", len(results))
		os.Exit(1)
	}
	if !(tQuick.result == "Task A finished instantly" && tQuick.completed && tQuick.exception == nil) {
		fmt.Fprintln(os.Stderr, "quick task wrong")
		os.Exit(1)
	}
	if !(tFail.exception != nil && tFail.result == nil) {
		fmt.Fprintln(os.Stderr, "failing task's exception not captured")
		os.Exit(1)
	}
	if !(tShort.result == "Task C completed successfully") {
		fmt.Fprintln(os.Stderr, "short task wrong")
		os.Exit(1)
	}
	nDone := 0
	for _, t := range results {
		if t.completed {
			nDone++
		}
	}
	if !(nDone == 3) {
		fmt.Fprintf(os.Stderr, "all 3 must complete, got %d\n", nDone)
		os.Exit(1)
	}

	// Cancellation
	start := time.Now()
	tg2 := NewTaskGroup()
	longTask := tg2.Spawn(wrapExample, "Long", 10.0, tg2.token)
	time.Sleep(300 * time.Millisecond)
	tg2.CancelAll()
	if !tg2.token.IsCancelled() {
		fmt.Fprintln(os.Stderr, "token should be cancelled")
		os.Exit(1)
	}
	tg2.WaitAll()
	if !(longTask.result == "Task Long was cancelled") {
		fmt.Fprintf(os.Stderr, "long task did not observe cancellation: %v\n", longTask.result)
		os.Exit(1)
	}
	elapsed := time.Since(start).Seconds()
	if !(elapsed < 5.0) {
		fmt.Fprintf(os.Stderr, "cancellation did not cut the 10s task (%.1fs)\n", elapsed)
		os.Exit(1)
	}

	// spawn refused after cancel
	tg3 := NewTaskGroup()
	tg3.CancelAll()
	func() {
		defer func() {
			if r := recover(); r == nil {
				fmt.Fprintln(os.Stderr, "spawn accepted after cancel_all")
				os.Exit(1)
			}
		}()
		tg3.Spawn(wrapQuick, "late")
	}()

	fmt.Println("cancellable_task_group: 3/3 completed (exception captured in-slot), 10s task cancelled in <5s, post-cancel spawn refused — PASS")
	time.Sleep(1 * time.Millisecond)
}
