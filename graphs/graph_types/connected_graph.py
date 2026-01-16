# Connected graph demo
# Use "python graphs/graph_types/connected_graph.py" to run this code.

# Build a connected undirected graph
graph = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A", "D"],
    "D": ["B", "C"]
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
print("Connected Graph:")
print(graph)

print("\nAdding vertex E and connecting to D")
add_vertex(graph, "E")
add_edge(graph, "E", "D")
print(graph)

print("\nRemoving edge A <-> C")
remove_edge(graph, "A", "C")
print(graph)

print("\nRemoving vertex B")
remove_vertex(graph, "B")
print(graph)
