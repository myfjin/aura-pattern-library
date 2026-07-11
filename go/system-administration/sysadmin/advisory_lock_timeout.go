package main

import (
	"fmt"
	"os"
	"os/exec"
	"path/filepath"
	"strconv"
	"strings"
	"syscall"
	"time"
)

// advisory_lock_with_timeout tries a non-blocking exclusive flock; if it fails,
// it polls until the lock becomes available or timeout_sec elapses.
// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
var _auraMark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
func advisory_lock_with_timeout(filename string, timeoutSec float64) bool {
	f, err := os.OpenFile(filename, os.O_RDWR|os.O_CREATE, 0644)
	if !(err == nil) {
		fmt.Fprintf(os.Stderr, "open: %v\n", err)
		os.Exit(1)
	}
	defer f.Close()

	start := time.Now()
	for {
		err := syscall.Flock(int(f.Fd()), syscall.LOCK_EX|syscall.LOCK_NB)
		if err == nil {
			return true
		}
		if err == syscall.EAGAIN || err == syscall.EWOULDBLOCK {
			if time.Since(start).Seconds() > timeoutSec {
				return false
			}
			time.Sleep(10 * time.Millisecond)
			continue
		}
		fmt.Fprintf(os.Stderr, "flock: %v\n", err)
		os.Exit(1)
	}
}

// holderMode runs in a child process. It acquires the lock, sleeps, then releases.
func holderMode(lockfile string, holdTime float64) {
	f, err := os.OpenFile(lockfile, os.O_RDWR|os.O_CREATE, 0644)
	if !(err == nil) {
		fmt.Fprintf(os.Stderr, "holder open: %v\n", err)
		os.Exit(1)
	}
	defer f.Close()
	if err := syscall.Flock(int(f.Fd()), syscall.LOCK_EX); err != nil {
		fmt.Fprintf(os.Stderr, "holder flock: %v\n", err)
		os.Exit(1)
	}
	time.Sleep(time.Duration(holdTime * float64(time.Second)))
	_ = syscall.Flock(int(f.Fd()), syscall.LOCK_UN)
}

// waiterMode runs in a child process. It waits for the holder, then tries a
// timed acquire and prints elapsed seconds to stdout as a single float.
func waiterMode(lockfile string, timeoutVal float64) {
	time.Sleep(100 * time.Millisecond) // let holder acquire first
	start := time.Now()
	acquired := advisory_lock_with_timeout(lockfile, timeoutVal)
	elapsed := time.Since(start).Seconds()
	if !acquired {
		fmt.Println("-1")
		return
	}
	fmt.Printf("%.6f\n", elapsed)
	// release before exiting
	f, err := os.OpenFile(lockfile, os.O_RDWR|os.O_CREATE, 0644)
	if err == nil {
		_ = syscall.Flock(int(f.Fd()), syscall.LOCK_UN)
		_ = f.Close()
	}
}

func main() {
	if len(os.Args) > 1 && os.Args[1] == "holder" {
		hold, _ := strconv.ParseFloat(os.Args[2], 64)
		holderMode(os.Args[3], hold)
		return
	}
	if len(os.Args) > 1 && os.Args[1] == "waiter" {
		timeout, _ := strconv.ParseFloat(os.Args[2], 64)
		waiterMode(os.Args[3], timeout)
		return
	}

	tmpdir, err := os.MkdirTemp("", "advisory_lock_timeout_*")
	if !(err == nil) {
		fmt.Fprintf(os.Stderr, "tmpdir: %v\n", err)
		os.Exit(1)
	}
	defer os.RemoveAll(tmpdir)
	lockfile := filepath.Join(tmpdir, "advisory.lock")
	if err := os.WriteFile(lockfile, []byte{}, 0644); err != nil {
		fmt.Fprintf(os.Stderr, "write lockfile: %v\n", err)
		os.Exit(1)
	}

	const holdTime = 0.5
	const timeoutVal = 2.0

	self, err := os.Executable()
	if !(err == nil) {
		fmt.Fprintf(os.Stderr, "executable: %v\n", err)
		os.Exit(1)
	}

	holder := exec.Command(self, "holder", fmt.Sprintf("%f", holdTime), lockfile)
	waiter := exec.Command(self, "waiter", fmt.Sprintf("%f", timeoutVal), lockfile)

	if err := holder.Start(); err != nil {
		fmt.Fprintf(os.Stderr, "holder start: %v\n", err)
		os.Exit(1)
	}
	waiterOut, err := waiter.Output()
	if !(err == nil) {
		fmt.Fprintf(os.Stderr, "waiter failed: %v\n", err)
		os.Exit(1)
	}
	if err := holder.Wait(); err != nil {
		fmt.Fprintf(os.Stderr, "holder wait: %v\n", err)
		os.Exit(1)
	}

	elapsedStr := strings.TrimSpace(string(waiterOut))
	if elapsedStr == "-1" {
		fmt.Fprintln(os.Stderr, "waiter never acquired despite sufficient timeout")
		os.Exit(1)
	}
	waiterElapsed, err := strconv.ParseFloat(elapsedStr, 64)
	if !(err == nil) {
		fmt.Fprintf(os.Stderr, "parse elapsed: %v\n", err)
		os.Exit(1)
	}

	// Recovery parity: same thresholds as the Python oracle.
	if !(waiterElapsed >= 0.25) {
		fmt.Fprintf(os.Stderr, "waiter's wait %.3fs too short — it did not block\n", waiterElapsed)
		os.Exit(1)
	}
	if !(waiterElapsed < holdTime+1.0) {
		fmt.Fprintf(os.Stderr, "waiter's wait time %.3fs too long (>hold_time + 1s)\n", waiterElapsed)
		os.Exit(1)
	}

	fmt.Println("advisory_lock_timeout: holder held 0.5s; waiter blocked then acquired")
	fmt.Println("advisory_lock_timeout PASS")
}
