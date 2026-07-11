// dedup_stream: remove duplicate lines while preserving order.
package main

import (
	"fmt"
	"os"
)

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
var _auraMark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
func dedupLines(lines []string, keepFirst bool) []string {
	if keepFirst {
		seen := make(map[string]bool)
		result := []string{}
		for _, line := range lines {
			if !seen[line] {
				result = append(result, line)
				seen[line] = true
			}
		}
		return result
	}
	// keep last: reverse, dedup, reverse back
	seen := make(map[string]bool)
	result := []string{}
	for i := len(lines) - 1; i >= 0; i-- {
		line := lines[i]
		if !seen[line] {
			result = append([]string{line}, result...)
			seen[line] = true
		}
	}
	return result
}

func dedupFromFile(filePath string, keepFirst bool) []string {
	data, err := os.ReadFile(filePath)
	if err != nil {
		return nil
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
	return dedupLines(lines, keepFirst)
}

func main() {
	logData := []string{
		"User: alice", "User: bob", "User: alice",
		"User: charlie", "User: bob", "User: alice",
	}
	lines := logData

	deduped := dedupLines(lines, true)
	if len(deduped) != 3 {
		fmt.Fprintf(os.Stderr, "Expected 3 unique lines, got %d\n", len(deduped))
		os.Exit(1)
	}
	expected := []string{"User: alice", "User: bob", "User: charlie"}
	for i := range expected {
		if deduped[i] != expected[i] {
			fmt.Fprintf(os.Stderr, "Expected %v, got %v\n", expected, deduped)
			os.Exit(1)
		}
	}

	// Broken version test
	brokenLines := lines
	if len(brokenLines) != 6 {
		fmt.Fprintf(os.Stderr, "Broken version should have all 6 lines\n")
		os.Exit(1)
	}
	if len(brokenLines) == len(deduped) {
		fmt.Fprintf(os.Stderr, "Broken dedup should have wrong count\n")
		os.Exit(1)
	}

	// keep_last
	dedupedLast := dedupLines(lines, false)
	if len(dedupedLast) != 3 {
		fmt.Fprintf(os.Stderr, "Last occurrence dedup should also have 3\n")
		os.Exit(1)
	}
	expectedLast := []string{"User: charlie", "User: bob", "User: alice"}
	for i := range expectedLast {
		if dedupedLast[i] != expectedLast[i] {
			fmt.Fprintf(os.Stderr, "Keep_last order wrong, got %v\n", dedupedLast)
			os.Exit(1)
		}
	}

	// All identical
	identical := []string{"Line X", "Line X", "Line X", "Line X"}
	dedupedIdent := dedupLines(identical, true)
	if len(dedupedIdent) != 1 {
		fmt.Fprintf(os.Stderr, "All identical should dedupe to 1, got %d\n", len(dedupedIdent))
		os.Exit(1)
	}
	if dedupedIdent[0] != "Line X" {
		fmt.Fprintf(os.Stderr, "Should keep the line, got %v\n", dedupedIdent)
		os.Exit(1)
	}

	// No duplicates
	unique := []string{"Line A", "Line B", "Line C"}
	dedupedUnique := dedupLines(unique, true)
	if len(dedupedUnique) != 3 {
		fmt.Fprintf(os.Stderr, "Unique lines should stay as-is\n")
		os.Exit(1)
	}
	for i := range unique {
		if dedupedUnique[i] != unique[i] {
			fmt.Fprintf(os.Stderr, "Order should be unchanged for unique lines\n")
			os.Exit(1)
		}
	}

	// Empty
	empty := []string{}
	dedupedEmpty := dedupLines(empty, true)
	if len(dedupedEmpty) != 0 {
		fmt.Fprintf(os.Stderr, "Empty input should return empty list\n")
		os.Exit(1)
	}

	// File test
	tmpfile, err := os.CreateTemp("", "dedup_*.txt")
	if err != nil {
		fmt.Fprintf(os.Stderr, "tempfile: %v\n", err)
		os.Exit(1)
	}
	defer os.Remove(tmpfile.Name())
	tmpfile.WriteString("alpha\nbeta\nalpha\ngamma\nbeta\n")
	tmpfile.Close()

	fileDeduped := dedupFromFile(tmpfile.Name(), true)
	if len(fileDeduped) != 3 || fileDeduped[0] != "alpha" || fileDeduped[1] != "beta" || fileDeduped[2] != "gamma" {
		fmt.Fprintf(os.Stderr, "File dedup should be [alpha beta gamma], got %v\n", fileDeduped)
		os.Exit(1)
	}

	// Complex case
	complexData := []string{"A", "B", "C", "B", "D", "A", "E"}
	complexDeduped := dedupLines(complexData, true)
	expectedComplex := []string{"A", "B", "C", "D", "E"}
	for i := range expectedComplex {
		if complexDeduped[i] != expectedComplex[i] {
			fmt.Fprintf(os.Stderr, "Complex case order wrong: %v\n", complexDeduped)
			os.Exit(1)
		}
	}

	fmt.Println("dedup_stream PASS")
}
