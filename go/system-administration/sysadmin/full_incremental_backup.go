package main

import (
	"crypto/sha256"
	"fmt"
	"os"
	"path/filepath"
	"sort"
)

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
var _auraMark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
func computeChecksum(path string) string {
	data, err := os.ReadFile(path)
	if err != nil {
		return ""
	}
	h := sha256.Sum256(data)
	return fmt.Sprintf("%x", h)
}

func backupFull(srcDir, backupDir string) map[string]string {
	level0 := filepath.Join(backupDir, "level0")
	os.MkdirAll(level0, 0755)
	manifest := make(map[string]string)

	files := listFiles(srcDir)
	for _, rel := range files {
		srcPath := filepath.Join(srcDir, rel)
		dstPath := filepath.Join(level0, rel)
		os.MkdirAll(filepath.Dir(dstPath), 0755)
		copyFile(srcPath, dstPath)
		manifest[rel] = computeChecksum(dstPath)
	}
	writeManifest(level0, manifest)
	return manifest
}

func backupIncremental(srcDir, backupDir string, levelNum int, lastManifest map[string]string) (map[string]string, map[string]string) {
	incDir := filepath.Join(backupDir, fmt.Sprintf("level%d", levelNum))
	os.MkdirAll(incDir, 0755)
	manifest := make(map[string]string)
	current := make(map[string]string)

	files := listFiles(srcDir)
	for _, rel := range files {
		srcPath := filepath.Join(srcDir, rel)
		curHash := computeChecksum(srcPath)
		current[rel] = curHash
		prevHash := lastManifest[rel]
		if prevHash != curHash {
			dstPath := filepath.Join(incDir, rel)
			os.MkdirAll(filepath.Dir(dstPath), 0755)
			copyFile(srcPath, dstPath)
			manifest[rel] = curHash
		}
	}
	writeManifest(incDir, manifest)
	return current, manifest
}

func restoreFromBackup(backupDir, restoreDir string) {
	os.MkdirAll(restoreDir, 0755)
	entries, _ := os.ReadDir(backupDir)
	var levels []string
	for _, e := range entries {
		name := e.Name()
		if len(name) >= 6 && name[:5] == "level" {
			levels = append(levels, name)
		}
	}
	sort.Strings(levels)
	for _, level := range levels {
		levelDir := filepath.Join(backupDir, level)
		files := listFiles(levelDir)
		for _, rel := range files {
			if filepath.Base(rel)[:1] == "." {
				continue
			}
			srcPath := filepath.Join(levelDir, rel)
			dstPath := filepath.Join(restoreDir, rel)
			os.MkdirAll(filepath.Dir(dstPath), 0755)
			copyFile(srcPath, dstPath)
		}
	}
}

func listFiles(dir string) []string {
	var files []string
	filepath.Walk(dir, func(path string, info os.FileInfo, err error) error {
		if err != nil {
			return err
		}
		if !info.IsDir() && filepath.Base(path)[:1] != "." {
			rel, _ := filepath.Rel(dir, path)
			files = append(files, rel)
		}
		return nil
	})
	sort.Strings(files)
	return files
}

func copyFile(src, dst string) error {
	data, err := os.ReadFile(src)
	if err != nil {
		return err
	}
	return os.WriteFile(dst, data, 0644)
}

func writeManifest(dir string, manifest map[string]string) {
	var lines []string
	for k, v := range manifest {
		lines = append(lines, fmt.Sprintf("%s %s", k, v))
	}
	sort.Strings(lines)
	content := ""
	for _, l := range lines {
		content += l + "\n"
	}
	os.WriteFile(filepath.Join(dir, ".manifest.txt"), []byte(content), 0644)
}

func main() {
	tmpdir, err := os.MkdirTemp("", "full_incremental_backup_*")
	if !(err == nil) {
		fmt.Fprintf(os.Stderr, "failed to create temp dir: %v\n", err)
		os.Exit(1)
	}
	defer os.RemoveAll(tmpdir)

	src := filepath.Join(tmpdir, "src")
	backupBase := filepath.Join(tmpdir, "backup")
	restoreBase := filepath.Join(tmpdir, "restore")
	os.MkdirAll(src, 0755)

	os.WriteFile(filepath.Join(src, "file1.txt"), []byte("content1"), 0644)
	os.WriteFile(filepath.Join(src, "file2.txt"), []byte("content2"), 0644)

	manifest0 := backupFull(src, backupBase)
	if !(len(manifest0) == 2) {
		fmt.Fprintf(os.Stderr, "expected 2 files in full backup, got %d\n", len(manifest0))
		os.Exit(1)
	}

	os.WriteFile(filepath.Join(src, "file1.txt"), []byte("content1_modified"), 0644)
	os.WriteFile(filepath.Join(src, "file3.txt"), []byte("content3"), 0644)

	current, manifest1 := backupIncremental(src, backupBase, 1, manifest0)
	_, ok1 := manifest1["file1.txt"]
	_, ok3 := manifest1["file3.txt"]
	if !ok1 {
		fmt.Fprintln(os.Stderr, "modified file1.txt not in incremental")
		os.Exit(1)
	}
	if !ok3 {
		fmt.Fprintln(os.Stderr, "new file3.txt not in incremental")
		os.Exit(1)
	}

	os.RemoveAll(src)
	restoreFromBackup(backupBase, restoreBase)

	restoredFile1, _ := os.ReadFile(filepath.Join(restoreBase, "file1.txt"))
	restoredFile2, _ := os.ReadFile(filepath.Join(restoreBase, "file2.txt"))
	restoredFile3, _ := os.ReadFile(filepath.Join(restoreBase, "file3.txt"))

	if !(string(restoredFile2) == "content2") {
		fmt.Fprintf(os.Stderr, "file2 mismatch: %s\n", restoredFile2)
		os.Exit(1)
	}
	if !(string(restoredFile3) == "content3") {
		fmt.Fprintln(os.Stderr, "file3 should be latest from incremental")
		os.Exit(1)
	}
	if !(string(restoredFile1) == "content1_modified") {
		fmt.Fprintln(os.Stderr, "file1 should be latest from incremental")
		os.Exit(1)
	}

	restoredHash1 := computeChecksum(filepath.Join(restoreBase, "file1.txt"))
	expectedHash1 := current["file1.txt"]
	if !(len(restoredHash1) == 64) {
		fmt.Fprintf(os.Stderr, "SHA256 hash must be 64 chars, got %d\n", len(restoredHash1))
		os.Exit(1)
	}
	if !(restoredHash1 == expectedHash1) {
		fmt.Fprintf(os.Stderr, "file1 hash mismatch: %s vs %s\n", restoredHash1, expectedHash1)
		os.Exit(1)
	}

	fmt.Println("✓ full_incremental_backup passed")
}
