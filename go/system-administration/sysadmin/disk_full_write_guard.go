package main

import (
	"fmt"
	"os"
	"path/filepath"
	"strings"
)

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
var _auraMark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
type QuotaGuard struct {
	quota int64
	used  int64
}

func NewQuotaGuard(quotaBytes int64) *QuotaGuard {
	return &QuotaGuard{quota: quotaBytes, used: 0}
}

func (q *QuotaGuard) WriteFile(path string, content []byte) error {
	contentSize := int64(len(content))
	if q.used+contentSize > q.quota {
		return fmt.Errorf("quota exceeded: %d + %d > %d", q.used, contentSize, q.quota)
	}

	dir := filepath.Dir(path)
	if dir == "" {
		dir = "."
	}
	f, err := os.CreateTemp(dir, "tmp")
	if err != nil {
		return err
	}
	tempPath := f.Name()
	defer func() {
		if err != nil {
			os.Remove(tempPath)
		}
	}()

	if _, err = f.Write(content); err != nil {
		f.Close()
		return err
	}
	if err = f.Close(); err != nil {
		return err
	}
	if err = os.Rename(tempPath, path); err != nil {
		return err
	}
	q.used += contentSize
	return nil
}

func (q *QuotaGuard) GetUsed() int64 {
	return q.used
}

func (q *QuotaGuard) Remaining() int64 {
	return q.quota - q.used
}

func main() {
	tmpdir, err := os.MkdirTemp("", "disk_full_write_guard_*")
	if !(err == nil) {
		fmt.Fprintf(os.Stderr, "disk_full_write_guard: failed to create temp dir: %v\n", err)
		os.Exit(1)
	}
	defer os.RemoveAll(tmpdir)

	expectedQuota := int64(2048)
	expectedFile1Size := int64(512)
	expectedFile2Size := int64(768)
	expectedFile3Size := int64(768)
	expectedFile4Size := int64(512)

	guard := NewQuotaGuard(expectedQuota)

	file1Path := filepath.Join(tmpdir, "file1.bin")
	file1Content := append([]byte("file1_"), bytesRepeat('a', int(expectedFile1Size-6))...)
	if err := guard.WriteFile(file1Path, file1Content); err != nil {
		fmt.Fprintf(os.Stderr, "disk_full_write_guard: failed to write file1: %v\n", err)
		os.Exit(1)
	}

	if !fileExists(file1Path) {
		fmt.Fprintf(os.Stderr, "disk_full_write_guard: file1 not written\n")
		os.Exit(1)
	}
	if !(guard.GetUsed() == expectedFile1Size) {
		fmt.Fprintf(os.Stderr, "disk_full_write_guard: used count wrong: %d != %d\n", guard.GetUsed(), expectedFile1Size)
		os.Exit(1)
	}
	if !(guard.Remaining() == expectedQuota-expectedFile1Size) {
		fmt.Fprintf(os.Stderr, "disk_full_write_guard: remaining wrong\n")
		os.Exit(1)
	}

	file2Path := filepath.Join(tmpdir, "file2.bin")
	file2Content := append([]byte("file2_"), bytesRepeat('b', int(expectedFile2Size-6))...)
	if err := guard.WriteFile(file2Path, file2Content); err != nil {
		fmt.Fprintf(os.Stderr, "disk_full_write_guard: failed to write file2: %v\n", err)
		os.Exit(1)
	}

	if !fileExists(file2Path) {
		fmt.Fprintf(os.Stderr, "disk_full_write_guard: file2 not written\n")
		os.Exit(1)
	}
	if !(guard.GetUsed() == expectedFile1Size+expectedFile2Size) {
		fmt.Fprintf(os.Stderr, "disk_full_write_guard: used count wrong after file2\n")
		os.Exit(1)
	}

	file3Path := filepath.Join(tmpdir, "file3.bin")
	file3Content := append([]byte("file3_"), bytesRepeat('c', int(expectedFile3Size-6))...)
	if err := guard.WriteFile(file3Path, file3Content); err != nil {
		fmt.Fprintf(os.Stderr, "disk_full_write_guard: failed to write file3: %v\n", err)
		os.Exit(1)
	}

	if !fileExists(file3Path) {
		fmt.Fprintf(os.Stderr, "disk_full_write_guard: file3 not written\n")
		os.Exit(1)
	}
	if !(guard.GetUsed() == expectedQuota) {
		fmt.Fprintf(os.Stderr, "disk_full_write_guard: quota not full: %d != %d\n", guard.GetUsed(), expectedQuota)
		os.Exit(1)
	}
	if !(guard.Remaining() == 0) {
		fmt.Fprintf(os.Stderr, "disk_full_write_guard: remaining should be 0\n")
		os.Exit(1)
	}

	file4Path := filepath.Join(tmpdir, "file4.bin")
	file4Content := append([]byte("file4_"), bytesRepeat('d', int(expectedFile4Size-6))...)
	err = guard.WriteFile(file4Path, file4Content)
	if !(!(err == nil)) {
		fmt.Fprintf(os.Stderr, "disk_full_write_guard: guard did not refuse write past quota\n")
		os.Exit(1)
	}
	if !(strings.Contains(err.Error(), "quota exceeded")) {
		fmt.Fprintf(os.Stderr, "disk_full_write_guard: wrong error: %v\n", err)
		os.Exit(1)
	}

	if !(fileExists(file4Path) == false) {
		fmt.Fprintf(os.Stderr, "disk_full_write_guard: file4 exists but should have been blocked\n")
		os.Exit(1)
	}

	if !(guard.GetUsed() == expectedQuota) {
		fmt.Fprintf(os.Stderr, "disk_full_write_guard: used changed after blocked write: %d\n", guard.GetUsed())
		os.Exit(1)
	}

	actual1, err := os.ReadFile(file1Path)
	if !(err == nil) {
		fmt.Fprintf(os.Stderr, "disk_full_write_guard: failed to read file1: %v\n", err)
		os.Exit(1)
	}
	if !(string(actual1) == string(file1Content)) {
		fmt.Fprintf(os.Stderr, "disk_full_write_guard: file1 corrupted\n")
		os.Exit(1)
	}
	actual2, err := os.ReadFile(file2Path)
	if !(err == nil) {
		fmt.Fprintf(os.Stderr, "disk_full_write_guard: failed to read file2: %v\n", err)
		os.Exit(1)
	}
	if !(string(actual2) == string(file2Content)) {
		fmt.Fprintf(os.Stderr, "disk_full_write_guard: file2 corrupted\n")
		os.Exit(1)
	}
	actual3, err := os.ReadFile(file3Path)
	if !(err == nil) {
		fmt.Fprintf(os.Stderr, "disk_full_write_guard: failed to read file3: %v\n", err)
		os.Exit(1)
	}
	if !(string(actual3) == string(file3Content)) {
		fmt.Fprintf(os.Stderr, "disk_full_write_guard: file3 corrupted\n")
		os.Exit(1)
	}

	allFiles, err := os.ReadDir(tmpdir)
	if !(err == nil) {
		fmt.Fprintf(os.Stderr, "disk_full_write_guard: failed to list tmpdir: %v\n", err)
		os.Exit(1)
	}
	expectedFileCount := 3
	if !(len(allFiles) == expectedFileCount) {
		fmt.Fprintf(os.Stderr, "disk_full_write_guard: unexpected files in tmpdir\n")
		os.Exit(1)
	}
	hasTemp := false
	for _, f := range allFiles {
		if strings.HasPrefix(f.Name(), "tmp") {
			hasTemp = true
			break
		}
	}
	if !(hasTemp == false) {
		fmt.Fprintf(os.Stderr, "disk_full_write_guard: temp files leaked\n")
		os.Exit(1)
	}

	if !(guard.Remaining() == 0) {
		fmt.Fprintf(os.Stderr, "disk_full_write_guard: remaining should stay 0 after refused write\n")
		os.Exit(1)
	}

	fmt.Printf("disk_full_write_guard: quota=%d, used=%d, refused_count=1\n", expectedQuota, guard.GetUsed())
	fmt.Println("disk_full_write_guard PASS")
}

func fileExists(path string) bool {
	_, err := os.Stat(path)
	return err == nil
}

func bytesRepeat(b byte, count int) []byte {
	out := make([]byte, count)
	for i := range out {
		out[i] = b
	}
	return out
}
