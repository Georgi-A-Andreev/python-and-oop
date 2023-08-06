from collections import deque
from queue import PriorityQueue

nodes = int(input())

graph = {}

for _ in range(nodes):
    first, second, weight_as_str = input().split(' - ')
    weight = int(weight_as_str)

    if first not in graph:
        graph[first] = []
    if second not in graph:
        graph[second] = []

    graph[first].append((weight, second))
    graph[second].append((weight, first))

removed_edges = set()
edges_to_ignore = input().split(',')
for el in edges_to_ignore:
    first, second = el.split('-')
    removed_edges.add((first, second))
    removed_edges.add((second, first))

start = input()
end = input()

distance = {key: float('inf') for key in graph.keys()}
prev = {key: None for key in graph.keys()}
distance[start] = 0

pq = PriorityQueue()
pq.put((0, start))

while not pq.empty():
    min_distance, node = pq.get()
    if node == end:
        break

    for child in graph[node]:
        if (child[-1], node) in removed_edges or (node, child[-1]) in removed_edges:
            continue
        new_distance = min_distance + child[0]
        if new_distance < distance[child[-1]]:
            distance[child[-1]] = new_distance
            prev[child[-1]] = node
            pq.put((new_distance, child[-1]))

result = deque()
node = end
while node is not None:
    result.appendleft(node)
    node = prev[node]

print(*result, sep=' - ')
print(distance[end])
