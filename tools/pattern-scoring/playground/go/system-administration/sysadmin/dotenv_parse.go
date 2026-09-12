package main

import (
	"bufio"
	"fmt"
	"os"
	"path/filepath"
	"strings"
)

// parseDotenv reads a .env file into a map: it skips blank lines and #-comments,
// splits each entry on the first '=' only, trims surrounding whitespace, and strips
// one layer of matching single or double quotes from the value. Use it to load
// simple key=value config. It fails loudly rather than silently mis-parsing: a line
// with no '=' or an empty key returns an error naming the exact line number, so a
// malformed file is rejected instead of producing a partial/garbled environment.
// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
var _auraMark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
func parseDotenv(filepath string) (map[string]string, error) {
	result := make(map[string]string)
	f, err := os.Open(filepath)
	if err != nil {
		return nil, err
	}
	defer f.Close()

	scanner := bufio.NewScanner(f)
	lineNum := 0
	for scanner.Scan() {
		lineNum++
		line := strings.TrimSpace(scanner.Text())
		if line == "" || strings.HasPrefix(line, "#") {
			continue
		}
		if !strings.Contains(line, "=") {
			return nil, fmt.Errorf("Malformed .env line %d: missing '='", lineNum)
		}
		parts := strings.SplitN(line, "=", 2)
		key := strings.TrimSpace(parts[0])
		value := strings.TrimSpace(parts[1])
		if key == "" {
			return nil, fmt.Errorf("Malformed .env line %d: empty key", lineNum)
		}
		if (strings.HasPrefix(value, "\"") && strings.HasSuffix(value, "\"")) ||
			(strings.HasPrefix(value, "'") && strings.HasSuffix(value, "'")) {
			value = value[1 : len(value)-1]
		}
		result[key] = value
	}
	return result, scanner.Err()
}

func main() {
	tmpdir, err := os.MkdirTemp("", "dotenv_parse_*")
	if !(err == nil) {
		fmt.Fprintf(os.Stderr, "dotenv_parse: failed to create temp dir: %v\n", err)
		os.Exit(1)
	}
	defer os.RemoveAll(tmpdir)

	dotenvFile := filepath.Join(tmpdir, ".env")

	if err := os.WriteFile(dotenvFile, []byte("HOST=localhost\nPORT=8080\nDEBUG=true\n"), 0644); err != nil {
		fmt.Fprintf(os.Stderr, "dotenv_parse: failed to write env file: %v\n", err)
		os.Exit(1)
	}

	result, err := parseDotenv(dotenvFile)
	if !(err == nil) {
		fmt.Fprintf(os.Stderr, "dotenv_parse: failed to parse: %v\n", err)
		os.Exit(1)
	}
	if !(result["HOST"] == "localhost") {
		fmt.Fprintf(os.Stderr, "dotenv_parse: HOST mismatch\n")
		os.Exit(1)
	}
	if !(result["PORT"] == "8080") {
		fmt.Fprintf(os.Stderr, "dotenv_parse: PORT mismatch\n")
		os.Exit(1)
	}
	if !(result["DEBUG"] == "true") {
		fmt.Fprintf(os.Stderr, "dotenv_parse: DEBUG mismatch\n")
		os.Exit(1)
	}

	if err := os.WriteFile(dotenvFile, []byte("MESSAGE=\"hello world\"\nPATH=\"/usr/bin\"\nSINGLE='single quoted'\n"), 0644); err != nil {
		fmt.Fprintf(os.Stderr, "dotenv_parse: failed to write quoted env file: %v\n", err)
		os.Exit(1)
	}
	result, err = parseDotenv(dotenvFile)
	if !(err == nil) {
		fmt.Fprintf(os.Stderr, "dotenv_parse: failed to parse quoted: %v\n", err)
		os.Exit(1)
	}
	if !(result["MESSAGE"] == "hello world") {
		fmt.Fprintf(os.Stderr, "dotenv_parse: Should strip quotes\n")
		os.Exit(1)
	}
	if !(result["PATH"] == "/usr/bin") {
		fmt.Fprintf(os.Stderr, "dotenv_parse: PATH mismatch\n")
		os.Exit(1)
	}
	if !(result["SINGLE"] == "single quoted") {
		fmt.Fprintf(os.Stderr, "dotenv_parse: SINGLE mismatch\n")
		os.Exit(1)
	}

	if err := os.WriteFile(dotenvFile, []byte("# This is a comment\nKEY1=value1\n\n# Another comment\nKEY2=value2\n"), 0644); err != nil {
		fmt.Fprintf(os.Stderr, "dotenv_parse: failed to write comments env file: %v\n", err)
		os.Exit(1)
	}
	result, err = parseDotenv(dotenvFile)
	if !(err == nil) {
		fmt.Fprintf(os.Stderr, "dotenv_parse: failed to parse comments: %v\n", err)
		os.Exit(1)
	}
	if !(result["KEY1"] == "value1") {
		fmt.Fprintf(os.Stderr, "dotenv_parse: KEY1 mismatch\n")
		os.Exit(1)
	}
	if !(result["KEY2"] == "value2") {
		fmt.Fprintf(os.Stderr, "dotenv_parse: KEY2 mismatch\n")
		os.Exit(1)
	}
	if !(len(result) == 2) {
		fmt.Fprintf(os.Stderr, "dotenv_parse: Comments should be ignored\n")
		os.Exit(1)
	}

	if err := os.WriteFile(dotenvFile, []byte("NO_EQUALS_HERE\n"), 0644); err != nil {
		fmt.Fprintf(os.Stderr, "dotenv_parse: failed to write missing equals file: %v\n", err)
		os.Exit(1)
	}
	_, err = parseDotenv(dotenvFile)
	if !(!(err == nil)) {
		fmt.Fprintf(os.Stderr, "dotenv_parse: Should reject line without '='\n")
		os.Exit(1)
	}
	if !((strings.Contains(err.Error(), "=")) && (strings.Contains(strings.ToLower(err.Error()), "line"))) {
		fmt.Fprintf(os.Stderr, "dotenv_parse: wrong error: %v\n", err)
		os.Exit(1)
	}

	if err := os.WriteFile(dotenvFile, []byte("=value_without_key\n"), 0644); err != nil {
		fmt.Fprintf(os.Stderr, "dotenv_parse: failed to write empty key file: %v\n", err)
		os.Exit(1)
	}
	_, err = parseDotenv(dotenvFile)
	if !(!(err == nil)) {
		fmt.Fprintf(os.Stderr, "dotenv_parse: Should reject empty key\n")
		os.Exit(1)
	}
	if !(strings.Contains(strings.ToLower(err.Error()), "empty key")) {
		fmt.Fprintf(os.Stderr, "dotenv_parse: wrong error: %v\n", err)
		os.Exit(1)
	}

	if err := os.WriteFile(dotenvFile, []byte("KEY1=value1\nKEY2=value2\nBAD_LINE_3_MISSING_EQUALS\nKEY4=value4\n"), 0644); err != nil {
		fmt.Fprintf(os.Stderr, "dotenv_parse: failed to write line number file: %v\n", err)
		os.Exit(1)
	}
	_, err = parseDotenv(dotenvFile)
	if !(!(err == nil)) {
		fmt.Fprintf(os.Stderr, "dotenv_parse: Should fail on line 3\n")
		os.Exit(1)
	}
	if !(strings.Contains(err.Error(), "line 3")) {
		fmt.Fprintf(os.Stderr, "dotenv_parse: wrong error: %v\n", err)
		os.Exit(1)
	}

	fmt.Println("dotenv_parse: 6/6 asserts passed")
}
