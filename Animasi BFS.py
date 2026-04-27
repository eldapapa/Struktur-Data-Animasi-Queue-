import time
from collections import deque

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

visited = set()
queue = deque()

start = 'A'
queue.append(start)
visited.add(start)

print("=== BFS TRAVERSAL ===\n")

while queue:
    print(f"Queue: {list(queue)}")
    node = queue.popleft()
    print(f"Proses: {node}")

    for neighbor in graph[node]:
        if neighbor not in visited:
            visited.add(neighbor)
            queue.append(neighbor)

    print(f"Visited: {visited}\n")
    time.sleep(2)
