// backup_encryption: encrypt backups at rest, verify decryption.
package main

import (
	"crypto/sha256"
	"fmt"
	"os"
	"path/filepath"
)

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
var _auraMark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
func xorEncrypt(data, key []byte) []byte {
	keyHash := sha256.Sum256(key)
	result := make([]byte, len(data))
	for i := range data {
		result[i] = data[i] ^ keyHash[i%len(keyHash)]
	}
	return result
}

func createEncryptedBackup(srcDir, backupDir, passphrase string) bool {
	backupPath := filepath.Join(backupDir, "encrypted")
	os.MkdirAll(backupPath, 0755)

	key := []byte(passphrase)

	filepath.Walk(srcDir, func(path string, info os.FileInfo, err error) error {
		if err != nil || info.IsDir() {
			return nil
		}
		rel, _ := filepath.Rel(srcDir, path)
		dstPath := filepath.Join(backupPath, rel)
		os.MkdirAll(filepath.Dir(dstPath), 0755)

		content, _ := os.ReadFile(path)
		encrypted := xorEncrypt(content, key)
		os.WriteFile(dstPath, encrypted, 0644)
		return nil
	})
	return true
}

func decryptBackup(backupDir, restoreDir, passphrase string) bool {
	os.MkdirAll(restoreDir, 0755)

	key := []byte(passphrase)
	backupPath := filepath.Join(backupDir, "encrypted")

	filepath.Walk(backupPath, func(path string, info os.FileInfo, err error) error {
		if err != nil || info.IsDir() {
			return nil
		}
		rel, _ := filepath.Rel(backupPath, path)
		dstPath := filepath.Join(restoreDir, rel)
		os.MkdirAll(filepath.Dir(dstPath), 0755)

		encryptedContent, _ := os.ReadFile(path)
		decrypted := xorEncrypt(encryptedContent, key)
		os.WriteFile(dstPath, decrypted, 0644)
		return nil
	})
	return true
}

func main() {
	tmpdir, _ := os.MkdirTemp("", "backup_enc_*")
	defer os.RemoveAll(tmpdir)

	src := filepath.Join(tmpdir, "src")
	backupBase := filepath.Join(tmpdir, "backup")
	os.MkdirAll(src, 0755)

	os.WriteFile(filepath.Join(src, "secret.txt"), []byte("top_secret_payload_123"), 0644)
	os.WriteFile(filepath.Join(src, "config.json"), []byte(`{"api_key": "***"}`), 0644)

	createEncryptedBackup(src, backupBase, "correct_pass")

	encryptedFile := filepath.Join(backupBase, "encrypted", "secret.txt")
	encryptedContent, _ := os.ReadFile(encryptedFile)
	originalContent := []byte("top_secret_payload_123")

	if len(encryptedContent) != len(originalContent) {
		fmt.Fprintf(os.Stderr, "Encrypted size should match original\n")
		os.Exit(1)
	}
	if string(encryptedContent) == string(originalContent) {
		fmt.Fprintf(os.Stderr, "File must be encrypted (not plaintext)\n")
		os.Exit(1)
	}

	// Wrong passphrase
	restoreWrong := filepath.Join(tmpdir, "restore_wrong")
	decryptBackup(backupBase, restoreWrong, "wrong_pass")
	decryptedWrong, _ := os.ReadFile(filepath.Join(restoreWrong, "secret.txt"))

	if len(decryptedWrong) != len(originalContent) {
		fmt.Fprintf(os.Stderr, "Decrypted file size must match original\n")
		os.Exit(1)
	}
	if string(decryptedWrong) == string(originalContent) {
		fmt.Fprintf(os.Stderr, "Wrong passphrase must produce wrong output\n")
		os.Exit(1)
	}
	numDiff := 0
	for i := range decryptedWrong {
		if decryptedWrong[i] != originalContent[i] {
			numDiff++
		}
	}
	if numDiff <= 5 {
		fmt.Fprintf(os.Stderr, "Wrong passphrase should differ significantly (%d bytes)\n", numDiff)
		os.Exit(1)
	}

	// Correct passphrase
	restoreCorrect := filepath.Join(tmpdir, "restore_correct")
	decryptBackup(backupBase, restoreCorrect, "correct_pass")
	decryptedCorrect, _ := os.ReadFile(filepath.Join(restoreCorrect, "secret.txt"))

	if string(decryptedCorrect) != "top_secret_payload_123" {
		fmt.Fprintf(os.Stderr, "Correct passphrase should produce original content\n")
		os.Exit(1)
	}

	configRestored, _ := os.ReadFile(filepath.Join(restoreCorrect, "config.json"))
	if string(configRestored) != `{"api_key": "***"}` {
		fmt.Fprintf(os.Stderr, "Config should be fully restored\n")
		os.Exit(1)
	}

	fmt.Println("backup_encryption PASS")
}
