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
    """Self-test: EVERY line byte-identical across buffer sizes that force
    splits mid-line (the failure this pattern exists to prevent), plus
    edge shapes: no trailing newline, empty lines, long lines."""
    import tempfile
    tmpdir = tempfile.mkdtemp(prefix="chunked_")
    path = os.path.join(tmpdir, "lines.txt")
    num_lines = 1000
    create_test_file(path, num_lines)
    truth = [f"This is line number {i+1} with some content" for i in range(num_lines)]

    # Buffer sizes chosen to split lines at awkward places (1 byte = every
    # boundary possible; 43/128 land mid-line constantly).
    for buffer_size in (1, 43, 128, 2048, 1 << 20):
        parser = LineParser(buffer_size=buffer_size)
        got = list(parser.parse_lines(path))
        assert got == truth, (
            f"buffer {buffer_size}: parsed lines differ from truth "
            f"(first divergence at line {next(i for i, (a, b) in enumerate(zip(got, truth)) if a != b) if got != truth else '?'})")
    assert len(got) == 1000

    # No trailing newline: the final partial line must still be yielded.
    path2 = os.path.join(tmpdir, "no_newline.txt")
    with open(path2, "w") as f:
        f.write("first\nsecond\nlast-without-newline")
    got = list(LineParser(buffer_size=4).parse_lines(path2))
    assert got == ["first", "second", "last-without-newline"], f"tail line lost: {got}"

    # Empty lines survive; a line longer than the buffer is reassembled whole.
    path3 = os.path.join(tmpdir, "edges.txt")
    long_line = "x" * 10_000
    with open(path3, "w") as f:
        f.write(f"\n\n{long_line}\nend\n")
    got = list(LineParser(buffer_size=64).parse_lines(path3))
    assert got == ["", "", long_line, "end"], \
        f"edge shapes broken: {[len(g) for g in got]}"
    assert len(got[2]) == 10000, "10k-char line not reassembled across ~156 chunks"

    # File objects (text mode) work too, not just paths.
    from io import StringIO
    got = list(LineParser(buffer_size=7).parse_lines(StringIO("a\nbb\nccc")))
    assert got == ["a", "bb", "ccc"]

    # Refusals.
    try:
        ChunkedReader(0)
        assert False, "buffer_size=0 accepted"
    except ValueError:
        pass
    try:
        list(ChunkedReader().read_chunks(12345))
        assert False, "non-file object accepted"
    except ValueError:
        pass

    for p in (path, path2, path3):
        os.remove(p)
    os.rmdir(tmpdir)
    print("chunked_reader: 1000 lines byte-identical at buffers 1/43/128/2048/1M, "
          "tail-without-newline kept, 10k line reassembled — PASS")


if __name__ == "__main__":
    main()