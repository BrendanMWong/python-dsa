# Acyclic graph demo
# Use "python graphs/graph_types/acyclic_graph.py" to run this code.

# Build an acyclic graph (DAG)
graph = {
    "A": ["B", "C"],
    "B": ["D"],
    "C": ["D"],
    "D": []
}

# Graph operations (same as before)
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
print("Acyclic Graph (DAG):")
print(graph)

print("\nAdding vertex E")
add_vertex(graph, "E")
print(graph)

print("\nAdding edge D -> E")
add_edge(graph, "D", "E")
print(graph)

print("\nRemoving edge B -> D")
remove_edge(graph, "B", "D")
print(graph)

print("\nRemoving vertex C")
remove_vertex(graph, "C")
print(graph)
