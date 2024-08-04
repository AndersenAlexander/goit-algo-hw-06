import networkx as nx
import matplotlib.pyplot as plt

# Create a directed graph (transportation networks are often directional)
G = nx.DiGraph()

# Adding vertices (locations)
locations = ["Station A", "Station B", "Station C", "Station D", "Station E"]

# Adding edges with attributes (distances in this case)
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
for u, v, dist in edges:
    G.add_edge(u, v, distance=dist)

# Visualizing the graph
plt.figure(figsize=(10, 8))
pos = nx.spring_layout(G)  # Positions for all nodes
nx.draw(G, pos, with_labels=True, node_color='lightblue', font_weight='bold', node_size=700)
labels = nx.get_edge_attributes(G, 'distance')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.title('City Transportation Network')
plt.show()

# Analyzing main characteristics
num_vertices = G.number_of_nodes()
num_edges = G.number_of_edges()
degrees = dict(G.degree())
average_degree = sum(degrees.values()) / num_vertices

print(f"Number of vertices: {num_vertices}")
print(f"Number of edges: {num_edges}")
print(f"Degrees of vertices: {degrees}")
print(f"Average degree: {average_degree:.2f}")
