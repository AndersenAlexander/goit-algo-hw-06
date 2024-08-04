# 1. DFS Implementation

def dfs(graph, start, goal, path=None):
    if path is None:
        path = []
    path = path + [start]

    if start == goal:
        return path

    for node in graph.neighbors(start):
        if node not in path:
            new_path = dfs(graph, node, goal, path)
            if new_path:
                return new_path
    return None

# 2. BFS Implementation

from collections import  deque

def bfs(graph, start, goal):
    queue = deque([(start, [start])])
    while queue:
        (vertex, path) = queue.popleft()
        for next_node in graph.neighbors(vertex):
            if next_node not in path:
                if next_node == goal:
                    return path + [next_node]
                else:
                    queue.append((next_node, path + [next_node]))

    return None

# 3. Testing DFS and BFS

start_node = "Station A"
goal_node = "Station D"

# Finding paths using DFS and BFS
dfs_path = dfs(G, start_node, goal_node)
bfs_path = bfs(G, start_node, goal_node)

print(f"DFS path from {start_node} to {goal_node}: {dfs_path}")
print(f"BFS path from {start_node} to {goal_node}: {bfs_path}")
