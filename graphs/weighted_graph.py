# Weighted Graph Algorithms in Python
# Use "python graphs/weighted_graph.py" to run this code

from collections import defaultdict
import heapq

# graph represented as adjacency list with weights
graph = {
    'A': [('B', 4), ('C', 2)],
    'B': [('A', 4), ('C', 5), ('D', 10)],
    'C': [('A', 2), ('B', 5), ('D', 3)],
    'D': [('B', 10), ('C', 3)]
}

# Dijkstra's algorithm for shortest paths (non-negative weights)
def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    pq = [(0, start)]

    while pq:
        current_distance, current_node = heapq.heappop(pq)
        if current_distance > distances[current_node]:
            continue
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    print(f"Dijkstra shortest distances from {start}:")
    for node in sorted(distances):
        print(node, distances[node])

# Bellman-Ford algorithm for shortest paths (can handle negative weights)
def bellman_ford(graph, start):
    edges = []
    for u in graph:
        for v, w in graph[u]:
            edges.append((u, v, w))

    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    for _ in range(len(graph) - 1):
        for u, v, w in edges:
            if distances[u] + w < distances[v]:
                distances[v] = distances[u] + w

    for u, v, w in edges:
        if distances[u] + w < distances[v]:
            print("Graph contains a negative weight cycle")
            return

    print(f"Bellman-Ford shortest distances from {start}:")
    for node in sorted(distances):
        print(node, distances[node])

# Kruskal's algorithm for minimum spanning tree
def kruskal(nodes, edges):
    parent = {node: node for node in nodes}

    def find(node):
        if parent[node] != node:
            parent[node] = find(parent[node])
        return parent[node]

    def union(u, v):
        parent[find(u)] = find(v)

    mst = []
    edges = sorted(edges, key=lambda x: x[2])
    for u, v, w in edges:
        if find(u) != find(v):
            union(u, v)
            mst.append((u, v, w))

    print("Kruskal MST edges:")
    for u, v, w in mst:
        print(u, v, w)

# Prim's algorithm for minimum spanning tree
def prim(graph, start):
    visited = set()
    pq = [(0, start, None)]
    mst = []

    while pq:
        weight, node, parent = heapq.heappop(pq)
        if node in visited:
            continue
        visited.add(node)
        if parent is not None:
            mst.append((parent, node, weight))
        for neighbor, w in graph[node]:
            if neighbor not in visited:
                heapq.heappush(pq, (w, neighbor, node))

    print("Prim MST edges:")
    for u, v, w in mst:
        print(u, v, w)

# prepare edges and nodes list for Kruskal
edges_list = []
for u in graph:
    for v, w in graph[u]:
        if (v, u, w) not in edges_list:
            edges_list.append((u, v, w))
nodes_list = list(graph.keys())

# run algorithms
dijkstra(graph, 'A')
print()
bellman_ford(graph, 'A')
print()
kruskal(nodes_list, edges_list)
print()
prim(graph, 'A')
