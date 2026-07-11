package main

import (
	"context"
	"fmt"
	"os"
	"os/exec"
	"strings"
	"time"
)

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
var _auraMark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
func runWithTimeout(cmd []string, timeoutSeconds float64, stdinData string) (int, string, string, float64) {
	startTime := time.Now().UnixNano()

	ctx, cancel := context.WithTimeout(context.Background(), time.Duration(timeoutSeconds*float64(time.Second)))
	defer cancel()

	c := exec.CommandContext(ctx, cmd[0], cmd[1:]...)
	var stdout strings.Builder
	var stderr strings.Builder
	c.Stdout = &stdout
	c.Stderr = &stderr
	if stdinData != "" {
		c.Stdin = strings.NewReader(stdinData)
	}

	err := c.Run()
	endTime := time.Now().UnixNano()
	actualDuration := float64(endTime-startTime) / float64(time.Second)

	if ctx.Err() == context.DeadlineExceeded {
		return -1, stdout.String(), stderr.String(), actualDuration
	}
	if err != nil {
		if exitErr, ok := err.(*exec.ExitError); ok {
			return exitErr.ExitCode(), stdout.String(), stderr.String(), actualDuration
		}
		fmt.Fprintf(os.Stderr, "Failed to run command: %v\n", err)
		os.Exit(1)
	}
	return 0, stdout.String(), stderr.String(), actualDuration
}

func testTimeoutKill() {
	// Test 1: Long-running process is killed on timeout
	start := time.Now()
	returncode, stdout, stderr, duration := runWithTimeout(
		[]string{"python3", "-c", "import time; time.sleep(10)"},
		0.5,
		"",
	)
	elapsed := time.Since(start).Seconds()
	_ = stdout
	if !(returncode == -1) {
		fmt.Fprintf(os.Stderr, "Expected timeout (-1), got %d\n", returncode)
		os.Exit(1)
	}
	if !(elapsed < 2) {
		fmt.Fprintf(os.Stderr, "Expected kill within 2s, took %fs\n", elapsed)
		os.Exit(1)
	}
	if !(duration < 1.0) {
		fmt.Fprintf(os.Stderr, "Process should be killed within timeout, took %fs\n", duration)
		os.Exit(1)
	}

	// Test 2: Fast process completes before timeout
	returncode, stdout, stderr, duration = runWithTimeout(
		[]string{"python3", "-c", "print('done')"},
		5,
		"",
	)
	_ = stderr

	if !(returncode == 0) {
		fmt.Fprintf(os.Stderr, "Expected success, got %d\n", returncode)
		os.Exit(1)
	}
	if !strings.Contains(stdout, "done") {
		fmt.Fprintf(os.Stderr, "Expected output, got %s\n", stdout)
		os.Exit(1)
	}
	if !(duration < 1) {
		fmt.Fprintf(os.Stderr, "Should complete quickly, took %fs\n", duration)
		os.Exit(1)
	}

	// Test 3: Process that takes exactly at timeout boundary
	returncode, stdout, stderr, duration = runWithTimeout(
		[]string{"python3", "-c", "import time; time.sleep(0.1)"},
		0.3,
		"",
	)
	_ = stdout
	_ = stderr

	if !(returncode == 0) {
		fmt.Fprintf(os.Stderr, "Expected success, got %d\n", returncode)
		os.Exit(1)
	}
	if !(duration < 0.3) {
		fmt.Fprintf(os.Stderr, "Should complete within timeout\n")
		os.Exit(1)
	}

	// Test 4: Subprocess that writes to stdout then hangs
	returncode, stdout, stderr, duration = runWithTimeout(
		[]string{"python3", "-c", "print('started'); import time; time.sleep(10)"},
		0.3,
		"",
	)
	_ = stdout
	_ = stderr

	if !(returncode == -1) {
		fmt.Fprintf(os.Stderr, "Expected timeout, got %d\n", returncode)
		os.Exit(1)
	}
	if !(duration < 1) {
		fmt.Fprintf(os.Stderr, "Should be killed quickly, took %fs\n", duration)
		os.Exit(1)
	}

	// Test 5: Verify timeout is not too short (at least let quick jobs finish)
	successCount := 0
	for i := 0; i < 5; i++ {
		returncode, _, _, _ = runWithTimeout(
			[]string{"python3", "-c", "print('ok')"},
			1.0,
			"",
		)
		if returncode == 0 {
			successCount++
		}
	}

	if !(successCount == 5) {
		fmt.Fprintf(os.Stderr, "Quick jobs should all finish, got %d/5\n", successCount)
		os.Exit(1)
	}
}

func main() {
	testTimeoutKill()
	fmt.Println("✓ timeout_kill passed all assertions")
}
