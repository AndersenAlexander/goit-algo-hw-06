import networkx as nx
import matplotlib.pyplot as plt

# Create a directed graph (transportation networks are often directional)
G = nx.DiGraph()

# Adding vertices (locations)
locations = ["Station A", "Station B", "Station C", "Station D", "Station E"]

# Adding edges with weights (distances)
edges = [
    ("Station A", "Station B", 5),
    ("Station A", "Station C", 10),
    ("Station B", "Station D", 3),
    ("Station C", "Station D", 1),
    ("Station D", "Station E", 2),
    ("Station E", "Station A", 8)
]

# Adding nodes
G.add_nodes_from(locations)

# Adding edges with distance attributes
for u, v, weight in edges:
    G.add_edge(u, v, weight=weight)

# Visualizing the graph
plt.figure(figsize=(10, 8))
pos = nx.spring_layout(G)  # Positions for all nodes
nx.draw(G, pos, with_labels=True, node_color='lightblue', font_weight='bold', node_size=700)
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.title('City Transportation Network with Weights')
plt.show()

# Implementing Dijkstra's Algorithm to find the shortest paths
start_node = "Station A"

# Dijkstra's algorithm
lengths, paths = nx.single_source_dijkstra(G, source=start_node)

# Displaying the results
print(f"Shortest paths from {start_node} to all other vertices:")
for destination in paths:
    print(f"To {destination}: path = {paths[destination]}, total weight = {lengths[destination]}")
