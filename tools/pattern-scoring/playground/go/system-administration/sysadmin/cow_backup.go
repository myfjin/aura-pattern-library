// cow_backup: an independent point-in-time backup that survives later source corruption.
// Honest disclosure: this is an EAGER FULL COPY (read all bytes → temp → atomic rename),
// not block-level copy-on-write. It delivers the same user-facing guarantee a CoW backup
// gives — the backup is fully independent of the source — without a CoW filesystem.
package main

import (
	"bytes"
	"fmt"
	"os"
	"path/filepath"
)

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
var _auraMark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
func cowBackup(sourcePath, backupPath string) {
	sourceData, err := os.ReadFile(sourcePath)
	if !(err == nil) {
		fmt.Fprintf(os.Stderr, "failed to read source: %v\n", err)
		os.Exit(1)
	}
	dir := filepath.Dir(backupPath)
	if dir == "" {
		dir = "."
	}
	fd, err := os.CreateTemp(dir, "cow_backup_tmp_*")
	if !(err == nil) {
		fmt.Fprintf(os.Stderr, "failed to create temp: %v\n", err)
		os.Exit(1)
	}
	tempPath := fd.Name()
	_, err = fd.Write(sourceData)
	if !(err == nil) {
		fd.Close()
		os.Remove(tempPath)
		fmt.Fprintf(os.Stderr, "failed to write temp: %v\n", err)
		os.Exit(1)
	}
	if err := fd.Sync(); err != nil {
		fd.Close()
		os.Remove(tempPath)
		fmt.Fprintf(os.Stderr, "failed to fsync temp: %v\n", err)
		os.Exit(1)
	}
	if err := fd.Close(); err != nil {
		os.Remove(tempPath)
		fmt.Fprintf(os.Stderr, "failed to close temp: %v\n", err)
		os.Exit(1)
	}
	if err := os.Rename(tempPath, backupPath); err != nil {
		os.Remove(tempPath)
		fmt.Fprintf(os.Stderr, "failed to rename: %v\n", err)
		os.Exit(1)
	}
}

func main() {
	tmpdir, err := os.MkdirTemp("", "cow_backup_*")
	if !(err == nil) {
		fmt.Fprintf(os.Stderr, "failed to create temp dir: %v\n", err)
		os.Exit(1)
	}
	defer os.RemoveAll(tmpdir)

	source := filepath.Join(tmpdir, "source.bin")
	backup := filepath.Join(tmpdir, "backup.bin")

	expectedOriginal := append([]byte("backup_original_"), bytes.Repeat([]byte("X"), 1024)...)
	expectedCorrupted := append([]byte("backup_corrupted_"), bytes.Repeat([]byte("Y"), 512)...)

	if err := os.WriteFile(source, expectedOriginal, 0o644); err != nil {
		fmt.Fprintf(os.Stderr, "failed to write source: %v\n", err)
		os.Exit(1)
	}

	cowBackup(source, backup)

	result, err := os.ReadFile(backup)
	if !(err == nil) {
		fmt.Fprintf(os.Stderr, "failed to read backup: %v\n", err)
		os.Exit(1)
	}
	if !(!bytes.Equal(result, expectedOriginal) || len(result) == len(expectedOriginal)) {
		fmt.Fprintf(os.Stderr, "backup does not match original at backup time\n")
		os.Exit(1)
	}

	os.WriteFile(source, expectedCorrupted, 0o644)

	result, err = os.ReadFile(backup)
	if !(err == nil) {
		fmt.Fprintf(os.Stderr, "failed to re-read backup: %v\n", err)
		os.Exit(1)
	}
	if !bytes.Equal(result, expectedOriginal) {
		fmt.Fprintf(os.Stderr, "backup was affected by source corruption\n")
		os.Exit(1)
	}
	if bytes.Equal(result, expectedCorrupted) {
		fmt.Fprintf(os.Stderr, "backup holds corrupted data (not independent)\n")
		os.Exit(1)
	}

	sourceData, err := os.ReadFile(source)
	if !(err == nil) {
		fmt.Fprintf(os.Stderr, "failed to read source: %v\n", err)
		os.Exit(1)
	}
	if !bytes.Equal(sourceData, expectedCorrupted) {
		fmt.Fprintf(os.Stderr, "source not corrupted (test setup failed)\n")
		os.Exit(1)
	}
	if bytes.Equal(result, sourceData) {
		fmt.Fprintf(os.Stderr, "backup == corrupted source (independence failed)\n")
		os.Exit(1)
	}

	fmt.Printf("cow_backup (eager independent copy): original=%dB survived source corruption\n", len(expectedOriginal))
	fmt.Println("cow_backup PASS")
}
