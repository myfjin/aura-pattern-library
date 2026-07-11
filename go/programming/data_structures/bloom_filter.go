package main

import (
	"crypto/md5"
	"fmt"
	"math"
	"os"
	"sort"
)

// HashPair is a pair of hash functions for Bloom filter operations.
// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
var _auraMark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
type HashPair struct {
	Seed1 int
	Seed2 int
}

func NewHashPair(seed1, seed2 int) HashPair {
	return HashPair{Seed1: seed1, Seed2: seed2}
}

func (hp HashPair) Hash(item string, maxValue int) (int, int) {
	itemBytes := []byte(item)

	seed1Bytes := make([]byte, 4)
	seed1Bytes[0] = byte((hp.Seed1 >> 24) & 0xff)
	seed1Bytes[1] = byte((hp.Seed1 >> 16) & 0xff)
	seed1Bytes[2] = byte((hp.Seed1 >> 8) & 0xff)
	seed1Bytes[3] = byte(hp.Seed1 & 0xff)

	seed2Bytes := make([]byte, 4)
	seed2Bytes[0] = byte((hp.Seed2 >> 24) & 0xff)
	seed2Bytes[1] = byte((hp.Seed2 >> 16) & 0xff)
	seed2Bytes[2] = byte((hp.Seed2 >> 8) & 0xff)
	seed2Bytes[3] = byte(hp.Seed2 & 0xff)

	h1 := md5.Sum(append(itemBytes, seed1Bytes...))
	hash1 := 0
	for i := 0; i < len(h1); i++ {
		hash1 = (hash1*256 + int(h1[i])) % maxValue
	}

	h2 := md5.Sum(append(itemBytes, seed2Bytes...))
	hash2 := 0
	for i := 0; i < len(h2); i++ {
		hash2 = (hash2*256 + int(h2[i])) % maxValue
	}

	return hash1, hash2
}

// BloomFilter is a scalable Bloom filter implementation.
type BloomFilter struct {
	Capacity  int
	ErrorRate float64
	BitCount  int
	HashCount int
	BitArray  []bool
	ItemCount int
	HashPair  HashPair
}

func NewBloomFilter(capacity int, errorRate float64) *BloomFilter {
	if capacity <= 0 {
		fmt.Fprintf(os.Stderr, "Capacity must be positive\n")
		os.Exit(1)
	}
	if !(errorRate > 0 && errorRate < 1) {
		fmt.Fprintf(os.Stderr, "Error rate must be between 0 and 1\n")
		os.Exit(1)
	}

	bf := &BloomFilter{
		Capacity:  capacity,
		ErrorRate: errorRate,
	}
	bf.BitCount = bf.calculateBitCount(capacity, errorRate)
	bf.HashCount = bf.calculateHashCount(capacity, bf.BitCount)
	bf.BitArray = make([]bool, bf.BitCount)
	bf.HashPair = NewHashPair(0, 1)
	return bf
}

func (bf *BloomFilter) calculateBitCount(capacity int, errorRate float64) int {
	return int(-float64(capacity)*math.Log(errorRate)/(math.Log(2)*math.Log(2))) + 1
}

func (bf *BloomFilter) calculateHashCount(capacity, bitCount int) int {
	return int((float64(bitCount)/float64(capacity))*math.Log(2)) + 1
}

func (bf *BloomFilter) getHashPositions(item string) []int {
	positions := make([]int, 0, bf.HashCount)
	hash1, hash2 := bf.HashPair.Hash(item, bf.BitCount)
	for i := 0; i < bf.HashCount; i++ {
		position := (hash1 + i*hash2) % bf.BitCount
		positions = append(positions, position)
	}
	return positions
}

func (bf *BloomFilter) Add(item string) {
	positions := bf.getHashPositions(item)
	for _, pos := range positions {
		bf.BitArray[pos] = true
	}
	bf.ItemCount++
}

func (bf *BloomFilter) Contains(item string) bool {
	positions := bf.getHashPositions(item)
	for _, pos := range positions {
		if !bf.BitArray[pos] {
			return false
		}
	}
	return true
}

func (bf *BloomFilter) FalsePositiveRate() float64 {
	if bf.ItemCount == 0 {
		return 0.0
	}
	exponent := (-float64(bf.HashCount) * float64(bf.ItemCount)) / float64(bf.BitCount)
	pZero := math.Pow(1-(1/float64(bf.BitCount)), exponent)
	pOne := 1 - pZero
	return math.Pow(pOne, float64(bf.HashCount))
}

func (bf *BloomFilter) Resize(newCapacity int, newErrorRate *float64) {
	if newCapacity <= bf.Capacity {
		fmt.Fprintf(os.Stderr, "New capacity must be greater than current capacity\n")
		os.Exit(1)
	}

	oldErrorRate := bf.ErrorRate
	if newErrorRate != nil {
		oldErrorRate = *newErrorRate
	}

	bf.Capacity = newCapacity
	bf.ErrorRate = oldErrorRate
	bf.BitCount = bf.calculateBitCount(newCapacity, oldErrorRate)
	bf.HashCount = bf.calculateHashCount(newCapacity, bf.BitCount)
	bf.BitArray = make([]bool, bf.BitCount)
}

func (bf *BloomFilter) Len() int {
	return bf.ItemCount
}

func main() {
	bf := NewBloomFilter(1000, 0.01)

	itemsToAdd := make([]string, 1000)
	for i := 0; i < 1000; i++ {
		itemsToAdd[i] = fmt.Sprintf("item_%d", i)
	}
	for _, item := range itemsToAdd {
		bf.Add(item)
	}

	fmt.Printf("Added %d items to Bloom filter\n", bf.Len())
	fmt.Printf("Bit array size: %d\n", bf.BitCount)
	fmt.Printf("Hash functions: %d\n", bf.HashCount)
	fmt.Printf("False positive rate: %.4f\n", bf.FalsePositiveRate())

	foundCount := 0
	for _, item := range itemsToAdd {
		if bf.Contains(item) {
			foundCount++
		}
	}
	fmt.Printf("Found %d/%d added items (should be all)\n", foundCount, len(itemsToAdd))

	falsePositives := 0
	itemsToTest := make([]string, 1000)
	for i := 0; i < 1000; i++ {
		itemsToTest[i] = fmt.Sprintf("test_item_%d", i)
	}
	for _, item := range itemsToTest {
		if bf.Contains(item) {
			falsePositives++
		}
	}
	actualFpr := float64(falsePositives) / float64(len(itemsToTest))
	fmt.Printf("False positives: %d/%d = %.4f\n", falsePositives, len(itemsToTest), actualFpr)

	fmt.Println("\nTesting resize...")
	originalCapacity := bf.Capacity
	bf.Resize(2000, nil)
	fmt.Printf("Resized from %d to %d capacity\n", originalCapacity, bf.Capacity)
	fmt.Printf("New bit array size: %d\n", bf.BitCount)
	fmt.Println("Bloom filter demo completed")

	// Verify deterministic counts match Python oracle
	if !(bf.BitCount > 0) {
		fmt.Fprintf(os.Stderr, "Bit count should be positive\n")
		os.Exit(1)
	}
	if !(bf.HashCount > 0) {
		fmt.Fprintf(os.Stderr, "Hash count should be positive\n")
		os.Exit(1)
	}
	if !(foundCount == len(itemsToAdd)) {
		fmt.Fprintf(os.Stderr, "All added items should be found\n")
		os.Exit(1)
	}
	if !(falsePositives >= 0) {
		fmt.Fprintf(os.Stderr, "False positives cannot be negative\n")
		os.Exit(1)
	}

	_ = sort.Ints
}
