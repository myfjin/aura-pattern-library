#!/usr/bin/env python3
"""
CSV to JSON converter module with type inference, nested key support, and streaming.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

import csv
import json
import sys
from typing import Dict, List, Any, Union, Optional, TextIO, Iterator
from pathlib import Path


class ColumnMapper:
    """Maps CSV column names to nested JSON key paths."""
    
    def __init__(self):
        self._mapping: Dict[str, List[str]] = {}
    
    def add_mapping(self, csv_column: str, json_path: str) -> None:
        """
        Add a mapping from CSV column to JSON nested path.
        
        Args:
            csv_column: Name of the CSV column
            json_path: Dot-separated path for nested JSON (e.g., 'user.profile.name')
        """
        self._mapping[csv_column] = json_path.split('.')
    
    def get_path(self, csv_column: str) -> Optional[List[str]]:
        """
        Get the JSON path for a CSV column.
        
        Args:
            csv_column: Name of the CSV column
            
        Returns:
            List of path components or None if not mapped
        """
        return self._mapping.get(csv_column)
    
    def get_mappings(self) -> Dict[str, str]:
        """
        Get all mappings as CSV column to JSON path strings.
        
        Returns:
            Dictionary of mappings
        """
        return {k: '.'.join(v) for k, v in self._mapping.items()}


class TypeInferer:
    """Infers and converts data types from string values."""
    
    @staticmethod
    def infer_and_convert(value: str) -> Any:
        """
        Infer and convert string value to appropriate Python type.
        
        Args:
            value: String value to convert
            
        Returns:
            Converted value (int, float, bool, None, or str)
        """
        if not isinstance(value, str):
            return value
            
        # Handle empty values
        if value == '' or value.lower() in ('null', 'none'):
            return None
            
        # Handle booleans
        if value.lower() in ('true', 'false'):
            return value.lower() == 'true'
            
        # Handle integers
        try:
            if '.' not in value and 'e' not in value.lower():
                return int(value)
        except ValueError:
            pass
            
        # Handle floats
        try:
            return float(value)
        except ValueError:
            pass
            
        # Return as string if no other type matches
        return value


class CSVtoJSON:
    """Converts CSV data to JSON with support for nested structures and streaming."""
    
    def __init__(self, column_mapper: Optional[ColumnMapper] = None):
        """
        Initialize converter.
        
        Args:
            column_mapper: Optional ColumnMapper for custom field mappings
        """
        self.column_mapper = column_mapper or ColumnMapper()
        self.type_inferer = TypeInferer()
    
    def _set_nested_value(self, obj: Dict[str, Any], path: List[str], value: Any) -> None:
        """
        Set a nested value in a dictionary using a path.
        
        Args:
            obj: Dictionary to modify
            path: List of keys representing the path
            value: Value to set
        """
        current = obj
        for key in path[:-1]:
            if key not in current:
                current[key] = {}
            current = current[key]
        current[path[-1]] = value
    
    def _process_row(self, row: Dict[str, str]) -> Dict[str, Any]:
        """
        Process a single CSV row into a JSON object.
        
        Args:
            row: Dictionary representing a CSV row
            
        Returns:
            Processed JSON object
        """
        result: Dict[str, Any] = {}
        
        for column_name, value in row.items():
            # Get the JSON path for this column
            path = self.column_mapper.get_path(column_name)
            if path is None:
                # Use column name directly if not mapped
                path = [column_name]
            
            # Convert value type
            converted_value = self.type_inferer.infer_and_convert(value)
            
            # Set nested value
            self._set_nested_value(result, path, converted_value)
        
        return result
    
    def convert_file(self, input_path: Union[str, Path], 
                     output_path: Union[str, Path],
                     streaming: bool = False) -> None:
        """
        Convert CSV file to JSON file.
        
        Args:
            input_path: Path to input CSV file
            output_path: Path to output JSON file
            streaming: Whether to process one row at a time (for large files)
        """
        input_path = Path(input_path)
        output_path = Path(output_path)
        
        if not input_path.exists():
            raise FileNotFoundError(f"Input file not found: {input_path}")
        
        if streaming:
            self._convert_streaming(input_path, output_path)
        else:
            self._convert_in_memory(input_path, output_path)
    
    def _convert_in_memory(self, input_path: Path, output_path: Path) -> None:
        """Convert CSV to JSON by loading all data into memory."""
        with open(input_path, 'r', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            data = [self._process_row(row) for row in reader]
        
        with open(output_path, 'w', encoding='utf-8') as jsonfile:
            json.dump(data, jsonfile, indent=2)
    
    def _convert_streaming(self, input_path: Path, output_path: Path) -> None:
        """Convert CSV to JSON using streaming for memory efficiency."""
        with open(input_path, 'r', newline='', encoding='utf-8') as csvfile, \
             open(output_path, 'w', encoding='utf-8') as jsonfile:
            
            reader = csv.DictReader(csvfile)
            jsonfile.write('[\n')
            
            first = True
            for row in reader:
                if not first:
                    jsonfile.write(',\n')
                else:
                    first = False
                
                processed_row = self._process_row(row)
                jsonfile.write(json.dumps(processed_row, separators=(',', ':')))
            
            jsonfile.write('\n]')
    
    def convert_string(self, csv_content: str) -> str:
        """
        Convert CSV content string to JSON string.
        
        Args:
            csv_content: CSV content as string
            
        Returns:
            JSON content as string
        """
        lines = csv_content.strip().split('\n')
        if not lines:
            return '[]'
        
        reader = csv.DictReader(lines)
        data = [self._process_row(row) for row in reader]
        return json.dumps(data, indent=2)
    
    def stream_convert(self, input_file: TextIO) -> Iterator[Dict[str, Any]]:
        """
        Stream convert CSV rows to JSON objects.
        
        Args:
            input_file: File-like object with CSV content
            
        Yields:
            Processed JSON objects
        """
        reader = csv.DictReader(input_file)
        for row in reader:
            yield self._process_row(row)


def main():
    """Demo the CSV to JSON converter functionality."""
    # Create sample CSV data
    sample_csv = """name,age,city,country,salary,is_employed,department.name,department.budget
John Doe,30,New York,USA,75000.50,true,Engineering,500000
Jane Smith,25,London,UK,65000,false,Marketing,250000
Bob Johnson,45,Sydney,Australia,85000.75,true,Sales,300000"""
    
    # Create column mapper for nested structure
    mapper = ColumnMapper()
    mapper.add_mapping('department.name', 'department.name')
    mapper.add_mapping('department.budget', 'department.budget')
    mapper.add_mapping('is_employed', 'employment.status')
    
    # Initialize converter
    converter = CSVtoJSON(mapper)
    
    # Demo 1: Convert string content
    print("Demo 1: String conversion")
    json_result = converter.convert_string(sample_csv)
    print(json_result[:200] + "..." if len(json_result) > 200 else json_result)
    print()
    
    # Demo 2: Stream conversion
    print("Demo 2: Stream conversion")
    from io import StringIO
    csv_io = StringIO(sample_csv)
    next(csv_io)  # Skip header for stream demo
    csv_io.seek(0)
    
    stream_results = list(converter.stream_convert(csv_io))
    print(f"Processed {len(stream_results)} records:")
    for i, record in enumerate(stream_results):
        print(f"  Record {i+1}: {record}")
        if i >= 2:  # Limit output
            break
    print()
    
    # Demo 3: File conversion (in-memory)
    print("Demo 3: File conversion")
    # Create temporary CSV file
    with open('demo.csv', 'w') as f:
        f.write(sample_csv)
    
    # Convert file
    converter.convert_file('demo.csv', 'demo.json', streaming=False)
    
    # Read and display result
    with open('demo.json', 'r') as f:
        file_result = f.read()
    print(file_result[:200] + "..." if len(file_result) > 200 else file_result)
    
    # Cleanup
    Path('demo.csv').unlink(missing_ok=True)
    Path('demo.json').unlink(missing_ok=True)
    
    print("\nAll demos completed successfully!")


if __name__ == '__main__':
    main()