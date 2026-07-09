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
        
        # Check for missing required fields
        for field in self.schema:
            if field.required and field.name not in row:
                errors.append(ValidationError(
                    row_index=row_index,
                    field_name=field.name,
                    value=None,
                    error_message=f"Required field '{field.name}' is missing"
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
    """Demo of CSV validator and transformer."""
    # Define schema
    schema = [
        FieldSchema("id", DataType.INTEGER, required=True),
        FieldSchema("name", DataType.STRING, required=True),
        FieldSchema("age", DataType.INTEGER, required=False, default=0),
        FieldSchema("salary", DataType.FLOAT, required=True),
        FieldSchema("active", DataType.BOOLEAN, required=False, default=True),
    ]
    
    # Sample CSV data
    csv_data = """id,name,age,salary,active
1,John Doe,30,50000.50,true
2,Jane Smith,,60000.75,1
3,Bob Johnson,45,invalid_salary,false
4,Alice Brown,28,55000.0,invalid_bool
5,Charlie Wilson,35,70000.25,TRUE"""
    
    # Validate and transform
    result = validate_and_transform_csv(csv_data, schema)
    
    # Print results
    print("Transformed Rows:")
    for i, row in enumerate(result['rows'], start=1):
        print(f"  Row {i}: {row}")
    
    print("\nValidation Errors:")
    for error in result['errors']:
        print(f"  Row {error.row_index}, Field '{error.field_name}': {error.error_message}")


if __name__ == "__main__":
    main()