class Edge:
    def __init__(self, first, second, weight):
        self.weight = weight
        self.second = second
        self.first = first


def find_root(node, parent):
    while node != parent[node]:
        node = parent[node]
    return node


max_node = float('-inf')
edges = int(input())
graph = []

for _ in range(edges):
    first, second, weight = [int(x) for x in input().split(', ')]
    graph.append(Edge(first, second, weight))
    max_node = max(first, second, max_node)

parent = [num for num in range(max_node + 1)]
forest = []
for edge in sorted(graph, key=lambda x: x.weight):
    first_node_root = find_root(edge.first, parent)
    second_node_root = find_root(edge.second, parent)
    if first_node_root != second_node_root:
        parent[first_node_root] = second_node_root
        forest.append(edge)

for edge in forest:
    print(f'{edge.first} - {edge.second}')
