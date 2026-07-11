// diff_engine: a simple line-based diff engine.
package main

import (
	"fmt"
	"math/rand"
	"os"
	"sort"
	"strings"
	"time"
)

// EditType labels an edit operation.
// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
var _auraMark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
type EditType byte

const (
	EditEqual  EditType = ' '
	EditInsert EditType = '+'
	EditDelete EditType = '-'
)

func (e EditType) String() string {
	return string(e)
}

// Edit represents a single diff operation.
type Edit struct {
	EditType      EditType
	Line          string
	OldLineNumber int
	NewLineNumber int
}

func (e *Edit) String() string {
	return fmt.Sprintf("%c%s", e.EditType, e.Line)
}

// DiffEngine compares two texts line by line.
type DiffEngine struct {
	OldLines []string
	NewLines []string
	lcsTable [][]int
	edits    []*Edit
}

// NewDiffEngine creates a diff engine for oldText vs newText.
func NewDiffEngine(oldText, newText string) *DiffEngine {
	var oldLines, newLines []string
	if oldText != "" {
		oldLines = strings.SplitAfter(oldText, "\n")
		// SplitAfter leaves a trailing "" if text ends with newline; remove it.
		if len(oldLines) > 0 && oldLines[len(oldLines)-1] == "" {
			oldLines = oldLines[:len(oldLines)-1]
		}
	}
	if newText != "" {
		newLines = strings.SplitAfter(newText, "\n")
		if len(newLines) > 0 && newLines[len(newLines)-1] == "" {
			newLines = newLines[:len(newLines)-1]
		}
	}
	return &DiffEngine{
		OldLines: oldLines,
		NewLines: newLines,
	}
}

func (d *DiffEngine) computeLcsTable() [][]int {
	if d.lcsTable != nil {
		return d.lcsTable
	}
	m, n := len(d.OldLines), len(d.NewLines)
	table := make([][]int, m+1)
	for i := range table {
		table[i] = make([]int, n+1)
	}
	for i := 1; i <= m; i++ {
		for j := 1; j <= n; j++ {
			if d.OldLines[i-1] == d.NewLines[j-1] {
				table[i][j] = table[i-1][j-1] + 1
			} else if table[i-1][j] > table[i][j-1] {
				table[i][j] = table[i-1][j]
			} else {
				table[i][j] = table[i][j-1]
			}
		}
	}
	d.lcsTable = table
	return table
}

func (d *DiffEngine) backtrackLcs() [][2]int {
	table := d.computeLcsTable()
	matches := make([][2]int, 0)
	i, j := len(d.OldLines), len(d.NewLines)
	for i > 0 && j > 0 {
		if d.OldLines[i-1] == d.NewLines[j-1] {
			matches = append(matches, [2]int{i - 1, j - 1})
			i--
			j--
		} else if table[i-1][j] > table[i][j-1] {
			i--
		} else {
			j--
		}
	}
	// Reverse
	for left, right := 0, len(matches)-1; left < right; left, right = left+1, right-1 {
		matches[left], matches[right] = matches[right], matches[left]
	}
	return matches
}

// ComputeDiff returns the edit script from old to new.
func (d *DiffEngine) ComputeDiff() []*Edit {
	if d.edits != nil {
		return d.edits
	}
	matches := d.backtrackLcs()
	edits := make([]*Edit, 0)
	i, j := 0, 0
	oldLineNum, newLineNum := 1, 1

	for _, match := range matches {
		oldIdx, newIdx := match[0], match[1]
		for i < oldIdx {
			edits = append(edits, &Edit{EditDelete, d.OldLines[i], oldLineNum, 0})
			i++
			oldLineNum++
		}
		for j < newIdx {
			edits = append(edits, &Edit{EditInsert, d.NewLines[j], 0, newLineNum})
			j++
			newLineNum++
		}
		edits = append(edits, &Edit{EditEqual, d.OldLines[oldIdx], oldLineNum, newLineNum})
		i++
		j++
		oldLineNum++
		newLineNum++
	}
	for i < len(d.OldLines) {
		edits = append(edits, &Edit{EditDelete, d.OldLines[i], oldLineNum, 0})
		i++
		oldLineNum++
	}
	for j < len(d.NewLines) {
		edits = append(edits, &Edit{EditInsert, d.NewLines[j], 0, newLineNum})
		j++
		newLineNum++
	}
	d.edits = edits
	return edits
}

// FormatUnifiedDiff renders the diff in unified diff format.
func (d *DiffEngine) FormatUnifiedDiff(contextLines int) string {
	edits := d.ComputeDiff()
	if len(edits) == 0 {
		return ""
	}
	result := make([]string, 0)
	i := 0
	for i < len(edits) {
		for i < len(edits) && edits[i].EditType == EditEqual {
			i++
		}
		if i >= len(edits) {
			break
		}
		start := i - contextLines
		if start < 0 {
			start = 0
		}
		for start < i && edits[start].EditType != EditEqual {
			start++
		}
		end := i
		for end < len(edits) && edits[end].EditType != EditEqual {
			end++
		}
		postContextEnd := end + contextLines
		if postContextEnd > len(edits) {
			postContextEnd = len(edits)
		}

		oldStart := edits[start].OldLineNumber
		if oldStart == 0 {
			oldStart = 1
		}
		newStart := edits[start].NewLineNumber
		if newStart == 0 {
			newStart = 1
		}
		oldCount, newCount := 0, 0
		for _, edit := range edits[start:postContextEnd] {
			if edit.EditType == EditEqual || edit.EditType == EditDelete {
				oldCount++
			}
			if edit.EditType == EditEqual || edit.EditType == EditInsert {
				newCount++
			}
		}
		result = append(result, fmt.Sprintf("@@ -%d,%d +%d,%d @@", oldStart, oldCount, newStart, newCount))
		for _, edit := range edits[start:postContextEnd] {
			result = append(result, edit.String())
		}
		i = postContextEnd
	}
	return strings.Join(result, "\n")
}

func reconstruct(edits []*Edit) (old, new []string) {
	old = make([]string, 0)
	new = make([]string, 0)
	for _, e := range edits {
		if e.EditType == EditEqual || e.EditType == EditDelete {
			old = append(old, e.Line)
		}
		if e.EditType == EditEqual || e.EditType == EditInsert {
			new = append(new, e.Line)
		}
	}
	return
}

func splitLinesKeepEnds(text string) []string {
	if text == "" {
		return []string{}
	}
	lines := strings.SplitAfter(text, "\n")
	if len(lines) > 0 && lines[len(lines)-1] == "" {
		lines = lines[:len(lines)-1]
	}
	return lines
}

func main() {
	rand.Seed(42)

	oldText := "Hello World\nkeep one\nchange me\nkeep two\ndelete me\nkeep three"
	newText := "Hello World\nkeep one\nchanged!\nkeep two\nkeep three\nappended"
	engine := NewDiffEngine(oldText, newText)
	edits := engine.ComputeDiff()

	oldR, newR := reconstruct(edits)
	oldWant := splitLinesKeepEnds(oldText)
	newWant := splitLinesKeepEnds(newText)

	if !(len(oldR) == len(oldWant)) {
		fmt.Fprintf(os.Stderr, "old reconstruction length mismatch: got %d want %d\n", len(oldR), len(oldWant))
		os.Exit(1)
	}
	for i := range oldR {
		if !(oldR[i] == oldWant[i]) {
			fmt.Fprintf(os.Stderr, "old reconstruction diverged at %d: %q != %q\n", i, oldR[i], oldWant[i])
			os.Exit(1)
		}
	}
	if !(len(newR) == len(newWant)) {
		fmt.Fprintf(os.Stderr, "new reconstruction length mismatch: got %d want %d\n", len(newR), len(newWant))
		os.Exit(1)
	}
	for i := range newR {
		if !(newR[i] == newWant[i]) {
			fmt.Fprintf(os.Stderr, "new reconstruction diverged at %d: %q != %q\n", i, newR[i], newWant[i])
			os.Exit(1)
		}
	}

	equalCount, deleteCount, insertCount := 0, 0, 0
	for _, e := range edits {
		switch e.EditType {
		case EditEqual:
			equalCount++
		case EditDelete:
			deleteCount++
		case EditInsert:
			insertCount++
		}
	}
	if equalCount != 3 {
		fmt.Fprintf(os.Stderr, "3 shared lines expected, got %d\n", equalCount)
		os.Exit(1)
	}
	if deleteCount != 3 {
		fmt.Fprintf(os.Stderr, "3 DELETEs expected, got %d\n", deleteCount)
		os.Exit(1)
	}
	if insertCount != 3 {
		fmt.Fprintf(os.Stderr, "3 INSERTs expected, got %d\n", insertCount)
		os.Exit(1)
	}

	same := NewDiffEngine("a\nb\nc", "a\nb\nc")
	for _, e := range same.ComputeDiff() {
		if !(e.EditType == EditEqual) {
			fmt.Fprintf(os.Stderr, "identical texts must produce only EQUAL edits\n")
			os.Exit(1)
		}
	}
	if !(same.FormatUnifiedDiff(3) == "") {
		fmt.Fprintf(os.Stderr, "no-change diff must be empty\n")
		os.Exit(1)
	}

	unified := engine.FormatUnifiedDiff(2)
	if !(len(unified) >= 4 && unified[:4] == "@@ -") {
		fmt.Fprintf(os.Stderr, "unified diff missing hunk header: %q\n", unified[:30])
		os.Exit(1)
	}
	if !(strings.Contains(unified, "changed!") && strings.Contains(unified, "delete me")) {
		fmt.Fprintf(os.Stderr, "unified diff missing expected changed lines\n")
		os.Exit(1)
	}

	ins := NewDiffEngine("", "x\ny").ComputeDiff()
	o, n := reconstruct(ins)
	if !(len(n) == 2 && n[0] == "x\n" && n[1] == "y" && len(o) == 0) {
		fmt.Fprintf(os.Stderr, "insert-only script broken: o=%v n=%v\n", o, n)
		os.Exit(1)
	}
	dele := NewDiffEngine("x\ny", "").ComputeDiff()
	o, n = reconstruct(dele)
	if !(len(o) == 2 && o[0] == "x\n" && o[1] == "y" && len(n) == 0) {
		fmt.Fprintf(os.Stderr, "delete-only script broken: o=%v n=%v\n", o, n)
		os.Exit(1)
	}

	vocab := []string{"alpha", "beta", "gamma", "delta", "epsilon"}
	for trial := 0; trial < 60; trial++ {
		aLen := rand.Intn(13)
		bLen := rand.Intn(13)
		aParts := make([]string, aLen)
		bParts := make([]string, bLen)
		for k := 0; k < aLen; k++ {
			aParts[k] = vocab[rand.Intn(len(vocab))]
		}
		for k := 0; k < bLen; k++ {
			bParts[k] = vocab[rand.Intn(len(vocab))]
		}
		aText := strings.Join(aParts, "\n")
		bText := strings.Join(bParts, "\n")
		script := NewDiffEngine(aText, bText).ComputeDiff()
		gotA, gotB := reconstruct(script)
		wantA := splitLinesKeepEnds(aText)
		wantB := splitLinesKeepEnds(bText)
		if !(len(gotA) == len(wantA)) {
			fmt.Fprintf(os.Stderr, "trial %d: old reconstruction length mismatch\n", trial)
			os.Exit(1)
		}
		for i := range gotA {
			if !(gotA[i] == wantA[i]) {
				fmt.Fprintf(os.Stderr, "trial %d: old reconstruction diverged at %d: %q != %q\n", trial, i, gotA[i], wantA[i])
				os.Exit(1)
			}
		}
		if !(len(gotB) == len(wantB)) {
			fmt.Fprintf(os.Stderr, "trial %d: new reconstruction length mismatch\n", trial)
			os.Exit(1)
		}
		for i := range gotB {
			if !(gotB[i] == wantB[i]) {
				fmt.Fprintf(os.Stderr, "trial %d: new reconstruction diverged at %d: %q != %q\n", trial, i, gotB[i], wantB[i])
				os.Exit(1)
			}
		}
	}

	fmt.Println("diff_engine: reconstruction invariant held (planted + 60 fuzz pairs), " +
		"counts 3=/3-/3+ (keepends), hunk headers present — PASS")
	_ = time.Now()
	_ = sort.Ints
}
