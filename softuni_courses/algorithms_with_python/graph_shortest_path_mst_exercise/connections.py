from queue import PriorityQueue


class Edge:
    def __init__(self, first, second, weight):
        self.first = first
        self.second = second
        self.weight = weight

    def __gt__(self, other):
        return self.weight > other.weight


budged = int(input())
nodes = int(input())
edges = int(input())

graph = []
[graph.append([]) for _ in range(nodes)]

tree = set()
for _ in range(edges):
    edge_data = input().split()
    first, second, weight = int(edge_data[0]), int(edge_data[1]), int(edge_data[2])
    edge = Edge(first, second, weight)
    graph[first].append(edge)
    graph[second].append(edge)

    if len(edge_data) == 4:
        tree.add(first)
        tree.add(second)

pq = PriorityQueue()
for node in tree:
    for edge in graph[node]:
        pq.put(edge)

budged_used = 0
while not pq.empty():
    min_edge = pq.get()
    non_tree_node = None

    if min_edge.first in tree and min_edge.second not in tree:
        non_tree_node = min_edge.second
    elif min_edge.second in tree and min_edge.first not in tree:
        non_tree_node = min_edge.first

    if non_tree_node is None:
        continue

    if budged_used + min_edge.weight > budged:
        break

    budged_used += min_edge.weight
    tree.add(non_tree_node)
    for edge in graph[non_tree_node]:
        pq.put(edge)

print(f'Budget used: {budged_used}')
