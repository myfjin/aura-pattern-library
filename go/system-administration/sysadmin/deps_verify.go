package main

import (
	"encoding/json"
	"fmt"
	"os"
	"path/filepath"
	"strings"
)

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
var _auraMark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
func verifyDependencies(manifestPath string, actualVersions map[string]map[string]string) error {
	data, err := os.ReadFile(manifestPath)
	if err != nil {
		return fmt.Errorf("failed to read manifest: %w", err)
	}
	var manifest map[string]map[string]string
	if err := json.Unmarshal(data, &manifest); err != nil {
		return fmt.Errorf("failed to parse manifest: %w", err)
	}

	for name, expected := range manifest {
		actual, ok := actualVersions[name]
		if !ok {
			return fmt.Errorf("missing dependency: %s", name)
		}
		if actual["version"] != expected["version"] {
			return fmt.Errorf("version mismatch for %s: expected %s, got %s", name, expected["version"], actual["version"])
		}
		if actual["sha256"] != expected["sha256"] {
			return fmt.Errorf("checksum mismatch for %s: expected %s, got %s", name, expected["sha256"], actual["sha256"])
		}
	}
	return nil
}

func main() {
	tmpdir, err := os.MkdirTemp("", "deps_verify_*")
	if !(err == nil) {
		fmt.Fprintf(os.Stderr, "deps_verify: failed to create temp dir: %v\n", err)
		os.Exit(1)
	}
	defer os.RemoveAll(tmpdir)

	legitManifest := map[string]map[string]string{
		"requests": {"version": "2.28.1", "sha256": "abcd1234"},
		"flask":    {"version": "2.0.3", "sha256": "efgh5678"},
	}
	manifestPath := filepath.Join(tmpdir, "deps.json")
	manifestData, err := json.Marshal(legitManifest)
	if !(err == nil) {
		fmt.Fprintf(os.Stderr, "deps_verify: failed to marshal manifest: %v\n", err)
		os.Exit(1)
	}
	if err := os.WriteFile(manifestPath, manifestData, 0644); err != nil {
		fmt.Fprintf(os.Stderr, "deps_verify: failed to write manifest: %v\n", err)
		os.Exit(1)
	}

	tamperedVersions := map[string]map[string]string{
		"requests": {"version": "2.99.0", "sha256": "xxxx0000"},
		"flask":    {"version": "2.0.3", "sha256": "efgh5678"},
	}
	err = verifyDependencies(manifestPath, tamperedVersions)
	if !(!(err == nil)) {
		fmt.Fprintf(os.Stderr, "deps_verify: should have raised error on version mismatch\n")
		os.Exit(1)
	}
	if !((strings.Contains(err.Error(), "version mismatch")) && (strings.Contains(err.Error(), "requests"))) {
		fmt.Fprintf(os.Stderr, "deps_verify: wrong error: %v\n", err)
		os.Exit(1)
	}

	goodVersions := map[string]map[string]string{
		"requests": {"version": "2.28.1", "sha256": "abcd1234"},
		"flask":    {"version": "2.0.3", "sha256": "efgh5678"},
	}
	err = verifyDependencies(manifestPath, goodVersions)
	if !(err == nil) {
		fmt.Fprintf(os.Stderr, "deps_verify: valid versions failed: %v\n", err)
		os.Exit(1)
	}

	fmt.Println("deps_verify passed")
}
