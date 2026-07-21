package main

import (
	"context"
	"fmt"
	"os"
	"sort"
	"strconv"
	"strings"
	"sync"
	"time"
)

// Request collapser: identical concurrent calls arriving within a time window are
// coalesced into a single backend call whose result (or error) fans out to every
// waiter; distinct request keys are kept separate. Keys normalize by sorting kwargs.
// Use to shed duplicate load (cache stampede / thundering herd) on an expensive backend.
// Guarantees (self-test): 5 identical calls -> 1 backend call, 3 distinct keys stay 3
// calls, a backend failure reaches all collapsed waiters, sync backends still collapse.
// BatchRequest represents a batched request with its identifier and arguments.
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

// requestKey generates a unique key for a request based on its arguments.
// Kwargs are sorted by key name, matching the Python implementation.
func requestKey(args []interface{}, kwargs map[string]interface{}) string {
	parts := make([]string, 0, len(args)+len(kwargs))
	for _, a := range args {
		parts = append(parts, fmt.Sprintf("%v", a))
	}
	keys := make([]string, 0, len(kwargs))
	for k := range kwargs {
		keys = append(keys, k)
	}
	sort.Strings(keys)
	for _, k := range keys {
		parts = append(parts, fmt.Sprintf("%s:%v", k, kwargs[k]))
	}
	return strings.Join(parts, "|")
}

// Submit sends a request to be collapsed and returns its result.
func (c *Collapser) Submit(ctx context.Context, args []interface{}, kwargs map[string]interface{}) (interface{}, error) {
	key := requestKey(args, kwargs)
	req := &BatchRequest{
		RequestID: strconv.FormatInt(time.Now().UnixNano(), 10),
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

func main() {
	calls := 0
	callArgs := []int{}

	countingBackend := func(ctx context.Context, args []interface{}, kwargs map[string]interface{}) (interface{}, error) {
		calls++
		if len(args) > 0 {
			if v, ok := args[0].(int); ok {
				callArgs = append(callArgs, v)
			}
		}
		time.Sleep(0)
		return map[string]interface{}{
			"user_id": args[0],
			"call_no": calls,
		}, nil
	}

	c := NewCollapser(countingBackend, 20, 10)

	// Request-key derivation is exact and order-normalizes kwargs.
	if got := requestKey([]interface{}{1}, map[string]interface{}{"b": 2, "a": 3}); got != "1|a:3|b:2" {
		fmt.Fprintf(os.Stderr, "request key must sort kwargs for stable identity: got %q\n", got)
		os.Exit(1)
	}

	// 5 identical concurrent requests = 1 backend call.
	ctx := context.Background()
	var wg sync.WaitGroup
	results := make([]map[string]interface{}, 5)
	errs := make([]error, 5)
	for i := 0; i < 5; i++ {
		wg.Add(1)
		go func(idx int) {
			defer wg.Done()
			res, err := c.Submit(ctx, []interface{}{123}, map[string]interface{}{"include_profile": true})
			errs[idx] = err
			if err == nil {
				results[idx] = res.(map[string]interface{})
			}
		}(i)
	}
	wg.Wait()
	if calls != 1 {
		fmt.Fprintf(os.Stderr, "5 identical requests caused %d backend calls, not 1\n", calls)
		os.Exit(1)
	}
	if !(calls == 1) {
		fmt.Fprintf(os.Stderr, "5 identical requests caused %d backend calls, not 1\n", calls)
		os.Exit(1)
	}
	first := results[0]
	for _, r := range results[1:] {
		if !(fmt.Sprintf("%v", r) == fmt.Sprintf("%v", first)) {
			fmt.Fprintln(os.Stderr, "collapsed waiters got different results")
			os.Exit(1)
		}
	}
	if !(first["user_id"] == 123 && first["call_no"] == 1) {
		fmt.Fprintf(os.Stderr, "unexpected result: %v\n", first)
		os.Exit(1)
	}
	if !(len(results) == 5) {
		fmt.Fprintln(os.Stderr, "expected 5 results")
		os.Exit(1)
	}

	// Distinct requests must NOT be collapsed: 3 keys → exactly 3 more calls.
	r2 := make([]map[string]interface{}, 3)
	var wg2 sync.WaitGroup
	tasks := [][2]interface{}{
		{123, true},
		{456, true},
		{789, false},
	}
	for i, t := range tasks {
		wg2.Add(1)
		go func(idx int, userID int, includeProfile bool) {
			defer wg2.Done()
			res, err := c.Submit(ctx, []interface{}{userID}, map[string]interface{}{"include_profile": includeProfile})
			if err != nil {
				fmt.Fprintf(os.Stderr, "distinct request failed: %v\n", err)
				os.Exit(1)
			}
			r2[idx] = res.(map[string]interface{})
		}(i, t[0].(int), t[1].(bool))
	}
	wg2.Wait()
	if calls != 4 {
		fmt.Fprintf(os.Stderr, "3 distinct requests after 1 must total 4 calls, got %d\n", calls)
		os.Exit(1)
	}
	if !(calls == 4) {
		fmt.Fprintf(os.Stderr, "3 distinct requests after 1 must total 4 calls, got %d\n", calls)
		os.Exit(1)
	}
	if r2[0]["user_id"] != 123 || r2[1]["user_id"] != 456 || r2[2]["user_id"] != 789 {
		fmt.Fprintf(os.Stderr, "unexpected user_ids: %v\n", r2)
		os.Exit(1)
	}
	want := []int{123, 456, 789}
	if !(r2[0]["user_id"] == want[0] && r2[1]["user_id"] == want[1] && r2[2]["user_id"] == want[2]) {
		fmt.Fprintf(os.Stderr, "unexpected user_ids: %v\n", r2)
		os.Exit(1)
	}
	for i, w := range want {
		if !(r2[i]["user_id"] == w) {
			fmt.Fprintf(os.Stderr, "expected user_ids %v, got %v\n", want, r2)
			os.Exit(1)
		}
	}

	// Backend exception must reach every collapsed waiter.
	failingBackend := func(ctx context.Context, args []interface{}, kwargs map[string]interface{}) (interface{}, error) {
		return nil, fmt.Errorf("backend down")
	}
	f := NewCollapser(failingBackend, 20, 10)
	failures := make([]error, 2)
	var wg3 sync.WaitGroup
	for i := 0; i < 2; i++ {
		wg3.Add(1)
		go func(idx int) {
			defer wg3.Done()
			_, err := f.Submit(ctx, []interface{}{7}, nil)
			failures[idx] = err
		}(i)
	}
	wg3.Wait()
	if !(len(failures) == 2) {
		fmt.Fprintf(os.Stderr, "expected 2 failures, got %d\n", len(failures))
		os.Exit(1)
	}
	for _, e := range failures {
		if !(e != nil && e.Error() == "backend down") {
			fmt.Fprintf(os.Stderr, "collapsed waiters did not all receive the backend failure: %v\n", failures)
			os.Exit(1)
		}
	}

	// Sync backends still collapse.
	syncCalls := 0
	syncBackend := func(ctx context.Context, args []interface{}, kwargs map[string]interface{}) (interface{}, error) {
		syncCalls++
		return args[0].(int) * 10, nil
	}
	s := NewCollapser(syncBackend, 20, 10)
	sr := make([]interface{}, 3)
	var wg4 sync.WaitGroup
	for i := 0; i < 3; i++ {
		wg4.Add(1)
		go func(idx int) {
			defer wg4.Done()
			res, err := s.Submit(ctx, []interface{}{4}, nil)
			if err != nil {
				fmt.Fprintf(os.Stderr, "sync backend failed: %v\n", err)
				os.Exit(1)
			}
			sr[idx] = res
		}(i)
	}
	wg4.Wait()
	for _, v := range sr {
		if !(v == 40) {
			fmt.Fprintf(os.Stderr, "sync backend results wrong: %v\n", sr)
			os.Exit(1)
		}
	}
	expectedSync := []int{40, 40, 40}
	for i, v := range sr {
		if !(v == expectedSync[i]) {
			fmt.Fprintf(os.Stderr, "sync backend results wrong: %v\n", sr)
			os.Exit(1)
		}
	}
	if syncCalls != 1 {
		fmt.Fprintf(os.Stderr, "sync backend called %d times, not 1\n", syncCalls)
		os.Exit(1)
	}

	fmt.Println("budget_allocator (request collapser): 5->1 collapsed, 3 distinct kept, failure fanned out to all waiters, sync path collapsed — PASS")
}
