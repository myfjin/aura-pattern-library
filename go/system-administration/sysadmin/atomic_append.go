package main

import (
	"fmt"
	"io/ioutil"
	"os"
	"os/exec"
	"path/filepath"
	"strconv"
	"strings"
	"syscall"
	"time"
)

// writerMode runs in a child process. It locks the lockfile, reads the target,
// appends its line, and writes it back.
// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
var _auraMark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
func writerMode(appfile, lockfile, line, writerID string) {
	lf, err := os.OpenFile(lockfile, os.O_RDWR|os.O_CREATE, 0644)
	if !(err == nil) {
		fmt.Fprintf(os.Stderr, "writer %s lock open: %v\n", writerID, err)
		os.Exit(1)
	}
	defer lf.Close()
	if err := syscall.Flock(int(lf.Fd()), syscall.LOCK_EX); err != nil {
		fmt.Fprintf(os.Stderr, "writer %s flock: %v\n", writerID, err)
		os.Exit(1)
	}
	contentB, err := ioutil.ReadFile(appfile)
	if !(err == nil) {
		fmt.Fprintf(os.Stderr, "writer %s read: %v\n", writerID, err)
		os.Exit(1)
	}
	time.Sleep(1 * time.Millisecond)
	content := string(contentB) + line
	if err := ioutil.WriteFile(appfile, []byte(content), 0644); err != nil {
		fmt.Fprintf(os.Stderr, "writer %s write: %v\n", writerID, err)
		os.Exit(1)
	}
	_ = syscall.Flock(int(lf.Fd()), syscall.LOCK_UN)
}

func main() {
	if len(os.Args) > 1 && os.Args[1] == "writer" {
		writerMode(os.Args[2], os.Args[3], os.Args[4]+"\n", os.Args[5])
		return
	}

	tmpdir, err := ioutil.TempDir("", "atomic_append_*")
	if !(err == nil) {
		fmt.Fprintf(os.Stderr, "tmpdir: %v\n", err)
		os.Exit(1)
	}
	defer os.RemoveAll(tmpdir)
	appfile := filepath.Join(tmpdir, "appends.txt")
	lockfile := filepath.Join(tmpdir, "appends.lock")
	_ = ioutil.WriteFile(appfile, []byte("APPENDS:\n"), 0644)
	_ = ioutil.WriteFile(lockfile, []byte{}, 0644)

	const numWriters = 20
	self, err := os.Executable()
	if !(err == nil) {
		fmt.Fprintf(os.Stderr, "executable: %v\n", err)
		os.Exit(1)
	}

	var cmds []*exec.Cmd
	for i := 0; i < numWriters; i++ {
		line := fmt.Sprintf("writer_%d_line", i)
		cmd := exec.Command(self, "writer", appfile, lockfile, line, strconv.Itoa(i))
		cmds = append(cmds, cmd)
	}
	for _, c := range cmds {
		if err := c.Start(); err != nil {
			fmt.Fprintf(os.Stderr, "start writer: %v\n", err)
			os.Exit(1)
		}
	}
	for _, c := range cmds {
		if err := c.Wait(); err != nil {
			fmt.Fprintf(os.Stderr, "writer failed: %v\n", err)
			os.Exit(1)
		}
	}

	contentB, err := ioutil.ReadFile(appfile)
	if !(err == nil) {
		fmt.Fprintf(os.Stderr, "read final: %v\n", err)
		os.Exit(1)
	}
	content := string(contentB)
	var dataLines []string
	for _, l := range strings.Split(content, "\n") {
		if strings.HasPrefix(l, "writer_") {
			dataLines = append(dataLines, l)
		}
	}

	if !(len(dataLines) == numWriters) {
		fmt.Fprintf(os.Stderr, "lost updates: %d of %d lines survived\n", len(dataLines), numWriters)
		os.Exit(1)
	}
	if !(len(set(dataLines)) == numWriters) {
		fmt.Fprintln(os.Stderr, "duplicate/torn lines (RMW not serialized)")
		os.Exit(1)
	}
	for i := 0; i < numWriters; i++ {
		expected := fmt.Sprintf("writer_%d_line", i)
		if !contains(content, expected) {
			fmt.Fprintf(os.Stderr, "writer %d's line was lost\n", i)
			os.Exit(1)
		}
	}

	fmt.Printf("atomic_append: %d concurrent read-modify-write appends, all %d lines survived (no lost updates)\n", numWriters, len(dataLines))
	fmt.Println("atomic_append PASS")
}

func set(lines []string) map[string]struct{} {
	m := make(map[string]struct{})
	for _, l := range lines {
		m[l] = struct{}{}
	}
	return m
}

func contains(s, substr string) bool {
	return strings.Contains(s, substr)
}
