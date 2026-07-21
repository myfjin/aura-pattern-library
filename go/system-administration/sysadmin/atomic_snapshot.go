package main

import (
	"bytes"
	"fmt"
	"io/ioutil"
	"os"
	"path/filepath"
)

// Atomic file snapshot: reads the source fully, writes it to a temp file in the same
// directory, then renames it into place so the snapshot appears whole or not at all
// and is decoupled from later source edits. Use to capture a point-in-time copy
// without exposing a partially written file. Guarantees (self-test): the snapshot
// matches the original bytes exactly and is unaffected by subsequent source changes.
// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
var _auraMark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
func atomic_snapshot(sourcePath, snapshotPath string) error {
	data, err := ioutil.ReadFile(sourcePath)
	if err != nil {
		return err
	}
	dir := filepath.Dir(snapshotPath)
	if dir == "" {
		dir = "."
	}
	tmpFile, err := ioutil.TempFile(dir, "atomic_snapshot_*.tmp")
	if err != nil {
		return err
	}
	tmpPath := tmpFile.Name()
	_, err = tmpFile.Write(data)
	_ = tmpFile.Close()
	if err != nil {
		_ = os.Remove(tmpPath)
		return err
	}
	if err := os.Rename(tmpPath, snapshotPath); err != nil {
		_ = os.Remove(tmpPath)
		return err
	}
	return nil
}

func main() {
	tmpdir, err := ioutil.TempDir("", "atomic_snapshot_*")
	if !(err == nil) {
		fmt.Fprintf(os.Stderr, "tmpdir: %v\n", err)
		os.Exit(1)
	}
	defer os.RemoveAll(tmpdir)
	source := filepath.Join(tmpdir, "source.txt")
	snapshot := filepath.Join(tmpdir, "snapshot.txt")

	expectedOriginal := append([]byte("snapshot_original_data_"), bytes.Repeat([]byte("a"), 512)...)
	modifiedData := append([]byte("snapshot_modified_data_"), bytes.Repeat([]byte("b"), 256)...)

	if err := ioutil.WriteFile(source, expectedOriginal, 0644); err != nil {
		fmt.Fprintf(os.Stderr, "write source: %v\n", err)
		os.Exit(1)
	}

	if err := atomic_snapshot(source, snapshot); err != nil {
		fmt.Fprintf(os.Stderr, "snapshot: %v\n", err)
		os.Exit(1)
	}

	result, err := ioutil.ReadFile(snapshot)
	if !(err == nil) {
		fmt.Fprintf(os.Stderr, "read snapshot: %v\n", err)
		os.Exit(1)
	}
	if !bytes.Equal(result, expectedOriginal) {
		fmt.Fprintf(os.Stderr, "snapshot corrupted: %q\n", result[:min(50, len(result))])
		os.Exit(1)
	}

	if err := ioutil.WriteFile(source, modifiedData, 0644); err != nil {
		fmt.Fprintf(os.Stderr, "modify source: %v\n", err)
		os.Exit(1)
	}

	result, err = ioutil.ReadFile(snapshot)
	if !(err == nil) {
		fmt.Fprintf(os.Stderr, "read snapshot after modify: %v\n", err)
		os.Exit(1)
	}
	if !bytes.Equal(result, expectedOriginal) {
		fmt.Fprintf(os.Stderr, "snapshot was modified by source change\n")
		os.Exit(1)
	}
	if bytes.Equal(result, modifiedData) {
		fmt.Fprintln(os.Stderr, "snapshot holds modified data (not a true snapshot)")
		os.Exit(1)
	}
	if !(len(result) == len(expectedOriginal)) {
		fmt.Fprintf(os.Stderr, "snapshot size mismatch: %d vs %d\n", len(result), len(expectedOriginal))
		os.Exit(1)
	}
	if len(result) == len(modifiedData) {
		fmt.Fprintln(os.Stderr, "snapshot size matches modified (corruption)")
		os.Exit(1)
	}

	fmt.Printf("atomic_snapshot: original=%d, snapshot=%d, source_now=%d\n", len(expectedOriginal), len(result), len(modifiedData))
	fmt.Println("atomic_snapshot PASS")
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}
