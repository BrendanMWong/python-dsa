# Breadth-First Search (BFS) Traversal of a Graph in Python
# Use "python graphs/graph_algorithms/graph_traversals/graph_bfs.py" to run this code

from collections import deque

# Build the graph as a dictionary
graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": ["F"],
    "F": []
}

# Breadth First Search
def bfs(graph, start):
    visited = set([start])
    queue = deque([start])

    while queue:
        node = queue.popleft()
        print(node, end=" ")

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

# Testing BFS
print("Graph:")
print(graph)

print("\nBFS starting from A:")
bfs(graph, "A")
print("\n")

# Optional: test starting from another node
print("BFS starting from B:")
bfs(graph, "B")
print("\n")