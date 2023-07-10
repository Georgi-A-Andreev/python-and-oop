from collections import deque
from queue import PriorityQueue

edges = int(input())
graph = {}

for _ in range(edges):
    s, d, weight = [int(x) for x in input().split(', ')]

    if s not in graph:
        graph[s] = []
    if d not in graph:
        graph[d] = []

    graph[s].append((weight, d))
    graph[d].append((weight, s))

start = int(input())
finish = int(input())

max_node = max(graph.keys())
distance = [float('inf')] * (max_node + 1)
prev = [None] * (max_node + 1)

distance[start] = 0

pq = PriorityQueue()
pq.put((0, start))

while not pq.empty():
    min_distance, node = pq.get()
    if node == finish:
        break

    for child in graph[node]:
        new_distance = min_distance + child[0]
        if new_distance < distance[child[-1]]:
            distance[child[-1]] = new_distance
            prev[child[-1]] = node
            pq.put((new_distance, child[-1]))

if distance[finish] == float('inf'):
    print('There is no such path.')
else:
    result = deque()
    node = finish
    while node is not None:
        result.appendleft(node)
        node = prev[node]

    print(distance[finish])
    print(*result, sep=' ')