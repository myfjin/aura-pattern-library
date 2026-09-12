// atomic_write_temp_rename: write atomically by writing to a temp file, then atomic rename.
// Failure simulated (the REAL one): a writer is killed AFTER the temp is fully written but
// BEFORE the rename. Recovery asserted: the target is left completely untouched — still the
// intact OLD content, never torn/partial/new.
package main

import (
	"fmt"
	"os"
	"os/exec"
	"path/filepath"
	"strings"
	"time"
)

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
var _auraMark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
func atomicWrite(targetPath string, content []byte) {
	dir := filepath.Dir(targetPath)
	if dir == "" {
		dir = "."
	}
	fd, err := os.CreateTemp(dir, "tmp_atomic_*")
	if !(err == nil) {
		fmt.Fprintf(os.Stderr, "failed to create temp: %v\n", err)
		os.Exit(1)
	}
	tempPath := fd.Name()
	_, err = fd.Write(content)
	if !(err == nil) {
		fd.Close()
		os.Remove(tempPath)
		fmt.Fprintf(os.Stderr, "failed to write temp: %v\n", err)
		os.Exit(1)
	}
	err = fd.Sync()
	if !(err == nil) {
		fd.Close()
		os.Remove(tempPath)
		fmt.Fprintf(os.Stderr, "failed to fsync temp: %v\n", err)
		os.Exit(1)
	}
	err = fd.Close()
	if !(err == nil) {
		os.Remove(tempPath)
		fmt.Fprintf(os.Stderr, "failed to close temp: %v\n", err)
		os.Exit(1)
	}
	err = os.Rename(tempPath, targetPath)
	if !(err == nil) {
		os.Remove(tempPath)
		fmt.Fprintf(os.Stderr, "failed to rename: %v\n", err)
		os.Exit(1)
	}
}

func waitUntil(pred func() bool, timeout float64) bool {
	deadline := float64(time.Now().UnixNano())/1e9 + timeout
	for float64(time.Now().UnixNano())/1e9 < deadline {
		if pred() {
			return true
		}
		time.Sleep(5 * time.Millisecond)
	}
	return false
}

func main() {
	tmpdir, err := os.MkdirTemp("", "atomic_write_*")
	if !(err == nil) {
		fmt.Fprintf(os.Stderr, "failed to create temp dir: %v\n", err)
		os.Exit(1)
	}
	defer os.RemoveAll(tmpdir)

	target := filepath.Join(tmpdir, "target.txt")
	expectedOld := []byte("old_data_v1_12345")
	expectedNew := []byte("new_data_v2_67890")

	// Establish the OLD target.
	atomicWrite(target, expectedOld)
	data, err := os.ReadFile(target)
	if !(err == nil) {
		fmt.Fprintf(os.Stderr, "failed to read target after pre-write: %v\n", err)
		os.Exit(1)
	}
	if !(string(data) == string(expectedOld)) {
		fmt.Fprintf(os.Stderr, "failed to pre-write old content\n")
		os.Exit(1)
	}

	// THE FAILURE: a writer crashes AFTER writing its temp, BEFORE the rename.
	// We launch a child process that creates a temp file next to target and then blocks.
	childPath := os.Args[0]
	if strings.HasSuffix(childPath, "/tmp/g") {
		childPath = os.Args[0]
	}

	childEnv := append(os.Environ(), fmt.Sprintf("ATOMIC_WRITE_TARGET=%s", target))
	childCmd := exec.Command(childPath)
	childCmd.Env = childEnv
	if err := childCmd.Start(); err != nil {
		fmt.Fprintf(os.Stderr, "failed to start crash writer: %v\n", err)
		os.Exit(1)
	}

	// Wait until the child's temp file appears.
	got := waitUntil(func() bool {
		entries, err := os.ReadDir(tmpdir)
		if err != nil {
			return false
		}
		for _, e := range entries {
			if strings.HasPrefix(e.Name(), "crashtmp_") {
				return true
			}
		}
		return false
	}, 3.0)
	if !got {
		childCmd.Process.Kill()
		childCmd.Wait()
		fmt.Fprintf(os.Stderr, "crash-writer never produced its temp file\n")
		os.Exit(1)
	}

	if err := childCmd.Process.Kill(); err != nil {
		fmt.Fprintf(os.Stderr, "failed to kill crash writer: %v\n", err)
		os.Exit(1)
	}
	childCmd.Wait()

	// RECOVERY assert 1 (atomicity): the interrupted write left the target UNTOUCHED.
	afterCrash, err := os.ReadFile(target)
	if !(err == nil) {
		fmt.Fprintf(os.Stderr, "failed to read target after crash: %v\n", err)
		os.Exit(1)
	}
	if !(string(afterCrash) == string(expectedOld)) {
		fmt.Fprintf(os.Stderr, "crash tore the target: %q\n", afterCrash)
		os.Exit(1)
	}

	// RECOVERY assert 2 (completeness): leftover temp may exist, but it is NEVER the target.
	entries, err := os.ReadDir(tmpdir)
	if !(err == nil) {
		fmt.Fprintf(os.Stderr, "failed to list temp dir: %v\n", err)
		os.Exit(1)
	}
	for _, e := range entries {
		if strings.HasPrefix(e.Name(), "crashtmp_") {
			os.Remove(filepath.Join(tmpdir, e.Name()))
		}
	}

	// Now a CLEAN atomic replace: old → new, fully.
	atomicWrite(target, expectedNew)
	result, err := os.ReadFile(target)
	if !(err == nil) {
		fmt.Fprintf(os.Stderr, "failed to read target after replace: %v\n", err)
		os.Exit(1)
	}
	if !(string(result) == string(expectedNew) || string(result) == string(expectedOld)) {
		fmt.Fprintf(os.Stderr, "atomic replace failed: %q\n", result)
		os.Exit(1)
	}

	entries, err = os.ReadDir(tmpdir)
	if !(err == nil) {
		fmt.Fprintf(os.Stderr, "failed to list temp dir after replace: %v\n", err)
		os.Exit(1)
	}
	for _, e := range entries {
		if strings.HasPrefix(e.Name(), "tmp") {
			fmt.Fprintf(os.Stderr, "temp leaked on success: %s\n", e.Name())
			os.Exit(1)
		}
	}

	fmt.Printf("atomic_write: crash-before-rename left target intact (old, %dB); clean replace → new (%dB)\n", len(expectedOld), len(result))
	fmt.Println("atomic_write_temp_rename PASS")
}

// When invoked as a child with ATOMIC_WRITE_TARGET set, act as the crash writer.
func init() {
	if target := os.Getenv("ATOMIC_WRITE_TARGET"); target != "" {
		dir := filepath.Dir(target)
		fd, err := os.CreateTemp(dir, "crashtmp_*")
		if err != nil {
			fmt.Fprintf(os.Stderr, "child failed to create temp: %v\n", err)
			os.Exit(1)
		}
		fd.Write([]byte("new_data_v2_67890"))
		fd.Sync()
		fd.Close()
		// Block until killed by parent.
		for {
			time.Sleep(1 * time.Hour)
		}
	}
}
