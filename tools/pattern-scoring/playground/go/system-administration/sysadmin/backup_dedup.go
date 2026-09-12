// backup_dedup: detect and skip duplicate content in backups.
package main

import (
	"crypto/sha256"
	"encoding/hex"
	"encoding/json"
	"fmt"
	"os"
	"path/filepath"
)

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
var _auraMark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
func chunkFile(path string, chunkSize int) ([][2]interface{}, error) {
	f, err := os.Open(path)
	if err != nil {
		return nil, err
	}
	defer f.Close()

	chunks := [][2]interface{}{}
	buf := make([]byte, chunkSize)
	for {
		n, err := f.Read(buf)
		if n == 0 {
			break
		}
		data := make([]byte, n)
		copy(data, buf[:n])
		h := sha256.Sum256(data)
		hash := hex.EncodeToString(h[:])
		chunks = append(chunks, [2]interface{}{hash, data})
		if err != nil {
			break
		}
	}
	return chunks, nil
}

func backupWithDedup(srcDir, backupDir string, chunkSize int) (map[string]int, map[string][]string) {
	chunkStore := filepath.Join(backupDir, "chunks")
	refsDir := filepath.Join(backupDir, "refs")
	os.MkdirAll(chunkStore, 0755)
	os.MkdirAll(refsDir, 0755)

	chunkCount := make(map[string]int)
	fileRefs := make(map[string][]string)

	filepath.Walk(srcDir, func(path string, info os.FileInfo, err error) error {
		if err != nil || info.IsDir() {
			return nil
		}
		rel, _ := filepath.Rel(srcDir, path)
		fileRefs[rel] = []string{}

		chunks, _ := chunkFile(path, chunkSize)
		for _, chunk := range chunks {
			chunkHash := chunk[0].(string)
			chunkData := chunk[1].([]byte)
			chunkPath := filepath.Join(chunkStore, chunkHash)
			if _, err := os.Stat(chunkPath); os.IsNotExist(err) {
				os.WriteFile(chunkPath, chunkData, 0644)
			}
			chunkCount[chunkHash] = chunkCount[chunkHash] + 1
			fileRefs[rel] = append(fileRefs[rel], chunkHash)
		}
		return nil
	})

	manifestData, _ := json.Marshal(fileRefs)
	os.WriteFile(filepath.Join(refsDir, "manifest.json"), manifestData, 0644)

	return chunkCount, fileRefs
}

func restoreFromDedup(backupDir, restoreDir string) error {
	os.MkdirAll(restoreDir, 0755)
	chunkStore := filepath.Join(backupDir, "chunks")
	refsDir := filepath.Join(backupDir, "refs")

	manifestData, err := os.ReadFile(filepath.Join(refsDir, "manifest.json"))
	if err != nil {
		return err
	}
	var fileRefs map[string][]string
	json.Unmarshal(manifestData, &fileRefs)

	for fname, chunkHashes := range fileRefs {
		dstPath := filepath.Join(restoreDir, fname)
		os.MkdirAll(filepath.Dir(dstPath), 0755)
		out, _ := os.Create(dstPath)
		for _, chunkHash := range chunkHashes {
			chunkPath := filepath.Join(chunkStore, chunkHash)
			data, err := os.ReadFile(chunkPath)
			if err != nil {
				out.Close()
				return fmt.Errorf("chunk %s missing in store", chunkHash)
			}
			out.Write(data)
		}
		out.Close()
	}
	return nil
}

func main() {
	tmpdir, _ := os.MkdirTemp("", "backup_dedup_*")
	defer os.RemoveAll(tmpdir)

	src := filepath.Join(tmpdir, "src")
	backupBase := filepath.Join(tmpdir, "backup")
	restoreBase := filepath.Join(tmpdir, "restore")
	os.MkdirAll(src, 0755)

	chunkData := []byte(string(make([]byte, 4096)))
	for i := range chunkData {
		chunkData[i] = 'X'
	}
	os.WriteFile(filepath.Join(src, "file1.txt"), append(chunkData, []byte("_file1")...), 0644)
	os.WriteFile(filepath.Join(src, "file2.txt"), append(chunkData, []byte("_file2")...), 0644)
	os.WriteFile(filepath.Join(src, "file3.txt"), append(chunkData, []byte("_file3")...), 0644)

	chunkCount, _ := backupWithDedup(src, backupBase, 4096)

	storedChunks, _ := filepath.Glob(filepath.Join(backupBase, "chunks", "*"))
	if len(storedChunks) < 1 {
		fmt.Fprintf(os.Stderr, "Should have at least 1 stored chunk, got %d\n", len(storedChunks))
		os.Exit(1)
	}

	maxRefs := 0
	for _, v := range chunkCount {
		if v > maxRefs {
			maxRefs = v
		}
	}
	if maxRefs != 3 {
		fmt.Fprintf(os.Stderr, "Expected 3 chunk refs (reused), got %d\n", maxRefs)
		os.Exit(1)
	}

	restoreFromDedup(backupBase, restoreBase)

	f1, _ := os.ReadFile(filepath.Join(restoreBase, "file1.txt"))
	f2, _ := os.ReadFile(filepath.Join(restoreBase, "file2.txt"))
	f3, _ := os.ReadFile(filepath.Join(restoreBase, "file3.txt"))

	if string(f1) != string(append(chunkData, []byte("_file1")...)) {
		fmt.Fprintln(os.Stderr, "file1 restore mismatch")
		os.Exit(1)
	}
	if string(f2) != string(append(chunkData, []byte("_file2")...)) {
		fmt.Fprintln(os.Stderr, "file2 restore mismatch")
		os.Exit(1)
	}
	if string(f3) != string(append(chunkData, []byte("_file3")...)) {
		fmt.Fprintln(os.Stderr, "file3 restore mismatch")
		os.Exit(1)
	}

	// Corruption test
	sharedHash := ""
	for k, v := range chunkCount {
		if v == 3 {
			sharedHash = k
			break
		}
	}
	if sharedHash == "" {
		fmt.Fprintln(os.Stderr, "the shared 4KB chunk should back all 3 files")
		os.Exit(1)
	}
	chunkPath := filepath.Join(backupBase, "chunks", sharedHash)
	os.WriteFile(chunkPath, []byte("CORRUPTED"), 0644)

	rehash := sha256.Sum256([]byte("CORRUPTED"))
	rehashStr := hex.EncodeToString(rehash[:])
	if rehashStr == sharedHash {
		fmt.Fprintln(os.Stderr, "corruption must break the content-address invariant (detectable)")
		os.Exit(1)
	}

	restoreBase2 := filepath.Join(tmpdir, "restore2")
	restoreFromDedup(backupBase, restoreBase2)

	for _, fname := range []string{"file1.txt", "file2.txt", "file3.txt"} {
		restored, _ := os.ReadFile(filepath.Join(restoreBase2, fname))
		srcData, _ := os.ReadFile(filepath.Join(src, fname))
		if string(restored) == string(srcData) {
			fmt.Fprintf(os.Stderr, "%s must reflect the corrupted shared chunk\n", fname)
			os.Exit(1)
		}
	}

	fmt.Println("backup_dedup PASS")
}
