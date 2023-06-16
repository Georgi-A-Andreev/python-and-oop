def dfs(node, graph, visited, cycles):
    if node in cycles:
        raise Exception
    if node in visited:
        return
    visited.add(node)
    cycles.add(node)

    for children in graph[node]:
        dfs(children, graph, visited, cycles)

    cycles.remove(node)


nodes = {}

while True:
    row = input()
    if row == 'End':
        break

    parent, child = row.split('-')

    if parent not in nodes:
        nodes[parent] = []
    if child not in nodes:
        nodes[child] = []

    nodes[parent].append(child)

visited = set()

try:
    for node in nodes:
        dfs(node, nodes, visited, set())
    print('Acyclic: Yes')
except Exception:
    print('Acyclic: No')
