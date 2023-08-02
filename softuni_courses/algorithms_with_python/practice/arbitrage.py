from collections import deque
from queue import PriorityQueue

edges = int(input())
graph = {}
distance = {}
prev = {}

for _ in range(edges):
    s, d, weight = input().split()
    weight = float(weight)
    if s not in graph:
        graph[s] = []
    if d not in graph:
        graph[d] = []
    distance[s] = 0
    distance[d] = 0
    prev[s] = None
    prev[s] = None

    graph[s].append((weight, d))


start = input()


distance[start] = 1

pq = PriorityQueue()
pq.put((1, start))
found = 0
while not pq.empty():
    min_distance, node = pq.get()
    if node == start and found == 1:
        break
    if node == start:
        found += 1
    for child in graph[node]:
        new_distance = min_distance * child[0]
        if new_distance > distance[child[1]]:
            distance[child[-1]] = new_distance
            prev[child[-1]] = node
            pq.put((new_distance, child[-1]))


if distance[start] > 1:
    print(True)
    path = deque()
    node = start
    counter = 0
    while counter < 2:
        if node == start:
            counter += 1
        path.appendleft(node)
        node = prev[node]

    print(*path, sep=' ')
else:
    print(False)

    path = [start]
    node = start
    while node in prev.values():
        for k, v in prev.items():
            if v == node:
                path.append(k)
                node = k

    for el in path:
        print(f'{el}: {distance[el]:.3f}')

