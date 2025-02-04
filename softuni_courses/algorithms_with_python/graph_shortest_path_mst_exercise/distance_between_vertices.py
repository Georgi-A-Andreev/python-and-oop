from collections import deque


nodes = int(input())
pairs = int(input())

graph = {}

for _ in range(nodes):
    s, d = input().split(':')
    s = int(s)
    graph[s] = [int(x) for x in d.split()] if d != '' else []


for _ in range(pairs):
    start, end = [int(x) for x in input().split('-')]
    que = deque([start])
    visited = {start}
    parent = {start: None}

    while que:
        node = que.popleft()
        if node == end:
            break
        for child in graph[node]:
            if child in visited:
                continue
            que.append(child)
            visited.add(child)
            parent[child] = node

    if end not in parent:
        print(f'{{{start}, {end}}} -> -1')
        continue

    counter = -1
    node = end
    while node is not None:
        node = parent[node]
        counter += 1

    print(f'{{{start}, {end}}} -> {counter}')
