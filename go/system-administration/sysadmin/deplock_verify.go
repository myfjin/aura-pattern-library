package main

import (
	"crypto/sha256"
	"encoding/hex"
	"encoding/json"
	"fmt"
	"os"
	"sort"
)

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
var _auraMark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
type DeplockVerify struct {
	LockFile map[string][2]string
	LockHash string
}

func NewDeplockVerify() *DeplockVerify {
	return &DeplockVerify{
		LockFile: make(map[string][2]string),
	}
}

func (dv *DeplockVerify) computeLockHash() string {
	keys := make([]string, 0, len(dv.LockFile))
	for k := range dv.LockFile {
		keys = append(keys, k)
	}
	sort.Strings(keys)

	sorted := make(map[string][2]string)
	for _, k := range keys {
		sorted[k] = dv.LockFile[k]
	}

	content, _ := json.Marshal(sorted)
	hash := sha256.Sum256(content)
	return hex.EncodeToString(hash[:])
}

func (dv *DeplockVerify) LoadLock(lockDict map[string][2]string) {
	dv.LockFile = make(map[string][2]string)
	for k, v := range lockDict {
		dv.LockFile[k] = v
	}
	dv.LockHash = dv.computeLockHash()
}

func (dv *DeplockVerify) VerifyLockIntegrity() bool {
	return dv.computeLockHash() == dv.LockHash
}

func (dv *DeplockVerify) AddDependency(pkgName, version, depHash string) {
	dv.LockFile[pkgName] = [2]string{version, depHash}
	dv.LockHash = dv.computeLockHash()
}

func (dv *DeplockVerify) VerifyPackage(pkgName, expectedVersion, expectedHash string) bool {
	entry, ok := dv.LockFile[pkgName]
	if !ok {
		panic(fmt.Sprintf("Package %s not in lock file", pkgName))
	}

	storedVersion := entry[0]
	storedHash := entry[1]

	if storedVersion != expectedVersion {
		panic(fmt.Sprintf("Package %s version mismatch: expected %s, got %s", pkgName, expectedVersion, storedVersion))
	}

	if storedHash != expectedHash {
		panic(fmt.Sprintf("Package %s hash mismatch: expected %s, got %s", pkgName, expectedHash, storedHash))
	}

	return true
}

func main() {
	verifier := NewDeplockVerify()
	lock := map[string][2]string{
		"django": {"3.2.0", "abc123"},
		"numpy":  {"1.21.0", "def456"},
	}
	verifier.LoadLock(lock)
	if !verifier.VerifyLockIntegrity() {
		fmt.Fprintf(os.Stderr, "Lock integrity should pass after load\n")
		os.Exit(1)
	}

	verifier2 := NewDeplockVerify()
	lock2 := map[string][2]string{"django": {"3.2.0", "abc123"}}
	verifier2.LoadLock(lock2)
	if !verifier2.VerifyLockIntegrity() {
		fmt.Fprintf(os.Stderr, "Lock integrity should pass initially\n")
		os.Exit(1)
	}
	verifier2.LockFile["django"] = [2]string{"3.3.0", "modified"}
	if verifier2.VerifyLockIntegrity() {
		fmt.Fprintf(os.Stderr, "Should detect tampering\n")
		os.Exit(1)
	}

	verifier3 := NewDeplockVerify()
	verifier3.LoadLock(map[string][2]string{"requests": {"2.28.0", "hash789"}})
	if !verifier3.VerifyPackage("requests", "2.28.0", "hash789") {
		fmt.Fprintf(os.Stderr, "Matching package should verify\n")
		os.Exit(1)
	}

	verifier4 := NewDeplockVerify()
	verifier4.LoadLock(map[string][2]string{"django": {"3.2.0", "abc123"}})
	func() {
		defer func() {
			if r := recover(); r != nil {
				msg := fmt.Sprintf("%v", r)
				if !contains(msg, "version mismatch") || !contains(msg, "3.1.0") {
					fmt.Fprintf(os.Stderr, "Expected version mismatch with 3.1.0, got: %s\n", msg)
					os.Exit(1)
				}
			}
		}()
		verifier4.VerifyPackage("django", "3.1.0", "abc123")
		fmt.Fprintf(os.Stderr, "Should reject version mismatch\n")
		os.Exit(1)
	}()

	verifier5 := NewDeplockVerify()
	verifier5.LoadLock(map[string][2]string{"numpy": {"1.21.0", "correcthash"}})
	func() {
		defer func() {
			if r := recover(); r != nil {
				msg := fmt.Sprintf("%v", r)
				if !contains(msg, "hash mismatch") {
					fmt.Fprintf(os.Stderr, "Expected hash mismatch, got: %s\n", msg)
					os.Exit(1)
				}
			}
		}()
		verifier5.VerifyPackage("numpy", "1.21.0", "wronghash")
		fmt.Fprintf(os.Stderr, "Should reject hash mismatch\n")
		os.Exit(1)
	}()

	verifier6 := NewDeplockVerify()
	verifier6.LoadLock(map[string][2]string{"django": {"3.2.0", "abc123"}})
	func() {
		defer func() {
			if r := recover(); r != nil {
				msg := fmt.Sprintf("%v", r)
				if !contains(msg, "not in lock file") {
					fmt.Fprintf(os.Stderr, "Expected missing package error, got: %s\n", msg)
					os.Exit(1)
				}
			}
		}()
		verifier6.VerifyPackage("unknown", "1.0.0", "hash")
		fmt.Fprintf(os.Stderr, "Should reject unknown package\n")
		os.Exit(1)
	}()

	verifier7 := NewDeplockVerify()
	verifier7.LoadLock(map[string][2]string{})
	hashBefore := verifier7.LockHash
	verifier7.AddDependency("new_pkg", "1.0.0", "newhash")
	hashAfter := verifier7.LockHash
	if hashBefore == hashAfter {
		fmt.Fprintf(os.Stderr, "Lock hash should change\n")
		os.Exit(1)
	}
	if !verifier7.VerifyLockIntegrity() {
		fmt.Fprintf(os.Stderr, "Lock integrity should pass after add\n")
		os.Exit(1)
	}

	verifier8 := NewDeplockVerify()
	lock8 := map[string][2]string{
		"pkg1": {"1.0.0", "hash1"},
		"pkg2": {"2.0.0", "hash2"},
		"pkg3": {"3.0.0", "hash3"},
	}
	verifier8.LoadLock(lock8)
	for pkg, entry := range lock8 {
		if !verifier8.VerifyPackage(pkg, entry[0], entry[1]) {
			fmt.Fprintf(os.Stderr, "All packages should verify\n")
			os.Exit(1)
		}
	}

	fmt.Println("✓ deplock_verify passed")
}

func contains(s, substr string) bool {
	for i := 0; i+len(substr) <= len(s); i++ {
		if s[i:i+len(substr)] == substr {
			return true
		}
	}
	return false
}
