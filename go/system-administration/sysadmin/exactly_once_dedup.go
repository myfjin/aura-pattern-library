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
type Record struct {
	ID    string `json:"id"`
	Value int    `json:"value"`
}

type ProcessedRecord struct {
	ID    string `json:"id"`
	Value int    `json:"value"`
	Seq   int    `json:"seq"`
}

func deduplicateStream(records []Record, journalPath string) ([]ProcessedRecord, []string, error) {
	journal := make(map[string]bool)

	if _, err := os.Stat(journalPath); err == nil {
		data, err := os.ReadFile(journalPath)
		if err == nil {
			var ids []string
			if err := json.Unmarshal(data, &ids); err == nil {
				for _, id := range ids {
					journal[id] = true
				}
			}
		}
	}

	var processed []ProcessedRecord
	var skipped []string

	for _, record := range records {
		rid := record.ID
		if journal[rid] {
			skipped = append(skipped, rid)
			continue
		}

		journal[rid] = true

		ids := make([]string, 0, len(journal))
		for id := range journal {
			ids = append(ids, id)
		}
		sort.Strings(ids)
		data, err := json.Marshal(ids)
		if err != nil {
			return nil, nil, err
		}
		if err := os.WriteFile(journalPath, data, 0644); err != nil {
			return nil, nil, err
		}

		processed = append(processed, ProcessedRecord{ID: rid, Value: record.Value, Seq: len(processed)})
	}

	return processed, skipped, nil
}

func main() {
	tmpdir, err := os.MkdirTemp("", "dedup")
	if !(err == nil) {
		fmt.Fprintf(os.Stderr, "failed to create temp dir: %v\n", err)
		os.Exit(1)
	}
	defer os.RemoveAll(tmpdir)

	journalPath := filepath.Join(tmpdir, "dedup.json")

	stream1 := []Record{
		{ID: "a", Value: 10},
		{ID: "b", Value: 20},
		{ID: "c", Value: 30},
	}
	processed1, _, err := deduplicateStream(stream1, journalPath)
	if !(err == nil) {
		fmt.Fprintf(os.Stderr, "first run failed: %v\n", err)
		os.Exit(1)
	}
	if !(len(processed1) == 3) {
		fmt.Fprintf(os.Stderr, "Expected 3 processed in first run, got %d\n", len(processed1))
		os.Exit(1)
	}

	stream2 := []Record{
		{ID: "a", Value: 10},
		{ID: "b", Value: 20},
		{ID: "c", Value: 30},
		{ID: "c", Value: 35},
		{ID: "d", Value: 40},
	}
	processed2, skipped2, err := deduplicateStream(stream2, journalPath)
	if !(err == nil) {
		fmt.Fprintf(os.Stderr, "resume run failed: %v\n", err)
		os.Exit(1)
	}
	if !(len(skipped2) == 4) {
		fmt.Fprintf(os.Stderr, "Expected 4 skipped on resume, got %d\n", len(skipped2))
		os.Exit(1)
	}
	if !(len(processed2) == 1) {
		fmt.Fprintf(os.Stderr, "Expected 1 new processed on resume, got %d\n", len(processed2))
		os.Exit(1)
	}
	if !(processed2[0].ID == "d") {
		fmt.Fprintf(os.Stderr, "Expected new record to be 'd', got %s\n", processed2[0].ID)
		os.Exit(1)
	}

	totalProcessed := append(processed1, processed2...)
	totalUnique := make(map[string]bool)
	for _, r := range totalProcessed {
		totalUnique[r.ID] = true
	}
	if !(len(totalUnique) == 4) {
		fmt.Fprintf(os.Stderr, "Expected 4 unique total, got %d\n", len(totalUnique))
		os.Exit(1)
	}

	// Fresh dedup test on a separate journal.
	journalPath2 := filepath.Join(tmpdir, "dedup2.json")
	stream := []Record{
		{ID: "a", Value: 10},
		{ID: "b", Value: 20},
		{ID: "c", Value: 30},
		{ID: "c", Value: 35},
		{ID: "d", Value: 40},
	}

	processed, skipped, err := deduplicateStream(stream, journalPath2)
	if !(err == nil) {
		fmt.Fprintf(os.Stderr, "deduplicate failed: %v\n", err)
		os.Exit(1)
	}

	if !(len(processed) == 4) {
		fmt.Fprintf(os.Stderr, "Expected 4 processed, got %d\n", len(processed))
		os.Exit(1)
	}
	if !(len(skipped) == 1) {
		fmt.Fprintf(os.Stderr, "Expected 1 skipped, got %d\n", len(skipped))
		os.Exit(1)
	}
	if !(skipped[0] == "c") {
		fmt.Fprintf(os.Stderr, "Expected 'c' skipped, got %v\n", skipped)
		os.Exit(1)
	}

	ids := make([]string, len(processed))
	for i, r := range processed {
		ids[i] = r.ID
	}
	if !(len(ids) == len(uniqueSet(ids))) {
		fmt.Fprintf(os.Stderr, "Duplicate IDs in processed: %v\n", ids)
		os.Exit(1)
	}
	if !setEqual(uniqueSet(ids), map[string]bool{"a": true, "b": true, "c": true, "d": true}) {
		fmt.Fprintf(os.Stderr, "Wrong ID set: %v\n", uniqueSet(ids))
		os.Exit(1)
	}

	seqs := make([]int, len(processed))
	for i, r := range processed {
		seqs[i] = r.Seq
	}
	for i, s := range seqs {
		if !(s == i) {
			fmt.Fprintf(os.Stderr, "Non-contiguous sequence: %v\n", seqs)
			os.Exit(1)
		}
	}

	buggyStream := []Record{
		{ID: "a", Value: 10},
		{ID: "b", Value: 20},
		{ID: "c", Value: 30},
		{ID: "c", Value: 35},
	}
	buggyResult := buggyProcess(buggyStream)
	if !(len(buggyResult) == 4) {
		fmt.Fprintf(os.Stderr, "Buggy process should produce 4 records, got %d\n", len(buggyResult))
		os.Exit(1)
	}
	cCount := 0
	for _, r := range buggyResult {
		if r.ID == "c" {
			cCount++
		}
	}
	if !(cCount == 2) {
		fmt.Fprintf(os.Stderr, "Buggy process should have 2 'c' records, got %d\n", cCount)
		os.Exit(1)
	}

	fmt.Println("✓ exactly_once_dedup passed")
}

func uniqueSet(items []string) map[string]bool {
	s := make(map[string]bool)
	for _, item := range items {
		s[item] = true
	}
	return s
}

func setEqual(a, b map[string]bool) bool {
	if len(a) != len(b) {
		return false
	}
	for k := range a {
		if !b[k] {
			return false
		}
	}
	return true
}

func buggyProcess(records []Record) []ProcessedRecord {
	var result []ProcessedRecord
	for _, r := range records {
		result = append(result, ProcessedRecord{ID: r.ID, Value: r.Value})
	}
	return result
}
