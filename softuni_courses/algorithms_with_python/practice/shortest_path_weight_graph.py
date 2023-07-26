from collections import deque
from queue import PriorityQueue

edges = int(input())
graph = {}

for _ in range(edges):
    first, second, weight = [int(x) for x in input().split(', ')]
    if first not in graph:
        graph[first] = []
    if second not in graph:
        graph[second] = []
    graph[first].append((weight, second))
    graph[second].append((weight, first))

max_node = max(graph.keys())

prev = [None] * (max_node + 1)
distance = [float('inf')] * (max_node + 1)

start = int(input())
destination = int(input())
distance[start] = 0

pq = PriorityQueue()
pq.put((0, start))

while not pq.empty():
    old_distance, node = pq.get()
    if node == destination:
        break
    for weight, child in graph[node]:
        new_distance = old_distance + weight
        if new_distance < distance[child]:
            distance[child] = new_distance
            prev[child] = node
            pq.put((new_distance, child))

if distance[destination] == float('inf'):
    print('There is no such path.')
else:
    path = deque()
    node = destination
    while node is not None:
        path.appendleft(node)
        node = prev[node]
    print(distance[destination])
    print(*path, sep=' ')
