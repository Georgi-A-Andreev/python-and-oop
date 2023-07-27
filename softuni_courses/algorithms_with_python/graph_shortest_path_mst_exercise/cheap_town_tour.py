class Edge:
    def __init__(self, first, second, weight):
        self.first = first
        self.second = second
        self.weight = weight


nodes = int(input())
edges = int(input())

graph = []

for _ in range(edges):
    first, second, weight = [int(x) for x in input().split(' - ')]
    edge = Edge(first, second, weight)
    graph.append(edge)

parent = [x for x in range(nodes)]
total_cost = 0


def find_root(parent, node):
    while node != parent[node]:
        node = parent[node]
    return node


for edge in sorted(graph, key=lambda x: x.weight):
    first_node_root = find_root(parent, edge.first)
    second_node_root = find_root(parent, edge.second)

    if first_node_root == second_node_root:
        continue

    parent[first_node_root] = second_node_root
    total_cost += edge.weight

print(f'Total cost: {total_cost}')