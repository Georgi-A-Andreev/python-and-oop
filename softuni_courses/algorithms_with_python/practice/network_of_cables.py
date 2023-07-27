from queue import PriorityQueue


class Edge:
    def __init__(self, first, second, weight):
        self.first = first
        self.second = second
        self.weight = weight

    def __gt__(self, other):
        return self.weight > other.weight


budged = int(input())
nodes_count = int(input())
edges_count = int(input())

graph = {}
forest = []
total_spent = 0
edges = PriorityQueue()

for _ in range(edges_count):
    line = input().split()
    first = int(line[0])
    second = int(line[1])
    weight = int(line[2])
    edge = Edge(first, second, weight)
    if len(line) > 3:
        forest.append(first)
        forest.append(second)
    else:
        if first not in graph:
            graph[first] = []
        if second not in graph:
            graph[second] = []
        graph[first].append(edge)
        graph[second].append(edge)

for el in forest:
    for edge in graph[el]:
        edges.put(edge)

while not edges.empty():
    edge = edges.get()
    non_tree_node = -1

    if edge.first in forest and edge.second not in forest:
        non_tree_node = edge.second
    elif edge.first not in forest and edge.second in forest:
        non_tree_node = edge.first

    if non_tree_node == -1:
        continue

    if total_spent + edge.weight > budged:
        break

    forest.append(non_tree_node)
    total_spent += edge.weight
    for child in graph[non_tree_node]:
        edges.put(child)

print(f'Budget used: {total_spent}')
