package main

import (
	"fmt"
	"os"
	"path/filepath"
)

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
var _auraMark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
func deploy(liveLink, newTarget string) error {
	if _, err := os.Stat(newTarget); os.IsNotExist(err) {
		return fmt.Errorf("new target does not exist: %s", newTarget)
	}
	parent := filepath.Dir(liveLink)
	if parent != "" && parent != "." {
		_ = os.MkdirAll(parent, 0755)
	}
	tempLink := liveLink + ".tmp"
	if _, err := os.Lstat(tempLink); err == nil {
		_ = os.Remove(tempLink)
	}
	if err := os.Symlink(newTarget, tempLink); err != nil {
		return err
	}
	return os.Rename(tempLink, liveLink)
}

func getTarget(liveLink string) string {
	target, err := os.Readlink(liveLink)
	if err != nil {
		return ""
	}
	return target
}

func linkExists(liveLink string) bool {
	_, err := os.Lstat(liveLink)
	return err == nil
}

func assert(cond bool, format string, args ...interface{}) {
	if !cond {
		fmt.Fprintf(os.Stderr, format+"\n", args...)
		os.Exit(1)
	}
}

func main() {
	tmpdir, err := os.MkdirTemp("", "atomic_symlink_swap_*")
	if !(err == nil) {
		fmt.Fprintf(os.Stderr, "tmpdir: %v\n", err)
		os.Exit(1)
	}
	defer os.RemoveAll(tmpdir)

	v1Dir := filepath.Join(tmpdir, "app-v1")
	v2Dir := filepath.Join(tmpdir, "app-v2")
	liveLink := filepath.Join(tmpdir, "app-live")

	_ = os.MkdirAll(v1Dir, 0755)
	_ = os.MkdirAll(v2Dir, 0755)

	// Test 1: swap points to new target.
	if err := deploy(liveLink, v1Dir); err != nil {
		fmt.Fprintf(os.Stderr, "deploy v1: %v\n", err)
		os.Exit(1)
	}
	assert(getTarget(liveLink) == v1Dir, "Should point to v1")
	assert(linkExists(liveLink), "Link should exist")

	if err := deploy(liveLink, v2Dir); err != nil {
		fmt.Fprintf(os.Stderr, "deploy v2: %v\n", err)
		os.Exit(1)
	}
	assert(getTarget(liveLink) == v2Dir, "Should point to v2")

	// Test 2: link validity.
	assert(linkExists(liveLink), "Link should exist")
	_, err = os.Stat(getTarget(liveLink))
	assert(err == nil, "Target should be accessible")

	// Test 3: crash simulation — temp symlink staged but rename not done.
	if err := deploy(liveLink, v1Dir); err != nil {
		fmt.Fprintf(os.Stderr, "deploy back to v1: %v\n", err)
		os.Exit(1)
	}
	assert(getTarget(liveLink) == v1Dir, "Should point to v1 before crash")
	tempLink := liveLink + ".tmp"
	_ = os.Remove(tempLink)
	if err := os.Symlink(v2Dir, tempLink); err != nil {
		fmt.Fprintf(os.Stderr, "stage temp link: %v\n", err)
		os.Exit(1)
	}
	// <<< CRASH HERE: rename never executes >>>
	assert(linkExists(liveLink), "Live link must survive the crash")
	assert(getTarget(liveLink) == v1Dir, "Live link must still point to OLD target after crash")
	_, err = os.Stat(getTarget(liveLink))
	assert(err == nil, "Live target must be accessible (never dangling)")
	// Recovery: complete the rename.
	if err := os.Rename(tempLink, liveLink); err != nil {
		fmt.Fprintf(os.Stderr, "complete rename: %v\n", err)
		os.Exit(1)
	}
	assert(getTarget(liveLink) == v2Dir, "After the rename completes, live points to v2")

	// Test 4: reject nonexistent target.
	badDir := filepath.Join(tmpdir, "nonexistent")
	if err := deploy(liveLink, badDir); err == nil {
		fmt.Fprintln(os.Stderr, "Should reject nonexistent target")
		os.Exit(1)
	} else if !contains(err.Error(), "does not exist") {
		fmt.Fprintf(os.Stderr, "unexpected error: %v\n", err)
		os.Exit(1)
	}

	// Test 5: rollback to previous.
	_ = os.MkdirAll(v1Dir, 0755)
	_ = os.MkdirAll(v2Dir, 0755)
	_ = os.RemoveAll(liveLink)
	if err := deploy(liveLink, v1Dir); err != nil {
		fmt.Fprintf(os.Stderr, "rollback deploy v1: %v\n", err)
		os.Exit(1)
	}
	assert(getTarget(liveLink) == v1Dir, "Rollback should restore v1")
	if err := deploy(liveLink, v2Dir); err != nil {
		fmt.Fprintf(os.Stderr, "rollback deploy v2: %v\n", err)
		os.Exit(1)
	}
	assert(getTarget(liveLink) == v2Dir, "Should point to v2")
	if err := deploy(liveLink, v1Dir); err != nil {
		fmt.Fprintf(os.Stderr, "rollback deploy v1 again: %v\n", err)
		os.Exit(1)
	}
	assert(getTarget(liveLink) == v1Dir, "Rollback should restore v1")

	// Test 6: multiple deployments.
	_ = os.RemoveAll(liveLink)
	for i := 1; i <= 5; i++ {
		verDir := filepath.Join(tmpdir, fmt.Sprintf("app-v%d", i))
		_ = os.MkdirAll(verDir, 0755)
		if err := deploy(liveLink, verDir); err != nil {
			fmt.Fprintf(os.Stderr, "deploy v%d: %v\n", i, err)
			os.Exit(1)
		}
		assert(linkExists(liveLink), "Link should exist")
		assert(getTarget(liveLink) == verDir, "Should point to v%d", i)
		_, err = os.Stat(getTarget(liveLink))
		assert(err == nil, "Target should be accessible")
	}

	fmt.Println("atomic_symlink_swap passed")
}

func contains(s, substr string) bool {
	return len(s) >= len(substr) && len(substr) > 0 && find(s, substr) >= 0
}

func find(s, substr string) int {
	for i := 0; i <= len(s)-len(substr); i++ {
		if s[i:i+len(substr)] == substr {
			return i
		}
	}
	return -1
}
