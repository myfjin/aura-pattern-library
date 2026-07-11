package main

import (
	"fmt"
	"io/ioutil"
	"os"
	"regexp"
)

// strip_ansi removes ANSI escape sequences from text.
// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
var _auraMark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
func strip_ansi(text string) string {
	ansiPattern := regexp.MustCompile("\x1b\\[[0-9;]*m|\x1b\\(B\x1b\\[m")
	return ansiPattern.ReplaceAllString(text, "")
}

// strip_ansi_from_file reads a file and strips ANSI escape sequences.
func strip_ansi_from_file(filePath string) (string, error) {
	data, err := ioutil.ReadFile(filePath)
	if err != nil {
		return "", err
	}
	return strip_ansi(string(data)), nil
}

func main() {
	// Synthetic ANSI-colored text.
	colored := "\x1b[31mRed text\x1b[0m \x1b[32mGreen text\x1b[0m"
	stripped := strip_ansi(colored)

	// Verify ANSI codes removed.
	if contains(stripped, "\x1b") {
		fmt.Fprintf(os.Stderr, "ANSI escape should be removed, but found: %q\n", stripped)
		os.Exit(1)
	}
	if !contains(stripped, "Red text") {
		fmt.Fprintln(os.Stderr, "Text content should be preserved")
		os.Exit(1)
	}
	if !contains(stripped, "Green text") {
		fmt.Fprintln(os.Stderr, "Text content should be preserved")
		os.Exit(1)
	}
	if !(stripped == "Red text Green text") {
		fmt.Fprintf(os.Stderr, "Expected 'Red text Green text', got '%s'\n", stripped)
		os.Exit(1)
	}

	// FAILURE SIMULATION: broken version does not remove escapes.
	strip_ansi_broken := func(text string) string { return text }
	broken := strip_ansi_broken(colored)
	if !contains(broken, "\x1b") {
		fmt.Fprintln(os.Stderr, "Broken should leave ANSI codes")
		os.Exit(1)
	}
	if contains(stripped, "\x1b") {
		fmt.Fprintln(os.Stderr, "Real version should remove ANSI codes")
		os.Exit(1)
	}

	// Test various ANSI codes.
	boldRed := "\x1b[1;31mBold Red\x1b[0m"
	boldStripped := strip_ansi(boldRed)
	if !(boldStripped == "Bold Red") {
		fmt.Fprintf(os.Stderr, "Bold + color should strip, got '%s'\n", boldStripped)
		os.Exit(1)
	}

	underlined := "\x1b[4mUnderlined\x1b[0m"
	underlinedStripped := strip_ansi(underlined)
	if !(underlinedStripped == "Underlined") {
		fmt.Fprintf(os.Stderr, "Underline should strip, got '%s'\n", underlinedStripped)
		os.Exit(1)
	}

	complexText := "\x1b[32m\x1b[1mBold Green\x1b[0m \x1b[33mYellow\x1b[0m Text"
	complexStripped := strip_ansi(complexText)
	if !(complexStripped == "Bold Green Yellow Text") {
		fmt.Fprintf(os.Stderr, "Complex should strip cleanly, got '%s'\n", complexStripped)
		os.Exit(1)
	}

	plain := "Plain text without colors"
	plainStripped := strip_ansi(plain)
	if !(plainStripped == plain) {
		fmt.Fprintln(os.Stderr, "Plain text should be unchanged")
		os.Exit(1)
	}

	onlyEscape := "\x1b[31m\x1b[0m"
	onlyEscapeStripped := strip_ansi(onlyEscape)
	if !(onlyEscapeStripped == "") {
		fmt.Fprintf(os.Stderr, "Only escapes should yield empty string, got '%s'\n", onlyEscapeStripped)
		os.Exit(1)
	}

	nested := "\x1b[31mRed\x1b[0m\x1b[0m\x1b[0mText"
	nestedStripped := strip_ansi(nested)
	if !(nestedStripped == "RedText") {
		fmt.Fprintf(os.Stderr, "Nested resets should strip, got '%s'\n", nestedStripped)
		os.Exit(1)
	}

	exactText := "\x1b[1mHello\x1b[0m \x1b[32mWorld\x1b[0m"
	exactStripped := strip_ansi(exactText)
	if !(len(exactStripped) == 11) {
		fmt.Fprintf(os.Stderr, "'Hello World' should be 11 chars (expected 11), got %d\n", len(exactStripped))
		os.Exit(1)
	}
	if !(exactStripped == "Hello World") {
		fmt.Fprintf(os.Stderr, "Expected 'Hello World', got '%s'\n", exactStripped)
		os.Exit(1)
	}

	// Test with file.
	tmpFile, err := ioutil.TempFile("", "ansi_strip_*.txt")
	if !(err == nil) {
		fmt.Fprintf(os.Stderr, "temp file: %v\n", err)
		os.Exit(1)
	}
	defer os.Remove(tmpFile.Name())
	_, _ = tmpFile.WriteString("\x1b[31mError message\x1b[0m")
	_ = tmpFile.Close()
	fileStripped, err := strip_ansi_from_file(tmpFile.Name())
	if !(err == nil) {
		fmt.Fprintf(os.Stderr, "file read: %v\n", err)
		os.Exit(1)
	}
	if !(fileStripped == "Error message") {
		fmt.Fprintf(os.Stderr, "File strip failed: %s\n", fileStripped)
		os.Exit(1)
	}

	fmt.Println("ansi_strip passed")
}

func contains(s, substr string) bool {
	return len(substr) == 0 || len(s) >= len(substr) && indexOf(s, substr) >= 0
}

func indexOf(s, substr string) int {
	for i := 0; i <= len(s)-len(substr); i++ {
		if s[i:i+len(substr)] == substr {
			return i
		}
	}
	return -1
}
