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
    
    print("JSON Schema Validator Demo")
    print("=" * 30)
    
    for i, test_data in enumerate(test_cases):
        print(f"\nTest case {i+1}:")
        print(f"Data: {json.dumps(test_data, indent=2)}")
        
        try:
            validator.validate(test_data)
            print("✓ Valid")
        except ValidationError as e:
            print(f"✗ Invalid: {e}")
    
    # Additional test with enum
    enum_schema = {
        "type": "object",
        "properties": {
            "status": {
                "type": "string",
                "enum": ["active", "inactive", "pending"]
            }
        }
    }
    
    enum_validator = SchemaValidator(enum_schema)
    
    print("\nEnum validation test:")
    try:
        enum_validator.validate({"status": "active"})
        print("✓ Valid enum value")
    except ValidationError as e:
        print(f"✗ {e}")
    
    try:
        enum_validator.validate({"status": "deleted"})
        print("✓ Valid enum value")
    except ValidationError as e:
        print(f"✗ Invalid enum value: {e}")


if __name__ == "__main__":
    main()