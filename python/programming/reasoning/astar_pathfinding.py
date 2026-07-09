"""
A* Pathfinding Algorithm Implementation

This module implements the A* pathfinding algorithm for grid-based navigation.
It includes classes for nodes, grid representation, and the A* algorithm itself.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

from typing import List, Tuple, Optional, Set, Dict
import heapq
import math


class Node:
    """
    Represents a single node in the grid for pathfinding.
    
    Attributes:
        x (int): X coordinate in the grid
        y (int): Y coordinate in the grid
        g (float): Cost from start node to this node
        h (float): Heuristic cost from this node to end node
        f (float): Total cost (g + h)
        parent (Optional[Node]): Parent node in the path
        walkable (bool): Whether this node can be traversed
    """
    
    def __init__(self, x: int, y: int, walkable: bool = True):
        self.x = x
        self.y = y
        self.g: float = float('inf')
        self.h: float = 0
        self.f: float = float('inf')
        self.parent: Optional['Node'] = None
        self.walkable: bool = walkable
    
    def __lt__(self, other: 'Node') -> bool:
        """For priority queue comparison"""
        return self.f < other.f
    
    def __eq__(self, other: object) -> bool:
        """Check equality based on coordinates"""
        if not isinstance(other, Node):
            return False
        return self.x == other.x and self.y == other.y
    
    def __hash__(self) -> int:
        """Hash based on coordinates"""
        return hash((self.x, self.y))
    
    def reset(self) -> None:
        """Reset node values for reuse"""
        self.g = float('inf')
        self.h = 0
        self.f = float('inf')
        self.parent = None


class Grid:
    """
    Represents a 2D grid for pathfinding.
    
    Attributes:
        width (int): Width of the grid
        height (int): Height of the grid
        nodes (List[List[Node]]): 2D list of nodes
    """
    
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.nodes: List[List[Node]] = [
            [Node(x, y) for x in range(width)] for y in range(height)
        ]
    
    def is_valid_position(self, x: int, y: int) -> bool:
        """Check if position is within grid bounds"""
        return 0 <= x < self.width and 0 <= y < self.height
    
    def get_node(self, x: int, y: int) -> Node:
        """Get node at specified coordinates"""
        if not self.is_valid_position(x, y):
            raise IndexError(f"Position ({x}, {y}) is out of bounds")
        return self.nodes[y][x]
    
    def set_walkable(self, x: int, y: int, walkable: bool) -> None:
        """Set whether a node is walkable"""
        node = self.get_node(x, y)
        node.walkable = walkable
    
    def get_neighbors(self, node: Node) -> List[Node]:
        """Get valid neighboring nodes (4-directional)"""
        neighbors = []
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Up, Right, Down, Left
        
        for dx, dy in directions:
            nx, ny = node.x + dx, node.y + dy
            if self.is_valid_position(nx, ny):
                neighbor = self.get_node(nx, ny)
                if neighbor.walkable:
                    neighbors.append(neighbor)
        
        return neighbors


class AStar:
    """
    A* pathfinding algorithm implementation.
    
    Attributes:
        grid (Grid): Grid to search on
    """
    
    def __init__(self, grid: Grid):
        self.grid = grid
    
    def heuristic(self, node_a: Node, node_b: Node) -> float:
        """
        Calculate heuristic distance between two nodes using Euclidean distance.
        
        Args:
            node_a (Node): First node
            node_b (Node): Second node
            
        Returns:
            float: Heuristic distance
        """
        return math.sqrt((node_a.x - node_b.x) ** 2 + (node_a.y - node_b.y) ** 2)
    
    def reconstruct_path(self, node: Node) -> List[Tuple[int, int]]:
        """
        Reconstruct path from end node to start node.
        
        Args:
            node (Node): End node
            
        Returns:
            List[Tuple[int, int]]: List of coordinates representing the path
        """
        path = []
        current: Optional[Node] = node
        while current is not None:
            path.append((current.x, current.y))
            current = current.parent
        return path[::-1]  # Reverse to get start-to-end path
    
    def find_path(self, start_pos: Tuple[int, int], end_pos: Tuple[int, int]) -> Optional[List[Tuple[int, int]]]:
        """
        Find path between start and end positions using A* algorithm.
        
        Args:
            start_pos (Tuple[int, int]): Start position (x, y)
            end_pos (Tuple[int, int]): End position (x, y)
            
        Returns:
            Optional[List[Tuple[int, int]]]: Path as list of coordinates, or None if no path found
        """
        # Reset all nodes
        for row in self.grid.nodes:
            for node in row:
                node.reset()
        
        # Get start and end nodes
        try:
            start_node = self.grid.get_node(start_pos[0], start_pos[1])
            end_node = self.grid.get_node(end_pos[0], end_pos[1])
        except IndexError as e:
            raise ValueError(f"Invalid start or end position: {e}")
        
        if not start_node.walkable or not end_node.walkable:
            return None
        
        # Initialize open and closed sets
        open_set: List[Node] = []
        closed_set: Set[Node] = set()
        
        # Initialize start node
        start_node.g = 0
        start_node.h = self.heuristic(start_node, end_node)
        start_node.f = start_node.g + start_node.h
        
        heapq.heappush(open_set, start_node)
        
        while open_set:
            current_node = heapq.heappop(open_set)
            
            if current_node in closed_set:
                continue
            
            closed_set.add(current_node)
            
            # Found the end
            if current_node == end_node:
                return self.reconstruct_path(end_node)
            
            # Check neighbors
            for neighbor in self.grid.get_neighbors(current_node):
                if neighbor in closed_set:
                    continue
                
                # Calculate tentative g score
                tentative_g = current_node.g + self.heuristic(current_node, neighbor)
                
                if tentative_g < neighbor.g:
                    neighbor.parent = current_node
                    neighbor.g = tentative_g
                    neighbor.h = self.heuristic(neighbor, end_node)
                    neighbor.f = neighbor.g + neighbor.h
                    
                    if neighbor not in open_set:
                        heapq.heappush(open_set, neighbor)
        
        # No path found
        return None


def main():
    """Demo of A* pathfinding with a simple maze"""
    # Create a 10x10 grid
    grid = Grid(10, 10)
    
    # Define a simple maze (False = wall, True = walkable)
    maze = [
        [True,  True,  True,  True,  False, True,  True,  True,  True,  True],
        [True,  False, False, True,  False, True,  False, False, False, True],
        [True,  False, True,  True,  False, True,  False, True,  True,  True],
        [True,  False, True,  False, False, True,  False, True,  False, False],
        [True,  True,  True,  True,  True,  True,  False, True,  True,  True],
        [False, False, False, True,  False, True,  False, False, True,  True],
        [True,  True,  False, True,  False, True,  True,  False, True,  True],
        [True,  True,  False, True,  True,  True,  True,  False, True,  True],
        [True,  False, False, False, False, False, True,  False, False, True],
        [True,  True,  True,  True,  True,  True,  True,  True,  True,  True]
    ]
    
    # Apply maze to grid
    for y in range(10):
        for x in range(10):
            grid.set_walkable(x, y, maze[y][x])
    
    # Create A* instance
    astar = AStar(grid)
    
    # Define start and end points
    start = (0, 0)
    end = (9, 9)
    
    # Find path
    path = astar.find_path(start, end)
    
    if path:
        print(f"Path found from {start} to {end}:")
        print(" -> ".join(str(p) for p in path))
        
        # Visualize path
        print("\nMaze visualization (Path marked with 'P'):")
        visual = [['.' if maze[y][x] else '#' for x in range(10)] for y in range(10)]
        for x, y in path:
            visual[y][x] = 'P'
        visual[start[1]][start[0]] = 'S'
        visual[end[1]][end[0]] = 'E'
        
        for row in visual:
            print(" ".join(row))
    else:
        print(f"No path found from {start} to {end}")


if __name__ == "__main__":
    main()