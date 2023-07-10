from collections import deque

nodes_c = int(input())
edges_c = int(input())

nodes = []
[nodes.append([]) for _ in range(nodes_c + 1)]

for _ in range(edges_c):
    s, d = [int(x) for x in input().split()]

    nodes[s].append(d)

start = int(input())
destination = int(input())

visited = [False] * (nodes_c + 1)
parent = [None] * (nodes_c + 1)

visited[start] = True
queue = deque([start])

while queue:
    node = queue.popleft()
    if node == destination:
        break

    for child in nodes[node]:
        if visited[child]:
            continue
        visited[child] = True
        queue.append(child)
        parent[child] = node

result = deque()
node = destination
while node is not None:
    result.appendleft(node)
    node = parent[node]


print(f'Shortest path length is: {len(result) - 1}')
print(*result, sep=' ')
