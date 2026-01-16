# Cyclic graph demo
# Use "python graphs/graph_types/cyclic_graph.py" to run this code.

# Build a cyclic graph
graph = {
    "A": ["B"],
    "B": ["C"],
    "C": ["A"],  # Cycle A -> B -> C -> A
    "D": ["C"]
}

# Graph operations
def add_vertex(graph, v):
    if v not in graph:
        graph[v] = []

def add_edge(graph, u, v):
    if u not in graph:
        add_vertex(graph, u)
    if v not in graph:
        add_vertex(graph, v)
    graph[u].append(v)

def remove_edge(graph, u, v):
    if u in graph and v in graph[u]:
        graph[u].remove(v)

def remove_vertex(graph, v):
    if v in graph:
        for node in graph:
            if v in graph[node]:
                graph[node].remove(v)
        del graph[v]

# Testing
print("Cyclic Graph:")
print(graph)

print("\nAdding edge D -> A (creates another cycle)")
add_edge(graph, "D", "A")
print(graph)

print("\nRemoving edge B -> C")
remove_edge(graph, "B", "C")
print(graph)

print("\nRemoving vertex C")
remove_vertex(graph, "C")
print(graph)
