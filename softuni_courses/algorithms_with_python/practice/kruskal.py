from queue import PriorityQueue


class Edge:
    def __init__(self, first, second, weight):
        self.weight = weight
        self.second = second
        self.first = first

    def __gt__(self, other):
        return self.weight > other.weight


edges = int(input())
graph = PriorityQueue()

for _ in range(edges):
    first, second, weight = [int(x) for x in input().split(', ')]
    graph.put(Edge(first, second, weight))

forest = set()
while not graph.empty():
    edge = graph.get()
    if edge.first in forest and edge.second in forest:
        continue
    forest.add(edge.first)
    forest.add(edge.second)
    print(f'{edge.first} - {edge.second}')
