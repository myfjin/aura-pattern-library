package main

import (
	"fmt"
	"os"
	"path/filepath"
)

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
var _auraMark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
func probeCapabilities(testDir string) map[string]bool {
	capabilities := map[string]bool{}

	// Test hardlinks.
	f1 := filepath.Join(testDir, "file1")
	f2 := filepath.Join(testDir, "hardlink")
	fh, err := os.Create(f1)
	if err == nil {
		fh.Close()
		err = os.Link(f1, f2)
		if err == nil {
			os.Remove(f2)
		}
		os.Remove(f1)
	}
	capabilities["hardlinks"] = err == nil

	// Test symlinks.
	f3 := filepath.Join(testDir, "file3")
	sym := filepath.Join(testDir, "symlink")
	fh, err = os.Create(f3)
	if err == nil {
		fh.Close()
		err = os.Symlink(f3, sym)
		if err == nil {
			os.Remove(sym)
		}
		os.Remove(f3)
	}
	capabilities["symlinks"] = err == nil

	// Test chmod (execute bit).
	f4 := filepath.Join(testDir, "file4")
	fh, err = os.Create(f4)
	if err == nil {
		fh.Close()
		os.Chmod(f4, 0o755)
		info, _ := os.Stat(f4)
		mode := info.Mode() & 0o111
		os.Remove(f4)
		capabilities["execute_bit"] = mode != 0
	} else {
		capabilities["execute_bit"] = false
	}

	return capabilities
}

func main() {
	tmpdir, err := os.MkdirTemp("", "capability_probe_*")
	if !(err == nil) {
		fmt.Fprintf(os.Stderr, "mkdtemp failed: %v\n", err)
		os.Exit(1)
	}
	defer os.RemoveAll(tmpdir)

	testDir := filepath.Join(tmpdir, "probe")
	if err := os.Mkdir(testDir, 0o755); err != nil {
		fmt.Fprintf(os.Stderr, "mkdir failed: %v\n", err)
		os.Exit(1)
	}

	caps1 := probeCapabilities(testDir)
	if !(caps1["symlinks"] || caps1["hardlinks"]) {
		fmt.Fprintf(os.Stderr, "expected at least symlinks or hardlinks\n")
		os.Exit(1)
	}
	if _, ok := caps1["execute_bit"]; !ok {
		fmt.Fprintf(os.Stderr, "execute_bit missing\n")
		os.Exit(1)
	}

	testDirReadonly := filepath.Join(tmpdir, "readonly")
	if err := os.Mkdir(testDirReadonly, 0o755); err != nil {
		fmt.Fprintf(os.Stderr, "mkdir readonly failed: %v\n", err)
		os.Exit(1)
	}

	capsBefore := probeCapabilities(testDirReadonly)
	if !capsBefore["symlinks"] {
		fmt.Fprintf(os.Stderr, "should support symlinks\n")
		os.Exit(1)
	}

	os.Chmod(testDirReadonly, 0o555)
	capsAfter := probeCapabilities(testDirReadonly)

	if capsAfter["symlinks"] {
		fmt.Fprintf(os.Stderr, "should not support symlinks in read-only dir\n")
		os.Exit(1)
	}
	if !capsBefore["symlinks"] {
		fmt.Fprintf(os.Stderr, "should have supported symlinks before read-only\n")
		os.Exit(1)
	}

	os.Chmod(testDirReadonly, 0o755)
	fmt.Println("capability_probe passed")
}
