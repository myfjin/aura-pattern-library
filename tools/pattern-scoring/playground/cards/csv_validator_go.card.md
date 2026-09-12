# CARD: csv_validator (GO batch 1 — compact format)
FILE: go/programming/io/csv_validator.go
BASELINE (verified 2026-07-21): csv_validator ... PASS
ENTRY: ValidateAndTransformCSV(csvData, schema, delimiter) · line 215 · demo line 273
RUN: `cd playground/go && go run programming/io/csv_validator.go`
PASTES: compile-verified in scratch 2026-07-21 — every attack runs and lands as predicted.
RESET: `git checkout pristine-full -- programming/io/csv_validator.go`
CLAIM UNDER TEST: "type coercions are EXACT, validation errors pinned to row+field"

PASTE-ATTACKS — one at a time, just above the final print (line 404).
`strictSchema` (id/name/salary) and `schema` are both in scope there.
1. ```go
	nanRes, _ := ValidateAndTransformCSV("id,name,salary\n9,NaNGuy,NaN\n", strictSchema, ',')
	fmt.Println("NaN salary:", nanRes["rows"], "errors:", nanRes["errors"])
   ```
   E008 — strconv.ParseFloat("NaN") SUCCEEDS in go. My prediction: zero validation
   errors, row kept, salary=NaN flows downstream as a "validated float". Same for "Inf".
2. ```go
	mixRes, _ := ValidateAndTransformCSV("id,name,age,salary,active\n6,Mix,abc,1.0,true\n", schema, ',')
	fmt.Println("bad optional:", mixRes["rows"], "errors:", mixRes["errors"])
   ```
   the coercion-exactness lie — age="abc" on an OPTIONAL integer field: error IS
   recorded, but the row is still kept and TransformRow line 197 falls back to the RAW
   STRING → the "integer" column now holds "abc". "Coercions are exact" = theater when
   validation fails: mixed-type column emitted with full confidence.
3. ```go
	nilRes, _ := ValidateAndTransformCSV("id,name,salary\n8,<nil>,3.5\n", strictSchema, ',')
	fmt.Println("literal <nil>:", nilRes["rows"], "errors:", nilRes["errors"])
   ```
   sentinel collision — the string "<nil>" is treated as MISSING (lines 87/106/181).
   A legal string value (common in exports from other tools) silently vanishes; here
   name is required → whole row EXCLUDED. Data loss keyed on a magic string.

FREE-PLAY: your garbage after mine — duplicate headers ("id,id,name") and huge ints
("99999999999999999999") are untouched territory.
