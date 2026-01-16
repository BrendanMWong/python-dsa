# Weighted graph demo
# Use "python graphs/graph_types/weighted_graph.py" to run this code.

# Build the graph as a dictionary of dictionaries
graph = {
    "A": {"B": 3, "C": 5},
    "B": {"D": 2},
    "C": {"E": 4},
    "D": {},
    "E": {}
}

# Add a vertex
def add_vertex(graph, v):
    if v not in graph:
        graph[v] = {}

# Add a weighted edge
def add_edge(graph, u, v, weight):
    if u not in graph:
        add_vertex(graph, u)
    if v not in graph:
        add_vertex(graph, v)
    graph[u][v] = weight

# Remove an edge
def remove_edge(graph, u, v):
    if u in graph and v in graph[u]:
        del graph[u][v]

# Remove a vertex
def remove_vertex(graph, v):
    if v in graph:
        for node in graph:
            if v in graph[node]:
                del graph[node][v]
        del graph[v]

# ------------------ Testing ------------------
print("Weighted Graph:")
print(graph)

print("\nAdding vertex F")
add_vertex(graph, "F")
print(graph)

print("\nAdding edge E -> F with weight 7")
add_edge(graph, "E", "F", 7)
print(graph)

print("\nRemoving edge B -> D")
remove_edge(graph, "B", "D")
print(graph)

print("\nRemoving vertex C")
remove_vertex(graph, "C")
print(graph)
