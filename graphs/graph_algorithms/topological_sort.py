# Topological sort demo
# Use "python graphs/graph_algorithms/topological_sort.py" to run this code

# Directed Acyclic Graph (DAG)
graph = {
    "A": ["C"],
    "B": ["C", "D"],
    "C": ["E"],
    "D": ["F"],
    "E": ["F"],
    "F": []
}

def topological_sort(graph):
    visited = set()
    stack = []

    def dfs(node):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor)
        stack.append(node)

    for node in graph:
        if node not in visited:
            dfs(node)

    return stack[::-1]

print("Graph:")
print(graph)

print("\nTopological order:")
print(topological_sort(graph))
