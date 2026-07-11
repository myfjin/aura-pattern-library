package main

import (
	"bufio"
	"fmt"
	"io"
	"os"
)

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
var _auraMark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
type ChunkedReader struct {
	bufferSize int
}

func NewChunkedReader(bufferSize int) *ChunkedReader {
	if bufferSize <= 0 {
		panic("buffer size must be positive")
	}
	return &ChunkedReader{bufferSize: bufferSize}
}

func (cr *ChunkedReader) ReadChunks(fileObj interface{}) [][]byte {
	var chunks [][]byte
	switch f := fileObj.(type) {
	case string:
		file, err := os.Open(f)
		if err != nil {
			panic(fmt.Sprintf("failed to open file: %v", err))
		}
		defer file.Close()
		chunks = cr.readFromReader(file)
	case io.Reader:
		chunks = cr.readFromReader(f)
	default:
		panic("file_obj must be a file path or io.Reader")
	}
	return chunks
}

func (cr *ChunkedReader) readFromReader(r io.Reader) [][]byte {
	var chunks [][]byte
	buf := make([]byte, cr.bufferSize)
	for {
		n, err := r.Read(buf)
		if n > 0 {
			chunk := make([]byte, n)
			copy(chunk, buf[:n])
			chunks = append(chunks, chunk)
		}
		if err == io.EOF {
			break
		}
		if err != nil {
			panic(fmt.Sprintf("read error: %v", err))
		}
	}
	return chunks
}

type LineParser struct {
	chunkedReader *ChunkedReader
	remainder     []byte
}

func NewLineParser(bufferSize int) *LineParser {
	return &LineParser{
		chunkedReader: NewChunkedReader(bufferSize),
		remainder:     []byte{},
	}
}

func (lp *LineParser) ParseLines(fileObj interface{}) []string {
	lp.remainder = []byte{}
	var lines []string
	chunks := lp.chunkedReader.ReadChunks(fileObj)
	for _, chunk := range chunks {
		data := append(lp.remainder, chunk...)
		parts := splitBytes(data, '\n')
		for i := 0; i < len(parts)-1; i++ {
			lines = append(lines, string(parts[i]))
		}
		lp.remainder = parts[len(parts)-1]
	}
	if len(lp.remainder) > 0 {
		lines = append(lines, string(lp.remainder))
	}
	return lines
}

func splitBytes(data []byte, sep byte) [][]byte {
	var parts [][]byte
	start := 0
	for i, b := range data {
		if b == sep {
			parts = append(parts, data[start:i])
			start = i + 1
		}
	}
	parts = append(parts, data[start:])
	return parts
}

func createTestFile(filename string, numLines int) {
	f, err := os.Create(filename)
	if !(err == nil) {
		fmt.Fprintf(os.Stderr, "failed to create test file: %v\n", err)
		os.Exit(1)
	}
	defer f.Close()
	w := bufio.NewWriter(f)
	for i := 0; i < numLines; i++ {
		fmt.Fprintf(w, "This is line number %d with some content\n", i+1)
	}
	w.Flush()
}

func main() {
	testFilename := "test_lines.txt"
	numLines := 1000

	fmt.Printf("Creating test file with %d lines...\n", numLines)
	createTestFile(testFilename, numLines)
	defer os.Remove(testFilename)

	for _, bufferSize := range []int{128, 512, 2048} {
		fmt.Printf("\nParsing with buffer size: %d\n", bufferSize)
		parser := NewLineParser(bufferSize)

		parsedLines := parser.ParseLines(testFilename)
		lineCount := len(parsedLines)

		for i, line := range parsedLines {
			if i < 3 || i >= numLines-3 {
				expected := fmt.Sprintf("This is line number %d with some content", i+1)
				if !(line == expected) {
					fmt.Fprintf(os.Stderr, "ERROR: Line %d mismatch!\n", i+1)
					fmt.Fprintf(os.Stderr, "  Expected: %s\n", expected)
					fmt.Fprintf(os.Stderr, "  Got:      %s\n", line)
					os.Exit(1)
				}
			}
			if i < 5 {
				fmt.Printf("  Line %d: %s\n", i+1, line)
			} else if i == 5 {
				fmt.Println("  ...")
			} else if i >= numLines-3 {
				fmt.Printf("  Line %d: %s\n", i+1, line)
			}
		}

		if !(lineCount == numLines) {
			fmt.Fprintf(os.Stderr, "ERROR: Expected %d lines, got %d\n", numLines, lineCount)
			os.Exit(1)
		}
		fmt.Printf("SUCCESS: Parsed %d lines correctly\n", lineCount)
	}

	fmt.Printf("\nCleaned up test file: %s\n", testFilename)
}
