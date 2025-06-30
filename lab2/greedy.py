import heapq

graph = {
    's': {'a': 6, 'd': 3},
    'a': {'b': 5, 's': 6},
    'b': {'c': 4, 'a': 5},
    'c': {'b': 4},
    'd': {'s': 3, 'e': 2},
    'e': {'d': 2, 'f': 4},
    'f': {'e': 4, 'g': 3},
    'g': {'f': 3}
}

heuristic = {
    's': 12,
    'a': 8,
    'd': 9,
    'b': 7,
    'c': 5,
    'e': 4,
    'f': 2,
    'g': 0
}

def greedy_search(graph, start, goal):
    visited = set()
    pq = []
    heapq.heappush(pq, (heuristic[start], start))  # (heuristic, node)
    path = []

    while pq:
        h, current = heapq.heappop(pq)
        if current in visited:
            continue
        visited.add(current)
        path.append(current)

        if current == goal:
            return path

        for neighbor in graph.get(current, {}):
            if neighbor not in visited:
                heapq.heappush(pq, (heuristic[neighbor], neighbor))

    return None  # if path not found

# Example usage:
start_node = 's'
goal_node = 'g'
result = greedy_search(graph, start_node, goal_node)
print("Path found by Greedy Best First Search:", result)
