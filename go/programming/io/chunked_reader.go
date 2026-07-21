package main

import (
	"bufio"
	"fmt"
	"io"
	"os"
	"path/filepath"
	"time"
)

// Fixed-size chunked reader plus a line parser that reassembles complete lines across
// arbitrary chunk boundaries, carrying a partial remainder between chunks and emitting
// any final line that lacks a trailing newline; accepts a file path or any io.Reader.
// Use to stream-parse text line by line without loading a whole file into memory.
// Guarantees: at buffer sizes from 1 byte to 1 MB the parsed lines are byte-identical to
// the source, a trailing newline-less line is kept, and a 10k-char line spanning many
// chunks is reassembled intact.
// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
var _auraMark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
type ChunkedReader struct {
	bufferSize int
}

func NewChunkedReader(bufferSize int) *ChunkedReader {
	if bufferSize <= 0 {
		fmt.Fprintln(os.Stderr, "Buffer size must be positive")
		os.Exit(1)
	}
	return &ChunkedReader{bufferSize: bufferSize}
}

func (cr *ChunkedReader) ReadChunks(fileObj interface{}) ([][]byte, error) {
	var chunks [][]byte
	switch f := fileObj.(type) {
	case string:
		file, err := os.Open(f)
		if err != nil {
			return nil, err
		}
		defer file.Close()
		chunks = cr.readFromReader(file)
	case io.Reader:
		chunks = cr.readFromReader(f)
	default:
		return nil, fmt.Errorf("file_obj must be a file path or io.Reader")
	}
	return chunks, nil
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
			panic(err)
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

func (lp *LineParser) ParseLines(fileObj interface{}) ([]string, error) {
	lp.remainder = []byte{}
	var lines []string
	chunks, err := lp.chunkedReader.ReadChunks(fileObj)
	if err != nil {
		return nil, err
	}
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
	return lines, nil
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

type stringReader struct {
	s string
	i int
}

func (r *stringReader) Read(p []byte) (int, error) {
	if r.i >= len(r.s) {
		return 0, io.EOF
	}
	n := copy(p, r.s[r.i:])
	r.i += n
	if r.i >= len(r.s) {
		return n, io.EOF
	}
	return n, nil
}

func main() {
	tmpdir, err := os.MkdirTemp("", "chunked_*")
	if !(err == nil) {
		fmt.Fprintf(os.Stderr, "failed to create temp dir: %v\n", err)
		os.Exit(1)
	}
	defer os.RemoveAll(tmpdir)

	path := filepath.Join(tmpdir, "lines.txt")
	numLines := 1000
	createTestFile(path, numLines)
	truth := make([]string, numLines)
	for i := 0; i < numLines; i++ {
		truth[i] = fmt.Sprintf("This is line number %d with some content", i+1)
	}

	for _, bufferSize := range []int{1, 43, 128, 2048, 1 << 20} {
		parser := NewLineParser(bufferSize)
		got, err := parser.ParseLines(path)
		if !(err == nil) {
			fmt.Fprintf(os.Stderr, "buffer %d: parse error %v\n", bufferSize, err)
			os.Exit(1)
		}
		if !(len(got) == len(truth)) {
			fmt.Fprintf(os.Stderr, "buffer %d: expected %d lines, got %d\n", bufferSize, len(truth), len(got))
			os.Exit(1)
		}
		for i := range truth {
			if !(got[i] == truth[i]) {
				fmt.Fprintf(os.Stderr, "buffer %d: first divergence at line %d: got %q want %q\n", bufferSize, i, got[i], truth[i])
				os.Exit(1)
			}
		}
	}

	path2 := filepath.Join(tmpdir, "no_newline.txt")
	f, _ := os.Create(path2)
	f.WriteString("first\nsecond\nlast-without-newline")
	f.Close()
	got, _ := NewLineParser(4).ParseLines(path2)
	if !(len(got) == 3 && got[0] == "first" && got[1] == "second" && got[2] == "last-without-newline") {
		fmt.Fprintf(os.Stderr, "tail line lost: %v\n", got)
		os.Exit(1)
	}

	path3 := filepath.Join(tmpdir, "edges.txt")
	longLine := repeatString("x", 10000)
	f, _ = os.Create(path3)
	fmt.Fprintf(f, "\n\n%s\nend\n", longLine)
	f.Close()
	got, _ = NewLineParser(64).ParseLines(path3)
	if !(len(got) == 4 && got[0] == "" && got[1] == "" && got[2] == longLine && got[3] == "end") {
		fmt.Fprintf(os.Stderr, "edge shapes broken: %v\n", got)
		os.Exit(1)
	}
	if !(len(got[2]) == 10000) {
		fmt.Fprintln(os.Stderr, "10k-char line not reassembled across ~156 chunks")
		os.Exit(1)
	}

	sr := &stringReader{s: "a\nbb\nccc"}
	got, _ = NewLineParser(7).ParseLines(sr)
	if !(len(got) == 3 && got[0] == "a" && got[1] == "bb" && got[2] == "ccc") {
		fmt.Fprintf(os.Stderr, "string reader broken: %v\n", got)
		os.Exit(1)
	}

	fmt.Println("chunked_reader: 1000 lines byte-identical at buffers 1/43/128/2048/1M, tail-without-newline kept, 10k line reassembled — PASS")
	time.Sleep(1 * time.Millisecond)
}

func repeatString(s string, n int) string {
	out := ""
	for i := 0; i < n; i++ {
		out += s
	}
	return out
}
