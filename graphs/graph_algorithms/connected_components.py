# Connected components demo
# Use "python graphs/graph_algorithms/connected_components.py" to run this code

# Undirected graph
graph = {
    "A": ["B"],
    "B": ["A", "C"],
    "C": ["B"],
    "D": ["E"],
    "E": ["D"],
    "F": []
}

def connected_components(graph):
    visited = set()
    count = 0

    def dfs(node):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor)

    for node in graph:
        if node not in visited:
            dfs(node)
            count += 1

    return count

print("Graph:")
print(graph)

print("\nNumber of connected components:")
print(connected_components(graph))
