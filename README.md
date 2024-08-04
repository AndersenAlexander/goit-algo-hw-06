# Homework on Graph Algorithms

## Task 2: DFS and BFS Pathfinding

### Implemented Algorithms
We implemented Depth-First Search (DFS) and Breadth-First Search (BFS) to find paths in a transportation network graph.

### Results and Comparison

- **DFS Path from Station A to Station D:** ["Station A", "Station B", "Station D"]
- **BFS Path from Station A to Station D:** ["Station A", "Station C", "Station D"]

### Analysis

**DFS:**
DFS explores as far as possible along each branch before backtracking. It does not guarantee the shortest path, as it may go deeper into the graph rather than exploring all neighbors first. The path obtained using DFS depends on the order of traversal and may not be optimal in terms of distance or the number of edges.

**BFS:**
BFS explores the nearest nodes first, level by level, ensuring the shortest path is found. BFS guarantees that the path found has the minimum number of edges, as it visits all nodes at the current distance from the start node before proceeding to the next.

### Conclusion

For finding the shortest path in an unweighted graph, BFS is the preferred algorithm due to its guarantee of finding the shortest path. In contrast, DFS may be more useful in scenarios where exploring all possible paths is necessary, or when the solution involves traversing deep into a graph without concern for path length.
