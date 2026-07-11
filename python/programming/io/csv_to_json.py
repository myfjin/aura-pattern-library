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
    """Self-test: type inference exact, nested mapping builds real structure,
    string/stream/file(x2 modes) all agree, missing file refused."""
    import tempfile
    sample_csv = """name,age,city,country,salary,is_employed,department.name,department.budget
John Doe,30,New York,USA,75000.50,true,Engineering,500000
Jane Smith,25,London,UK,65000,false,Marketing,250000
Bob Johnson,45,Sydney,Australia,85000.75,true,Sales,300000"""

    mapper = ColumnMapper()
    mapper.add_mapping('department.name', 'department.name')
    mapper.add_mapping('department.budget', 'department.budget')
    mapper.add_mapping('is_employed', 'employment.status')
    converter = CSVtoJSON(mapper)

    # String conversion: types inferred, nesting built, values exact.
    rows = json.loads(converter.convert_string(sample_csv))
    assert len(rows) == 3
    john = rows[0]
    assert john["name"] == "John Doe"
    assert john["age"] == 30 and isinstance(john["age"], int), "int not inferred"
    assert john["salary"] == 75000.50 and isinstance(john["salary"], float), "float not inferred"
    assert john["employment"]["status"] is True, "mapped bool not nested/converted"
    assert john["department"] == {"name": "Engineering", "budget": 500000}, \
        f"nested mapping wrong: {john.get('department')}"
    assert rows[1]["employment"]["status"] is False
    assert sum(r["age"] for r in rows) == 100, "ages 30+25+45 must sum to 100"
    assert sum(r["department"]["budget"] for r in rows) == 1050000

    # Stream conversion agrees with string conversion.
    from io import StringIO
    streamed = list(converter.stream_convert(StringIO(sample_csv)))
    assert streamed == rows, "stream_convert diverged from convert_string"

    # File conversion, BOTH modes, must produce the same data.
    tmpdir = tempfile.mkdtemp(prefix="csv2json_")
    csv_path = Path(tmpdir) / "in.csv"
    csv_path.write_text(sample_csv)
    for streaming in (False, True):
        out = Path(tmpdir) / f"out_{streaming}.json"
        converter.convert_file(csv_path, out, streaming=streaming)
        assert json.loads(out.read_text()) == rows, \
            f"file conversion (streaming={streaming}) diverged"

    # Unmapped converter keeps flat keys (dots stay literal).
    flat = json.loads(CSVtoJSON().convert_string("a.b,c\n1,x\n"))
    assert flat == [{"a.b": 1, "c": "x"}], f"unmapped conversion wrong: {flat}"

    # Missing input file is refused.
    try:
        converter.convert_file(Path(tmpdir) / "ghost.csv", Path(tmpdir) / "o.json")
        assert False, "missing input accepted"
    except FileNotFoundError:
        pass

    for p in Path(tmpdir).iterdir():
        p.unlink()
    Path(tmpdir).rmdir()
    print("csv_to_json: types inferred (30/75000.5/true), nesting exact, "
          "string==stream==file(x2 modes), ages sum 100 — PASS")


if __name__ == '__main__':
    main()