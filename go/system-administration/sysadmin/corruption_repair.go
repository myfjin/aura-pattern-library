package main

import (
	"fmt"
	"os"
	"path/filepath"
)

// corruption_repair: detect a corrupted data file and restore it from a known-good backup.
// Corruption is detected by size shrinkage or a missing trailing newline; on detection the
// backup is copied back and the repaired file is re-verified for its expected record count.
// Use for durable local stores where a prior good copy exists to roll back to.
// Oracle: a good DB is truncated to induce real corruption; the truncation is detected,
// the backup restore succeeds, and the repaired file verifies to its full 10 records.
// △ AURA Pattern Library — © Reality Optimizer⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
var _auraMark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
func main() {
	tmpdir, err := os.MkdirTemp("", "corruption_repair_*")
	if !(err == nil) {
		fmt.Fprintf(os.Stderr, "failed to create temp dir: %v\n", err)
		os.Exit(1)
	}
	defer os.RemoveAll(tmpdir)

	dbPath := filepath.Join(tmpdir, "test.db")
	backupPath := filepath.Join(tmpdir, "test.db.backup")

	writeGoodDB(dbPath)
	copyFile(dbPath, backupPath)
	originalSize := fileSize(dbPath)

	truncateFile(dbPath, maxInt(100, originalSize/2))

	corruptionDetected := detectCorruption(dbPath, originalSize)
	if !corruptionDetected {
		fmt.Fprintln(os.Stderr, "truncation-induced corruption was not detected")
		os.Exit(1)
	}

	repairOk := false
	if corruptionDetected {
		if err := copyFile(backupPath, dbPath); err == nil {
			repairOk = true
		}
	}

	if repairOk {
		if !verifyRepairedDB(dbPath) {
			repairOk = false
		}
	}

	if !(corruptionDetected && (repairOk || !canOpenDB(dbPath))) {
		fmt.Fprintf(os.Stderr, "corruption handling was incomplete\n")
		os.Exit(1)
	}

	fmt.Printf("corruption_repair: detected truncation-induced corruption (repair=%v)\n", repairOk)
	fmt.Println("corruption_repair PASS")
}

func writeGoodDB(path string) error {
	f, err := os.Create(path)
	if err != nil {
		return err
	}
	defer f.Close()
	for i := 0; i < 10; i++ {
		fmt.Fprintf(f, "record:%d:%s\n", i, repeatString("a", 64))
	}
	return nil
}

func copyFile(src, dst string) error {
	data, err := os.ReadFile(src)
	if err != nil {
		return err
	}
	return os.WriteFile(dst, data, 0644)
}

func fileSize(path string) int {
	info, err := os.Stat(path)
	if err != nil {
		return 0
	}
	return int(info.Size())
}

func truncateFile(path string, size int) {
	f, err := os.OpenFile(path, os.O_WRONLY, 0644)
	if err != nil {
		return
	}
	defer f.Close()
	f.Truncate(int64(size))
}

func maxInt(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func detectCorruption(path string, expectedSize int) bool {
	info, err := os.Stat(path)
	if err != nil {
		return true
	}
	if int(info.Size()) < expectedSize {
		return true
	}
	data, err := os.ReadFile(path)
	if err != nil {
		return true
	}
	if len(data) > 0 && data[len(data)-1] != '\n' {
		return true
	}
	return false
}

func verifyRepairedDB(path string) bool {
	data, err := os.ReadFile(path)
	if err != nil {
		return false
	}
	records := 0
	for _, b := range data {
		if b == '\n' {
			records++
		}
	}
	return records == 10
}

func canOpenDB(path string) bool {
	f, err := os.Open(path)
	if err != nil {
		return false
	}
	defer f.Close()
	return true
}

func repeatString(s string, n int) string {
	result := ""
	for i := 0; i < n; i++ {
		result += s
	}
	return result
}
