#!/usr/bin/env python3
"""
Line-delimited file parser with chunked reads.

This module provides classes for efficiently reading and parsing large files
by reading them in chunks and processing line by line, handling partial lines
across chunk boundaries correctly.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

import os
from typing import Iterator, Optional, TextIO, Union
from io import StringIO


class ChunkedReader:
    """Reads files in chunks with configurable buffer size."""
    
    def __init__(self, buffer_size: int = 8192) -> None:
        """
        Initialize the ChunkedReader.
        
        Args:
            buffer_size: Size of buffer for each read operation in bytes.
        """
        if buffer_size <= 0:
            raise ValueError("Buffer size must be positive")
        self.buffer_size = buffer_size
    
    def read_chunks(self, file_obj: Union[str, TextIO]) -> Iterator[bytes]:
        """
        Read file in chunks.
        
        Args:
            file_obj: File path or file object to read from.
            
        Yields:
            Bytes from the file in chunks.
            
        Raises:
            IOError: If file cannot be opened or read.
            ValueError: If file_obj is neither a string nor file object.
        """
        if isinstance(file_obj, str):
            with open(file_obj, 'rb') as f:
                while True:
                    chunk = f.read(self.buffer_size)
                    if not chunk:
                        break
                    yield chunk
        elif hasattr(file_obj, 'read') and callable(file_obj.read):
            while True:
                chunk = file_obj.read(self.buffer_size)
                if not chunk:
                    break
                # Handle text files by encoding to bytes
                if isinstance(chunk, str):
                    chunk = chunk.encode('utf-8')
                yield chunk
        else:
            raise ValueError("file_obj must be a file path or file object")


class LineParser:
    """Parses lines from chunked file reads, handling partial lines correctly."""
    
    def __init__(self, buffer_size: int = 8192) -> None:
        """
        Initialize the LineParser.
        
        Args:
            buffer_size: Size of buffer for each read operation in bytes.
        """
        self.chunked_reader = ChunkedReader(buffer_size)
        self._remainder = b""
    
    def parse_lines(self, file_obj: Union[str, TextIO]) -> Iterator[str]:
        """
        Parse lines from a file object or file path.
        
        Args:
            file_obj: File path or file object to parse.
            
        Yields:
            Complete lines from the file.
            
        Raises:
            IOError: If file cannot be opened or read.
        """
        self._remainder = b""  # Reset remainder for new parsing
        
        try:
            for chunk in self.chunked_reader.read_chunks(file_obj):
                # Combine remainder from previous chunk with current chunk
                data = self._remainder + chunk
                
                # Split by lines but keep track of incomplete line at the end
                lines = data.split(b'\n')
                
                # All but the last element are complete lines
                for line in lines[:-1]:
                    yield line.decode('utf-8', errors='replace')
                
                # The last element might be incomplete, save it for next chunk
                self._remainder = lines[-1]
            
            # Yield the final line if there's a remainder
            if self._remainder:
                yield self._remainder.decode('utf-8', errors='replace')
        except Exception as e:
            raise IOError(f"Error parsing lines: {e}") from e


def create_test_file(filename: str, num_lines: int) -> None:
    """
    Create a test file with specified number of lines.
    
    Args:
        filename: Name of file to create.
        num_lines: Number of lines to write.
    """
    with open(filename, 'w') as f:
        for i in range(num_lines):
            f.write(f"This is line number {i+1} with some content\n")


def main() -> None:
    """Demo the line parser with a generated test file."""
    test_filename = "test_lines.txt"
    num_lines = 1000
    
    # Create test file
    print(f"Creating test file with {num_lines} lines...")
    create_test_file(test_filename, num_lines)
    
    # Parse with different buffer sizes
    for buffer_size in [128, 512, 2048]:
        print(f"\nParsing with buffer size: {buffer_size}")
        parser = LineParser(buffer_size=buffer_size)
        
        line_count = 0
        try:
            for i, line in enumerate(parser.parse_lines(test_filename)):
                line_count += 1
                # Validate first and last few lines
                if i < 3 or i >= num_lines - 3:
                    expected = f"This is line number {i+1} with some content"
                    if line != expected:
                        print(f"ERROR: Line {i+1} mismatch!")
                        print(f"  Expected: {expected}")
                        print(f"  Got:      {line}")
                        break
                # Limit output for readability
                if i < 5:
                    print(f"  Line {i+1}: {line}")
                elif i == 5:
                    print("  ...")
                elif i >= num_lines - 3:
                    print(f"  Line {i+1}: {line}")
            
            if line_count == num_lines:
                print(f"SUCCESS: Parsed {line_count} lines correctly")
            else:
                print(f"ERROR: Expected {num_lines} lines, got {line_count}")
                
        except Exception as e:
            print(f"ERROR: {e}")
    
    # Clean up test file
    try:
        os.remove(test_filename)
        print(f"\nCleaned up test file: {test_filename}")
    except OSError:
        pass


if __name__ == "__main__":
    main()