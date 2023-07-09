nodes = int(input())
total_edges_to_remove = 0
total_edges = []
graph = {}
edges = []
for _ in range(nodes):
    source, destination = input().split(' -> ')
    graph[source] = destination.split()
    for edge in destination.split():
        edges.append((source, edge))


def dfs(node, graph, visited):
    if node in visited:
        return
    visited.add(node)

    for child in graph[node]:
        dfs(child, graph, visited)


def path_exits(source, destination, graph):
    visited = set()

    dfs(source, graph, visited)

    return destination in visited


for source, destination in sorted(edges, key=lambda x: (x[0], x[1])):
    if destination not in graph[source] or source not in graph[destination]:
        continue
    graph[source].remove(destination)
    graph[destination].remove(source)

    if path_exits(source, destination, graph):
        total_edges_to_remove += 1
        total_edges.append(f'{source} - {destination}')
    else:
        graph[source].append(destination)
        graph[destination].append(source)

print(f'Edges to remove: {total_edges_to_remove}')
for el in total_edges:
    print(el)