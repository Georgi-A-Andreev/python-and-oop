from collections import deque

nodes_c = int(input())
edges_c = int(input())

nodes = []
[nodes.append([]) for _ in range(nodes_c + 1)]

for _ in range(edges_c):
    s, d = [int(x) for x in input().split()]

    nodes[s].append(d)

start = int(input())


visited = [False] * (nodes_c + 1)
parent = [None] * (nodes_c + 1)

visited[start] = True
queue = deque([start])

while queue:
    node = queue.popleft()

    for child in nodes[node]:
        if visited[child]:
            continue
        visited[child] = True
        queue.append(child)
        parent[child] = node


for i in range(1, len(visited)):
    if not visited[i]:
        print(i, end=' ')