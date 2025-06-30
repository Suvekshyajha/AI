# Full graph with all nodes defined
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

# Iterative DFS function
def dfs_iterative(graph, start):
    visited = set()         # Set to keep track of visited nodes
    stack = [start]         # Stack to control the order of visiting

    while stack:
        node = stack.pop()  # Pop the last node added
        if node not in visited:
            print(node, end=' ')   # Visit the node
            visited.add(node)      # Mark as visited
            # Add neighbors in reverse to maintain order
            stack.extend(reversed(graph[node]))

# Main driver code
if __name__ == "__main__":
    print("DFS Iterative Traversal:")
    dfs_iterative(graph, 'A')
