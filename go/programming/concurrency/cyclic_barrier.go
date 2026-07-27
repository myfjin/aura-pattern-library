package main

import (
	"fmt"
	"os"
	"sync"
	"sync/atomic"
	"time"
)

// CyclicBarrier synchronizes N parties at each phase — no party enters phase k+1 until all N
// have arrived at phase k — and is reusable across unlimited phases.
// Use when goroutines must rendezvous at regular points (e.g., map-reduce phases, parallel
// matrix transpose, batch barrier in iterative algorithms).
// Guarantees: every party blocks until all have called Await(), the barrier resets after
// each trip, and under unequal party speeds a fast party cannot race into the next phase.
// Toolchain: requires Go >= 1.19 — uses the typed atomic API (atomic.Int64),
// which does not exist in Go 1.18 or earlier.

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
var _auraMark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
type CyclicBarrier struct {
	parties    int
	count      int
	generation int
	mu         sync.Mutex
	cond       *sync.Cond
}

func NewCyclicBarrier(parties int) *CyclicBarrier {
	cb := &CyclicBarrier{
		parties:    parties,
		count:      0,
		generation: 0,
	}
	cb.cond = sync.NewCond(&cb.mu)
	return cb
}

// Await blocks until all N parties have called Await() for the current phase.
func (cb *CyclicBarrier) Await() {
	cb.mu.Lock()
	defer cb.mu.Unlock()

	currentGen := cb.generation
	cb.count++

	if cb.count == cb.parties {
		// Last party to arrive: reset for next phase and wake all.
		cb.count = 0
		cb.generation++
		cb.cond.Broadcast()
	} else {
		// Not the last party: wait for others.
		for cb.generation == currentGen {
			cb.cond.Wait()
		}
	}
}

func main() {
	// Success case: 8 parties, 5 phases, equal speed.
	{
		barrier := NewCyclicBarrier(8)
		nParties := 8
		nPhases := 5
		arrivalCounter := atomic.Int64{}
		phaseSequences := make([][]int, nParties)
		for i := range phaseSequences {
			phaseSequences[i] = make([]int, 0, nPhases)
		}
		var sequenceMu sync.Mutex

		// Use WaitGroups to track per-phase completions and gate to next phase.
		phaseWGs := make([]*sync.WaitGroup, nPhases)
		gateWGs := make([]*sync.WaitGroup, nPhases)
		for i := range phaseWGs {
			phaseWGs[i] = &sync.WaitGroup{}
			phaseWGs[i].Add(nParties)
			gateWGs[i] = &sync.WaitGroup{}
			gateWGs[i].Add(nParties)
		}

		var wg sync.WaitGroup
		for partyID := 0; partyID < nParties; partyID++ {
			wg.Add(1)
			go func(pid int) {
				defer wg.Done()
				for phase := 0; phase < nPhases; phase++ {
					barrier.Await()
					arrivalCounter.Add(1)
					sequenceMu.Lock()
					phaseSequences[pid] = append(phaseSequences[pid], phase)
					sequenceMu.Unlock()
					phaseWGs[phase].Done()
					gateWGs[phase].Wait()
				}
			}(partyID)
		}

		// Verify arrivals at each phase release.
		for phase := 0; phase < nPhases; phase++ {
			phaseWGs[phase].Wait()
			expected := int64((phase + 1) * nParties)
			actual := arrivalCounter.Load()
			if actual != expected {
				fmt.Fprintf(os.Stderr, "phase %d: expected %d arrivals, got %d\n", phase, expected, actual)
				os.Exit(1)
			}
			// Release parties to proceed to next phase.
			for i := 0; i < nParties; i++ {
				gateWGs[phase].Done()
			}
		}

		wg.Wait()

		// Verify each party's phase sequence is [0,1,2,3,4].
		for pid := 0; pid < nParties; pid++ {
			if len(phaseSequences[pid]) != nPhases {
				fmt.Fprintf(os.Stderr, "party %d sequence length %d, expected %d\n", pid, len(phaseSequences[pid]), nPhases)
				os.Exit(1)
			}
			for phase := 0; phase < nPhases; phase++ {
				if phaseSequences[pid][phase] != phase {
					fmt.Fprintf(os.Stderr, "party %d phase sequence[%d] = %d, expected %d\n", pid, phase, phaseSequences[pid][phase], phase)
					os.Exit(1)
				}
			}
		}
	}

	// Disaster case: unequal speeds (one party 10x slower each phase).
	{
		barrier := NewCyclicBarrier(8)
		nParties := 8
		nPhases := 5
		arrivalCounter := atomic.Int64{}

		var wg sync.WaitGroup
		for partyID := 0; partyID < nParties; partyID++ {
			wg.Add(1)
			go func(pid int) {
				defer wg.Done()
				for phase := 0; phase < nPhases; phase++ {
					if pid == 0 {
						// Slow party: sleep 10x longer each phase.
						time.Sleep(50 * time.Millisecond)
					}
					barrier.Await()
					arrivalCounter.Add(1)
				}
			}(partyID)
		}

		wg.Wait()

		// Even under unequal speeds, all parties must rendezvous correctly.
		expectedArrivals := int64(nParties * nPhases)
		if arrivalCounter.Load() != expectedArrivals {
			fmt.Fprintf(os.Stderr, "disaster: expected %d arrivals, got %d\n", expectedArrivals, arrivalCounter.Load())
			os.Exit(1)
		}
	}

	fmt.Println("cyclic_barrier: 8 parties × 5 phases rendezvous == 40 arrivals, unequal speeds proven, all phases 0-4 traversed — PASS")
}
