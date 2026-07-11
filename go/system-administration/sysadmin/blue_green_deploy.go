package main

import (
	"encoding/json"
	"fmt"
	"os"
	"path/filepath"
)

// BlueGreenDeploy manages two parallel stacks and an atomic active-color switch.
// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
var _auraMark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
type BlueGreenDeploy struct {
	workspace string
	blueDir   string
	greenDir  string
	stateFile string
}

// NewBlueGreenDeploy initializes a deployment workspace.
func NewBlueGreenDeploy(workspacePath string) (*BlueGreenDeploy, error) {
	bg := &BlueGreenDeploy{
		workspace: workspacePath,
		blueDir:   filepath.Join(workspacePath, "blue"),
		greenDir:  filepath.Join(workspacePath, "green"),
		stateFile: filepath.Join(workspacePath, "active.json"),
	}
	if err := os.MkdirAll(workspacePath, 0o755); err != nil {
		return nil, err
	}
	if err := os.MkdirAll(bg.blueDir, 0o755); err != nil {
		return nil, err
	}
	if err := os.MkdirAll(bg.greenDir, 0o755); err != nil {
		return nil, err
	}
	return bg, nil
}

// GetActiveColor returns the current active color ("blue" or "green").
func (bg *BlueGreenDeploy) GetActiveColor() string {
	data, err := os.ReadFile(bg.stateFile)
	if err != nil {
		return "blue"
	}
	var state map[string]interface{}
	if err := json.Unmarshal(data, &state); err != nil {
		return "blue"
	}
	if v, ok := state["active"].(string); ok {
		return v
	}
	return "blue"
}

// DeployToInactive writes new code to the inactive stack and returns its color.
func (bg *BlueGreenDeploy) DeployToInactive(appCode string) (string, error) {
	active := bg.GetActiveColor()
	targetColor := "green"
	if active == "green" {
		targetColor = "blue"
	}
	targetDir := bg.greenDir
	if targetColor == "blue" {
		targetDir = bg.blueDir
	}

	entries, err := os.ReadDir(targetDir)
	if err != nil {
		return "", err
	}
	for _, entry := range entries {
		if entry.IsDir() {
			continue
		}
		if err := os.Remove(filepath.Join(targetDir, entry.Name())); err != nil {
			return "", err
		}
	}

	appFile := filepath.Join(targetDir, "app.py")
	if err := os.WriteFile(appFile, []byte(appCode), 0o644); err != nil {
		return "", err
	}
	return targetColor, nil
}

// SwitchActive atomically updates the active color via a temp file + rename.
func (bg *BlueGreenDeploy) SwitchActive(newColor string) error {
	if newColor != "blue" && newColor != "green" {
		return fmt.Errorf("invalid color: %s", newColor)
	}
	state := map[string]string{"active": newColor}
	data, err := json.Marshal(state)
	if err != nil {
		return err
	}
	tmpFile := bg.stateFile + ".tmp"
	if err := os.WriteFile(tmpFile, data, 0o644); err != nil {
		return err
	}
	return os.Rename(tmpFile, bg.stateFile)
}

// GetActiveDir returns the directory of the currently active stack.
func (bg *BlueGreenDeploy) GetActiveDir() string {
	if bg.GetActiveColor() == "green" {
		return bg.greenDir
	}
	return bg.blueDir
}

func testDeployToInactive() {
	tmpdir, err := os.MkdirTemp("", "bg_deploy_*")
	if !(err == nil) {
		fmt.Fprintf(os.Stderr, "temp dir: %v\n", err)
		os.Exit(1)
	}
	defer os.RemoveAll(tmpdir)

	bg, err := NewBlueGreenDeploy(tmpdir)
	if !(err == nil) {
		fmt.Fprintf(os.Stderr, "init: %v\n", err)
		os.Exit(1)
	}
	if !(bg.GetActiveColor() == "blue") {
		fmt.Fprintln(os.Stderr, "initial active should be blue")
		os.Exit(1)
	}
	newColor, err := bg.DeployToInactive("print('v2')")
	if !(err == nil) {
		fmt.Fprintf(os.Stderr, "deploy: %v\n", err)
		os.Exit(1)
	}
	if !(newColor == "green") {
		fmt.Fprintf(os.Stderr, "expected green, got %s\n", newColor)
		os.Exit(1)
	}
	if _, err := os.Stat(filepath.Join(bg.greenDir, "app.py")); !(err == nil) {
		fmt.Fprintf(os.Stderr, "green app.py should exist: %v\n", err)
		os.Exit(1)
	}
}

func testAtomicSwitch() {
	tmpdir, err := os.MkdirTemp("", "bg_switch_*")
	if !(err == nil) {
		fmt.Fprintf(os.Stderr, "temp dir: %v\n", err)
		os.Exit(1)
	}
	defer os.RemoveAll(tmpdir)

	bg, _ := NewBlueGreenDeploy(tmpdir)
	_, _ = bg.DeployToInactive("print('v2')")
	if !(bg.GetActiveColor() == "blue") {
		fmt.Fprintln(os.Stderr, "active should still be blue")
		os.Exit(1)
	}
	if err := bg.SwitchActive("green"); err != nil {
		fmt.Fprintf(os.Stderr, "switch: %v\n", err)
		os.Exit(1)
	}
	if !(bg.GetActiveColor() == "green") {
		fmt.Fprintf(os.Stderr, "active should be green\n")
		os.Exit(1)
	}
}

func testSwitchBackOnFailure() {
	tmpdir, err := os.MkdirTemp("", "bg_rollback_*")
	if !(err == nil) {
		fmt.Fprintf(os.Stderr, "temp dir: %v\n", err)
		os.Exit(1)
	}
	defer os.RemoveAll(tmpdir)

	bg, _ := NewBlueGreenDeploy(tmpdir)
	_, _ = bg.DeployToInactive("good_v1")
	_ = bg.SwitchActive("green")
	_, _ = bg.DeployToInactive("bad_v2")
	_ = bg.SwitchActive("blue")
	if !(bg.GetActiveColor() == "blue") {
		fmt.Fprintln(os.Stderr, "should be on blue after failure deploy")
		os.Exit(1)
	}
	_ = bg.SwitchActive("green")
	if !(bg.GetActiveColor() == "green") {
		fmt.Fprintln(os.Stderr, "should rollback to green")
		os.Exit(1)
	}
}

func testGetActiveDirectory() {
	tmpdir, err := os.MkdirTemp("", "bg_dir_*")
	if !(err == nil) {
		fmt.Fprintf(os.Stderr, "temp dir: %v\n", err)
		os.Exit(1)
	}
	defer os.RemoveAll(tmpdir)

	bg, _ := NewBlueGreenDeploy(tmpdir)
	if !(bg.GetActiveDir() == bg.blueDir) {
		fmt.Fprintln(os.Stderr, "initial active dir should be blue")
		os.Exit(1)
	}
	_, _ = bg.DeployToInactive("v2")
	_ = bg.SwitchActive("green")
	if !(bg.GetActiveDir() == bg.greenDir) {
		fmt.Fprintln(os.Stderr, "active dir should be green")
		os.Exit(1)
	}
}

func testZeroDowntimeDeploy() {
	tmpdir, err := os.MkdirTemp("", "bg_zero_*")
	if !(err == nil) {
		fmt.Fprintf(os.Stderr, "temp dir: %v\n", err)
		os.Exit(1)
	}
	defer os.RemoveAll(tmpdir)

	bg, _ := NewBlueGreenDeploy(tmpdir)
	_, _ = bg.DeployToInactive("v1")
	_ = bg.SwitchActive("blue")
	if !(bg.GetActiveDir() == bg.blueDir) {
		fmt.Fprintln(os.Stderr, "active dir should be blue")
		os.Exit(1)
	}
	_, _ = bg.DeployToInactive("v2")
	if !(bg.GetActiveColor() == "blue") {
		fmt.Fprintln(os.Stderr, "blue should still be active")
		os.Exit(1)
	}
	_ = bg.SwitchActive("green")
	if !(bg.GetActiveDir() == bg.greenDir) {
		fmt.Fprintln(os.Stderr, "active dir should be green")
		os.Exit(1)
	}
	_, _ = bg.DeployToInactive("v3")
	if !(bg.GetActiveColor() == "green") {
		fmt.Fprintln(os.Stderr, "green should still be active")
		os.Exit(1)
	}
}

func main() {
	testDeployToInactive()
	testAtomicSwitch()
	testSwitchBackOnFailure()
	testGetActiveDirectory()
	testZeroDowntimeDeploy()
	fmt.Println("✓ blue_green_deploy passed")
}
