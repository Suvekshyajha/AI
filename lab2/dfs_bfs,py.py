# Define the graph as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': ['H', 'I'],
    'E': ['J'],
    'F': [],
    'G': ['K'],
    'H': [],
    'I': [],
    'J': [],
    'K': []
}

# DFS Iterative Function
def dfs_iterative(graph, start):
    visited = set()
    stack = [start]
    print("DFS Traversal:", end=' ')
    while stack:
        node = stack.pop()
        if node not in visited:
            print(node, end=' ')
            visited.add(node)
            stack.extend(reversed(graph[node]))  # Reverse for correct order

# BFS Function
def bfs(graph, start):
    visited = set()
    queue = [start]
    print("\nBFS Traversal:", end=' ')
    while queue:
        node = queue.pop(0)
        if node not in visited:
            print(node, end=' ')
            visited.add(node)
            queue.extend(graph[node])

# Main Execution
if __name__ == "__main__":
    start_node = 'A'
    dfs_iterative(graph, start_node)
    bfs(graph, start_node)
