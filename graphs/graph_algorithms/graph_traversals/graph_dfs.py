# Depth-First Search (DFS) Traversal of a Graph in Python
# Use "python graphs/graph_algorithms/graph_traversals/graph_dfs.py" to run this code

# Build the graph as a dictionary
graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": ["F"],
    "F": []
}

# Depth First Search
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()

    visited.add(start)
    print(start, end=" ")

    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

# Testing DFS
print("Graph:")
print(graph)

print("\nDFS starting from A:")
dfs(graph, "A")
print("\n")

# Optional: test starting from another node
print("DFS starting from B:")
dfs(graph, "B")
print("\n")