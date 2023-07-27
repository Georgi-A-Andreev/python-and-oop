from collections import deque

nodes_count = int(input())
edges_count = int(input())

graph = []

for _ in range(edges_count):
    first, second, weight = [int(x) for x in input().split()]
    graph.append((first, second, weight))

start = int(input())
end = int(input())

distance = [float('inf')] * (nodes_count + 1)
distance[start] = 0
prev = [None] * (nodes_count + 1)

for _ in range(nodes_count - 1):
    for edge in graph:
        first, second, weight = edge
        if distance[first] == float('inf'):
            continue
        if distance[second] > distance[first] + weight:
            distance[second] = distance[first] + weight
            prev[second] = first

for edge in graph:
    first, second, weight = edge
    if distance[second] > distance[first] + weight:
        print('Undefined')
        break
else:
    path = deque()
    node = end
    while node is not None:
        path.appendleft(node)
        node = prev[node]

    print(*path, sep=' ')
    print(distance[end])