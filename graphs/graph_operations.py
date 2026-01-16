# Graph implementation without classes, is an adjacency list in Python
# Use "python graphs/graph_operations.py" to run this code

# Build the graph as a dictionary
graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": ["F"],
    "F": []
}

# Graph operations

# Add a vertex to the graph
def add_vertex(graph, v):
    if v not in graph:
        graph[v] = []

# Add an edge to the graph
def add_edge(graph, u, v, directed=True):
    if u not in graph:
        add_vertex(graph, u)
    if v not in graph:
        add_vertex(graph, v)

    if v not in graph[u]:
        graph[u].append(v)

    if not directed and u not in graph[v]:
        graph[v].append(u)

# Remove an edge from the graph
def remove_edge(graph, u, v, directed=True):
    if u in graph and v in graph[u]:
        graph[u].remove(v)

    if not directed and v in graph and u in graph[v]:
        graph[v].remove(u)

# Remove a vertex from the graph
def remove_vertex(graph, v):
    if v not in graph:
        return

    # Remove all edges pointing to v
    for node in graph:
        if v in graph[node]:
            graph[node].remove(v)

    # Remove the vertex itself
    del graph[v]

print("Initial graph:")
print(graph)

print("\nAdding vertex G")
add_vertex(graph, "G")
print(graph)

print("\nAdding edge F -> G")
add_edge(graph, "F", "G")
print(graph)

print("\nAdding undirected edge D <-> A")
add_edge(graph, "D", "A", directed=False)
print(graph)

print("\nRemoving edge B -> E")
remove_edge(graph, "B", "E")
print(graph)

print("\nRemoving vertex C")
remove_vertex(graph, "C")
print(graph)