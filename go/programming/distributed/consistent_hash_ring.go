package main

import (
	"crypto/md5"
	"fmt"
	"os"
	"sort"
)

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
var _auraMark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
type VirtualNode struct {
	nodeID    string
	index     int
	hashValue string
}

type HashRing struct {
	virtualNodesPerPhysicalNode int
	ring                        []*VirtualNode
	nodes                       map[string]interface{}
	sortedHashes                []string
}

func NewHashRing(virtualNodesPerPhysicalNode int) *HashRing {
	if virtualNodesPerPhysicalNode < 1 {
		panic("virtual_nodes_per_physical_node must be at least 1")
	}
	return &HashRing{
		virtualNodesPerPhysicalNode: virtualNodesPerPhysicalNode,
		ring:                        make([]*VirtualNode, 0),
		nodes:                       make(map[string]interface{}),
		sortedHashes:                make([]string, 0),
	}
}

func (h *HashRing) hash(key string) string {
	sum := md5.Sum([]byte(key))
	return fmt.Sprintf("%x", sum)
}

func (h *HashRing) AddNode(nodeID string, nodeData interface{}) {
	if _, ok := h.nodes[nodeID]; ok {
		return
	}
	h.nodes[nodeID] = nodeData
	for i := 0; i < h.virtualNodesPerPhysicalNode; i++ {
		virtualNodeKey := fmt.Sprintf("%s:%d", nodeID, i)
		hashValue := h.hash(virtualNodeKey)
		vn := &VirtualNode{nodeID: nodeID, index: i, hashValue: hashValue}
		// Insert into sorted positions
		insertIdx := sort.Search(len(h.sortedHashes), func(j int) bool {
			return h.sortedHashes[j] >= hashValue
		})
		h.sortedHashes = append(h.sortedHashes, "")
		copy(h.sortedHashes[insertIdx+1:], h.sortedHashes[insertIdx:])
		h.sortedHashes[insertIdx] = hashValue

		h.ring = append(h.ring, nil)
		copy(h.ring[insertIdx+1:], h.ring[insertIdx:])
		h.ring[insertIdx] = vn
	}
}

func (h *HashRing) RemoveNode(nodeID string) {
	if _, ok := h.nodes[nodeID]; !ok {
		panic(fmt.Sprintf("Node '%s' not found in ring", nodeID))
	}
	newRing := make([]*VirtualNode, 0)
	newHashes := make([]string, 0)
	for _, vn := range h.ring {
		if vn.nodeID != nodeID {
			newRing = append(newRing, vn)
			newHashes = append(newHashes, vn.hashValue)
		}
	}
	h.ring = newRing
	h.sortedHashes = newHashes
	delete(h.nodes, nodeID)
}

func (h *HashRing) GetNode(key string) string {
	if len(h.ring) == 0 {
		return ""
	}
	if len(h.ring) == 1 {
		return h.ring[0].nodeID
	}
	keyHash := h.hash(key)
	idx := sort.Search(len(h.sortedHashes), func(i int) bool {
		return h.sortedHashes[i] >= keyHash
	})
	if idx == len(h.sortedHashes) {
		idx = 0
	}
	return h.ring[idx].nodeID
}

func (h *HashRing) Rebalance() map[string][]string {
	return map[string][]string{}
}

func main() {
	ring := NewHashRing(40)
	nodes := []string{"node1", "node2", "node3"}
	for _, node := range nodes {
		ring.AddNode(node, map[string]interface{}{"host": node})
	}
	if !(len(ring.ring) == 120) {
		fmt.Fprintf(os.Stderr, "3 nodes x 40 vnodes must be 120, got %d\n", len(ring.ring))
		os.Exit(1)
	}

	keys := make([]string, 1000)
	for i := 0; i < 1000; i++ {
		keys[i] = fmt.Sprintf("key_%d", i)
	}

	before := make(map[string]string)
	for _, k := range keys {
		node := ring.GetNode(k)
		before[k] = node
		if node != "node1" && node != "node2" && node != "node3" {
			fmt.Fprintf(os.Stderr, "key mapped to a ghost node: %s -> %s\n", k, node)
			os.Exit(1)
		}
	}

	again := make(map[string]string)
	for _, k := range keys {
		again[k] = ring.GetNode(k)
	}
	beforeStr := fmt.Sprintf("%v", before)
	againStr := fmt.Sprintf("%v", again)
	if beforeStr != againStr {
		fmt.Fprintln(os.Stderr, "mapping not stable")
		os.Exit(1)
	}

	counts := make(map[string]int)
	for _, v := range before {
		counts[v]++
	}
	if !(counts["node1"]+counts["node2"]+counts["node3"] == 1000) {
		fmt.Fprintf(os.Stderr, "sum of counts must be 1000, got %d\n", counts["node1"]+counts["node2"]+counts["node3"])
		os.Exit(1)
	}
	for _, n := range nodes {
		c := counts[n]
		if !(150 <= c && c <= 550) {
			fmt.Fprintf(os.Stderr, "distribution badly skewed: %v\n", counts)
			os.Exit(1)
		}
	}

	ring.AddNode("node4", map[string]interface{}{"host": "node4"})
	after := make(map[string]string)
	for _, k := range keys {
		after[k] = ring.GetNode(k)
	}
	moved := 0
	illegal := []string{}
	for _, k := range keys {
		if before[k] != after[k] {
			moved++
			if after[k] != "node4" {
				illegal = append(illegal, k)
			}
		}
	}
	if !(len(illegal) == 0) {
		fmt.Fprintf(os.Stderr, "%d keys moved between OLD nodes (consistency broken)\n", len(illegal))
		os.Exit(1)
	}
	if !(0 < moved && moved < 500) {
		fmt.Fprintf(os.Stderr, "adding 1 of 4 nodes should move ~250/1000 keys, moved %d\n", moved)
		os.Exit(1)
	}

	ring.RemoveNode("node4")
	restored := make(map[string]string)
	for _, k := range keys {
		restored[k] = ring.GetNode(k)
	}
	if !(fmt.Sprintf("%v", restored) == beforeStr) {
		fmt.Fprintln(os.Stderr, "remove(add(ring)) must restore the exact original mapping")
		os.Exit(1)
	}

	ring.RemoveNode("node2")
	final := make(map[string]string)
	for _, k := range keys {
		final[k] = ring.GetNode(k)
	}
	node2CountBefore := 0
	node2CountAfter := 0
	for _, k := range keys {
		if before[k] != "node2" {
			if !(final[k] == before[k]) {
				fmt.Fprintf(os.Stderr, "key %s moved although its node was not removed\n", k)
				os.Exit(1)
			}
		} else {
			node2CountBefore++
			if !(final[k] == "node1" || final[k] == "node3") {
				fmt.Fprintf(os.Stderr, "orphaned key %s -> %s\n", k, final[k])
				os.Exit(1)
			}
			if final[k] == "node2" {
				node2CountAfter++
			}
		}
	}
	if !(node2CountBefore == node2CountAfter+counts["node2"]) {
		fmt.Fprintf(os.Stderr, "counts[node2] != sum(1 for k in keys if before[k] == node2): %d != %d\n", node2CountBefore, node2CountAfter+counts["node2"])
		os.Exit(1)
	}

	empty := NewHashRing(100)
	if !(empty.GetNode("anything") == "") {
		fmt.Fprintln(os.Stderr, "empty ring invented a node")
		os.Exit(1)
	}

	fmt.Printf("consistent_hash_ring: 1000 keys stable, balance %v, add moved %d (all to node4), remove restored exactly — PASS\n",
		[]int{counts["node1"], counts["node2"], counts["node3"]}, moved)
}
