# Cycle detection demo
# Use "python graphs/graph_algorithms/cycle_detection.py" to run this code

# Directed graph
graph = {
    "A": ["B"],
    "B": ["C"],
    "C": ["D"],
    "D": ["B"]  # cycle here
}

def has_cycle(graph):
    visited = set()
    rec_stack = set()

    def dfs(node):
        visited.add(node)
        rec_stack.add(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                if dfs(neighbor):
                    return True
            elif neighbor in rec_stack:
                return True

        rec_stack.remove(node)
        return False

    for node in graph:
        if node not in visited:
            if dfs(node):
                return True

    return False

print("Graph:")
print(graph)

print("\nCycle detected:")
print(has_cycle(graph))
