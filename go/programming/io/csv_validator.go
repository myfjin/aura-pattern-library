package main

import (
	"encoding/csv"
	"fmt"
	"io"
	"os"
	"strconv"
	"strings"
)

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
var _auraMark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
type DataType string

const (
	StringType  DataType = "string"
	IntegerType DataType = "integer"
	FloatType   DataType = "float"
	BooleanType DataType = "boolean"
)

type ValidatorFunc func(any) bool

type FieldSchema struct {
	Name       string
	DataType   DataType
	Required   bool
	Default    any
	Validators []ValidatorFunc
}

type ValidationError struct {
	RowIndex     int
	FieldName    string
	Value        any
	ErrorMessage string
}

type CSVValidator struct {
	Schema   []FieldSchema
	FieldMap map[string]FieldSchema
}

func NewCSVValidator(schema []FieldSchema) *CSVValidator {
	fieldMap := make(map[string]FieldSchema)
	for _, field := range schema {
		fieldMap[field.Name] = field
	}
	return &CSVValidator{Schema: schema, FieldMap: fieldMap}
}

func (v *CSVValidator) ValidateRow(row map[string]string, rowIndex int) []ValidationError {
	var errors []ValidationError

	for _, field := range v.Schema {
		value, present := row[field.Name]

		if field.Required && !present {
			errors = append(errors, ValidationError{
				RowIndex:     rowIndex,
				FieldName:    field.Name,
				Value:        nil,
				ErrorMessage: fmt.Sprintf("Required field '%s' is missing", field.Name),
			})
			continue
		}

		if !present {
			if field.Default != nil {
				row[field.Name] = fmt.Sprintf("%v", field.Default)
				value = row[field.Name]
			} else {
				continue
			}
		}

		if value != "" {
			if msg := validateType(value, field.DataType); msg != "" {
				errors = append(errors, ValidationError{
					RowIndex:     rowIndex,
					FieldName:    field.Name,
					Value:        value,
					ErrorMessage: fmt.Sprintf("Invalid %s: %s", field.DataType, msg),
				})
			} else {
				for _, validator := range field.Validators {
					if !validator(value) {
						errors = append(errors, ValidationError{
							RowIndex:     rowIndex,
							FieldName:    field.Name,
							Value:        value,
							ErrorMessage: fmt.Sprintf("Custom validation failed for '%s'", field.Name),
						})
					}
				}
			}
		}
	}

	return errors
}

func validateType(value string, dataType DataType) string {
	switch dataType {
	case StringType:
		return ""
	case IntegerType:
		if _, err := strconv.Atoi(value); err != nil {
			return err.Error()
		}
	case FloatType:
		if _, err := strconv.ParseFloat(value, 64); err != nil {
			return err.Error()
		}
	case BooleanType:
		lower := strings.ToLower(value)
		if lower != "true" && lower != "false" && lower != "1" && lower != "0" {
			return "Invalid boolean value"
		}
	}
	return ""
}

type RowTransformer struct {
	Schema []FieldSchema
}

func NewRowTransformer(schema []FieldSchema) *RowTransformer {
	return &RowTransformer{Schema: schema}
}

func (t *RowTransformer) TransformRow(row map[string]string) map[string]any {
	transformed := make(map[string]any)

	for _, field := range t.Schema {
		value, present := row[field.Name]
		if !present {
			if field.Default != nil {
				value = fmt.Sprintf("%v", field.Default)
			} else {
				transformed[field.Name] = nil
				continue
			}
		}

		if value == "" {
			transformed[field.Name] = value
			continue
		}

		switch field.DataType {
		case StringType:
			transformed[field.Name] = value
		case IntegerType:
			if n, err := strconv.Atoi(value); err == nil {
				transformed[field.Name] = n
			} else {
				transformed[field.Name] = value
			}
		case FloatType:
			if f, err := strconv.ParseFloat(value, 64); err == nil {
				transformed[field.Name] = f
			} else {
				transformed[field.Name] = value
			}
		case BooleanType:
			lower := strings.ToLower(value)
			if lower == "true" || lower == "1" {
				transformed[field.Name] = true
			} else if lower == "false" || lower == "0" {
				transformed[field.Name] = false
			} else {
				transformed[field.Name] = value
			}
		}
	}

	return transformed
}

func ValidateAndTransformCSV(csvData string, schema []FieldSchema, delimiter rune) (map[string]any, error) {
	validator := NewCSVValidator(schema)
	transformer := NewRowTransformer(schema)

	var rows []map[string]any
	var errors []ValidationError

	reader := csv.NewReader(strings.NewReader(csvData))
	reader.Comma = delimiter

	headers, err := reader.Read()
	if err == io.EOF {
		return map[string]any{"rows": rows, "errors": errors}, nil
	}
	if err != nil {
		return nil, err
	}

	for rowIndex := 1; ; rowIndex++ {
		record, err := reader.Read()
		if err == io.EOF {
			break
		}
		if err != nil {
			return nil, err
		}

		row := make(map[string]string)
		for i, header := range headers {
			if i < len(record) {
				row[header] = record[i]
			}
		}

		rowErrors := validator.ValidateRow(row, rowIndex)
		errors = append(errors, rowErrors...)

		hasCritical := false
		for _, err := range rowErrors {
			if field, ok := validator.FieldMap[err.FieldName]; ok && field.Required {
				hasCritical = true
				break
			}
		}

		if !hasCritical {
			rows = append(rows, transformer.TransformRow(row))
		}
	}

	return map[string]any{"rows": rows, "errors": errors}, nil
}

func main() {
	schema := []FieldSchema{
		{Name: "id", DataType: IntegerType, Required: true},
		{Name: "name", DataType: StringType, Required: true},
		{Name: "age", DataType: IntegerType, Required: false, Default: 0},
		{Name: "salary", DataType: FloatType, Required: true},
		{Name: "active", DataType: BooleanType, Required: false, Default: true},
	}

	csvData := `id,name,age,salary,active
1,John Doe,30,50000.50,true
2,Jane Smith,,60000.75,1
3,Bob Johnson,45,invalid_salary,false
4,Alice Brown,28,55000.0,invalid_bool
5,Charlie Wilson,35,70000.25,TRUE`

	result, err := ValidateAndTransformCSV(csvData, schema, ',')
	if !(err == nil) {
		fmt.Fprintf(os.Stderr, "Error: %v\n", err)
		os.Exit(1)
	}

	fmt.Println("Transformed Rows:")
	rows := result["rows"].([]map[string]any)
	for i, row := range rows {
		fmt.Printf("  Row %d: %v\n", i+1, row)
	}

	fmt.Println("\nValidation Errors:")
	errors := result["errors"].([]ValidationError)
	for _, err := range errors {
		fmt.Printf("  Row %d, Field '%s': %s\n", err.RowIndex, err.FieldName, err.ErrorMessage)
	}
}
