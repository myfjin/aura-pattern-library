package main

import (
	"crypto/md5"
	"fmt"
	"math"
	"os"
	"strconv"
)

// Space-efficient probabilistic set membership: a Bloom filter sizes its bit array and
// hash count from a target capacity and error rate, using double hashing (two md5-
// derived hashes) to set and test bits; membership may false-positive, never false-
// negative. Use to cheaply pre-filter "definitely not present" lookups.
// Guarantees: every added item reports present (no false negatives), the false-positive
// rate stays within ~3x the target, bit sizing grows with capacity and strictness,
// resize clears the filter, and shrinking or invalid parameters are refused.
// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
var _auraMark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
type BloomFilter struct {
	capacity  int
	errorRate float64
	bitCount  int
	hashCount int
	bitArray  []bool
	itemCount int
}

func NewBloomFilter(capacity int, errorRate float64) *BloomFilter {
	if capacity <= 0 {
		panic("Capacity must be positive")
	}
	if !(0 < errorRate && errorRate < 1) {
		panic("Error rate must be between 0 and 1")
	}
	bitCount := calculateBitCount(capacity, errorRate)
	hashCount := calculateHashCount(capacity, bitCount)
	return &BloomFilter{
		capacity:  capacity,
		errorRate: errorRate,
		bitCount:  bitCount,
		hashCount: hashCount,
		bitArray:  make([]bool, bitCount),
	}
}

func calculateBitCount(capacity int, errorRate float64) int {
	return int(-float64(capacity)*math.Log(errorRate)/(math.Log(2)*math.Log(2))) + 1
}

func calculateHashCount(capacity, bitCount int) int {
	return int((float64(bitCount)/float64(capacity))*math.Log(2)) + 1
}

func hashPair(item string, maxValue int) (int, int) {
	b := []byte(item)
	h1 := md5.Sum(append(b, byte(0), byte(0), byte(0), byte(0)))
	hash1 := 0
	for i := 0; i < 8; i++ {
		hash1 = hash1<<8 + int(h1[i])
	}
	if hash1 < 0 {
		hash1 = -hash1
	}
	hash1 = hash1 % maxValue

	h2 := md5.Sum(append(b, byte(0), byte(0), byte(0), byte(1)))
	hash2 := 0
	for i := 0; i < 8; i++ {
		hash2 = hash2<<8 + int(h2[i])
	}
	if hash2 < 0 {
		hash2 = -hash2
	}
	hash2 = hash2 % maxValue

	return hash1, hash2
}

func (bf *BloomFilter) getHashPositions(item string) []int {
	hash1, hash2 := hashPair(item, bf.bitCount)
	positions := make([]int, bf.hashCount)
	for i := 0; i < bf.hashCount; i++ {
		positions[i] = (hash1 + i*hash2) % bf.bitCount
	}
	return positions
}

func (bf *BloomFilter) Add(item string) {
	for _, pos := range bf.getHashPositions(item) {
		bf.bitArray[pos] = true
	}
	bf.itemCount++
}

func (bf *BloomFilter) Contains(item string) bool {
	for _, pos := range bf.getHashPositions(item) {
		if !bf.bitArray[pos] {
			return false
		}
	}
	return true
}

func (bf *BloomFilter) FalsePositiveRate() float64 {
	if bf.itemCount == 0 {
		return 0.0
	}
	pZero := math.Pow(1.0-(1.0/float64(bf.bitCount)), float64(bf.hashCount*bf.itemCount))
	return math.Pow(1.0-pZero, float64(bf.hashCount))
}

func (bf *BloomFilter) Resize(newCapacity int) {
	if !(newCapacity > bf.capacity) {
		panic("New capacity must be greater than current capacity")
	}
	bf.capacity = newCapacity
	bf.bitCount = calculateBitCount(newCapacity, bf.errorRate)
	bf.hashCount = calculateHashCount(newCapacity, bf.bitCount)
	bf.bitArray = make([]bool, bf.bitCount)
	// Resize clears the bits, so it must also reset the count — otherwise itemCount and the
	// analytic FalsePositiveRate described a filter that no longer exists (the shipped
	// state-accounting lie; snapshot at bloom_filter.BROKEN.go).
	bf.itemCount = 0
}

func main() {
	bf := NewBloomFilter(1000, 0.01)

	if !(bf.FalsePositiveRate() == 0.0) {
		fmt.Fprintf(os.Stderr, "empty filter fpr should be 0, got %v\n", bf.FalsePositiveRate())
		os.Exit(1)
	}
	emptyClaims := 0
	for i := 0; i < 50; i++ {
		if bf.Contains(fmt.Sprintf("probe_%d", i)) {
			emptyClaims++
		}
	}
	if !(emptyClaims == 0) {
		fmt.Fprintf(os.Stderr, "empty filter claimed to contain %d items\n", emptyClaims)
		os.Exit(1)
	}

	var items []string
	for i := 0; i < 1000; i++ {
		items = append(items, fmt.Sprintf("item_%d", i))
	}
	for _, item := range items {
		bf.Add(item)
	}
	if !(bf.itemCount == 1000) {
		fmt.Fprintf(os.Stderr, "expected 1000 items, got %d\n", bf.itemCount)
		os.Exit(1)
	}
	found := 0
	for _, item := range items {
		if bf.Contains(item) {
			found++
		}
	}
	if !(found == 1000) {
		fmt.Fprintf(os.Stderr, "FALSE NEGATIVE: only %d/1000 added items found\n", found)
		os.Exit(1)
	}

	fp := 0
	for i := 0; i < 2000; i++ {
		if bf.Contains(fmt.Sprintf("unknown_%d", i)) {
			fp++
		}
	}
	if !(fp < 60) {
		fmt.Fprintf(os.Stderr, "false-positive rate %d/2000 blows past 3x the 1%% target\n", fp)
		os.Exit(1)
	}
	est := bf.FalsePositiveRate()
	if !(0.0 < est && est < 0.05) {
		fmt.Fprintf(os.Stderr, "analytic FPR estimate %v out of band\n", est)
		os.Exit(1)
	}

	bf2 := NewBloomFilter(2000, 0.01)
	if !(bf2.bitCount > bf.bitCount) {
		fmt.Fprintln(os.Stderr, "more capacity should yield more bits")
		os.Exit(1)
	}
	bf3 := NewBloomFilter(1000, 0.001)
	if !(bf3.bitCount > bf.bitCount) {
		fmt.Fprintln(os.Stderr, "stricter error rate should yield more bits")
		os.Exit(1)
	}

	bf.Resize(2000)
	if !(bf.capacity == 2000) {
		fmt.Fprintf(os.Stderr, "resize capacity should be 2000, got %d\n", bf.capacity)
		os.Exit(1)
	}
	anySet := false
	for _, b := range bf.bitArray {
		if b {
			anySet = true
			break
		}
	}
	if anySet {
		fmt.Fprintln(os.Stderr, "resize claims to clear, but bits survived")
		os.Exit(1)
	}
	if bf.Contains("item_0") {
		fmt.Fprintln(os.Stderr, "cleared filter still claims membership")
		os.Exit(1)
	}

	// shrinking resize refused
	func() {
		defer func() {
			if r := recover(); r == nil {
				fmt.Fprintln(os.Stderr, "shrinking resize accepted")
				os.Exit(1)
			}
		}()
		bf.Resize(100)
	}()

	// Invalid construction refused.
	for _, params := range [][2]int{{0, 1}, {100, 0}, {100, 100}, {-5, 50}} {
		cap, errInt := params[0], params[1]
		errRate := float64(errInt) / 100.0
		func() {
			defer func() {
				if r := recover(); r == nil {
					fmt.Fprintf(os.Stderr, "BloomFilter(%d, %v) accepted\n", cap, errRate)
					os.Exit(1)
				}
			}()
			_ = NewBloomFilter(cap, errRate)
		}()
	}

	fmt.Printf("bloom_filter: 1000/1000 found (no false negatives), %d/2000 false positives (≤1%% target x3), sizing monotone, resize clears — PASS\n", fp)
}

func itoa(i int) string {
	return strconv.Itoa(i)
}
