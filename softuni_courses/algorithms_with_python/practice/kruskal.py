class Edge:
    def __init__(self, first, second, weight):
        self.first = first
        self.second = second
        self.weight = weight


def find_root(node, prev):
    while node != prev[node]:
        node = prev[node]
    return node


edges_count = int(input())
max_node = float('-inf')
edges = []

for _ in range(edges_count):
    first, second, weight = [int(x) for x in input().split(', ')]
    edges.append(Edge(first, second, weight))
    max_node = max(first, second, max_node)

prev = [num for num in range(max_node + 1)]
forest = []


for edge in sorted(edges, key=lambda x: x.weight):
    first_node_root = find_root(edge.first, prev)
    second_node_root = find_root(edge.second, prev)
    if first_node_root != second_node_root:
        prev[first_node_root] = second_node_root
        forest.append(edge)

for edge in forest:
    print(f'{edge.first} - {edge.second}')