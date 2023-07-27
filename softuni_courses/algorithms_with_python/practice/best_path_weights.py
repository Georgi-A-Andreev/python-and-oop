from collections import deque
from queue import PriorityQueue


nodes = int(input())
edges_count = int(input())

graph = {}

for _ in range(edges_count):
    first, second, weight = [int(x) for x in input().split()]
    if first not in graph:
        graph[first] = []
    if second not in graph:
        graph[second] = []
    graph[first].append((weight, second))
    graph[second].append((weight, first))

start = int(input())
end = int(input())

pq = PriorityQueue()
pq.put((-100, start))
distance = [float('-inf')] * nodes
distance[start] = 100
prev = [None] * nodes

while not pq.empty():
    old_distance, node = pq.get()
    if node == end:
        break
    for child in graph[node]:
        new_distance, destination = child
        total_new_distance = (-old_distance * new_distance) / 100
        if total_new_distance > distance[destination]:
            distance[destination] = total_new_distance
            prev[destination] = node
            pq.put((-total_new_distance, destination))

print(f'Most reliable path reliability: {distance[end]:.2f}%')
path = deque()
node = end
while node is not None:
    path.appendleft(node)
    node = prev[node]

print(*path, sep=' -> ')