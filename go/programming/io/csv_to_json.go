// csv_to_json: CSV to JSON converter with type inference, nested key support, and streaming.
package main

import (
	"encoding/csv"
	"encoding/json"
	"fmt"
	"io"
	"os"
	"path/filepath"
	"strconv"
	"strings"
)

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
var _auraMark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
type ColumnMapper struct {
	mapping map[string][]string
}

func newColumnMapper() *ColumnMapper {
	return &ColumnMapper{mapping: make(map[string][]string)}
}

func (m *ColumnMapper) addMapping(csvColumn, jsonPath string) {
	m.mapping[csvColumn] = strings.Split(jsonPath, ".")
}

func (m *ColumnMapper) getPath(csvColumn string) []string {
	if path, ok := m.mapping[csvColumn]; ok {
		return path
	}
	return nil
}

func inferAndConvert(value string) interface{} {
	if value == "" || strings.ToLower(value) == "null" || strings.ToLower(value) == "none" {
		return nil
	}
	if strings.ToLower(value) == "true" {
		return true
	}
	if strings.ToLower(value) == "false" {
		return false
	}
	if !strings.Contains(value, ".") && !strings.Contains(strings.ToLower(value), "e") {
		if i, err := strconv.Atoi(value); err == nil {
			return i
		}
	}
	if f, err := strconv.ParseFloat(value, 64); err == nil {
		return f
	}
	return value
}

func setNestedValue(obj map[string]interface{}, path []string, value interface{}) {
	current := obj
	for _, key := range path[:len(path)-1] {
		if _, ok := current[key]; !ok {
			current[key] = make(map[string]interface{})
		}
		current = current[key].(map[string]interface{})
	}
	current[path[len(path)-1]] = value
}

func processRow(mapper *ColumnMapper, row map[string]string) map[string]interface{} {
	result := make(map[string]interface{})
	for column, value := range row {
		path := mapper.getPath(column)
		if path == nil {
			path = []string{column}
		}
		setNestedValue(result, path, inferAndConvert(value))
	}
	return result
}

type CSVtoJSON struct {
	mapper *ColumnMapper
}

func newCSVtoJSON(mapper *ColumnMapper) *CSVtoJSON {
	return &CSVtoJSON{mapper: mapper}
}

func (c *CSVtoJSON) convertString(csvContent string) string {
	reader := csv.NewReader(strings.NewReader(csvContent))
	records, err := reader.ReadAll()
	if err != nil {
		return "[]"
	}
	if len(records) == 0 {
		return "[]"
	}
	data := processAllRecords(c.mapper, records)
	b, _ := json.MarshalIndent(data, "", "  ")
	return string(b)
}

func (c *CSVtoJSON) streamConvert(input io.Reader) []map[string]interface{} {
	reader := csv.NewReader(input)
	header, err := reader.Read()
	if err != nil {
		return nil
	}
	var results []map[string]interface{}
	for {
		record, err := reader.Read()
		if err == io.EOF {
			break
		}
		if err != nil {
			continue
		}
		row := make(map[string]string)
		for i, h := range header {
			if i < len(record) {
				row[h] = record[i]
			}
		}
		results = append(results, processRow(c.mapper, row))
	}
	return results
}

func processAllRecords(mapper *ColumnMapper, records [][]string) []map[string]interface{} {
	if len(records) == 0 {
		return nil
	}
	header := records[0]
	var results []map[string]interface{}
	for _, record := range records[1:] {
		row := make(map[string]string)
		for i, h := range header {
			if i < len(record) {
				row[h] = record[i]
			}
		}
		results = append(results, processRow(mapper, row))
	}
	return results
}

func main() {
	sampleCSV := `name,age,city,country,salary,is_employed,department.name,department.budget
John Doe,30,New York,USA,75000.50,true,Engineering,500000
Jane Smith,25,London,UK,65000,false,Marketing,250000
Bob Johnson,45,Sydney,Australia,85000.75,true,Sales,300000`

	mapper := newColumnMapper()
	mapper.addMapping("department.name", "department.name")
	mapper.addMapping("department.budget", "department.budget")
	mapper.addMapping("is_employed", "employment.status")

	converter := newCSVtoJSON(mapper)

	fmt.Println("Demo 1: String conversion")
	jsonResult := converter.convertString(sampleCSV)
	if len(jsonResult) > 200 {
		fmt.Println(jsonResult[:200] + "...")
	} else {
		fmt.Println(jsonResult)
	}
	fmt.Println()

	fmt.Println("Demo 2: Stream conversion")
	csvIO := strings.NewReader(sampleCSV)
	streamResults := converter.streamConvert(csvIO)
	fmt.Printf("Processed %d records:\n", len(streamResults))
	for i, record := range streamResults {
		fmt.Printf("  Record %d: %v\n", i+1, record)
		if i >= 2 {
			break
		}
	}
	fmt.Println()

	fmt.Println("Demo 3: File conversion")
	tmpdir, err := os.MkdirTemp("", "csv_to_json_*")
	if !(err == nil) {
		fmt.Fprintf(os.Stderr, "failed to create temp dir: %v\n", err)
		os.Exit(1)
	}
	defer os.RemoveAll(tmpdir)

	demoCSV := filepath.Join(tmpdir, "demo.csv")
	demoJSON := filepath.Join(tmpdir, "demo.json")

	if err := os.WriteFile(demoCSV, []byte(sampleCSV), 0o644); err != nil {
		fmt.Fprintf(os.Stderr, "failed to write demo csv: %v\n", err)
		os.Exit(1)
	}

	input, err := os.Open(demoCSV)
	if !(err == nil) {
		fmt.Fprintf(os.Stderr, "failed to open demo csv: %v\n", err)
		os.Exit(1)
	}
	data := converter.streamConvert(input)
	input.Close()

	out, err := json.MarshalIndent(data, "", "  ")
	if !(err == nil) {
		fmt.Fprintf(os.Stderr, "failed to marshal json: %v\n", err)
		os.Exit(1)
	}
	if err := os.WriteFile(demoJSON, out, 0o644); err != nil {
		fmt.Fprintf(os.Stderr, "failed to write demo json: %v\n", err)
		os.Exit(1)
	}

	fileResult, err := os.ReadFile(demoJSON)
	if !(err == nil) {
		fmt.Fprintf(os.Stderr, "failed to read demo json: %v\n", err)
		os.Exit(1)
	}
	if len(fileResult) > 200 {
		fmt.Println(string(fileResult[:200]) + "...")
	} else {
		fmt.Println(string(fileResult))
	}

	fmt.Println("\nAll demos completed successfully!")
}
