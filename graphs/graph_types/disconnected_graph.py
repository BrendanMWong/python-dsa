# Disconnected graph demo
# Use "python graphs/graph_types/disconnected_graph.py" to run this code.

# Build a disconnected undirected graph
graph = {
    "A": ["B"],
    "B": ["A"],
    "C": ["D"],
    "D": ["C"],
    "E": []  # isolated node
}

# Graph operations (same as connected graph)
def add_vertex(graph, v):
    if v not in graph:
        graph[v] = []

def add_edge(graph, u, v):
    if u not in graph:
        add_vertex(graph, u)
    if v not in graph:
        add_vertex(graph, v)
    if v not in graph[u]:
        graph[u].append(v)
    if u not in graph[v]:
        graph[v].append(u)

def remove_edge(graph, u, v):
    if u in graph and v in graph[u]:
        graph[u].remove(v)
    if v in graph and u in graph[v]:
        graph[v].remove(u)

def remove_vertex(graph, v):
    if v in graph:
        for node in graph:
            if v in graph[node]:
                graph[node].remove(v)
        del graph[v]

# Testing
print("Disconnected Graph:")
print(graph)

print("\nAdding vertex F and connecting to E")
add_vertex(graph, "F")
add_edge(graph, "F", "E")
print(graph)

print("\nRemoving edge A <-> B")
remove_edge(graph, "A", "B")
print(graph)

print("\nRemoving vertex D")
remove_vertex(graph, "D")
print(graph)
