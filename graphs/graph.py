# Graph implementation without classes
# Use "python graphs/graph.py" to run this code

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

# Breadth-First Search (BFS) traversal
def bfs(graph, start):
    visited = set()
    queue = deque()
    queue.append(start)
    visited.add(start)

    print(f"BFS starting from {start}:")
    while queue:
        current = queue.popleft()
        print(current)
        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

# Depth-First Search (DFS) traversal
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
        print(f"DFS starting from {start}:")

    visited.add(start)
    print(start)
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)


# Run traversals
bfs(graph, "A")
print()
dfs(graph, "A")
