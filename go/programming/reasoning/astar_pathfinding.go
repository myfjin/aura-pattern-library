// A* Pathfinding Algorithm Implementation
//
// This file implements the A* pathfinding algorithm for grid-based navigation.
// It includes node, grid, and A* algorithm types, and replicates the Python
// self-tests exactly.

package main

import (
	"container/heap"
	"fmt"
	"math"
	"math/rand"
	"os"
)

// Node represents a single node in the grid for pathfinding.
// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
var _auraMark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
type Node struct {
	x, y     int
	g        float64
	h        float64
	f        float64
	parent   *Node
	walkable bool
}

// nodeIndex returns a flat coordinate key for the node.
func (n *Node) nodeIndex() int {
	return n.y*1000000 + n.x // sufficiently large width multiplier
}

// reset clears node values for reuse.
func (n *Node) reset() {
	n.g = math.Inf(1)
	n.h = 0
	n.f = math.Inf(1)
	n.parent = nil
}

// nodeHeap is a min-heap of *Node ordered by f.
type nodeHeap []*Node

func (h nodeHeap) Len() int            { return len(h) }
func (h nodeHeap) Less(i, j int) bool  { return h[i].f < h[j].f }
func (h nodeHeap) Swap(i, j int)       { h[i], h[j] = h[j], h[i] }
func (h *nodeHeap) Push(x interface{}) { *h = append(*h, x.(*Node)) }
func (h *nodeHeap) Pop() interface{} {
	old := *h
	n := len(old)
	item := old[n-1]
	*h = old[:n-1]
	return item
}

// Grid represents a 2D grid for pathfinding.
type Grid struct {
	width  int
	height int
	nodes  [][]*Node
}

// newGrid creates a width×height grid of walkable nodes.
func newGrid(width, height int) *Grid {
	nodes := make([][]*Node, height)
	for y := 0; y < height; y++ {
		row := make([]*Node, width)
		for x := 0; x < width; x++ {
			row[x] = &Node{x: x, y: y, walkable: true, g: math.Inf(1), f: math.Inf(1)}
		}
		nodes[y] = row
	}
	return &Grid{width: width, height: height, nodes: nodes}
}

func (g *Grid) isValidPosition(x, y int) bool {
	return 0 <= x && x < g.width && 0 <= y && y < g.height
}

func (g *Grid) getNode(x, y int) (*Node, error) {
	if !g.isValidPosition(x, y) {
		return nil, fmt.Errorf("position (%d, %d) is out of bounds", x, y)
	}
	return g.nodes[y][x], nil
}

func (g *Grid) setWalkable(x, y int, walkable bool) error {
	node, err := g.getNode(x, y)
	if err != nil {
		return err
	}
	node.walkable = walkable
	return nil
}

func (g *Grid) getNeighbors(node *Node) []*Node {
	var neighbors []*Node
	directions := [][2]int{{0, 1}, {1, 0}, {0, -1}, {-1, 0}}
	for _, d := range directions {
		nx, ny := node.x+d[0], node.y+d[1]
		if g.isValidPosition(nx, ny) {
			neighbor := g.nodes[ny][nx]
			if neighbor.walkable {
				neighbors = append(neighbors, neighbor)
			}
		}
	}
	return neighbors
}

// AStar implements the A* pathfinding algorithm on a grid.
type AStar struct {
	grid *Grid
}

func newAStar(grid *Grid) *AStar {
	return &AStar{grid: grid}
}

func (a *AStar) heuristic(nodeA, nodeB *Node) float64 {
	dx := float64(nodeA.x - nodeB.x)
	dy := float64(nodeA.y - nodeB.y)
	return math.Sqrt(dx*dx + dy*dy)
}

func (a *AStar) reconstructPath(node *Node) [][2]int {
	var path [][2]int
	current := node
	for current != nil {
		path = append(path, [2]int{current.x, current.y})
		current = current.parent
	}
	// Reverse to get start-to-end path.
	for i, j := 0, len(path)-1; i < j; i, j = i+1, j-1 {
		path[i], path[j] = path[j], path[i]
	}
	return path
}

func (a *AStar) findPath(startPos, endPos [2]int) ([][2]int, error) {
	// Reset all nodes.
	for y := 0; y < a.grid.height; y++ {
		for x := 0; x < a.grid.width; x++ {
			a.grid.nodes[y][x].reset()
		}
	}

	startNode, err := a.grid.getNode(startPos[0], startPos[1])
	if err != nil {
		return nil, fmt.Errorf("invalid start or end position: %v", err)
	}
	endNode, err := a.grid.getNode(endPos[0], endPos[1])
	if err != nil {
		return nil, fmt.Errorf("invalid start or end position: %v", err)
	}

	if !startNode.walkable || !endNode.walkable {
		return nil, nil
	}

	openSet := make(nodeHeap, 0)
	heap.Init(&openSet)
	closedSet := make(map[int]struct{})

	startNode.g = 0
	startNode.h = a.heuristic(startNode, endNode)
	startNode.f = startNode.g + startNode.h
	heap.Push(&openSet, startNode)

	for openSet.Len() > 0 {
		currentNode := heap.Pop(&openSet).(*Node)

		if _, ok := closedSet[currentNode.nodeIndex()]; ok {
			continue
		}
		closedSet[currentNode.nodeIndex()] = struct{}{}

		if currentNode.x == endNode.x && currentNode.y == endNode.y {
			return a.reconstructPath(endNode), nil
		}

		for _, neighbor := range a.grid.getNeighbors(currentNode) {
			if _, ok := closedSet[neighbor.nodeIndex()]; ok {
				continue
			}

			tentativeG := currentNode.g + a.heuristic(currentNode, neighbor)
			if tentativeG < neighbor.g {
				neighbor.parent = currentNode
				neighbor.g = tentativeG
				neighbor.h = a.heuristic(neighbor, endNode)
				neighbor.f = neighbor.g + neighbor.h
				heap.Push(&openSet, neighbor)
			}
		}
	}

	return nil, nil
}

// bfsShortestSteps is a brute-force BFS oracle for an exact shortest step count.
func bfsShortestSteps(maze [][]bool, start, end [2]int) *int {
	h := len(maze)
	w := len(maze[0])
	seen := make(map[[2]int]struct{})
	seen[start] = struct{}{}
	type item struct {
		pos [2]int
		d   int
	}
	q := []item{{pos: start, d: 0}}
	directions := [][2]int{{1, 0}, {-1, 0}, {0, 1}, {0, -1}}
	for len(q) > 0 {
		cur := q[0]
		q = q[1:]
		if cur.pos == end {
			return &cur.d
		}
		for _, d := range directions {
			nx, ny := cur.pos[0]+d[0], cur.pos[1]+d[1]
			np := [2]int{nx, ny}
			if nx >= 0 && nx < w && ny >= 0 && ny < h && maze[ny][nx] {
				if _, ok := seen[np]; !ok {
					seen[np] = struct{}{}
					q = append(q, item{pos: np, d: cur.d + 1})
				}
			}
		}
	}
	return nil
}

func apply(grid *Grid, maze [][]bool) {
	for y := 0; y < len(maze); y++ {
		for x := 0; x < len(maze[0]); x++ {
			grid.setWalkable(x, y, maze[y][x])
		}
	}
}

func validPath(path [][2]int, maze [][]bool, start, end [2]int) bool {
	if len(path) == 0 {
		return false
	}
	if path[0] != start || path[len(path)-1] != end {
		return false
	}
	for i := 0; i < len(path)-1; i++ {
		x1, y1 := path[i][0], path[i][1]
		x2, y2 := path[i+1][0], path[i+1][1]
		if abs(x1-x2)+abs(y1-y2) != 1 {
			return false
		}
		if !maze[y2][x2] {
			return false
		}
	}
	return true
}

func abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}

func main() {
	rand.Seed(1)

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
	grid := newGrid(10, 10)
	apply(grid, maze)
	path, err := newAStar(grid).findPath([2]int{0, 0}, [2]int{9, 9})
	if err != nil {
		fmt.Fprintf(os.Stderr, "demo maze error: %v\n", err)
		os.Exit(1)
	}
	if path == nil {
		fmt.Fprintln(os.Stderr, "demo maze has a path but A* found none")
		os.Exit(1)
	}
	if !validPath(path, maze, [2]int{0, 0}, [2]int{9, 9}) {
		fmt.Fprintf(os.Stderr, "invalid path: %v\n", path)
		os.Exit(1)
	}
	oracle := bfsShortestSteps(maze, [2]int{0, 0}, [2]int{9, 9})
	if oracle == nil {
		fmt.Fprintln(os.Stderr, "BFS could not solve demo maze")
		os.Exit(1)
	}
	if len(path)-1 != *oracle {
		fmt.Fprintf(os.Stderr, "A* path has %d steps, BFS optimum is %d\n", len(path)-1, *oracle)
		os.Exit(1)
	}

	openGrid := newGrid(10, 10)
	openMaze := make([][]bool, 10)
	for i := 0; i < 10; i++ {
		openMaze[i] = make([]bool, 10)
		for j := 0; j < 10; j++ {
			openMaze[i][j] = true
		}
	}
	apply(openGrid, openMaze)
	p, err := newAStar(openGrid).findPath([2]int{0, 0}, [2]int{9, 9})
	if err != nil {
		fmt.Fprintf(os.Stderr, "open grid error: %v\n", err)
		os.Exit(1)
	}
	if len(p)-1 != 18 {
		fmt.Fprintf(os.Stderr, "open-grid path must take 18 steps, took %d\n", len(p)-1)
		os.Exit(1)
	}

	boxed := make([][]bool, 10)
	for y := 0; y < 10; y++ {
		boxed[y] = make([]bool, 10)
		copy(boxed[y], openMaze[y])
	}
	boxed[8][9] = false
	boxed[8][8] = false
	boxed[9][8] = false
	g2 := newGrid(10, 10)
	apply(g2, boxed)
	walled, err := newAStar(g2).findPath([2]int{0, 0}, [2]int{9, 9})
	if err != nil {
		fmt.Fprintf(os.Stderr, "walled goal error: %v\n", err)
		os.Exit(1)
	}
	if walled != nil {
		fmt.Fprintln(os.Stderr, "A* invented a path to a walled-off goal")
		os.Exit(1)
	}

	wallCell, err := newAStar(g2).findPath([2]int{0, 0}, [2]int{9, 8})
	if err != nil {
		fmt.Fprintf(os.Stderr, "wall cell error: %v\n", err)
		os.Exit(1)
	}
	if wallCell != nil {
		fmt.Fprintln(os.Stderr, "path to a wall cell")
		os.Exit(1)
	}

	_, err = newAStar(g2).findPath([2]int{0, 0}, [2]int{99, 99})
	if err == nil {
		fmt.Fprintln(os.Stderr, "out-of-bounds goal accepted")
		os.Exit(1)
	}

	agreements := 0
	for i := 0; i < 30; i++ {
		m := make([][]bool, 8)
		for y := 0; y < 8; y++ {
			m[y] = make([]bool, 8)
			for x := 0; x < 8; x++ {
				m[y][x] = rand.Float64() > 0.35
			}
		}
		m[0][0] = true
		m[7][7] = true
		g := newGrid(8, 8)
		apply(g, m)
		aPath, err := newAStar(g).findPath([2]int{0, 0}, [2]int{7, 7})
		if err != nil {
			fmt.Fprintf(os.Stderr, "fuzz error: %v\n", err)
			os.Exit(1)
		}
		truth := bfsShortestSteps(m, [2]int{0, 0}, [2]int{7, 7})
		if truth == nil {
			if aPath != nil {
				fmt.Fprintln(os.Stderr, "A* found a path BFS proves impossible")
				os.Exit(1)
			}
		} else {
			if aPath == nil {
				fmt.Fprintf(os.Stderr, "A* missed an existing %d-step path\n", *truth)
				os.Exit(1)
			}
			if !validPath(aPath, m, [2]int{0, 0}, [2]int{7, 7}) {
				fmt.Fprintln(os.Stderr, "fuzz path invalid")
				os.Exit(1)
			}
			if len(aPath)-1 != *truth {
				fmt.Fprintf(os.Stderr, "A* took %d steps, optimum %d (not optimal!)\n", len(aPath)-1, *truth)
				os.Exit(1)
			}
		}
		agreements++
	}
	if agreements != 30 {
		fmt.Fprintf(os.Stderr, "agreements %d != 30\n", agreements)
		os.Exit(1)
	}

	fmt.Printf("astar_pathfinding: demo maze optimal (%d steps == BFS), open grid 18 exact, walled goal None, 30/30 fuzz mazes optimal -- PASS\n", *oracle)
}
