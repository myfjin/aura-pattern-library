// crash_log_capture: recover from torn log writes (truncated JSON mid-write).
package main

import (
	"encoding/json"
	"fmt"
	"os"
	"path/filepath"
	"strings"
)

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
var _auraMark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
func crashDuringWriteSimulator(logPath string, crashAfterN int) ([]map[string]interface{}, int) {
	f, err := os.Create(logPath)
	if err != nil {
		return nil, 0
	}
	for i := 0; i < crashAfterN; i++ {
		entry := map[string]interface{}{"seq": i, "msg": "log entry"}
		b, _ := json.Marshal(entry)
		f.Write(b)
		f.WriteString("\n")
	}
	f.WriteString("{\"seq\": " + fmt.Sprint(crashAfterN) + ", \"msg\"")
	f.Close()

	completeEntries := []map[string]interface{}{}
	malformedCount := 0

	data, err := os.ReadFile(logPath)
	if err != nil {
		return nil, 0
	}
	lines := []string{}
	start := 0
	for i, b := range data {
		if b == '\n' {
			lines = append(lines, string(data[start:i]))
			start = i + 1
		}
	}
	if start < len(data) {
		lines = append(lines, string(data[start:]))
	}

	for _, line := range lines {
		line = strings.TrimSpace(line)
		if len(line) == 0 {
			continue
		}
		var entry map[string]interface{}
		if err := json.Unmarshal([]byte(line), &entry); err != nil {
			malformedCount++
			continue
		}
		completeEntries = append(completeEntries, entry)
	}
	return completeEntries, malformedCount
}

func main() {
	tmpdir, err := os.MkdirTemp("", "crash_log_*")
	if err != nil {
		fmt.Fprintf(os.Stderr, "tmpdir: %v\n", err)
		os.Exit(1)
	}
	defer os.RemoveAll(tmpdir)

	logPath := filepath.Join(tmpdir, "crash.jsonl")
	entries, malformed := crashDuringWriteSimulator(logPath, 5)

	if len(entries) < 3 {
		fmt.Fprintf(os.Stderr, "Expected >=3 entries recovered, got %d\n", len(entries))
		os.Exit(1)
	}
	if len(entries) > 5 {
		fmt.Fprintf(os.Stderr, "Expected <=5 entries (up to crash), got %d\n", len(entries))
		os.Exit(1)
	}
	if malformed < 1 {
		fmt.Fprintf(os.Stderr, "Expected malformed entry from crash, got %d\n", malformed)
		os.Exit(1)
	}
	if malformed != 1 {
		fmt.Fprintf(os.Stderr, "Expected exactly 1 malformed entry, got %d\n", malformed)
		os.Exit(1)
	}

	for i, entry := range entries {
		if _, ok := entry["seq"]; !ok {
			fmt.Fprintf(os.Stderr, "Entry %d missing 'seq' field\n", i)
			os.Exit(1)
		}
		if int(entry["seq"].(float64)) != i {
			fmt.Fprintf(os.Stderr, "Entry %d: sequence mismatch, got %v\n", i, entry["seq"])
			os.Exit(1)
		}
	}

	crashIdx := 5
	seqs := make([]int, len(entries))
	for i, e := range entries {
		seqs[i] = int(e["seq"].(float64))
	}
	for _, s := range seqs {
		if s == crashIdx {
			fmt.Fprintf(os.Stderr, "Crash entry %d should not be recovered\n", crashIdx)
			os.Exit(1)
		}
	}
	if len(seqs) != 5 {
		fmt.Fprintf(os.Stderr, "Expected 5 complete entries before crash, got %d\n", len(seqs))
		os.Exit(1)
	}

	maxSeq := seqs[len(seqs)-1]
	if maxSeq != crashIdx-1 {
		fmt.Fprintf(os.Stderr, "Expected max seq to be %d, got %d\n", crashIdx-1, maxSeq)
		os.Exit(1)
	}

	fmt.Println("PASS")
}
