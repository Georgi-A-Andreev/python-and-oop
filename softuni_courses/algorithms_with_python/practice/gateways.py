from collections import deque

nodes = int(input())
edges = int(input())


graph = []
[graph.append([]) for _ in range(nodes + 1)]
visited = [False] * (nodes + 1)
prev = [None] * (nodes + 1)

for _ in range(edges):
    first, second = [int(x) for x in input().split()]
    graph[first].append(second)


start = int(input())
visited[start] = True
end = int(input())

queue = deque()
queue.append(start)
while queue:
    node = queue.popleft()
    if node == end:
        break

    for child in graph[node]:
        if visited[child]:
            continue
        visited[child] = True
        queue.append(child)
        prev[child] = node

if not visited[end]:
    pass
else:
    path = deque()
    node = end

    while node is not None:
        path.appendleft(node)
        node = prev[node]

    print(*path, sep=' ')
