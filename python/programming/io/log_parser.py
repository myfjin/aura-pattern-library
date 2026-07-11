"""
JSON Schema Validator Module

This module provides a lightweight JSON schema validator that supports:
- Type checking
- Required fields
- Nested object validation
- Custom validation errors
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

from typing import Any, Dict, List, Union, Optional
import json


class ValidationError(Exception):
    """Custom exception for validation errors."""
    
    def __init__(self, message: str, path: str = ""):
        super().__init__(message)
        self.message = message
        self.path = path
    
    def __str__(self):
        if self.path:
            return f"{self.path}: {self.message}"
        return self.message


class SchemaValidator:
    """JSON Schema Validator class."""
    
    def __init__(self, schema: Dict[str, Any]):
        """
        Initialize the validator with a schema.
        
        Args:
            schema: Dictionary defining the validation schema
        """
        self.schema = schema
    
    def validate(self, data: Any) -> bool:
        """
        Validate data against the schema.
        
        Args:
            data: Data to validate
            
        Returns:
            True if valid
            
        Raises:
            ValidationError: If validation fails
        """
        self._validate_value(data, self.schema, "")
        return True
    
    def _validate_value(self, value: Any, schema: Dict[str, Any], path: str) -> None:
        """Validate a value against a schema definition."""
        # Type validation
        if "type" in schema:
            expected_type = schema["type"]
            if not self._check_type(value, expected_type):
                raise ValidationError(
                    f"Expected type '{expected_type}', got '{type(value).__name__}'",
                    path
                )
        
        # Required fields validation for objects
        if isinstance(value, dict) and "properties" in schema:
            self._validate_object(value, schema, path)
        
        # Array validation
        if isinstance(value, list) and "items" in schema:
            self._validate_array(value, schema, path)
        
        # Enum validation
        if "enum" in schema and value not in schema["enum"]:
            raise ValidationError(
                f"Value '{value}' is not in allowed values {schema['enum']}",
                path
            )
        
        # Minimum/maximum validation for numbers
        if isinstance(value, (int, float)):
            if "minimum" in schema and value < schema["minimum"]:
                raise ValidationError(
                    f"Value {value} is less than minimum {schema['minimum']}",
                    path
                )
            if "maximum" in schema and value > schema["maximum"]:
                raise ValidationError(
                    f"Value {value} is greater than maximum {schema['maximum']}",
                    path
                )
        
        # String length validation
        if isinstance(value, str):
            if "minLength" in schema and len(value) < schema["minLength"]:
                raise ValidationError(
                    f"String length {len(value)} is less than minimum {schema['minLength']}",
                    path
                )
            if "maxLength" in schema and len(value) > schema["maxLength"]:
                raise ValidationError(
                    f"String length {len(value)} is greater than maximum {schema['maxLength']}",
                    path
                )
    
    def _check_type(self, value: Any, expected_type: str) -> bool:
        """Check if value matches expected type."""
        type_mapping = {
            "string": str,
            "number": (int, float),
            "integer": int,
            "boolean": bool,
            "object": dict,
            "array": list,
            "null": type(None)
        }
        
        if expected_type not in type_mapping:
            raise ValidationError(f"Unknown type '{expected_type}'")
        
        expected_python_type = type_mapping[expected_type]
        if isinstance(expected_python_type, tuple):
            return isinstance(value, expected_python_type)
        return isinstance(value, expected_python_type)
    
    def _validate_object(self, obj: Dict[str, Any], schema: Dict[str, Any], path: str) -> None:
        """Validate object properties."""
        properties = schema.get("properties", {})
        required = schema.get("required", [])
        
        # Check required fields
        for field in required:
            if field not in obj:
                raise ValidationError(f"Required field '{field}' is missing", path)
        
        # Validate each property
        for key, value in obj.items():
            if key in properties:
                property_path = f"{path}.{key}" if path else key
                self._validate_value(value, properties[key], property_path)
            elif schema.get("additionalProperties", True) is False:
                raise ValidationError(f"Additional property '{key}' not allowed", path)
    
    def _validate_array(self, arr: List[Any], schema: Dict[str, Any], path: str) -> None:
        """Validate array items."""
        items_schema = schema["items"]
        for i, item in enumerate(arr):
            item_path = f"{path}[{i}]"
            self._validate_value(item, items_schema, item_path)


def main():
    """Demo of the JSON Schema Validator."""
    
    # Define a schema
    user_schema = {
        "type": "object",
        "properties": {
            "name": {
                "type": "string",
                "minLength": 1,
                "maxLength": 50
            },
            "age": {
                "type": "integer",
                "minimum": 0,
                "maximum": 150
            },
            "email": {
                "type": "string"
            },
            "address": {
                "type": "object",
                "properties": {
                    "street": {"type": "string"},
                    "city": {"type": "string"}
                },
                "required": ["street", "city"]
            },
            "tags": {
                "type": "array",
                "items": {
                    "type": "string"
                }
            }
        },
        "required": ["name", "age"]
    }
    
    # Create validator
    validator = SchemaValidator(user_schema)
    
    # Test cases
    test_cases = [
        # Valid case
        {
            "name": "John Doe",
            "age": 30,
            "email": "john@example.com",
            "address": {
                "street": "123 Main St",
                "city": "Anytown"
            },
            "tags": ["developer", "python"]
        },
        # Invalid: missing required field
        {
            "age": 25
        },
        # Invalid: wrong type
        {
            "name": "Jane",
            "age": "thirty"
        },
        # Invalid: age out of range
        {
            "name": "Bob",
            "age": -5
        },
        # Invalid: nested object missing required field
        {
            "name": "Alice",
            "age": 28,
            "address": {
                "street": "456 Oak Ave"
                # missing "city"
            }
        }
    ]
    
    # Self-test: the valid document passes; every planted violation is
    # REFUSED with the offending field named in the error.
    validator.validate(test_cases[0])  # must not raise

    failing = [
        (test_cases[1], "name"),       # missing required field
        (test_cases[2], "age"),        # wrong type (string for integer)
        (test_cases[3], "age"),        # below minimum
        (test_cases[4], "city"),       # nested required missing
    ]
    caught = 0
    for data, field in failing:
        try:
            validator.validate(data)
            assert False, f"invalid document accepted (expected {field} violation): {data}"
        except ValidationError as e:
            assert field in str(e), f"error must name {field!r}, said: {e}"
            caught += 1
    assert caught == 4, f"all 4 planted violations must be caught, got {caught}"

    # Bounds are inclusive: 0 and 150 pass, 151 fails.
    validator.validate({"name": "Edge", "age": 0})
    validator.validate({"name": "Edge", "age": 150})
    try:
        validator.validate({"name": "Edge", "age": 151})
        assert False, "age above maximum accepted"
    except ValidationError:
        pass

    # String length limits.
    try:
        validator.validate({"name": "", "age": 5})
        assert False, "empty name accepted below minLength"
    except ValidationError:
        pass
    try:
        validator.validate({"name": "x" * 51, "age": 5})
        assert False, "51-char name accepted above maxLength"
    except ValidationError:
        pass

    # Array items are validated element-wise, with the index in the path.
    try:
        validator.validate({"name": "T", "age": 1, "tags": ["ok", 7]})
        assert False, "non-string array element accepted"
    except ValidationError as e:
        assert "[1]" in str(e), f"error must point at element [1], said: {e}"

    # Enum membership.
    enum_validator = SchemaValidator({
        "type": "object",
        "properties": {"status": {"type": "string",
                                  "enum": ["active", "inactive", "pending"]}}})
    enum_validator.validate({"status": "active"})
    try:
        enum_validator.validate({"status": "deleted"})
        assert False, "value outside enum accepted"
    except ValidationError:
        pass

    print("log_parser (json-schema validator): valid doc passed, 4 planted "
          "violations named, bounds inclusive 0..150, tags[1] pinned — PASS")


if __name__ == "__main__":
    main()