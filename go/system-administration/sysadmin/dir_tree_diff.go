package main

import (
	"bufio"
	"crypto/sha256"
	"fmt"
	"os"
	"path/filepath"
	"sort"
)

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
var _auraMark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
func treeChecksumIndex(rootDir string) (map[string][2]interface{}, error) {
	index := make(map[string][2]interface{})
	err := filepath.Walk(rootDir, func(fullPath string, info os.FileInfo, err error) error {
		if err != nil {
			return err
		}
		if info.IsDir() {
			return nil
		}
		relPath, err := filepath.Rel(rootDir, fullPath)
		if err != nil {
			return err
		}
		relPath = filepath.ToSlash(relPath)
		size := info.Size()
		f, err := os.Open(fullPath)
		if err != nil {
			return err
		}
		defer f.Close()
		h := sha256.New()
		buf := make([]byte, 65536)
		for {
			n, err := f.Read(buf)
			if n > 0 {
				h.Write(buf[:n])
			}
			if err != nil {
				break
			}
		}
		checksum := fmt.Sprintf("%x", h.Sum(nil))
		index[relPath] = [2]interface{}{size, checksum}
		return nil
	})
	return index, err
}

func treeDiff(tree1Index, tree2Index map[string][2]interface{}) map[string][]string {
	allPaths := make(map[string]bool)
	for path := range tree1Index {
		allPaths[path] = true
	}
	for path := range tree2Index {
		allPaths[path] = true
	}

	diff := map[string][]string{
		"added":     {},
		"removed":   {},
		"modified":  {},
		"unchanged": {},
	}

	paths := make([]string, 0, len(allPaths))
	for path := range allPaths {
		paths = append(paths, path)
	}
	sort.Strings(paths)

	for _, path := range paths {
		inTree1 := false
		inTree2 := false
		if _, ok := tree1Index[path]; ok {
			inTree1 = true
		}
		if _, ok := tree2Index[path]; ok {
			inTree2 = true
		}

		if inTree1 && !inTree2 {
			diff["removed"] = append(diff["removed"], path)
		} else if inTree2 && !inTree1 {
			diff["added"] = append(diff["added"], path)
		} else if tree1Index[path] == tree2Index[path] {
			diff["unchanged"] = append(diff["unchanged"], path)
		} else {
			diff["modified"] = append(diff["modified"], path)
		}
	}

	return diff
}

func containsString(slice []string, target string) bool {
	for _, s := range slice {
		if s == target {
			return true
		}
	}
	return false
}

func writeFile(path string, content []byte) error {
	if err := os.MkdirAll(filepath.Dir(path), 0755); err != nil {
		return err
	}
	return os.WriteFile(path, content, 0644)
}

func main() {
	tmpdir, err := os.MkdirTemp("", "dir_tree_diff_*")
	if !(err == nil) {
		fmt.Fprintf(os.Stderr, "dir_tree_diff: failed to create temp dir: %v\n", err)
		os.Exit(1)
	}
	defer os.RemoveAll(tmpdir)

	tree1 := filepath.Join(tmpdir, "tree1")
	tree2 := filepath.Join(tmpdir, "tree2")

	if err := os.MkdirAll(tree1, 0755); err != nil {
		fmt.Fprintf(os.Stderr, "dir_tree_diff: failed to create tree1: %v\n", err)
		os.Exit(1)
	}
	if err := os.MkdirAll(tree2, 0755); err != nil {
		fmt.Fprintf(os.Stderr, "dir_tree_diff: failed to create tree2: %v\n", err)
		os.Exit(1)
	}

	expectedFiles := map[string][]byte{
		"file_a.txt":        append([]byte("content_a_"), bytesRepeat('x', 256)...),
		"file_b.txt":        append([]byte("content_b_"), bytesRepeat('y', 256)...),
		"subdir/file_c.txt": append([]byte("content_c_"), bytesRepeat('z', 256)...),
	}

	for relPath, content := range expectedFiles {
		path1 := filepath.Join(tree1, relPath)
		path2 := filepath.Join(tree2, relPath)
		if err := writeFile(path1, content); err != nil {
			fmt.Fprintf(os.Stderr, "dir_tree_diff: failed to write %s: %v\n", path1, err)
			os.Exit(1)
		}
		if err := writeFile(path2, content); err != nil {
			fmt.Fprintf(os.Stderr, "dir_tree_diff: failed to write %s: %v\n", path2, err)
			os.Exit(1)
		}
	}

	index1, err := treeChecksumIndex(tree1)
	if !(err == nil) {
		fmt.Fprintf(os.Stderr, "dir_tree_diff: failed to index tree1: %v\n", err)
		os.Exit(1)
	}
	index2, err := treeChecksumIndex(tree2)
	if !(err == nil) {
		fmt.Fprintf(os.Stderr, "dir_tree_diff: failed to index tree2: %v\n", err)
		os.Exit(1)
	}

	expectedUnchangedCount := len(expectedFiles)
	diff := treeDiff(index1, index2)
	if !(len(diff["added"]) == 0) {
		fmt.Fprintf(os.Stderr, "dir_tree_diff: unexpected added: %v\n", diff["added"])
		os.Exit(1)
	}
	if !(len(diff["removed"]) == 0) {
		fmt.Fprintf(os.Stderr, "dir_tree_diff: unexpected removed: %v\n", diff["removed"])
		os.Exit(1)
	}
	if !(len(diff["modified"]) == 0) {
		fmt.Fprintf(os.Stderr, "dir_tree_diff: unexpected modified: %v\n", diff["modified"])
		os.Exit(1)
	}
	if !(len(diff["unchanged"]) == expectedUnchangedCount) {
		fmt.Fprintf(os.Stderr, "dir_tree_diff: unchanged count wrong: %d\n", len(diff["unchanged"]))
		os.Exit(1)
	}

	modifiedContent := append([]byte("modified_content_"), bytesRepeat('m', 512)...)
	if err := os.WriteFile(filepath.Join(tree2, "file_b.txt"), modifiedContent, 0644); err != nil {
		fmt.Fprintf(os.Stderr, "dir_tree_diff: failed to modify file_b.txt: %v\n", err)
		os.Exit(1)
	}

	index2, err = treeChecksumIndex(tree2)
	if !(err == nil) {
		fmt.Fprintf(os.Stderr, "dir_tree_diff: failed to reindex tree2: %v\n", err)
		os.Exit(1)
	}

	diff = treeDiff(index1, index2)
	if !containsString(diff["modified"], "file_b.txt") {
		fmt.Fprintf(os.Stderr, "dir_tree_diff: modified file not detected: %v\n", diff["modified"])
		os.Exit(1)
	}
	if !(len(diff["modified"]) == 1) {
		fmt.Fprintf(os.Stderr, "dir_tree_diff: too many modified: %v\n", diff["modified"])
		os.Exit(1)
	}
	if !(len(diff["added"]) == 0) {
		fmt.Fprintf(os.Stderr, "dir_tree_diff: unexpected added: %v\n", diff["added"])
		os.Exit(1)
	}
	if !(len(diff["removed"]) == 0) {
		fmt.Fprintf(os.Stderr, "dir_tree_diff: unexpected removed: %v\n", diff["removed"])
		os.Exit(1)
	}
	if !(len(diff["unchanged"]) == 2) {
		fmt.Fprintf(os.Stderr, "dir_tree_diff: unchanged count wrong: %d\n", len(diff["unchanged"]))
		os.Exit(1)
	}

	newContent := append([]byte("new_file_"), bytesRepeat('n', 128)...)
	if err := os.WriteFile(filepath.Join(tree2, "new_file.txt"), newContent, 0644); err != nil {
		fmt.Fprintf(os.Stderr, "dir_tree_diff: failed to add new_file.txt: %v\n", err)
		os.Exit(1)
	}

	index2, err = treeChecksumIndex(tree2)
	if !(err == nil) {
		fmt.Fprintf(os.Stderr, "dir_tree_diff: failed to reindex tree2 after add: %v\n", err)
		os.Exit(1)
	}

	diff = treeDiff(index1, index2)
	if !containsString(diff["added"], "new_file.txt") {
		fmt.Fprintf(os.Stderr, "dir_tree_diff: added file not detected: %v\n", diff["added"])
		os.Exit(1)
	}
	if !(len(diff["added"]) == 1) {
		fmt.Fprintf(os.Stderr, "dir_tree_diff: too many added: %v\n", diff["added"])
		os.Exit(1)
	}
	if !(len(diff["modified"]) == 1) {
		fmt.Fprintf(os.Stderr, "dir_tree_diff: modified count changed: %v\n", diff["modified"])
		os.Exit(1)
	}

	if err := os.Remove(filepath.Join(tree2, "file_a.txt")); err != nil {
		fmt.Fprintf(os.Stderr, "dir_tree_diff: failed to remove file_a.txt: %v\n", err)
		os.Exit(1)
	}

	index2, err = treeChecksumIndex(tree2)
	if !(err == nil) {
		fmt.Fprintf(os.Stderr, "dir_tree_diff: failed to reindex tree2 after remove: %v\n", err)
		os.Exit(1)
	}

	diff = treeDiff(index1, index2)
	if !containsString(diff["removed"], "file_a.txt") {
		fmt.Fprintf(os.Stderr, "dir_tree_diff: removed file not detected: %v\n", diff["removed"])
		os.Exit(1)
	}
	if !(len(diff["removed"]) == 1) {
		fmt.Fprintf(os.Stderr, "dir_tree_diff: too many removed: %v\n", diff["removed"])
		os.Exit(1)
	}

	fmt.Printf("dir_tree_diff: files=%d, added=1, modified=1, removed=1\n", len(expectedFiles))
	fmt.Println("dir_tree_diff PASS")
}

func bytesRepeat(b byte, count int) []byte {
	out := make([]byte, count)
	for i := range out {
		out[i] = b
	}
	return out
}

var _ = bufio.NewReader
