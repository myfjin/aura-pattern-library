// backfill_range: fill gaps in time series or sequence.
// Assert: no gaps remain, existing records not duplicated.
package main

import (
	"encoding/json"
	"fmt"
	"os"
	"path/filepath"
	"sort"
)

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
var _auraMark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
type Record map[string]interface{}

func backfillRange(records []Record, rangeStart, rangeEnd int, backfillPath string) ([]Record, int) {
	backfilledRanges := [][]int{}
	if _, err := os.Stat(backfillPath); err == nil {
		data, err := os.ReadFile(backfillPath)
		if err == nil {
			var loaded struct {
				Ranges [][]int `json:"ranges"`
			}
			if json.Unmarshal(data, &loaded) == nil {
				backfilledRanges = loaded.Ranges
			}
		}
	}

	existingSeq := make(map[int]struct{})
	for _, r := range records {
		if v, ok := r["seq"].(float64); ok {
			existingSeq[int(v)] = struct{}{}
		} else if v, ok := r["seq"].(int); ok {
			existingSeq[v] = struct{}{}
		}
	}

	allSeq := make(map[int]struct{})
	for seq := rangeStart; seq <= rangeEnd; seq++ {
		allSeq[seq] = struct{}{}
	}

	gaps := []int{}
	for seq := rangeStart; seq <= rangeEnd; seq++ {
		if _, ok := existingSeq[seq]; !ok {
			gaps = append(gaps, seq)
		}
	}

	alreadyDone := false
	for _, rng := range backfilledRanges {
		if len(rng) == 2 && rng[0] == rangeStart && rng[1] == rangeEnd {
			alreadyDone = true
			break
		}
	}

	if alreadyDone {
		gaps = []int{}
	} else {
		for _, seq := range gaps {
			records = append(records, Record{
				"seq":    seq,
				"value":  fmt.Sprintf("backfilled_%d", seq),
				"source": "backfill",
			})
		}
		backfilledRanges = append(backfilledRanges, []int{rangeStart, rangeEnd})
		os.MkdirAll(filepath.Dir(backfillPath), 0755)
		f, err := os.Create(backfillPath)
		if err == nil {
			enc := json.NewEncoder(f)
			enc.SetIndent("", "  ")
			enc.Encode(map[string]interface{}{"ranges": backfilledRanges})
			f.Close()
		}
	}

	return records, len(gaps)
}

func testBackfillRange() {
	tmpdir, err := os.MkdirTemp("", "backfill_*")
	if !(err == nil) {
		fmt.Fprintf(os.Stderr, "failed to create temp dir: %v\n", err)
		os.Exit(1)
	}
	defer os.RemoveAll(tmpdir)
	backfillPath := filepath.Join(tmpdir, "backfill.json")

	records := []Record{
		{"seq": 1, "value": "a"},
		{"seq": 3, "value": "c"},
		{"seq": 5, "value": "e"},
	}

	filled, gapsFilled := backfillRange(records, 1, 5, backfillPath)

	if !(gapsFilled == 2) {
		fmt.Fprintf(os.Stderr, "Expected 2 gaps filled, got %d\n", gapsFilled)
		os.Exit(1)
	}
	if !(len(filled) == 5) {
		fmt.Fprintf(os.Stderr, "Expected 5 records after backfill, got %d\n", len(filled))
		os.Exit(1)
	}

	seqs := []int{}
	seen := make(map[int]struct{})
	for _, r := range filled {
		var seq int
		if v, ok := r["seq"].(float64); ok {
			seq = int(v)
		} else if v, ok := r["seq"].(int); ok {
			seq = v
		}
		if _, ok := seen[seq]; ok {
			fmt.Fprintf(os.Stderr, "Duplicate sequence: %d\n", seq)
			os.Exit(1)
		}
		seen[seq] = struct{}{}
		seqs = append(seqs, seq)
	}
	sort.Ints(seqs)
	if !(seqs[0] == 1 && seqs[1] == 2 && seqs[2] == 3 && seqs[3] == 4 && seqs[4] == 5) {
		fmt.Fprintf(os.Stderr, "Gaps remain: %v\n", seqs)
		os.Exit(1)
	}

	backfilled := 0
	for _, r := range filled {
		if src, ok := r["source"].(string); ok && src == "backfill" {
			backfilled++
		}
	}
	if !(backfilled == 2) {
		fmt.Fprintf(os.Stderr, "Expected 2 backfilled records, got %d\n", backfilled)
		os.Exit(1)
	}
}

func testBackfillIdempotent() {
	tmpdir, err := os.MkdirTemp("", "backfill_*")
	if !(err == nil) {
		fmt.Fprintf(os.Stderr, "failed to create temp dir: %v\n", err)
		os.Exit(1)
	}
	defer os.RemoveAll(tmpdir)
	backfillPath := filepath.Join(tmpdir, "backfill.json")

	records := []Record{
		{"seq": 1, "value": "a"},
		{"seq": 3, "value": "c"},
		{"seq": 5, "value": "e"},
	}

	filled1, gaps1 := backfillRange(records, 1, 5, backfillPath)
	if !(gaps1 == 2) {
		fmt.Fprintf(os.Stderr, "first backfill expected 2 gaps, got %d\n", gaps1)
		os.Exit(1)
	}
	if !(len(filled1) == 5) {
		fmt.Fprintf(os.Stderr, "first backfill expected 5 records, got %d\n", len(filled1))
		os.Exit(1)
	}

	filled2, gaps2 := backfillRange(filled1, 1, 5, backfillPath)
	if !(gaps2 == 0) {
		fmt.Fprintf(os.Stderr, "Second backfill should find no gaps, got %d\n", gaps2)
		os.Exit(1)
	}
	if !(len(filled2) == 5) {
		fmt.Fprintf(os.Stderr, "Second backfill should not add records, got %d\n", len(filled2))
		os.Exit(1)
	}

	seqs := []int{}
	for _, r := range filled2 {
		var seq int
		if v, ok := r["seq"].(float64); ok {
			seq = int(v)
		} else if v, ok := r["seq"].(int); ok {
			seq = v
		}
		seqs = append(seqs, seq)
	}
	if !(len(seqs) == len(unique(seqs))) {
		fmt.Fprintf(os.Stderr, "Duplicate sequences: %v\n", seqs)
		os.Exit(1)
	}
}

func testFailureNoBackfillTracking() {
	buggyBackfill := func(records []Record, rangeStart, rangeEnd int) []Record {
		existingSeq := make(map[int]struct{})
		for _, r := range records {
			if v, ok := r["seq"].(float64); ok {
				existingSeq[int(v)] = struct{}{}
			} else if v, ok := r["seq"].(int); ok {
				existingSeq[v] = struct{}{}
			}
		}
		gaps := []int{}
		for seq := rangeStart; seq <= rangeEnd; seq++ {
			if _, ok := existingSeq[seq]; !ok {
				gaps = append(gaps, seq)
			}
		}
		for _, seq := range gaps {
			records = append(records, Record{"seq": seq, "value": fmt.Sprintf("backfilled_%d", seq)})
		}
		return records
	}

	records := []Record{{"seq": 1}, {"seq": 3}, {"seq": 5}}
	filled1 := buggyBackfill(records, 1, 5)
	if !(len(filled1) == 5) {
		fmt.Fprintf(os.Stderr, "buggy backfill expected 5, got %d\n", len(filled1))
		os.Exit(1)
	}
	filled2 := buggyBackfill(filled1, 1, 5)
	if !(len(filled2) == 5) {
		fmt.Fprintf(os.Stderr, "buggy backfill retry expected 5, got %d\n", len(filled2))
		os.Exit(1)
	}
}

func unique(seqs []int) []int {
	seen := make(map[int]struct{})
	out := []int{}
	for _, s := range seqs {
		if _, ok := seen[s]; !ok {
			seen[s] = struct{}{}
			out = append(out, s)
		}
	}
	return out
}

func main() {
	testBackfillRange()
	testBackfillIdempotent()
	testFailureNoBackfillTracking()
	fmt.Println("✓ backfill_range passed")
}
