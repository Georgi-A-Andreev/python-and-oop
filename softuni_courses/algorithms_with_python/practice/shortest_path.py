from collections import deque

nodes = int(input())
edges_count = int(input())

graph = []
[graph.append([]) for _ in range(nodes + 1)]

for _ in range(edges_count):
    first, second = [int(x) for x in input().split()]
    graph[first].append(second)
    graph[second].append(first)


start = int(input())
end = int(input())

visited = [False] * (nodes + 1)
prev = [None] * (nodes + 1)
queue = deque([start])

while queue:
    node = queue.popleft()
    if node == end:
        break

    visited[node] = True
    for child in graph[node]:
        if visited[child]:
            continue
        visited[child] = True
        queue.append(child)
        prev[child] = node

path = deque()
node = end
while node is not None:
    path.appendleft(node)
    node = prev[node]

print(f'Shortest path length is: {len(path) - 1}')
print(*path, sep=' ')
