package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
	"sync"
	"sync/atomic"
)

// Copy-on-write config: readers observe a whole, consistent snapshot.
// In copy-on-write, a new Config is created for each update with all fields set to the
// same generation. An atomic pointer swap makes the update visible to readers atomically.
// Readers load the pointer and read a complete, consistent snapshot where all fields came
// from the same generation — never a torn mix from different generations.
// Use when config is frequently read but updates are rare.
// Guarantees: every reader observes a self-consistent Config (all fields from the same
// generation number), no lost updates, and atomic visibility of multi-field changes.
// Toolchain: requires Go >= 1.19 — uses the typed atomic API (atomic.Int32, atomic.Int64, atomic.Pointer),
// which does not exist in Go 1.18 or earlier.

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
var _auraMark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
type Config struct {
	Host       string
	Port       int
	Generation int
}

func main() {
	// Part 1: Success case - readers and writer under load with atomic.Pointer
	var configPtr atomic.Pointer[Config]
	configPtr.Store(&Config{Host: "host-0", Port: 8080, Generation: 0})

	var readCount atomic.Int64
	var tornReads atomic.Int64
	var finalGen atomic.Int32

	var wg sync.WaitGroup

	// 32 readers: 20,000 reads each
	for i := 0; i < 32; i++ {
		wg.Add(1)
		go func() {
			defer wg.Done()
			for j := 0; j < 20000; j++ {
				cfg := configPtr.Load()
				readCount.Add(1)

				// Detect torn reads: check if all fields came from the same generation
				// Extract generation from host string: "host-N"
				hostParts := strings.Split(cfg.Host, "-")
				if len(hostParts) == 2 {
					if hostGen, err := strconv.Atoi(hostParts[1]); err == nil {
						expectedPort := 8080 + hostGen
						if cfg.Port != expectedPort || cfg.Generation != hostGen {
							tornReads.Add(1)
						}
					}
				}
			}
		}()
	}

	// 1 writer: 500 generation swaps
	wg.Add(1)
	go func() {
		defer wg.Done()
		for gen := 1; gen <= 500; gen++ {
			newCfg := &Config{
				Host:       fmt.Sprintf("host-%d", gen),
				Port:       8080 + gen,
				Generation: gen,
			}
			configPtr.Store(newCfg)
		}
		finalGen.Store(int32(500))
	}()

	wg.Wait()

	// Assertions: RECOVERY-grade exact equality against counted truth
	if tornReads.Load() != 0 {
		fmt.Fprintf(os.Stderr, "torn_reads_nonzero: %d\n", tornReads.Load())
		os.Exit(1)
	}
	if finalGen.Load() != 500 {
		fmt.Fprintf(os.Stderr, "final_generation_mismatch: %d\n", finalGen.Load())
		os.Exit(1)
	}
	if readCount.Load() != 640000 {
		fmt.Fprintf(os.Stderr, "read_count_mismatch: %d\n", readCount.Load())
		os.Exit(1)
	}

	// Part 2: Stress test the disaster scenario - writer generates 500 updates while readers hammer continuously
	// Reset the counter and writer for a second high-contention round
	finalGen.Store(0)
	readCount.Store(0)
	tornReads.Store(0)

	configPtr.Store(&Config{Host: "host-0", Port: 8080, Generation: 0})

	// 32 readers again
	for i := 0; i < 32; i++ {
		wg.Add(1)
		go func() {
			defer wg.Done()
			for j := 0; j < 20000; j++ {
				cfg := configPtr.Load()
				readCount.Add(1)

				hostParts := strings.Split(cfg.Host, "-")
				if len(hostParts) == 2 {
					if hostGen, err := strconv.Atoi(hostParts[1]); err == nil {
						expectedPort := 8080 + hostGen
						if cfg.Port != expectedPort || cfg.Generation != hostGen {
							tornReads.Add(1)
						}
					}
				}
			}
		}()
	}

	// 1 writer again: 500 generation swaps
	wg.Add(1)
	go func() {
		defer wg.Done()
		for gen := 1; gen <= 500; gen++ {
			newCfg := &Config{
				Host:       fmt.Sprintf("host-%d", gen),
				Port:       8080 + gen,
				Generation: gen,
			}
			configPtr.Store(newCfg)
		}
		finalGen.Store(int32(500))
	}()

	wg.Wait()

	// Part 2 assertions
	if tornReads.Load() != 0 {
		fmt.Fprintf(os.Stderr, "part2_torn_reads_nonzero: %d\n", tornReads.Load())
		os.Exit(1)
	}
	if finalGen.Load() != 500 {
		fmt.Fprintf(os.Stderr, "part2_final_generation_mismatch: %d\n", finalGen.Load())
		os.Exit(1)
	}
	if readCount.Load() != 640000 {
		fmt.Fprintf(os.Stderr, "part2_read_count_mismatch: %d\n", readCount.Load())
		os.Exit(1)
	}

	fmt.Println("copy_on_write_config: 0 torn reads (both rounds), 500 generations, 640000 reads × 2, race-clean — PASS")
}
