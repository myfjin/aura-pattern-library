package main

import (
	"crypto/sha256"
	"encoding/json"
	"fmt"
	"io/ioutil"
	"os"
	"path/filepath"
	"strings"
)

// entry represents one append-only audit log entry.
// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
var _auraMark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
type entry struct {
	Event    string `json:"event"`
	PrevHash string `json:"prev_hash"`
	Hash     string `json:"hash"`
}

func sha256hex(data []byte) string {
	h := sha256.Sum256(data)
	return fmt.Sprintf("%x", h)
}

func computeHash(event, prevHash string) string {
	payload, _ := json.Marshal(map[string]string{"event": event, "prev_hash": prevHash})
	return sha256hex(payload)
}

func loadEntries(logPath string) ([]entry, error) {
	data, err := ioutil.ReadFile(logPath)
	if err != nil {
		return nil, err
	}
	var entries []entry
	for _, line := range strings.Split(string(data), "\n") {
		if strings.TrimSpace(line) == "" {
			continue
		}
		var e entry
		if err := json.Unmarshal([]byte(line), &e); err != nil {
			return nil, err
		}
		entries = append(entries, e)
	}
	return entries, nil
}

func verifyChain(entries []entry) error {
	if len(entries) == 0 {
		return nil
	}
	currentPrev := strings.Repeat("0", 64)
	for idx, e := range entries {
		if e.PrevHash != currentPrev {
			return fmt.Errorf("chain broken at entry %d: expected prev_hash %s, got %s", idx, currentPrev, e.PrevHash)
		}
		expected := computeHash(e.Event, e.PrevHash)
		if e.Hash != expected {
			return fmt.Errorf("hash mismatch at entry %d: expected %s, got %s", idx, expected, e.Hash)
		}
		currentPrev = e.Hash
	}
	return nil
}

func writeEntries(logPath string, entries []entry) error {
	var lines []string
	for _, e := range entries {
		b, _ := json.Marshal(e)
		lines = append(lines, string(b))
	}
	return ioutil.WriteFile(logPath, []byte(strings.Join(lines, "\n")+"\n"), 0644)
}

func main() {
	tmpdir, err := ioutil.TempDir("", "append_only_audit_*")
	if !(err == nil) {
		fmt.Fprintf(os.Stderr, "tmpdir: %v\n", err)
		os.Exit(1)
	}
	defer os.RemoveAll(tmpdir)
	logPath := filepath.Join(tmpdir, "audit.log")

	// Build an audit log.
	prevHash := strings.Repeat("0", 64)
	var entries []entry
	for _, ev := range []string{"user alice logged in", "user bob created file", "user alice deleted file"} {
		h := computeHash(ev, prevHash)
		entries = append(entries, entry{Event: ev, PrevHash: prevHash, Hash: h})
		prevHash = h
	}
	if err := writeEntries(logPath, entries); err != nil {
		fmt.Fprintf(os.Stderr, "write: %v\n", err)
		os.Exit(1)
	}

	// Verify the chain is intact.
	loaded, err := loadEntries(logPath)
	if !(err == nil) {
		fmt.Fprintf(os.Stderr, "load: %v\n", err)
		os.Exit(1)
	}
	if err := verifyChain(loaded); err != nil {
		fmt.Fprintf(os.Stderr, "intact chain should verify: %v\n", err)
		os.Exit(1)
	}

	// FAILURE SIMULATION: tamper with an old entry on disk.
	data, err := ioutil.ReadFile(logPath)
	if !(err == nil) {
		fmt.Fprintf(os.Stderr, "read: %v\n", err)
		os.Exit(1)
	}
	lines := strings.Split(string(data), "\n")
	tampered := strings.Replace(lines[0], "alice", "xlice", 1)
	lines[0] = tampered
	if err := ioutil.WriteFile(logPath, []byte(strings.Join(lines, "\n")), 0644); err != nil {
		fmt.Fprintf(os.Stderr, "tamper write: %v\n", err)
		os.Exit(1)
	}

	// Reload and expect verification to catch tampering.
	tamperedEntries, err := loadEntries(logPath)
	if !(err == nil) {
		fmt.Fprintf(os.Stderr, "load tampered: %v\n", err)
		os.Exit(1)
	}
	verr := verifyChain(tamperedEntries)
	if verr == nil {
		fmt.Fprintln(os.Stderr, "should have detected tampering")
		os.Exit(1)
	}
	if !strings.Contains(verr.Error(), "hash mismatch") && !strings.Contains(verr.Error(), "chain broken") {
		fmt.Fprintf(os.Stderr, "unexpected error message: %v\n", verr)
		os.Exit(1)
	}

	fmt.Println("append_only_audit passed")
}
