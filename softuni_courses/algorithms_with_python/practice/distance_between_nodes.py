from collections import deque

nodes = int(input())
pairs_to_check = int(input())

graph = {}
for _ in range(nodes):
    source, destination = input().split(':')
    source = int(source)
    graph[source] = [int(x) for x in destination.split()]


for _ in range(pairs_to_check):
    start, end = [int(x) for x in input().split('-')]
    que = deque([start])
    visited = {start}
    prev = {start: None}

    while que:
        node = que.popleft()
        if node == end:
            break
        for child in graph[node]:
            if child in visited:
                continue
            visited.add(child)
            prev[child] = node
            que.append(child)
    if end not in prev:
        print(f'{{{start}, {end}}} -> -1')
        continue

    counter = -1
    node = end
    while node is not None:
        node = prev[node]
        counter += 1

    print(f'{{{start}, {end}}} -> {counter}')
