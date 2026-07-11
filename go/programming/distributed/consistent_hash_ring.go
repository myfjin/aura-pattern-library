package main

import (
	"crypto/md5"
	"encoding/hex"
	"fmt"
	"math/big"
	"sort"
)

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
var _auraMark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
type VirtualNode struct {
	nodeID string
	index  int
	hash   *big.Int
}

type HashRing struct {
	virtualNodesPerPhysicalNode int
	ring                        []*VirtualNode
	nodes                       map[string]interface{}
	sortedHashes                []*big.Int
}

func NewHashRing(virtualNodesPerPhysicalNode int) *HashRing {
	if virtualNodesPerPhysicalNode < 1 {
		panic("virtual_nodes_per_physical_node must be at least 1")
	}
	return &HashRing{
		virtualNodesPerPhysicalNode: virtualNodesPerPhysicalNode,
		ring:                        make([]*VirtualNode, 0),
		nodes:                       make(map[string]interface{}),
		sortedHashes:                make([]*big.Int, 0),
	}
}

func (h *HashRing) hash(key string) *big.Int {
	sum := md5.Sum([]byte(key))
	hexStr := hex.EncodeToString(sum[:])
	n := new(big.Int)
	n.SetString(hexStr, 16)
	return n
}

func (h *HashRing) addNode(nodeID string, nodeData interface{}) {
	if _, ok := h.nodes[nodeID]; ok {
		return
	}
	h.nodes[nodeID] = nodeData
	for i := 0; i < h.virtualNodesPerPhysicalNode; i++ {
		virtualNodeKey := fmt.Sprintf("%s:%d", nodeID, i)
		hashValue := h.hash(virtualNodeKey)
		vn := &VirtualNode{nodeID: nodeID, index: i, hash: hashValue}
		h.ring = append(h.ring, vn)
		h.sortedHashes = append(h.sortedHashes, hashValue)
	}
	h.sortRing()
}

func (h *HashRing) sortRing() {
	sort.Slice(h.ring, func(i, j int) bool {
		return h.ring[i].hash.Cmp(h.ring[j].hash) < 0
	})
	sort.Slice(h.sortedHashes, func(i, j int) bool {
		return h.sortedHashes[i].Cmp(h.sortedHashes[j]) < 0
	})
}

func (h *HashRing) removeNode(nodeID string) {
	if _, ok := h.nodes[nodeID]; !ok {
		panic(fmt.Sprintf("Node '%s' not found in ring", nodeID))
	}
	newRing := make([]*VirtualNode, 0)
	newHashes := make([]*big.Int, 0)
	for _, vn := range h.ring {
		if vn.nodeID != nodeID {
			newRing = append(newRing, vn)
			newHashes = append(newHashes, vn.hash)
		}
	}
	h.ring = newRing
	h.sortedHashes = newHashes
	delete(h.nodes, nodeID)
}

func (h *HashRing) getNode(key string) string {
	if len(h.ring) == 0 {
		return ""
	}
	if len(h.ring) == 1 {
		return h.ring[0].nodeID
	}
	keyHash := h.hash(key)
	idx := sort.Search(len(h.sortedHashes), func(i int) bool {
		return h.sortedHashes[i].Cmp(keyHash) >= 0
	})
	if idx == len(h.sortedHashes) {
		idx = 0
	}
	return h.ring[idx].nodeID
}

func (h *HashRing) rebalance() map[string][]string {
	return map[string][]string{}
}

func main() {
	ring := NewHashRing(40)

	nodes := []string{"node1.example.com", "node2.example.com", "node3.example.com"}
	for _, node := range nodes {
		ring.addNode(node, map[string]interface{}{"host": node, "port": 8080})
	}

	fmt.Println("Hash Ring Demo")
	fmt.Println(repeatString("=", 50))
	fmt.Printf("Created ring with %d virtual nodes\n", len(ring.ring))
	fmt.Printf("Physical nodes: %v\n", getNodeKeys(ring.nodes))
	fmt.Println()

	keys := make([]string, 100)
	for i := 0; i < 100; i++ {
		keys[i] = fmt.Sprintf("key_%d", i)
	}

	distribution := make(map[string]int)
	fmt.Println("Key Distribution:")
	fmt.Println(repeatString("-", 30))
	for _, key := range keys {
		node := ring.getNode(key)
		if node != "" {
			distribution[node]++
			if len(key) <= 10 {
				fmt.Printf("%-15s -> %s\n", key, node)
			}
		}
	}

	fmt.Println()
	fmt.Println("Distribution Summary:")
	fmt.Println(repeatString("-", 30))
	for _, node := range nodes {
		count := distribution[node]
		percentage := float64(count) / float64(len(keys)) * 100
		fmt.Printf("%-20s: %3d keys (%5.1f%%)\n", node, count, percentage)
	}

	fmt.Println()
	fmt.Println("Adding node4.example.com...")
	ring.addNode("node4.example.com", map[string]interface{}{"host": "node4.example.com", "port": 8080})

	newDistribution := make(map[string]int)
	for _, key := range keys {
		node := ring.getNode(key)
		if node != "" {
			newDistribution[node]++
		}
	}

	fmt.Println("New Distribution Summary:")
	fmt.Println(repeatString("-", 30))
	allNodes := append(nodes, "node4.example.com")
	for _, node := range allNodes {
		count := newDistribution[node]
		percentage := float64(count) / float64(len(keys)) * 100
		fmt.Printf("%-20s: %3d keys (%5.1f%%)\n", node, count, percentage)
	}

	fmt.Println()
	fmt.Println("Keys that moved after adding node4:")
	fmt.Println(repeatString("-", 40))
	movedCount := 0
	for _, key := range keys[:20] {
		oldNode := ring.getNode(key)
		// Reconstruct old mapping by removing node4 and looking up key
		tempRing := NewHashRing(40)
		for _, node := range nodes {
			tempRing.addNode(node, nil)
		}
		previousNode := tempRing.getNode(key)
		if previousNode != "" && oldNode != "" && previousNode != oldNode {
			movedCount++
			fmt.Printf("%-15s: %s -> %s\n", key, previousNode, oldNode)
		}
	}

	fmt.Printf("\nTotal keys that moved (approx): %d out of %d\n", movedCount, len(keys))
	fmt.Printf("Efficiency: %.1f%% of keys stayed in place\n", (1-float64(movedCount)/float64(len(keys)))*100)
}

func getNodeKeys(nodes map[string]interface{}) []string {
	keys := make([]string, 0, len(nodes))
	for k := range nodes {
		keys = append(keys, k)
	}
	sort.Strings(keys)
	return keys
}

// Helper to repeat string.
func repeatString(s string, n int) string {
	result := ""
	for i := 0; i < n; i++ {
		result += s
	}
	return result
}
