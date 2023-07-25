def dfs(node, graph, visited):
    if node in visited:
        return
    visited.add(node)
    for child in graph[node]:
        dfs(child, graph, visited)


def have_path(source, destination, graph):
    visited = set()

    dfs(source, graph, visited)

    return destination in visited


nodes = int(input())

edges = []
graph = {}
edges_to_remove = []

for _ in range(nodes):
    first, second = input().split(' -> ')
    graph[first] = second.split()
    for el in second.split():
        edges.append((first, el))


for edge in sorted(edges, key=lambda x: (x[0], x[1])):
    source, destination = edge
    if source not in graph[destination] or destination not in graph[source]:
        continue
    graph[source].remove(destination)
    graph[destination].remove(source)
    if have_path(source, destination, graph):
        edges_to_remove.append(f'{source} - {destination}')
    else:
        graph[source].append(destination)
        graph[destination].append(source)


print(f'Edges to remove: {len(edges_to_remove)}')
for el in edges_to_remove:
    print(el)
