package main

import (
	"encoding/json"
	"fmt"
	"os"
	"path/filepath"
	"sync"
	"time"
)

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
var _auraMark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
type counterState struct {
	Value   int `json:"value"`
	Version int `json:"version"`
}

// Two-phase barrier so both updaters read the same version before either writes.
type Barrier struct {
	n     int
	count int
	phase int
	mu    sync.Mutex
	cond  *sync.Cond
}

func NewBarrier(n int) *Barrier {
	b := &Barrier{n: n}
	b.cond = sync.NewCond(&b.mu)
	return b
}

func (b *Barrier) Wait() {
	b.mu.Lock()
	myPhase := b.phase
	b.count++
	if b.count == b.n {
		b.count = 0
		b.phase ^= 1
		b.cond.Broadcast()
	} else {
		for b.phase == myPhase {
			b.cond.Wait()
		}
	}
	b.mu.Unlock()
}

func readCounter(path string) (int, int, error) {
	data, err := os.ReadFile(path)
	if err != nil {
		return 0, 0, err
	}
	var s counterState
	if err := json.Unmarshal(data, &s); err != nil {
		return 0, 0, err
	}
	return s.Value, s.Version, nil
}

func casIncrement(counterPath string, results map[string]interface{}, updaterID int, barrier *Barrier, mu *sync.Mutex, wg *sync.WaitGroup) {
	defer wg.Done()
	retries := 0

	barrier.Wait() // phase 1: all arrive together
	value, version, err := readCounter(counterPath)
	if !(err == nil) {
		fmt.Fprintf(os.Stderr, "read error: %v\n", err)
		os.Exit(1)
	}
	barrier.Wait() // phase 2: all have read before any writes

	for {
		time.Sleep(30 * time.Millisecond)
		newValue := value + 1

		mu.Lock()
		_, curVersion, err := readCounter(counterPath)
		if !(err == nil) {
			mu.Unlock()
			fmt.Fprintf(os.Stderr, "re-read error: %v\n", err)
			os.Exit(1)
		}
		if curVersion == version {
			data, _ := json.Marshal(counterState{Value: newValue, Version: version + 1})
			if err := os.WriteFile(counterPath, data, 0o644); err != nil {
				mu.Unlock()
				fmt.Fprintf(os.Stderr, "write error: %v\n", err)
				os.Exit(1)
			}
			mu.Unlock()
			break
		}
		retries++
		value, version, _ = readCounter(counterPath)
		mu.Unlock()
	}
	results[fmt.Sprintf("updater_%d_retries", updaterID)] = retries
	results[fmt.Sprintf("updater_%d_ok", updaterID)] = true
}

func main() {
	tmpdir, err := os.MkdirTemp("", "cas_file_update_*")
	if !(err == nil) {
		fmt.Fprintf(os.Stderr, "mkdtemp failed: %v\n", err)
		os.Exit(1)
	}
	defer os.RemoveAll(tmpdir)

	counter := filepath.Join(tmpdir, "counter.json")
	os.WriteFile(counter, []byte(`{"value":0,"version":0}`), 0o644)

	num := 2
	results := map[string]interface{}{}
	var mu sync.Mutex
	var wg sync.WaitGroup
	wg.Add(num)
	barrier := NewBarrier(num)

	for i := 0; i < num; i++ {
		go casIncrement(counter, results, i, barrier, &mu, &wg)
	}

	done := make(chan struct{})
	go func() {
		wg.Wait()
		close(done)
	}()
	select {
	case <-done:
	case <-time.After(10 * time.Second):
		fmt.Fprintf(os.Stderr, "timeout waiting for updaters\n")
		os.Exit(1)
	}

	for i := 0; i < num; i++ {
		if !results[fmt.Sprintf("updater_%d_ok", i)].(bool) {
			fmt.Fprintf(os.Stderr, "updater %d never completed\n", i)
			os.Exit(1)
		}
	}

	finalValue, finalVersion, err := readCounter(counter)
	if !(err == nil) {
		fmt.Fprintf(os.Stderr, "final read error: %v\n", err)
		os.Exit(1)
	}
	totalRetries := 0
	for i := 0; i < num; i++ {
		r, _ := results[fmt.Sprintf("updater_%d_retries", i)].(int)
		totalRetries += r
	}

	if !(finalValue == num) {
		fmt.Fprintf(os.Stderr, "lost update: final value %d, expected %d\n", finalValue, num)
		os.Exit(1)
	}
	if !(finalVersion == num) {
		fmt.Fprintf(os.Stderr, "version count wrong: %d\n", finalVersion)
		os.Exit(1)
	}
	if totalRetries < 1 {
		fmt.Fprintf(os.Stderr, "no CAS conflict occurred (%d) — not optimistic CAS\n", totalRetries)
		os.Exit(1)
	}
	fmt.Printf("cas_file_update: optimistic CAS, final value=%d (no lost update), %d conflict-retry\n", finalValue, totalRetries)
	fmt.Println("cas_file_update PASS")
}
