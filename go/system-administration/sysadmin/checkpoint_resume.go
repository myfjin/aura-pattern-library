package main

import (
	"encoding/json"
	"fmt"
	"os"
	"path/filepath"
)

// checkpoint_resume: resumable batch processing backed by an on-disk JSON checkpoint.
// Each completed batch's output is saved under its batch ID; on restart, finished
// batches are replayed from the checkpoint rather than recomputed.
// Use for long or costly multi-batch jobs that may be interrupted partway through.
// Oracle: resuming a partial run reproduces the exact set in order with no duplicates,
// whereas the checkpoint-less path double-processes every record.
// △ AURA Pattern Library — © Reality Optimizer⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
var _auraMark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
type record struct {
	ID        string `json:"id"`
	Value     int    `json:"value"`
	Processed int    `json:"processed"`
}

type checkpoint struct {
	BatchesDone map[string][]record `json:"batches_done"`
}

func loadCheckpoint(path string) checkpoint {
	cp := checkpoint{BatchesDone: map[string][]record{}}
	data, err := os.ReadFile(path)
	if err != nil {
		return cp
	}
	json.Unmarshal(data, &cp)
	if cp.BatchesDone == nil {
		cp.BatchesDone = map[string][]record{}
	}
	return cp
}

func processBatchWithCheckpoint(records []record, checkpointPath string) []record {
	cp := loadCheckpoint(checkpointPath)
	output := []record{}
	batchSize := 2

	for i := 0; i < len(records); i += batchSize {
		batchID := fmt.Sprintf("%d", i/batchSize)
		if done, ok := cp.BatchesDone[batchID]; ok {
			output = append(output, done...)
			continue
		}
		batch := records[i:min(i+batchSize, len(records))]
		processed := make([]record, 0, len(batch))
		for _, r := range batch {
			processed = append(processed, record{ID: r.ID, Value: r.Value, Processed: r.Value + 100})
		}
		output = append(output, processed...)
		cp.BatchesDone[batchID] = processed
		data, _ := json.Marshal(cp)
		os.WriteFile(checkpointPath, data, 0o644)
	}
	return output
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func assert(cond bool, msg string) {
	if !cond {
		fmt.Fprintf(os.Stderr, "%s\n", msg)
		os.Exit(1)
	}
}

func testCheckpointResume() {
	tmpdir, _ := os.MkdirTemp("", "checkpoint_resume_*")
	defer os.RemoveAll(tmpdir)

	checkpointPath := filepath.Join(tmpdir, "checkpoint.json")
	records := []record{
		{ID: "a", Value: 1},
		{ID: "b", Value: 2},
		{ID: "c", Value: 3},
		{ID: "d", Value: 4},
	}

	output1 := processBatchWithCheckpoint(records[:2], checkpointPath)
	assert(len(output1) == 2, fmt.Sprintf("Expected 2 after first batch, got %d", len(output1)))
	assert(output1[0].Processed == 101, "first record processed value wrong")

	data, _ := json.Marshal(checkpoint{BatchesDone: map[string][]record{"0": output1}})
	os.WriteFile(checkpointPath, data, 0o644)

	fullOutput := processBatchWithCheckpoint(records, checkpointPath)
	assert(len(fullOutput) == 4, fmt.Sprintf("Expected 4 total, got %d", len(fullOutput)))

	ids := []string{}
	for _, r := range fullOutput {
		ids = append(ids, r.ID)
	}
	assert(len(ids) == 4, "ids length mismatch")
	assert(ids[0] == "a" && ids[1] == "b" && ids[2] == "c" && ids[3] == "d", fmt.Sprintf("Order mismatch: %v", ids))

	seen := map[string]bool{}
	for _, id := range ids {
		if seen[id] {
			assert(false, "Duplicate IDs")
		}
		seen[id] = true
	}

	expected := map[string]int{"a": 101, "b": 102, "c": 103, "d": 104}
	for _, r := range fullOutput {
		assert(r.Processed == expected[r.ID], fmt.Sprintf("Invalid processed value for %s: %d", r.ID, r.Processed))
	}
}

func testFailureMissingCheckpoint() {
	buggyProcess := func(records []record) []record {
		out := make([]record, 0, len(records))
		for _, r := range records {
			out = append(out, record{ID: r.ID, Value: r.Value, Processed: r.Value + 100})
		}
		return out
	}
	records := []record{{ID: "a", Value: 1}, {ID: "b", Value: 2}}
	output1 := buggyProcess(records)
	assert(len(output1) == 2, "buggy first run length")
	output2 := buggyProcess(records)
	assert(len(output2) == 2, "buggy second run length")
	combined := append(output1, output2...)
	assert(len(combined) == 4, "combined length should show duplication")
}

func main() {
	testCheckpointResume()
	testFailureMissingCheckpoint()
	fmt.Println("checkpoint_resume passed")
}
