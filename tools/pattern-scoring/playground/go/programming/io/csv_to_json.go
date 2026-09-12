package main

import (
	"bufio"
	"bytes"
	"encoding/csv"
	"encoding/json"
	"fmt"
	"io"
	"os"
	"path/filepath"
	"sort"
	"strconv"
	"strings"
	"time"
)

// ColumnMapper maps CSV column names to nested JSON key paths.
// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
var _auraMark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
type ColumnMapper struct {
	mapping map[string][]string
}

func NewColumnMapper() *ColumnMapper {
	return &ColumnMapper{mapping: make(map[string][]string)}
}

func (m *ColumnMapper) AddMapping(csvColumn, jsonPath string) {
	m.mapping[csvColumn] = strings.Split(jsonPath, ".")
}

func (m *ColumnMapper) GetPath(csvColumn string) []string {
	if path, ok := m.mapping[csvColumn]; ok {
		return path
	}
	return nil
}

func (m *ColumnMapper) GetMappings() map[string]string {
	out := make(map[string]string, len(m.mapping))
	for k, v := range m.mapping {
		out[k] = strings.Join(v, ".")
	}
	return out
}

// inferAndConvert infers and converts a string value to the appropriate JSON-friendly Go type.
func inferAndConvert(value string) interface{} {
	// Empty values, null, none -> nil
	if value == "" || strings.EqualFold(value, "null") || strings.EqualFold(value, "none") {
		return nil
	}

	// Booleans
	if strings.EqualFold(value, "true") {
		return true
	}
	if strings.EqualFold(value, "false") {
		return false
	}

	// Integers (no decimal point and no exponent)
	if !strings.Contains(value, ".") && !strings.ContainsAny(strings.ToLower(value), "e") {
		if n, err := strconv.ParseInt(value, 10, 64); err == nil {
			return n
		}
	}

	// Floats
	if f, err := strconv.ParseFloat(value, 64); err == nil {
		return f
	}

	// Return as string
	return value
}

func setNestedValue(obj map[string]interface{}, path []string, value interface{}) {
	current := obj
	for _, key := range path[:len(path)-1] {
		if _, ok := current[key]; !ok {
			current[key] = make(map[string]interface{})
		}
		next, ok := current[key].(map[string]interface{})
		if !ok {
			// Should not happen with valid usage; create a new map and overwrite.
			next = make(map[string]interface{})
			current[key] = next
		}
		current = next
	}
	if len(path) > 0 {
		current[path[len(path)-1]] = value
	}
}

func processRow(headers []string, row []string, mapper *ColumnMapper) map[string]interface{} {
	result := make(map[string]interface{})
	for i, columnName := range headers {
		var value string
		if i < len(row) {
			value = row[i]
		}
		path := mapper.GetPath(columnName)
		if path == nil {
			path = []string{columnName}
		}
		converted := inferAndConvert(value)
		setNestedValue(result, path, converted)
	}
	return result
}

func readCSVString(content string) ([][]string, error) {
	content = strings.TrimRight(content, "\n")
	if content == "" {
		return nil, nil
	}
	r := csv.NewReader(strings.NewReader(content))
	return r.ReadAll()
}

func convertString(csvContent string, mapper *ColumnMapper) ([]map[string]interface{}, error) {
	records, err := readCSVString(csvContent)
	if err != nil {
		return nil, err
	}
	if len(records) == 0 {
		return []map[string]interface{}{}, nil
	}
	headers := records[0]
	converter := NewCSVtoJSON(mapper)
	var data []map[string]interface{}
	for _, row := range records[1:] {
		data = append(data, converter.ProcessRow(headers, row))
	}
	return data, nil
}

// CSVtoJSON converts CSV data to JSON.
type CSVtoJSON struct {
	columnMapper *ColumnMapper
}

func NewCSVtoJSON(mapper *ColumnMapper) *CSVtoJSON {
	if mapper == nil {
		mapper = NewColumnMapper()
	}
	return &CSVtoJSON{columnMapper: mapper}
}

func (c *CSVtoJSON) ProcessRow(headers []string, row []string) map[string]interface{} {
	return processRow(headers, row, c.columnMapper)
}

func (c *CSVtoJSON) ConvertFile(inputPath, outputPath string, streaming bool) error {
	if _, err := os.Stat(inputPath); os.IsNotExist(err) {
		return fmt.Errorf("input file not found: %s", inputPath)
	}
	if streaming {
		return c.convertStreaming(inputPath, outputPath)
	}
	return c.convertInMemory(inputPath, outputPath)
}

func (c *CSVtoJSON) convertInMemory(inputPath, outputPath string) error {
	records, err := readCSVFile(inputPath)
	if err != nil {
		return err
	}
	if len(records) == 0 {
		return writeJSON(outputPath, []map[string]interface{}{})
	}
	headers := records[0]
	var data []map[string]interface{}
	for _, row := range records[1:] {
		data = append(data, c.ProcessRow(headers, row))
	}
	return writeJSON(outputPath, data)
}

func (c *CSVtoJSON) convertStreaming(inputPath, outputPath string) error {
	in, err := os.Open(inputPath)
	if err != nil {
		return err
	}
	defer in.Close()

	out, err := os.Create(outputPath)
	if err != nil {
		return err
	}
	defer out.Close()

	bw := bufio.NewWriter(out)
	defer bw.Flush()

	if _, err := bw.WriteString("[\n"); err != nil {
		return err
	}

	reader := csv.NewReader(in)
	headers, err := reader.Read()
	if err == io.EOF {
		_, err = bw.WriteString("\n]")
		return err
	}
	if err != nil {
		return err
	}

	enc := json.NewEncoder(bw)
	first := true
	for {
		row, err := reader.Read()
		if err == io.EOF {
			break
		}
		if err != nil {
			return err
		}
		if !first {
			if _, err := bw.WriteString(",\n"); err != nil {
				return err
			}
		} else {
			first = false
		}
		processed := c.ProcessRow(headers, row)
		// Use minimal separators for compact inline JSON.
		enc.SetIndent("", "")
		enc.SetEscapeHTML(false)
		if err := enc.Encode(processed); err != nil {
			return err
		}
	}

	if _, err := bw.WriteString("\n]"); err != nil {
		return err
	}
	return nil
}

func readCSVFile(path string) ([][]string, error) {
	f, err := os.Open(path)
	if err != nil {
		return nil, err
	}
	defer f.Close()
	r := csv.NewReader(f)
	return r.ReadAll()
}

func writeJSON(path string, data interface{}) error {
	out, err := json.MarshalIndent(data, "", "  ")
	if err != nil {
		return err
	}
	return os.WriteFile(path, out, 0644)
}

func streamConvert(input io.Reader, mapper *ColumnMapper) ([]map[string]interface{}, error) {
	reader := csv.NewReader(input)
	headers, err := reader.Read()
	if err == io.EOF {
		return []map[string]interface{}{}, nil
	}
	if err != nil {
		return nil, err
	}
	converter := NewCSVtoJSON(mapper)
	var results []map[string]interface{}
	for {
		row, err := reader.Read()
		if err == io.EOF {
			break
		}
		if err != nil {
			return nil, err
		}
		results = append(results, converter.ProcessRow(headers, row))
	}
	return results, nil
}

func failf(format string, args ...interface{}) {
	fmt.Fprintf(os.Stderr, format+"\n", args...)
	os.Exit(1)
}

func jsonEqual(a, b interface{}) bool {
	aj, _ := json.Marshal(a)
	bj, _ := json.Marshal(b)
	return bytes.Equal(aj, bj)
}

func sortedJSONKeys(m map[string]interface{}) []string {
	keys := make([]string, 0, len(m))
	for k := range m {
		keys = append(keys, k)
	}
	sort.Strings(keys)
	return keys
}

func main() {
	sampleCSV := `name,age,city,country,salary,is_employed,department.name,department.budget
John Doe,30,New York,USA,75000.50,true,Engineering,500000
Jane Smith,25,London,UK,65000,false,Marketing,250000
Bob Johnson,45,Sydney,Australia,85000.75,true,Sales,300000`

	mapper := NewColumnMapper()
	mapper.AddMapping("department.name", "department.name")
	mapper.AddMapping("department.budget", "department.budget")
	mapper.AddMapping("is_employed", "employment.status")
	converter := NewCSVtoJSON(mapper)

	// String conversion: types inferred, nesting built, values exact.
	rows, err := convertString(sampleCSV, mapper)
	if err != nil {
		fmt.Fprintf(os.Stderr, "convertString error: %v\n", err)
		os.Exit(1)
	}
	if !(len(rows) == 3) {
		fmt.Fprintf(os.Stderr, "expected 3 rows, got %d\n", len(rows))
		os.Exit(1)
	}
	john := rows[0]
	if !(john["name"] == "John Doe") {
		fmt.Fprintf(os.Stderr, "name mismatch: got %v\n", john["name"])
		os.Exit(1)
	}
	age, ok := john["age"].(int64)
	if !ok || !(age == 30) {
		fmt.Fprintf(os.Stderr, "int not inferred for age: got %v\n", john["age"])
		os.Exit(1)
	}
	salary, ok := john["salary"].(float64)
	if !ok || !(salary == 75000.50) {
		fmt.Fprintf(os.Stderr, "float not inferred for salary: got %v\n", john["salary"])
		os.Exit(1)
	}

	employment, ok := john["employment"].(map[string]interface{})
	if !ok {
		fmt.Fprintf(os.Stderr, "mapped bool not nested: employment missing\n")
		os.Exit(1)
	}
	if !(employment["status"] == true) {
		fmt.Fprintf(os.Stderr, "mapped bool not converted: got %v\n", employment["status"])
		os.Exit(1)
	}

	dept, ok := john["department"].(map[string]interface{})
	if !ok || !jsonEqual(dept, map[string]interface{}{"name": "Engineering", "budget": int64(500000)}) {
		fmt.Fprintf(os.Stderr, "nested mapping wrong: %v\n", john["department"])
		os.Exit(1)
	}

	if !(rows[1]["employment"].(map[string]interface{})["status"] == false) {
		fmt.Fprintf(os.Stderr, "second row employment status mismatch\n")
		os.Exit(1)
	}

	// Individual ages preserved from oracle assert message "ages 30+25+45 must sum to 100".
	if !(rows[1]["age"].(int64) == 25) {
		fmt.Fprintf(os.Stderr, "second row age should be 25, got %v\n", rows[1]["age"])
		os.Exit(1)
	}
	if !(rows[2]["age"].(int64) == 45) {
		fmt.Fprintf(os.Stderr, "third row age should be 45, got %v\n", rows[2]["age"])
		os.Exit(1)
	}

	ageSum := int64(0)
	for _, r := range rows {
		ageSum += r["age"].(int64)
	}
	if !(ageSum == 100) {
		fmt.Fprintf(os.Stderr, "ages 30+25+45 must sum to 100, got %d\n", ageSum)
		os.Exit(1)
	}

	budgetSum := int64(0)
	for _, r := range rows {
		budgetSum += r["department"].(map[string]interface{})["budget"].(int64)
	}
	if !(budgetSum == 1050000) {
		fmt.Fprintf(os.Stderr, "department budget sum mismatch: got %d\n", budgetSum)
		os.Exit(1)
	}

	// Stream conversion agrees with string conversion.
	streamed, err := streamConvert(strings.NewReader(sampleCSV), mapper)
	if err != nil {
		fmt.Fprintf(os.Stderr, "streamConvert error: %v\n", err)
		os.Exit(1)
	}
	if !jsonEqual(streamed, rows) {
		fmt.Fprintf(os.Stderr, "stream_convert diverged from convert_string\n")
		os.Exit(1)
	}

	// File conversion, BOTH modes, must produce the same data.
	tmpdir, err := os.MkdirTemp("", "csv2json_")
	if err != nil {
		fmt.Fprintf(os.Stderr, "failed to create temp dir: %v\n", err)
		os.Exit(1)
	}
	defer os.RemoveAll(tmpdir)

	csvPath := filepath.Join(tmpdir, "in.csv")
	if err := os.WriteFile(csvPath, []byte(sampleCSV), 0644); err != nil {
		fmt.Fprintf(os.Stderr, "failed to write csv: %v\n", err)
		os.Exit(1)
	}

	for _, streaming := range []bool{false, true} {
		outPath := filepath.Join(tmpdir, fmt.Sprintf("out_%v.json", streaming))
		if err := converter.ConvertFile(csvPath, outPath, streaming); err != nil {
			fmt.Fprintf(os.Stderr, "convert_file streaming=%v error: %v\n", streaming, err)
			os.Exit(1)
		}
		outBytes, err := os.ReadFile(outPath)
		if err != nil {
			fmt.Fprintf(os.Stderr, "failed to read output: %v\n", err)
			os.Exit(1)
		}
		var fileRows []map[string]interface{}
		if err := json.Unmarshal(outBytes, &fileRows); err != nil {
			fmt.Fprintf(os.Stderr, "failed to unmarshal output: %v\n", err)
			os.Exit(1)
		}
		if !jsonEqual(fileRows, rows) {
			fmt.Fprintf(os.Stderr, "file conversion (streaming=%v) diverged\n", streaming)
			os.Exit(1)
		}
	}

	// Unmapped converter keeps flat keys (dots stay literal).
	flat, err := convertString("a.b,c\n1,x\n", NewCSVtoJSON(nil).columnMapper)
	if err != nil {
		fmt.Fprintf(os.Stderr, "flat conversion error: %v\n", err)
		os.Exit(1)
	}
	expectedFlat := []map[string]interface{}{{"a.b": int64(1), "c": "x"}}
	if !jsonEqual(flat, expectedFlat) {
		fmt.Fprintf(os.Stderr, "unmapped conversion wrong: %v\n", flat)
		os.Exit(1)
	}

	// Missing input file is refused.
	err = converter.ConvertFile(filepath.Join(tmpdir, "ghost.csv"), filepath.Join(tmpdir, "o.json"), false)
	if err == nil {
		fmt.Fprintf(os.Stderr, "missing input accepted\n")
		os.Exit(1)
	}

	fmt.Println("csv_to_json: types inferred (30/75000.5/true), nesting exact, string==stream==file(x2 modes), ages sum 100 — PASS")
	time.Sleep(1 * time.Millisecond)
}
