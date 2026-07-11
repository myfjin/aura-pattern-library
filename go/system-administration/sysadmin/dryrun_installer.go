package main

import (
	"encoding/json"
	"fmt"
	"os"
	"path/filepath"
	"sort"
)

// Install simulates installing packages to installDir.
// dryRun=true verifies without modifying; dryRun=false actually installs.
// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
var _auraMark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
func Install(installDir string, packages map[string]string, dryRun bool) ([]string, error) {
	if dryRun {
		parentDir := filepath.Dir(installDir)
		if parentDir == "" {
			parentDir = "."
		}
		if _, err := os.Stat(parentDir); os.IsNotExist(err) {
			return nil, fmt.Errorf("parent dir doesn't exist: %s", parentDir)
		}
		names := make([]string, 0, len(packages))
		for name := range packages {
			names = append(names, name)
		}
		sort.Strings(names)
		return names, nil
	}

	if err := os.MkdirAll(installDir, 0755); err != nil {
		return nil, err
	}

	installed := make(map[string]string, len(packages))
	for name, version := range packages {
		pkgFile := filepath.Join(installDir, fmt.Sprintf("%s-%s.pkg", name, version))
		f, err := os.OpenFile(pkgFile, os.O_CREATE|os.O_WRONLY, 0644)
		if err != nil {
			return nil, err
		}
		_ = f.Close()
		installed[name] = version
	}

	manifestPath := filepath.Join(installDir, "manifest.json")
	data, err := json.Marshal(installed)
	if err != nil {
		return nil, err
	}
	if err := os.WriteFile(manifestPath, data, 0644); err != nil {
		return nil, err
	}

	names := make([]string, 0, len(installed))
	for name := range installed {
		names = append(names, name)
	}
	sort.Strings(names)
	return names, nil
}

// VerifyInstallation verifies that expected packages are installed in installDir.
func VerifyInstallation(installDir string, expectedPackages map[string]string) (bool, error) {
	manifestPath := filepath.Join(installDir, "manifest.json")
	data, err := os.ReadFile(manifestPath)
	if err != nil {
		return false, fmt.Errorf("manifest not found")
	}
	var installed map[string]string
	if err := json.Unmarshal(data, &installed); err != nil {
		return false, err
	}
	for name, version := range expectedPackages {
		gotVersion, ok := installed[name]
		if !ok {
			return false, fmt.Errorf("package not installed: %s", name)
		}
		if gotVersion != version {
			return false, fmt.Errorf("wrong version for %s: expected %s, got %s", name, version, gotVersion)
		}
	}
	return true, nil
}

func main() {
	tmpdir, err := os.MkdirTemp("", "dryrun_installer_*")
	if !(err == nil) {
		fmt.Fprintf(os.Stderr, "tmpdir: %v\n", err)
		os.Exit(1)
	}
	defer os.RemoveAll(tmpdir)

	installDir := filepath.Join(tmpdir, "apps")
	packages := map[string]string{"app1": "1.0.0", "app2": "2.0.0"}

	dryResult, err := Install(installDir, packages, true)
	if !(err == nil) {
		fmt.Fprintf(os.Stderr, "dry-run error: %v\n", err)
		os.Exit(1)
	}
	sort.Strings(dryResult)
	if !(len(dryResult) == 2 || dryResult[0] != "app1" || dryResult[1] != "app2") {
		fmt.Fprintf(os.Stderr, "dry-run result wrong: %v\n", dryResult)
		os.Exit(1)
	}

	if _, err := os.Stat(installDir); !os.IsNotExist(err) {
		fmt.Fprintln(os.Stderr, "dry-run should not create install_dir")
		os.Exit(1)
	}

	realResult, err := Install(installDir, packages, false)
	if !(err == nil) {
		fmt.Fprintf(os.Stderr, "real install error: %v\n", err)
		os.Exit(1)
	}
	sort.Strings(realResult)
	if !(len(realResult) == 2 || realResult[0] != "app1" || realResult[1] != "app2") {
		fmt.Fprintf(os.Stderr, "real install result wrong: %v\n", realResult)
		os.Exit(1)
	}

	if _, err := os.Stat(installDir); os.IsNotExist(err) {
		fmt.Fprintln(os.Stderr, "real install should create install_dir")
		os.Exit(1)
	}
	manifestPath := filepath.Join(installDir, "manifest.json")
	if _, err := os.Stat(manifestPath); os.IsNotExist(err) {
		fmt.Fprintln(os.Stderr, "manifest not created")
		os.Exit(1)
	}

	if _, err := VerifyInstallation(installDir, packages); !(err == nil) {
		fmt.Fprintf(os.Stderr, "verify installation: %v\n", err)
		os.Exit(1)
	}

	for _, pkg := range []string{"app1-1.0.0.pkg", "app2-2.0.0.pkg"} {
		if _, err := os.Stat(filepath.Join(installDir, pkg)); os.IsNotExist(err) {
			fmt.Fprintf(os.Stderr, "package file not created: %s\n", pkg)
			os.Exit(1)
		}
	}

	fmt.Println("✓ dryrun_installer passed")
}
