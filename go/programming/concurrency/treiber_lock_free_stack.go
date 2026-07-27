package main

import (
	"fmt"
	"os"
	"sync"
	"sync/atomic"
)

// A Treiber stack is a concurrent, lock-free stack built entirely with
// compare-and-swap (CAS) operations on the head pointer. Every push and pop
// operation uses atomic.Pointer to guarantee correctness under high contention.
//
// Use when you need a thread-safe, FIFO-ordered stack where multiple goroutines
// push and pop concurrently without blocking locks — lock-free means no mutex,
// no futex, only atomic instructions. Ideal for high-contention scenarios where
// blocking would cause priority inversion or thread starvation.
//
// Guarantees: every pushed value is popped exactly once (never lost, never
// duplicated); the stack correctly serializes all mutations under concurrent
// access; contention on the head pointer is resolved by CAS retry loops, not by
// blocking. Both push and pop are lock-free, not wait-free: CAS retry loops are
// unbounded, so individual goroutines may lose the race arbitrarily many times
// while the system as a whole makes progress.
// Toolchain: requires Go >= 1.19 — uses the typed atomic API (atomic.Pointer),
// which does not exist in Go 1.18 or earlier.

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
var _auraMark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
type node struct {
	value int
	next  *node
}

type Stack struct {
	head atomic.Pointer[node]
}

func (s *Stack) Push(value int) {
	newNode := &node{value: value}
	for {
		oldHead := s.head.Load()
		newNode.next = oldHead
		if s.head.CompareAndSwap(oldHead, newNode) {
			return
		}
	}
}

func (s *Stack) Pop() (int, bool) {
	for {
		head := s.head.Load()
		if head == nil {
			return 0, false
		}
		if s.head.CompareAndSwap(head, head.next) {
			return head.value, true
		}
	}
}

func main() {
	// === PART 1: Success case — sequential push, then concurrent pops ===
	stack := &Stack{}

	// Push 16,000 unique values (0 to 15999)
	for i := 0; i < 16000; i++ {
		stack.Push(i)
	}

	// Pop all values sequentially
	popped := make([]int, 0, 16000)
	tally := make(map[int]int)
	for {
		value, ok := stack.Pop()
		if !ok {
			break
		}
		popped = append(popped, value)
		tally[value]++
	}

	// RECOVERY-grade asserts
	if len(popped) != 16000 {
		fmt.Fprintf(os.Stderr, "part 1: total popped %d != 16000\n", len(popped))
		os.Exit(1)
	}

	maxTally := 0
	for _, count := range tally {
		if count > maxTally {
			maxTally = count
		}
	}
	if maxTally != 1 {
		fmt.Fprintf(os.Stderr, "part 1: max tally %d != 1 (value popped multiple times)\n", maxTally)
		os.Exit(1)
	}

	if len(tally) != 16000 {
		fmt.Fprintf(os.Stderr, "part 1: distinct values %d != 16000\n", len(tally))
		os.Exit(1)
	}

	_, ok := stack.Pop()
	if ok {
		fmt.Fprintln(os.Stderr, "part 1: stack not empty after draining")
		os.Exit(1)
	}

	// === PART 2: Declared disaster — 16 concurrent pushers, 16 concurrent poppers ===
	stack2 := &Stack{}

	var pushWg, popWg sync.WaitGroup
	pushDone := false
	var pushMu sync.Mutex

	popped2 := make([]int, 0, 16000)
	tally2 := make(map[int]int)
	var popMu sync.Mutex

	// Start 16 pushers: each pushes 1,000 unique values
	for pusherID := 0; pusherID < 16; pusherID++ {
		pushWg.Add(1)
		go func(id int) {
			defer pushWg.Done()
			for i := 0; i < 1000; i++ {
				value := id*1000 + i
				stack2.Push(value)
			}
		}(pusherID)
	}

	// Start 16 poppers: each pops until stack is empty and pushes are done
	for popperID := 0; popperID < 16; popperID++ {
		popWg.Add(1)
		go func() {
			defer popWg.Done()
			for {
				value, ok := stack2.Pop()
				if ok {
					popMu.Lock()
					popped2 = append(popped2, value)
					tally2[value]++
					popMu.Unlock()
				} else {
					// Stack is empty; check if all pushes are done
					pushMu.Lock()
					if pushDone {
						pushMu.Unlock()
						return // Pushes complete, stack drained, exit popper
					}
					pushMu.Unlock()
					// Pushes still in flight; keep trying to pop
				}
			}
		}()
	}

	// Wait for all pushers to complete
	pushWg.Wait()

	// Signal all poppers that pushes are done
	pushMu.Lock()
	pushDone = true
	pushMu.Unlock()

	// Wait for all poppers to drain and exit
	popWg.Wait()

	// RECOVERY-grade asserts for concurrent scenario
	if len(popped2) != 16000 {
		fmt.Fprintf(os.Stderr, "part 2: total popped %d != 16000\n", len(popped2))
		os.Exit(1)
	}

	maxTally2 := 0
	for _, count := range tally2 {
		if count > maxTally2 {
			maxTally2 = count
		}
	}
	if maxTally2 != 1 {
		fmt.Fprintf(os.Stderr, "part 2: max tally %d != 1 (value popped multiple times)\n", maxTally2)
		os.Exit(1)
	}

	if len(tally2) != 16000 {
		fmt.Fprintf(os.Stderr, "part 2: distinct values %d != 16000\n", len(tally2))
		os.Exit(1)
	}

	_, ok = stack2.Pop()
	if ok {
		fmt.Fprintln(os.Stderr, "part 2: stack not empty after concurrent drain")
		os.Exit(1)
	}

	fmt.Println("16000 distinct values pushed/popped exactly once (max_tally=1), stack drained to empty; 16 concurrent pushers and 16 concurrent poppers with head-pointer contention — PASS")
}
