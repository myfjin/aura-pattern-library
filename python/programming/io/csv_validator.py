"""
CSV Validator and Transformer Module

This module provides classes for validating and transforming CSV data based on a schema.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

import csv
from typing import List, Dict, Any, Optional, Union, Callable
from dataclasses import dataclass, field
from enum import Enum
import io


class DataType(Enum):
    """Supported data types for validation."""
    STRING = "string"
    INTEGER = "integer"
    FLOAT = "float"
    BOOLEAN = "boolean"


@dataclass
class FieldSchema:
    """Schema definition for a single CSV field."""
    name: str
    data_type: DataType
    required: bool = True
    default: Optional[Any] = None
    validators: List[Callable[[Any], bool]] = field(default_factory=list)


@dataclass
class ValidationError:
    """Represents a single validation error."""
    row_index: int
    field_name: str
    value: Any
    error_message: str


class CSVValidator:
    """Validates CSV rows against a schema."""
    
    def __init__(self, schema: List[FieldSchema]):
        """
        Initialize the validator with a schema.
        
        Args:
            schema: List of FieldSchema objects defining the expected structure
        """
        self.schema = schema
        self.field_map = {field.name: field for field in schema}
    
    def validate_row(self, row: Dict[str, Any], row_index: int) -> List[ValidationError]:
        """
        Validate a single CSV row against the schema.
        
        Args:
            row: Dictionary representing a CSV row
            row_index: Index of the row (for error reporting)
            
        Returns:
            List of ValidationError objects
        """
        errors = []
        
        # Check for missing required fields. A present-but-EMPTY value is
        # missing too — csv.DictReader always supplies the key, so the old
        # `name not in row` check let required-but-blank fields through.
        for field in self.schema:
            if field.required and row.get(field.name) in (None, ""):
                errors.append(ValidationError(
                    row_index=row_index,
                    field_name=field.name,
                    value=row.get(field.name),
                    error_message=f"Required field '{field.name}' is missing or empty"
                ))
                continue
                
            # Use default value if field is missing but not required
            if field.name not in row:
                if field.default is not None:
                    row[field.name] = field.default
                else:
                    row[field.name] = None
                continue
                
            # Validate data type
            value = row[field.name]
            if value is not None and value != "":
                try:
                    self._validate_type(value, field, row_index, errors)
                except Exception as e:
                    errors.append(ValidationError(
                        row_index=row_index,
                        field_name=field.name,
                        value=value,
                        error_message=str(e)
                    ))
            
            # Run custom validators
            for validator in field.validators:
                if value is not None and not validator(value):
                    errors.append(ValidationError(
                        row_index=row_index,
                        field_name=field.name,
                        value=value,
                        error_message=f"Custom validation failed for '{field.name}'"
                    ))
        
        return errors
    
    def _validate_type(self, value: Any, field: FieldSchema, row_index: int, errors: List[ValidationError]) -> None:
        """Validate that a value matches the expected data type."""
        try:
            if field.data_type == DataType.STRING:
                # Everything can be a string
                pass
            elif field.data_type == DataType.INTEGER:
                int(value)
            elif field.data_type == DataType.FLOAT:
                float(value)
            elif field.data_type == DataType.BOOLEAN:
                if isinstance(value, str):
                    if value.lower() not in ('true', 'false', '1', '0'):
                        raise ValueError("Invalid boolean value")
                elif not isinstance(value, (bool, int)):
                    raise ValueError("Invalid boolean value")
        except (ValueError, TypeError) as e:
            errors.append(ValidationError(
                row_index=row_index,
                field_name=field.name,
                value=value,
                error_message=f"Invalid {field.data_type.value}: {str(e)}"
            ))


class RowTransformer:
    """Transforms CSV rows according to a schema."""
    
    def __init__(self, schema: List[FieldSchema]):
        """
        Initialize the transformer with a schema.
        
        Args:
            schema: List of FieldSchema objects defining transformations
        """
        self.schema = schema
        self.field_map = {field.name: field for field in schema}
    
    def transform_row(self, row: Dict[str, Any]) -> Dict[str, Any]:
        """
        Transform a CSV row by applying type coercion.
        
        Args:
            row: Dictionary representing a CSV row
            
        Returns:
            Transformed row with proper data types
        """
        transformed_row = {}
        
        for field in self.schema:
            value = row.get(field.name, field.default)
            
            if value is None or value == "":
                transformed_row[field.name] = value
                continue
            
            try:
                if field.data_type == DataType.STRING:
                    transformed_row[field.name] = str(value)
                elif field.data_type == DataType.INTEGER:
                    transformed_row[field.name] = int(value)
                elif field.data_type == DataType.FLOAT:
                    transformed_row[field.name] = float(value)
                elif field.data_type == DataType.BOOLEAN:
                    if isinstance(value, str):
                        transformed_row[field.name] = value.lower() in ('true', '1')
                    else:
                        transformed_row[field.name] = bool(value)
            except (ValueError, TypeError):
                # If conversion fails, keep original value
                transformed_row[field.name] = value
                
        return transformed_row


def validate_and_transform_csv(
    csv_data: str, 
    schema: List[FieldSchema],
    delimiter: str = ','
) -> Dict[str, Union[List[Dict[str, Any]], List[ValidationError]]]:
    """
    Validate and transform CSV data according to a schema.
    
    Args:
        csv_data: CSV data as a string
        schema: Schema to validate against
        delimiter: CSV delimiter character
        
    Returns:
        Dictionary with 'rows' and 'errors' keys
    """
    validator = CSVValidator(schema)
    transformer = RowTransformer(schema)
    
    rows = []
    errors = []
    
    # Parse CSV data
    reader = csv.DictReader(io.StringIO(csv_data), delimiter=delimiter)
    
    for row_index, row in enumerate(reader, start=1):
        # Validate row
        row_errors = validator.validate_row(row, row_index)
        errors.extend(row_errors)
        
        # Transform row if no critical errors
        if not any(error.field_name in validator.field_map and 
                  validator.field_map[error.field_name].required 
                  for error in row_errors):
            transformed_row = transformer.transform_row(row)
            rows.append(transformed_row)
    
    return {
        'rows': rows,
        'errors': errors
    }


def main():
    """Self-test: typed coercion exact, bad values produce NAMED errors on the
    RIGHT rows, clean rows survive, boolean spellings normalize."""
    schema = [
        FieldSchema("id", DataType.INTEGER, required=True),
        FieldSchema("name", DataType.STRING, required=True),
        FieldSchema("age", DataType.INTEGER, required=False, default=0),
        FieldSchema("salary", DataType.FLOAT, required=True),
        FieldSchema("active", DataType.BOOLEAN, required=False, default=True),
    ]
    csv_data = """id,name,age,salary,active
1,John Doe,30,50000.50,true
2,Jane Smith,,60000.75,1
3,Bob Johnson,45,invalid_salary,false
4,Alice Brown,28,55000.0,invalid_bool
5,Charlie Wilson,35,70000.25,TRUE"""

    result = validate_and_transform_csv(csv_data, schema)
    rows, errors = result["rows"], result["errors"]

    # Clean row 1: every coercion exact and typed.
    john = next(r for r in rows if r["name"] == "John Doe")
    assert john["id"] == 1 and isinstance(john["id"], int)
    assert john["age"] == 30
    assert john["salary"] == 50000.50 and isinstance(john["salary"], float)
    assert john["active"] is True

    # Boolean spellings: "1" and "TRUE" are true, "false" is false.
    jane = next(r for r in rows if r["name"] == "Jane Smith")
    assert jane["active"] is True, "'1' must coerce to True"
    charlie = next(r for r in rows if r["name"] == "Charlie Wilson")
    assert charlie["active"] is True, "'TRUE' must coerce to True"
    assert charlie["salary"] == 70000.25

    # THE POINT: bad values are flagged on the right row and field.
    salary_errors = [e for e in errors if e.field_name == "salary"]
    assert len(salary_errors) == 1 and salary_errors[0].row_index == 3, \
        f"invalid_salary must error on row 3: {[(e.row_index, e.field_name) for e in errors]}"
    bool_errors = [e for e in errors if e.field_name == "active"]
    assert len(bool_errors) == 1 and bool_errors[0].row_index == 4, \
        "invalid_bool must error on row 4"

    # Missing optional value (Jane's age) is not an error.
    assert not any(e.field_name == "age" for e in errors), \
        "optional empty field flagged as an error"

    # A missing REQUIRED field errors AND excludes the row.
    strict = validate_and_transform_csv("id,name,salary\n,NoId,100.0\n7,Ok,1.5\n", schema[:2] + [schema[3]])
    assert any(e.field_name == "id" and e.row_index == 1 for e in strict["errors"]), \
        "missing required id not flagged"
    kept = [r["name"] for r in strict["rows"]]
    assert kept == ["Ok"], f"row with missing required field must be excluded: {kept}"
    assert strict["rows"][0]["salary"] == 1.5

    # Alternate delimiter works.
    semi = validate_and_transform_csv("id;name;salary\n9;Semi;2.5\n",
                                      [schema[0], schema[1], schema[3]], delimiter=";")
    assert semi["rows"][0] == {"id": 9, "name": "Semi", "salary": 2.5}
    assert semi["errors"] == []

    print("csv_validator: coercions exact (1/30/50000.5/True), errors pinned to "
          "rows 3+4, required-miss excluded, ';' delimiter OK — PASS")


if __name__ == "__main__":
    main()