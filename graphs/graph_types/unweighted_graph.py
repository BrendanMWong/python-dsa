# Unweighted graph demo
# Use "python graphs/graph_types/unweighted_graph.py" to run this code.

# Build the graph as a dictionary
graph = {
    "A": ["B", "C"],
    "B": ["D"],
    "C": ["E"],
    "D": [],
    "E": []
}

# Add a vertex
def add_vertex(graph, v):
    if v not in graph:
        graph[v] = []

# Add an edge
def add_edge(graph, u, v):
    if u not in graph:
        add_vertex(graph, u)
    if v not in graph:
        add_vertex(graph, v)
    if v not in graph[u]:
        graph[u].append(v)

# Remove an edge
def remove_edge(graph, u, v):
    if u in graph and v in graph[u]:
        graph[u].remove(v)

# Remove a vertex
def remove_vertex(graph, v):
    if v in graph:
        for node in graph:
            if v in graph[node]:
                graph[node].remove(v)
        del graph[v]

# ------------------ Testing ------------------
print("Unweighted Graph:")
print(graph)

print("\nAdding vertex F")
add_vertex(graph, "F")
print(graph)

print("\nAdding edge E -> F")
add_edge(graph, "E", "F")
print(graph)

print("\nRemoving edge B -> D")
remove_edge(graph, "B", "D")
print(graph)

print("\nRemoving vertex C")
remove_vertex(graph, "C")
print(graph)
