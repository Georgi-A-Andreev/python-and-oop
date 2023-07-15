from collections import deque
from functools import reduce
from queue import PriorityQueue


class Edge:
    def __init__(self, first, second, weight):
        self.first = first
        self.second = second
        self.weight = weight

    def __lt__(self, other):
        return self.weight > other.weight


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
distance[start] = 0

que = PriorityQueue()
que.put((100, start))

while que:
    node = que.get()
    if node == end:
        break

    for child, weight in graph[node]:
        que.put(child)
        if distance[child] < weight:
            distance[child] = weight
            parent[child] = node

path = deque()
reliability = []

print(parent)
print(distance)
