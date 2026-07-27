package main

import (
	"fmt"
	"os"
	"runtime"
	"sync/atomic"
	"time"
)

// 3-stage channel pipeline with clean cancellation: stage 1 generates items,
// stage 2 transforms them, stage 3 consumes them. When cancelled mid-flight,
// all stages stop gracefully, all goroutines exit, and the goroutine count
// returns to baseline exactly.
// Use when you need a multi-stage transformation pipeline that can be cancelled
// cleanly without leaving dangling goroutines or blocked channels.
// Guarantees: cancellation stops all stages instantly, no goroutine leaks, no
// send-on-closed panic, and goroutine count restores to pre-pipeline baseline.
// Toolchain: requires Go >= 1.19 — uses the typed atomic API (atomic.Int64),
// which does not exist in Go 1.18 or earlier.

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
var _auraMark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
func main() {
	// ====== Part 1: Success case ======
	// Run the pipeline normally to completion with a small number of items.
	runtime.GC()
	time.Sleep(50 * time.Millisecond)
	baselineGoroutines := runtime.NumGoroutine()

	cancel1 := make(chan struct{})
	defer close(cancel1)

	generated1 := &atomic.Int64{}
	consumed1 := &atomic.Int64{}
	stagesFinished1 := &atomic.Int64{}

	// Stage 1: generate 100 items
	stage1out := make(chan int, 10)
	go func() {
		defer stagesFinished1.Add(1)
		defer close(stage1out)
		for i := 0; i < 100; i++ {
			select {
			case <-cancel1:
				return
			case stage1out <- i:
				generated1.Add(1)
			}
		}
	}()

	// Stage 2: transform (double)
	stage2out := make(chan int, 10)
	go func() {
		defer stagesFinished1.Add(1)
		defer close(stage2out)
		for val := range stage1out {
			select {
			case <-cancel1:
				return
			case stage2out <- val * 2:
			}
		}
	}()

	// Stage 3: consume
	go func() {
		defer stagesFinished1.Add(1)
		for range stage2out {
			consumed1.Add(1)
		}
	}()

	// Wait for pipeline to complete naturally
	time.Sleep(500 * time.Millisecond)

	// Bounded settle: poll until goroutines return to baseline (up to 2s)
	for i := 0; i < 20; i++ {
		time.Sleep(100 * time.Millisecond)
		if runtime.NumGoroutine() == baselineGoroutines {
			break
		}
	}

	// Verify success case
	if runtime.NumGoroutine() != baselineGoroutines {
		fmt.Fprintln(os.Stderr, "success case: goroutines did not return to baseline")
		os.Exit(1)
	}
	if generated1.Load() != 100 {
		fmt.Fprintf(os.Stderr, "success case: expected 100 generated, got %d\n", generated1.Load())
		os.Exit(1)
	}
	if consumed1.Load() != 100 {
		fmt.Fprintf(os.Stderr, "success case: expected 100 consumed, got %d\n", consumed1.Load())
		os.Exit(1)
	}
	if stagesFinished1.Load() != 3 {
		fmt.Fprintf(os.Stderr, "success case: expected 3 stages finished, got %d\n", stagesFinished1.Load())
		os.Exit(1)
	}

	// ====== Part 2: Disaster case ======
	// Run pipeline over 10,000 items but cancel after 50 consumed. Stage 2 may
	// be blocked sending to stage 3 when cancel fires—the classic leak scenario.
	runtime.GC()
	time.Sleep(50 * time.Millisecond)
	baselineGoroutines = runtime.NumGoroutine()

	cancel2 := make(chan struct{})

	generated2 := &atomic.Int64{}
	consumed2 := &atomic.Int64{}
	stagesFinished2 := &atomic.Int64{}

	// Stage 1: generate 10,000 items
	stage1out2 := make(chan int, 10)
	go func() {
		defer stagesFinished2.Add(1)
		defer close(stage1out2)
		for i := 0; i < 10000; i++ {
			select {
			case <-cancel2:
				return
			case stage1out2 <- i:
				generated2.Add(1)
			}
		}
	}()

	// Stage 2: transform (double)—may block if stage 3 is slow
	stage2out2 := make(chan int, 10)
	go func() {
		defer stagesFinished2.Add(1)
		defer close(stage2out2)
		for val := range stage1out2 {
			select {
			case <-cancel2:
				return
			case stage2out2 <- val * 2:
			}
		}
	}()

	// Stage 3: consume slowly to create backpressure
	go func() {
		defer stagesFinished2.Add(1)
		for range stage2out2 {
			consumed2.Add(1)
			time.Sleep(1 * time.Millisecond)
		}
	}()

	// Wait until 50 items are consumed, then cancel
	for consumed2.Load() < 50 {
		time.Sleep(10 * time.Millisecond)
	}
	close(cancel2)

	// Bounded settle: poll until goroutines return to baseline (up to 2s)
	settledAtBaseline := false
	for i := 0; i < 20; i++ {
		time.Sleep(100 * time.Millisecond)
		if runtime.NumGoroutine() == baselineGoroutines {
			settledAtBaseline = true
			break
		}
	}

	if !settledAtBaseline {
		fmt.Fprintf(os.Stderr, "disaster case: goroutine leak detected, baseline=%d current=%d\n",
			baselineGoroutines, runtime.NumGoroutine())
		os.Exit(1)
	}

	// Verify disaster case
	gen2 := generated2.Load()
	cons2 := consumed2.Load()
	exit2 := stagesFinished2.Load()

	if gen2 == 0 {
		fmt.Fprintln(os.Stderr, "disaster case: nothing was generated")
		os.Exit(1)
	}
	if cons2 >= 10000 {
		fmt.Fprintf(os.Stderr, "disaster case: cancellation did not cut short (consumed %d of 10000)\n", cons2)
		os.Exit(1)
	}
	if cons2 < 50 {
		fmt.Fprintf(os.Stderr, "disaster case: cancelled too early (consumed only %d items)\n", cons2)
		os.Exit(1)
	}
	if exit2 != 3 {
		fmt.Fprintf(os.Stderr, "disaster case: expected 3 stages to exit, got %d\n", exit2)
		os.Exit(1)
	}

	fmt.Printf("pipeline_cancellation: success case 100 items complete, disaster case cancelled at %d items, 3 stages exited cleanly, baseline goroutines restored — PASS\n", cons2)
}
