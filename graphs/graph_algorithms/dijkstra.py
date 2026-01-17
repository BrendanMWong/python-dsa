# Dijkstra's algorithm demo
# Use "python graphs/graph_algorithms/dijkstra.py" to run this code

import heapq

# Weighted graph (adjacency list)
graph = {
    "A": [("B", 1), ("C", 4)],
    "B": [("C", 2), ("D", 5)],
    "C": [("D", 1)],
    "D": []
}

def dijkstra(graph, start):
    distances = {node: float("inf") for node in graph}
    distances[start] = 0

    pq = [(0, start)]

    while pq:
        current_distance, node = heapq.heappop(pq)

        if current_distance > distances[node]:
            continue

        for neighbor, weight in graph[node]:
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances

print("Graph:")
print(graph)

print("\nShortest distances from A:")
print(dijkstra(graph, "A"))
