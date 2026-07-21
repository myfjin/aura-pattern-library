package main

import (
	"encoding/csv"
	"math"
	"fmt"
	"os"
	"strconv"
	"strings"
)

// Schema-driven CSV validation and transformation: each field declares a type
// (string/integer/float/boolean), a required flag, a default, and optional custom
// validators; rows are validated and then coerced to typed values, delimiter-configurable.
// Use to validate and type-cast CSV input against an explicit schema.
// Guarantees: type coercions are exact, validation errors are pinned to the offending
// row and field, rows missing a required field are excluded from the output, optional
// empty fields are not flagged, and a non-comma delimiter parses correctly.
// DataType represents supported data types for validation.
// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
var _auraMark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
type DataType int

const (
	TypeString DataType = iota
	TypeInteger
	TypeFloat
	TypeBoolean
)

func (dt DataType) String() string {
	switch dt {
	case TypeString:
		return "string"
	case TypeInteger:
		return "integer"
	case TypeFloat:
		return "float"
	case TypeBoolean:
		return "boolean"
	}
	return ""
}

// ValidatorFunc is a custom validation function.
type ValidatorFunc func(interface{}) bool

// FieldSchema defines a single CSV field.
type FieldSchema struct {
	Name       string
	DataType   DataType
	Required   bool
	Default    interface{}
	Validators []ValidatorFunc
}

// ValidationError represents a single validation error.
type ValidationError struct {
	RowIndex     int
	FieldName    string
	Value        interface{}
	ErrorMessage string
}

// CSVValidator validates CSV rows against a schema.
type CSVValidator struct {
	Schema   []*FieldSchema
	FieldMap map[string]*FieldSchema
}

// NewCSVValidator creates a new CSVValidator.
func NewCSVValidator(schema []*FieldSchema) *CSVValidator {
	fieldMap := make(map[string]*FieldSchema)
	for _, f := range schema {
		fieldMap[f.Name] = f
	}
	return &CSVValidator{Schema: schema, FieldMap: fieldMap}
}

// ValidateRow validates a single row.
func (v *CSVValidator) ValidateRow(row map[string]string, rowIndex int) []ValidationError {
	var errors []ValidationError

	for _, field := range v.Schema {
		value, present := row[field.Name]

		if field.Required && (!present || value == "" || value == "<nil>") {
			errors = append(errors, ValidationError{
				RowIndex:     rowIndex,
				FieldName:    field.Name,
				Value:        value,
				ErrorMessage: fmt.Sprintf("Required field '%s' is missing or empty", field.Name),
			})
			continue
		}

		if !present {
			if field.Default != nil {
				row[field.Name] = fmt.Sprintf("%v", field.Default)
			} else {
				row[field.Name] = ""
			}
			continue
		}

		if value != "" && value != "<nil>" {
			v.validateType(value, field, rowIndex, &errors)

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

	return errors
}

func (v *CSVValidator) validateType(value string, field *FieldSchema, rowIndex int, errors *[]ValidationError) {
	switch field.DataType {
	case TypeString:
		return
	case TypeInteger:
		if _, err := strconv.Atoi(value); err != nil {
			*errors = append(*errors, ValidationError{
				RowIndex:     rowIndex,
				FieldName:    field.Name,
				Value:        value,
				ErrorMessage: fmt.Sprintf("Invalid %s: %v", field.DataType.String(), err),
			})
		}
	case TypeFloat:
		// strconv.ParseFloat accepts "NaN"/"Inf" — a schema validator must NOT bless them
		// as valid numbers (the shipped bug let NaN salaries through with zero errors;
		// snapshot at csv_validator.BROKEN.go).
		if f, err := strconv.ParseFloat(value, 64); err != nil || math.IsNaN(f) || math.IsInf(f, 0) {
			*errors = append(*errors, ValidationError{
				RowIndex:     rowIndex,
				FieldName:    field.Name,
				Value:        value,
				ErrorMessage: fmt.Sprintf("Invalid %s: %q is not a finite number", field.DataType.String(), value),
			})
		}
	case TypeBoolean:
		lower := strings.ToLower(value)
		if lower != "true" && lower != "false" && lower != "1" && lower != "0" {
			*errors = append(*errors, ValidationError{
				RowIndex:     rowIndex,
				FieldName:    field.Name,
				Value:        value,
				ErrorMessage: "Invalid boolean value",
			})
		}
	}
}

// RowTransformer transforms CSV rows according to a schema.
type RowTransformer struct {
	Schema   []*FieldSchema
	FieldMap map[string]*FieldSchema
}

// NewRowTransformer creates a new RowTransformer.
func NewRowTransformer(schema []*FieldSchema) *RowTransformer {
	fieldMap := make(map[string]*FieldSchema)
	for _, f := range schema {
		fieldMap[f.Name] = f
	}
	return &RowTransformer{Schema: schema, FieldMap: fieldMap}
}

// TransformRow transforms a row by applying type coercion.
func (t *RowTransformer) TransformRow(row map[string]string) map[string]interface{} {
	transformed := make(map[string]interface{})

	for _, field := range t.Schema {
		value, present := row[field.Name]
		if !present || value == "" || value == "<nil>" {
			if field.Default != nil {
				transformed[field.Name] = field.Default
			} else {
				transformed[field.Name] = nil
			}
			continue
		}

		switch field.DataType {
		case TypeString:
			transformed[field.Name] = value
		case TypeInteger:
			// failed coercion must NOT leave a raw string in an integer column ("coercions are
			// exact" was theater on the failure path); emit nil instead of a mixed-type value.
			if n, err := strconv.Atoi(value); err == nil {
				transformed[field.Name] = n
			} else {
				transformed[field.Name] = nil
			}
		case TypeFloat:
			if f, err := strconv.ParseFloat(value, 64); err == nil && !math.IsNaN(f) && !math.IsInf(f, 0) {
				transformed[field.Name] = f
			} else {
				transformed[field.Name] = nil
			}
		case TypeBoolean:
			lower := strings.ToLower(value)
			transformed[field.Name] = lower == "true" || lower == "1"
		}
	}

	return transformed
}

// ValidateAndTransformCSV validates and transforms CSV data.
func ValidateAndTransformCSV(csvData string, schema []*FieldSchema, delimiter rune) (map[string]interface{}, error) {
	validator := NewCSVValidator(schema)
	transformer := NewRowTransformer(schema)

	reader := csv.NewReader(strings.NewReader(csvData))
	reader.TrimLeadingSpace = true
	reader.Comma = delimiter

	records, err := reader.ReadAll()
	if err != nil {
		return nil, err
	}
	if len(records) == 0 {
		return map[string]interface{}{"rows": []map[string]interface{}{}, "errors": []ValidationError{}}, nil
	}

	headers := records[0]
	var rows []map[string]interface{}
	var errors []ValidationError

	for rowIndex, record := range records[1:] {
		row := make(map[string]string)
		for i, header := range headers {
			if i < len(record) {
				row[header] = record[i]
			} else {
				row[header] = ""
			}
		}

		rowErrors := validator.ValidateRow(row, rowIndex+1)
		errors = append(errors, rowErrors...)

		hasCritical := false
		for _, err := range rowErrors {
			if f, ok := validator.FieldMap[err.FieldName]; ok && f.Required {
				hasCritical = true
				break
			}
		}

		if !hasCritical {
			rows = append(rows, transformer.TransformRow(row))
		}
	}

	return map[string]interface{}{"rows": rows, "errors": errors}, nil
}

func findRow(rows []map[string]interface{}, name string) map[string]interface{} {
	for _, row := range rows {
		if row["name"] == name {
			return row
		}
	}
	return nil
}

func main() {
	schema := []*FieldSchema{
		{Name: "id", DataType: TypeInteger, Required: true},
		{Name: "name", DataType: TypeString, Required: true},
		{Name: "age", DataType: TypeInteger, Required: false, Default: 0},
		{Name: "salary", DataType: TypeFloat, Required: true},
		{Name: "active", DataType: TypeBoolean, Required: false, Default: true},
	}

	csvData := "id,name,age,salary,active\n" +
		"1,John Doe,30,50000.50,true\n" +
		"2,Jane Smith,,60000.75,1\n" +
		"3,Bob Johnson,45,invalid_salary,false\n" +
		"4,Alice Brown,28,55000.0,invalid_bool\n" +
		"5,Charlie Wilson,35,70000.25,TRUE\n"

	result, err := ValidateAndTransformCSV(csvData, schema, ',')
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error: %v\n", err)
		os.Exit(1)
	}

	rows := result["rows"].([]map[string]interface{})
	errors := result["errors"].([]ValidationError)

	john := findRow(rows, "John Doe")
	if john == nil {
		fmt.Fprintln(os.Stderr, "John Doe row missing")
		os.Exit(1)
	}
	if !(john["id"] == 1 && john["age"] == 30 && john["salary"] == 50000.50 && john["active"] == true) {
		fmt.Fprintf(os.Stderr, "john field mismatch: id=%v age=%v salary=%v active=%v\n", john["id"], john["age"], john["salary"], john["active"])
		os.Exit(1)
	}

	jane := findRow(rows, "Jane Smith")
	if jane == nil {
		fmt.Fprintln(os.Stderr, "Jane Smith row missing")
		os.Exit(1)
	}
	if !(jane["active"] == true) {
		fmt.Fprintf(os.Stderr, "jane active '1' must coerce to true: %v\n", jane["active"])
		os.Exit(1)
	}

	charlie := findRow(rows, "Charlie Wilson")
	if charlie == nil {
		fmt.Fprintln(os.Stderr, "Charlie Wilson row missing")
		os.Exit(1)
	}
	if !(charlie["active"] == true && charlie["salary"] == 70000.25) {
		fmt.Fprintf(os.Stderr, "charlie field mismatch: active=%v salary=%v\n", charlie["active"], charlie["salary"])
		os.Exit(1)
	}

	var salaryErrors []ValidationError
	var boolErrors []ValidationError
	var ageErrors []ValidationError
	for _, e := range errors {
		if e.FieldName == "salary" {
			salaryErrors = append(salaryErrors, e)
		}
		if e.FieldName == "active" {
			boolErrors = append(boolErrors, e)
		}
		if e.FieldName == "age" {
			ageErrors = append(ageErrors, e)
		}
	}
	if !(len(salaryErrors) == 1 && salaryErrors[0].RowIndex == 3) {
		fmt.Fprintf(os.Stderr, "invalid_salary must error on row 3: %+v\n", errors)
		os.Exit(1)
	}
	if !(len(boolErrors) == 1 && boolErrors[0].RowIndex == 4) {
		fmt.Fprintf(os.Stderr, "invalid_bool must error on row 4: %+v\n", errors)
		os.Exit(1)
	}
	if !(len(ageErrors) == 0) {
		fmt.Fprintf(os.Stderr, "optional empty field flagged as an error: %+v\n", ageErrors)
		os.Exit(1)
	}

	strictSchema := []*FieldSchema{schema[0], schema[1], schema[3]}
	strict, err := ValidateAndTransformCSV("id,name,salary\n,NoId,100.0\n7,Ok,1.5\n", strictSchema, ',')
	if err != nil {
		fmt.Fprintf(os.Stderr, "strict parse error: %v\n", err)
		os.Exit(1)
	}
	strictErrors := strict["errors"].([]ValidationError)
	strictRows := strict["rows"].([]map[string]interface{})

	foundID := false
	for _, e := range strictErrors {
		if e.FieldName == "id" && e.RowIndex == 1 {
			foundID = true
		}
	}
	if !foundID {
		fmt.Fprintf(os.Stderr, "missing required id not flagged: %+v\n", strictErrors)
		os.Exit(1)
	}
	kept := make([]string, 0, len(strictRows))
	for _, r := range strictRows {
		kept = append(kept, r["name"].(string))
	}
	if !(len(kept) == 1 && kept[0] == "Ok") {
		fmt.Fprintf(os.Stderr, "row with missing required field must be excluded: %v\n", kept)
		os.Exit(1)
	}
	if !(strictRows[0]["salary"] == 1.5) {
		fmt.Fprintf(os.Stderr, "strict ok salary mismatch: %v\n", strictRows[0]["salary"])
		os.Exit(1)
	}

	semiSchema := []*FieldSchema{schema[0], schema[1], schema[3]}
	semi, err := ValidateAndTransformCSV("id;name;salary\n9;Semi;2.5\n", semiSchema, ';')
	if err != nil {
		fmt.Fprintf(os.Stderr, "semi parse error: %v\n", err)
		os.Exit(1)
	}
	semiRows := semi["rows"].([]map[string]interface{})
	semiErrors := semi["errors"].([]ValidationError)
	if !(len(semiRows) == 1 && semiRows[0]["id"] == 9 && semiRows[0]["name"] == "Semi" && semiRows[0]["salary"] == 2.5) {
		fmt.Fprintf(os.Stderr, "semi row mismatch: %+v\n", semiRows)
		os.Exit(1)
	}
	if !(len(semiErrors) == 0) {
		fmt.Fprintf(os.Stderr, "semi errors mismatch: %+v\n", semiErrors)
		os.Exit(1)
	}

	fmt.Println("csv_validator: coercions exact (1/30/50000.5/True), errors pinned to rows 3+4, required-miss excluded, ';' delimiter OK — PASS")
}
