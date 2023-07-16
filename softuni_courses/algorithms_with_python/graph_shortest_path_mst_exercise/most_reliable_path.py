from collections import deque
from queue import PriorityQueue


class Edge:
    def __init__(self, first, second, weight):
        self.first = first
        self.second = second
        self.weight = weight


nodes = int(input())
edges = int(input())

graph = []
[graph.append([]) for _ in range(nodes)]
distance = [float('-inf')] * nodes
parent = [None] * nodes

for _ in range(edges):
    source, destination, weight = [int(x) for x in input().split()]
    edge = Edge(source, destination, weight)
    graph[source].append(edge)
    graph[destination].append(edge)

start = int(input())
end = int(input())
distance[start] = 100

que = PriorityQueue()
que.put((-100, start))

while not que.empty():
    max_distance, node = que.get()
    if node == end:
        break

    for edge in graph[node]:
        child = edge.second if edge.first == node else edge.first
        new_distance = -max_distance * edge.weight / 100
        if new_distance > distance[child]:
            distance[child] = new_distance
            parent[child] = node
            que.put((-new_distance, child))


path = deque()

print(f'Most reliable path reliability: {distance[end]:.2f}%')
node = end
while node is not None:
    path.appendleft(node)
    node = parent[node]

print(*path, sep=' -> ')