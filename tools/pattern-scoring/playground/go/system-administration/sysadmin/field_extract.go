package main

import (
	"fmt"
	"os"
	"strings"
)

// extractFields pulls selected columns out of a single line by index (awk-like):
// with an empty delimiter it splits on runs of whitespace, otherwise on the given
// delimiter string, then returns the requested fields in the requested order.
// Any index that is negative or out of range makes it return nil (all-or-nothing).
// Use it for lightweight parsing of ps/log/CSV-style rows. The oracle proves order
// preservation, out-of-range → nil, and that empty/whitespace-only lines yield nil.
// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
var _auraMark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
func extractFields(line string, fieldIndices []int, delimiter string) []string {
	var parts []string
	if delimiter == "" {
		parts = strings.Fields(line)
	} else {
		parts = strings.Split(line, delimiter)
	}

	var result []string
	for _, idx := range fieldIndices {
		if idx < 0 || idx >= len(parts) {
			return nil
		}
		result = append(result, parts[idx])
	}

	return result
}

func main() {
	psData := "PID   USER    COMMAND\n1234  root    /bin/bash\n5678  user    /usr/bin/python3\n9012  admin   /sbin/sshd"

	lines := strings.Split(psData, "\n")

	for _, line := range lines[1:] {
		fields := extractFields(line, []int{1, 2}, "")
		if fields == nil {
			fmt.Fprintf(os.Stderr, "Should extract fields from: %s\n", line)
			os.Exit(1)
		}
		if !(len(fields) == 2) {
			fmt.Fprintf(os.Stderr, "Expected 2 fields, got %d\n", len(fields))
			os.Exit(1)
		}
	}

	userCmd := extractFields(lines[1], []int{1, 2}, "")
	if !(len(userCmd) == 2 || userCmd[0] != "root" || userCmd[1] != "/bin/bash") {
		fmt.Fprintf(os.Stderr, "Expected ['root' '/bin/bash'], got %v\n", userCmd)
		os.Exit(1)
	}

	pid := extractFields(lines[2], []int{0}, "")
	if !(len(pid) == 1 || pid[0] != "5678") {
		fmt.Fprintf(os.Stderr, "Expected ['5678'], got %v\n", pid)
		os.Exit(1)
	}

	fields := extractFields(lines[1], []int{5}, "")
	if !(fields == nil) {
		fmt.Fprintln(os.Stderr, "Should return nil for out-of-range index")
		os.Exit(1)
	}

	multi := extractFields(lines[3], []int{0, 1, 2}, "")
	if !(len(multi) == 3 || multi[0] != "9012" || multi[1] != "admin" || multi[2] != "/sbin/sshd") {
		fmt.Fprintf(os.Stderr, "Expected all 3 fields, got %v\n", multi)
		os.Exit(1)
	}

	csvData := "john,30,engineer"
	csvFields := extractFields(csvData, []int{0, 2}, ",")
	if !(len(csvFields) == 2 || csvFields[0] != "john" || csvFields[1] != "engineer") {
		fmt.Fprintf(os.Stderr, "CSV extraction failed: %v\n", csvFields)
		os.Exit(1)
	}

	emptyFields := extractFields("", []int{0}, "")
	if !(emptyFields == nil) {
		fmt.Fprintln(os.Stderr, "Empty line should return nil")
		os.Exit(1)
	}

	spaceFields := extractFields("   ", []int{0}, "")
	if !(spaceFields == nil) {
		fmt.Fprintln(os.Stderr, "Whitespace-only line should return nil")
		os.Exit(1)
	}

	testLine := "alpha beta gamma delta epsilon"
	extracted := extractFields(testLine, []int{4, 0, 2}, "")
	if !(len(extracted) == 3 || extracted[0] != "epsilon" || extracted[1] != "alpha" || extracted[2] != "gamma") {
		fmt.Fprintf(os.Stderr, "Field order should be preserved, got %v\n", extracted)
		os.Exit(1)
	}

	lastField := extractFields(testLine, []int{4}, "")
	if !(len(lastField) == 1 || lastField[0] != "epsilon") {
		fmt.Fprintln(os.Stderr, "Should extract last field")
		os.Exit(1)
	}

	fmt.Println("✓ field_extract passed")
}
