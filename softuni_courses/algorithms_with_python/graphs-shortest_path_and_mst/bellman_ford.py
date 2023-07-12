from collections import deque


class Edge:
    def __init__(self, source, destination, weight):
        self.destination = destination
        self.source = source
        self.weight = weight


n = int(input())
e = int(input())

graph = []
path = deque()
for _ in range(e):
    s, d, w = [int(x) for x in input().split()]
    graph.append(Edge(s, d, w))

start = int(input())
end = int(input())

distance = [float('inf')] * (n + 1)
parent = [None] * (n + 1)
distance[start] = 0

for _ in range(n - 1):
    updated = False
    for edge in graph:
        if distance[edge.source] == float('inf'):
            continue
        new_distance = distance[edge.source] + edge.weight
        if new_distance < distance[edge.destination]:
            distance[edge.destination] = new_distance
            parent[edge.destination] = edge.source
            updated = True
    if not updated:
        break

for edge in graph:
    new_distance = distance[edge.source] + edge.weight
    if new_distance < distance[edge.destination]:
        print('Negative Cycle Detected')
        break
else:
    current = end
    while current is not None:
        path.appendleft(current)
        current = parent[current]

    print(*path, sep=' ')
    print(distance[end])
