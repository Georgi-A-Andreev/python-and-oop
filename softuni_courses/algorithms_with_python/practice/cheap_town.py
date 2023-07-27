class Edge:
    def __init__(self, first, second, weight):
        self.first = first
        self.second = second
        self.weight = weight

    def __gt__(self, other):
        return self.weight > other.weight


cities_count = int(input())
edges_count = int(input())

edges = []

for _ in range(edges_count):
    first, second, weight = [int(x) for x in input().split(' - ')]
    edges.append(Edge(first, second, weight))

prev = [num for num in range(cities_count)]
forest = set()


def find_root(node, prev):
    while node != prev[node]:
        node = prev[node]
    return node


result = 0
for edge in sorted(edges, key=lambda x: x.weight):
    first_root = find_root(edge.first, prev)
    second_root = find_root(edge.second, prev)
    if first_root == second_root:
        continue
    prev[first_root] = second_root
    result += edge.weight

print(f'Total cost: {result}')