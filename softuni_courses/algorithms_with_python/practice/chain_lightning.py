from queue import PriorityQueue


def calc_dmg(jumps, damage):
    for _ in range(jumps):
        damage //= 2

    return damage


def prim(node, damage, graph, damage_by_node):
    damage_by_node[node] += damage
    tree = {node}
    jumps = [0] * len(graph)
    pq = PriorityQueue()
    [pq.put(edge) for edge in graph[node]]
    while not pq.empty():
        min_edge = pq.get()
        non_tree_node, tree_node = -1, -1
        if min_edge.first in tree and min_edge.second not in tree:
            tree_node, non_tree_node = min_edge.first, min_edge.second
        elif min_edge.first not in tree and min_edge.second in tree:
            tree_node, non_tree_node = min_edge.second, min_edge.first

        if non_tree_node == -1:
            continue

        jumps[non_tree_node] = jumps[tree_node] + 1
        damage_by_node[non_tree_node] += calc_dmg(jumps[non_tree_node], damage)
        tree.add(non_tree_node)
        for edge in graph[non_tree_node]:
            pq.put(edge)


class Edge:
    def __init__(self, first, second, weight):
        self.weight = weight
        self.second = second
        self.first = first

    def __gt__(self, other):
        return self.weight > other.weight


nodes = int(input())
edges_count = int(input())
hits = int(input())
graph = {node: [] for node in range(nodes)}


for _ in range(edges_count):
    first, second, weight = [int(x) for x in input().split()]
    edge = Edge(first, second, weight)
    graph[first].append(edge)
    graph[second].append(edge)


damage_by_node = [0] * nodes
for _ in range(hits):
    node, damage = [int(x) for x in input().split()]
    prim(node, damage, graph, damage_by_node)

print(max(damage_by_node))
