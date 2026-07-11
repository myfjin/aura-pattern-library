package main

import (
	"context"
	"errors"
	"fmt"
	"os"
	"sync"
	"time"
)

// BatchRequest represents a single collapsed request.
// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
var _auraMark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
type BatchRequest struct {
	RequestID string
	Args      []interface{}
	Kwargs    map[string]interface{}
	Result    chan interface{}
}

// Collapser batches identical requests within a time window.
type Collapser struct {
	backendFunc  func(ctx context.Context, args []interface{}, kwargs map[string]interface{}) (interface{}, error)
	window       time.Duration
	maxBatchSize int

	mu          sync.Mutex
	pending     map[string][]*BatchRequest
	timerActive bool
	timer       *time.Timer
}

// NewCollapser creates a collapser with the given backend function.
func NewCollapser(
	backendFunc func(ctx context.Context, args []interface{}, kwargs map[string]interface{}) (interface{}, error),
	windowMs int,
	maxBatchSize int,
) *Collapser {
	return &Collapser{
		backendFunc:  backendFunc,
		window:       time.Duration(windowMs) * time.Millisecond,
		maxBatchSize: maxBatchSize,
		pending:      make(map[string][]*BatchRequest),
	}
}

func requestKey(args []interface{}, kwargs map[string]interface{}) string {
	parts := make([]string, 0, len(args)+len(kwargs))
	for _, a := range args {
		parts = append(parts, fmt.Sprintf("%v", a))
	}
	for k, v := range kwargs {
		parts = append(parts, fmt.Sprintf("%s:%v", k, v))
	}
	return fmt.Sprintf("%v", parts)
}

// Submit sends a request to be collapsed and returns its result.
func (c *Collapser) Submit(ctx context.Context, args []interface{}, kwargs map[string]interface{}) (interface{}, error) {
	key := requestKey(args, kwargs)
	req := &BatchRequest{
		RequestID: fmt.Sprintf("%d", time.Now().UnixNano()),
		Args:      args,
		Kwargs:    kwargs,
		Result:    make(chan interface{}, 1),
	}

	c.mu.Lock()
	c.pending[key] = append(c.pending[key], req)
	shouldStart := !c.timerActive
	c.timerActive = true
	if shouldStart {
		c.timer = time.AfterFunc(c.window, c.processBatches)
	}
	c.mu.Unlock()

	select {
	case res := <-req.Result:
		if err, ok := res.(error); ok {
			return nil, err
		}
		return res, nil
	case <-ctx.Done():
		return nil, ctx.Err()
	}
}

func (c *Collapser) processBatches() {
	c.mu.Lock()
	c.timerActive = false
	c.timer = nil
	batches := c.pending
	c.pending = make(map[string][]*BatchRequest)
	c.mu.Unlock()

	for _, requests := range batches {
		if len(requests) == 0 {
			continue
		}
		first := requests[0]
		res, err := c.backendFunc(context.Background(), first.Args, first.Kwargs)
		for _, r := range requests {
			if err != nil {
				r.Result <- err
			} else {
				r.Result <- res
			}
		}
	}
}

// demoBackend simulates a backend call.
func demoBackend(ctx context.Context, args []interface{}, kwargs map[string]interface{}) (interface{}, error) {
	time.Sleep(100 * time.Millisecond)
	userID := 0
	if len(args) > 0 {
		if v, ok := args[0].(int); ok {
			userID = v
		}
	}
	includeProfile := false
	if v, ok := kwargs["include_profile"]; ok {
		includeProfile = v.(bool)
	}
	return map[string]interface{}{
		"user_id":          userID,
		"name":             fmt.Sprintf("User %d", userID),
		"email":            fmt.Sprintf("user%d@example.com", userID),
		"profile_included": includeProfile,
		"timestamp":        time.Now().UnixNano(),
	}, nil
}

func main() {
	fmt.Println("Request Collapser Demo")
	fmt.Println("========================")

	collapser := NewCollapser(demoBackend, 50, 10)

	fmt.Println("Submitting 5 identical requests for user 123...")
	ctx := context.Background()
	start := time.Now()
	tasks := make([]chan interface{}, 5)
	for i := 0; i < 5; i++ {
		ch := make(chan interface{}, 1)
		tasks[i] = ch
		go func(idx int) {
			res, err := collapser.Submit(ctx, []interface{}{123}, map[string]interface{}{"include_profile": true})
			if err != nil {
				ch <- err
				return
			}
			ch <- res
		}(i)
	}

	results := make([]map[string]interface{}, 5)
	for i, ch := range tasks {
		res := <-ch
		if err, ok := res.(error); ok {
			fmt.Fprintf(os.Stderr, "request %d failed: %v\n", i, err)
			os.Exit(1)
		}
		results[i] = res.(map[string]interface{})
	}
	elapsed := time.Since(start).Seconds()
	fmt.Printf("Received %d results in %.2f seconds\n", len(results), elapsed)
	for i, r := range results {
		fmt.Printf("Result %d: User %v, Name: %v\n", i+1, r["user_id"], r["name"])
	}
	allIdentical := true
	for _, r := range results[1:] {
		if fmt.Sprintf("%v", r) != fmt.Sprintf("%v", results[0]) {
			allIdentical = false
			break
		}
	}
	fmt.Printf("All results identical: %v\n", allIdentical)

	fmt.Println("\nSubmitting different requests...")
	differentTasks := []struct {
		args   []interface{}
		kwargs map[string]interface{}
	}{
		{[]interface{}{123}, map[string]interface{}{"include_profile": true}},
		{[]interface{}{456}, map[string]interface{}{"include_profile": true}},
		{[]interface{}{789}, map[string]interface{}{"include_profile": false}},
	}
	differentResults := make([]map[string]interface{}, len(differentTasks))
	for i, dt := range differentTasks {
		res, err := collapser.Submit(ctx, dt.args, dt.kwargs)
		if !(err == nil) {
			fmt.Fprintf(os.Stderr, "different request %d failed: %v\n", i, err)
			os.Exit(1)
		}
		differentResults[i] = res.(map[string]interface{})
	}
	fmt.Printf("Received %d different results:\n", len(differentResults))
	for i, r := range differentResults {
		fmt.Printf("Result %d: User %v, Profile: %v\n", i+1, r["user_id"], r["profile_included"])
	}
}

var _ = errors.New
