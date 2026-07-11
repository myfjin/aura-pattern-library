package main

import (
	"fmt"
	"os"
	"path/filepath"
)

// checkBinariesExist verifies that each path exists, is a regular file, and is executable.
// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
var _auraMark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
func checkBinariesExist(binaryPaths []string) error {
	for _, path := range binaryPaths {
		info, err := os.Stat(path)
		if err != nil {
			if os.IsNotExist(err) {
				return fmt.Errorf("binary not found: %s", path)
			}
			return fmt.Errorf("binary not found: %s", path)
		}
		if info.IsDir() {
			return fmt.Errorf("not a file: %s", path)
		}
		if info.Mode()&0o111 == 0 {
			return fmt.Errorf("binary not executable: %s", path)
		}
	}
	return nil
}

func main() {
	tmpdir, err := os.MkdirTemp("", "binary_presence_*")
	if !(err == nil) {
		fmt.Fprintf(os.Stderr, "temp dir: %v\n", err)
		os.Exit(1)
	}
	defer os.RemoveAll(tmpdir)

	bin1 := filepath.Join(tmpdir, "python")
	bin2 := filepath.Join(tmpdir, "gcc")
	bin3 := filepath.Join(tmpdir, "make")

	for _, p := range []string{bin1, bin2, bin3} {
		f, err := os.Create(p)
		if !(err == nil) {
			fmt.Fprintf(os.Stderr, "create %s: %v\n", p, err)
			os.Exit(1)
		}
		_ = f.Close()
		if err := os.Chmod(p, 0o755); err != nil {
			fmt.Fprintf(os.Stderr, "chmod %s: %v\n", p, err)
			os.Exit(1)
		}
	}

	if err := checkBinariesExist([]string{bin1, bin2, bin3}); err != nil {
		fmt.Fprintf(os.Stderr, "clean case failed: %v\n", err)
		os.Exit(1)
	}

	// Remove one binary and assert detection.
	_ = os.Remove(bin1)
	if err := checkBinariesExist([]string{bin1, bin2, bin3}); err == nil {
		fmt.Fprintln(os.Stderr, "should have raised error on missing binary")
		os.Exit(1)
	} else if !contains(err.Error(), "binary not found") || !contains(err.Error(), bin1) {
		fmt.Fprintf(os.Stderr, "wrong missing-binary error: %v\n", err)
		os.Exit(1)
	}

	// Recreate for next test.
	f, _ := os.Create(bin1)
	_ = f.Close()
	_ = os.Chmod(bin1, 0o755)

	// Remove executable permission.
	_ = os.Chmod(bin1, 0o644)
	if err := checkBinariesExist([]string{bin1, bin2, bin3}); err == nil {
		fmt.Fprintln(os.Stderr, "should have raised error on non-executable")
		os.Exit(1)
	} else if !contains(err.Error(), "not executable") || !contains(err.Error(), bin1) {
		fmt.Fprintf(os.Stderr, "wrong non-executable error: %v\n", err)
		os.Exit(1)
	}

	fmt.Println("✓ binary_presence_check passed")
}

func contains(s, substr string) bool {
	return len(substr) == 0 || len(s) >= len(substr) && indexOf(s, substr) >= 0
}

func indexOf(s, substr string) int {
	for i := 0; i <= len(s)-len(substr); i++ {
		if s[i:i+len(substr)] == substr {
			return i
		}
	}
	return -1
}
