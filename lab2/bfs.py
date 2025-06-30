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
def bfs(graph,start):
    visited=set()
    stack=[start]
    while stack :
        node = stack.pop()  # Pop the last node added
        if node not in visited:
            print(node, end=' ')   # Visit the node
            visited.add(node)
            stack.extend(graph[node])

if __name__ == "__main__":
    print("BFS  Traversal:")
    bfs(graph, 'A')
    