package main

import (
	"container/heap"
	"fmt"
	"math"
	"strings"
)

// Node represents a single node in the grid for pathfinding.
// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
var _auraMark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
type Node struct {
	X        int
	Y        int
	G        float64
	H        float64
	F        float64
	Parent   *Node
	Walkable bool
}

// NewNode initializes a Node.
func NewNode(x, y int, walkable bool) *Node {
	return &Node{
		X:        x,
		Y:        y,
		G:        math.Inf(1),
		H:        0,
		F:        math.Inf(1),
		Walkable: walkable,
	}
}

// Reset resets node values for reuse.
func (n *Node) Reset() {
	n.G = math.Inf(1)
	n.H = 0
	n.F = math.Inf(1)
	n.Parent = nil
}

// NodeHeap implements heap.Interface for priority queue of Nodes.
type NodeHeap []*Node

func (h NodeHeap) Len() int           { return len(h) }
func (h NodeHeap) Less(i, j int) bool { return h[i].F < h[j].F }
func (h NodeHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }

func (h *NodeHeap) Push(x interface{}) {
	*h = append(*h, x.(*Node))
}

func (h *NodeHeap) Pop() interface{} {
	old := *h
	n := len(old)
	item := old[n-1]
	*h = old[:n-1]
	return item
}

// Grid represents a 2D grid for pathfinding.
type Grid struct {
	Width  int
	Height int
	Nodes  [][]*Node
}

// NewGrid creates a new Grid.
func NewGrid(width, height int) *Grid {
	nodes := make([][]*Node, height)
	for y := 0; y < height; y++ {
		nodes[y] = make([]*Node, width)
		for x := 0; x < width; x++ {
			nodes[y][x] = NewNode(x, y, true)
		}
	}
	return &Grid{Width: width, Height: height, Nodes: nodes}
}

// IsValidPosition checks if position is within grid bounds.
func (g *Grid) IsValidPosition(x, y int) bool {
	return x >= 0 && x < g.Width && y >= 0 && y < g.Height
}

// GetNode gets node at specified coordinates.
func (g *Grid) GetNode(x, y int) (*Node, error) {
	if !g.IsValidPosition(x, y) {
		return nil, fmt.Errorf("Position (%d, %d) is out of bounds", x, y)
	}
	return g.Nodes[y][x], nil
}

// SetWalkable sets whether a node is walkable.
func (g *Grid) SetWalkable(x, y int, walkable bool) error {
	node, err := g.GetNode(x, y)
	if err != nil {
		return err
	}
	node.Walkable = walkable
	return nil
}

// GetNeighbors gets valid neighboring nodes (4-directional).
func (g *Grid) GetNeighbors(node *Node) []*Node {
	neighbors := []*Node{}
	directions := [][2]int{{0, 1}, {1, 0}, {0, -1}, {-1, 0}}
	for _, d := range directions {
		nx, ny := node.X+d[0], node.Y+d[1]
		if g.IsValidPosition(nx, ny) {
			neighbor := g.Nodes[ny][nx]
			if neighbor.Walkable {
				neighbors = append(neighbors, neighbor)
			}
		}
	}
	return neighbors
}

// AStar is the A* pathfinding algorithm implementation.
type AStar struct {
	Grid *Grid
}

// NewAStar creates an AStar instance.
func NewAStar(grid *Grid) *AStar {
	return &AStar{Grid: grid}
}

// Heuristic calculates Euclidean distance between two nodes.
func (a *AStar) Heuristic(nodeA, nodeB *Node) float64 {
	return math.Sqrt(float64((nodeA.X-nodeB.X)*(nodeA.X-nodeB.X)) + float64((nodeA.Y-nodeB.Y)*(nodeA.Y-nodeB.Y)))
}

// ReconstructPath reconstructs path from end node to start node.
func (a *AStar) ReconstructPath(node *Node) [][2]int {
	path := [][2]int{}
	current := node
	for current != nil {
		path = append(path, [2]int{current.X, current.Y})
		current = current.Parent
	}
	// Reverse to get start-to-end path
	for i, j := 0, len(path)-1; i < j; i, j = i+1, j-1 {
		path[i], path[j] = path[j], path[i]
	}
	return path
}

// FindPath finds path between start and end positions using A* algorithm.
func (a *AStar) FindPath(startPos, endPos [2]int) ([][2]int, error) {
	// Reset all nodes
	for y := 0; y < a.Grid.Height; y++ {
		for x := 0; x < a.Grid.Width; x++ {
			a.Grid.Nodes[y][x].Reset()
		}
	}

	startNode, err := a.Grid.GetNode(startPos[0], startPos[1])
	if err != nil {
		return nil, fmt.Errorf("Invalid start or end position: %v", err)
	}
	endNode, err := a.Grid.GetNode(endPos[0], endPos[1])
	if err != nil {
		return nil, fmt.Errorf("Invalid start or end position: %v", err)
	}

	if !startNode.Walkable || !endNode.Walkable {
		return nil, nil
	}

	openSet := &NodeHeap{}
	heap.Init(openSet)
	closedSet := make(map[*Node]struct{})

	startNode.G = 0
	startNode.H = a.Heuristic(startNode, endNode)
	startNode.F = startNode.G + startNode.H

	heap.Push(openSet, startNode)

	for openSet.Len() > 0 {
		currentNode := heap.Pop(openSet).(*Node)

		if _, ok := closedSet[currentNode]; ok {
			continue
		}
		closedSet[currentNode] = struct{}{}

		if currentNode == endNode {
			return a.ReconstructPath(endNode), nil
		}

		for _, neighbor := range a.Grid.GetNeighbors(currentNode) {
			if _, ok := closedSet[neighbor]; ok {
				continue
			}

			tentativeG := currentNode.G + a.Heuristic(currentNode, neighbor)
			if tentativeG < neighbor.G {
				neighbor.Parent = currentNode
				neighbor.G = tentativeG
				neighbor.H = a.Heuristic(neighbor, endNode)
				neighbor.F = neighbor.G + neighbor.H
				heap.Push(openSet, neighbor)
			}
		}
	}

	return nil, nil
}

func main() {
	grid := NewGrid(10, 10)

	maze := [][]bool{
		{true, true, true, true, false, true, true, true, true, true},
		{true, false, false, true, false, true, false, false, false, true},
		{true, false, true, true, false, true, false, true, true, true},
		{true, false, true, false, false, true, false, true, false, false},
		{true, true, true, true, true, true, false, true, true, true},
		{false, false, false, true, false, true, false, false, true, true},
		{true, true, false, true, false, true, true, false, true, true},
		{true, true, false, true, true, true, true, false, true, true},
		{true, false, false, false, false, false, true, false, false, true},
		{true, true, true, true, true, true, true, true, true, true},
	}

	for y := 0; y < 10; y++ {
		for x := 0; x < 10; x++ {
			grid.SetWalkable(x, y, maze[y][x])
		}
	}

	astar := NewAStar(grid)
	start := [2]int{0, 0}
	end := [2]int{9, 9}

	path, err := astar.FindPath(start, end)
	if err != nil {
		fmt.Printf("Error: %v\n", err)
		return
	}

	if path != nil {
		fmt.Printf("Path found from %v to %v:\n", start, end)
		parts := []string{}
		for _, p := range path {
			parts = append(parts, fmt.Sprintf("(%d, %d)", p[0], p[1]))
		}
		fmt.Println(strings.Join(parts, " -> "))

		fmt.Println("\nMaze visualization (Path marked with 'P'):")
		visual := make([][]rune, 10)
		for y := 0; y < 10; y++ {
			visual[y] = make([]rune, 10)
			for x := 0; x < 10; x++ {
				if maze[y][x] {
					visual[y][x] = '.'
				} else {
					visual[y][x] = '#'
				}
			}
		}
		for _, p := range path {
			visual[p[1]][p[0]] = 'P'
		}
		visual[start[1]][start[0]] = 'S'
		visual[end[1]][end[0]] = 'E'

		for _, row := range visual {
			fmt.Println(strings.Join(toStrings(row), " "))
		}
	} else {
		fmt.Printf("No path found from %v to %v\n", start, end)
	}
}

func toStrings(runes []rune) []string {
	out := make([]string, len(runes))
	for i, r := range runes {
		out[i] = string(r)
	}
	return out
}
