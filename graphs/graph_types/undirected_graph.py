# Undirected graph demo
# Use "python graphs/graph_types/undirected_graph.py" to run this code

# Build the graph as a dictionary
graph = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A", "E"],
    "D": ["B"],
    "E": ["C"]
}

# Add a vertex
def add_vertex(graph, v):
    if v not in graph:
        graph[v] = []

# Add an undirected edge
def add_edge(graph, u, v):
    if u not in graph:
        add_vertex(graph, u)
    if v not in graph:
        add_vertex(graph, v)
    if v not in graph[u]:
        graph[u].append(v)
    if u not in graph[v]:
        graph[v].append(u)

# Remove an edge
def remove_edge(graph, u, v):
    if u in graph and v in graph[u]:
        graph[u].remove(v)
    if v in graph and u in graph[v]:
        graph[v].remove(u)

# Remove a vertex
def remove_vertex(graph, v):
    if v in graph:
        for node in graph:
            if v in graph[node]:
                graph[node].remove(v)
        del graph[v]

# ------------------ Testing ------------------
print("Undirected Graph:")
print(graph)

print("\nAdding vertex F")
add_vertex(graph, "F")
print(graph)

print("\nAdding edge D <-> F")
add_edge(graph, "D", "F")
print(graph)

print("\nRemoving edge B <-> D")
remove_edge(graph, "B", "D")
print(graph)

print("\nRemoving vertex C")
remove_vertex(graph, "C")
print(graph)
