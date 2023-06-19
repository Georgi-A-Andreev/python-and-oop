def dfs(node, graph, visited):
    if node in visited:
        return
    visited.add(node)
    for child in graph[node]:
        dfs(child, graph, visited)


def path_exist(source, destination, graph):
    visited = set()

    dfs(source, graph, visited)

    return destination in visited


nodes = int(input())

graph = {}
edges = []
for _ in range(nodes):
    node, children = input().split(" -> ")
    children = children.split()
    graph[node] = children
    for c in children:
        edges.append((node, c))

removed_edges = []
for source, destination in sorted(edges, key=lambda x: (x[0], x[1])):
    if destination not in graph[source] or source not in graph[destination]:
        continue
    graph[source].remove(destination)
    graph[destination].remove(source)

    if path_exist(source, destination, graph):
        removed_edges.append((source, destination))
    else:
        graph[source].append(destination)
        graph[destination].append(source)

print(f'Edges to remove: {len(removed_edges)}')
for el in removed_edges:
    print(' - '.join(el))
