def dfs(node, graph, visited):
    if visited[node]:
        return
    visited[node] = True

    for child in graph[node]:
        dfs(child, graph, visited)


def find_path(source, graph):
    visited = [False] * len(graph)

    dfs(source, graph, visited)

    return all(visited)


nodes = int(input())
edges_count = int(input())
important_streets = []
graph = []
[graph.append([]) for _ in range(nodes)]
edges = []

for _ in range(edges_count):
    first, second = [int(x) for x in input().split(' - ')]
    edges.append((min(first, second), max(first, second)))
    graph[first].append(second)
    graph[second].append(first)


for edge in sorted(edges, key=lambda x: (x[0], x[1])):
    source, destination = edge[0], edge[1]
    if source not in graph[destination] or destination not in graph[source]:
        continue
    graph[source].remove(destination)
    graph[destination].remove(source)

    if not find_path(source, graph):
        important_streets.append(f'{source} {destination}')
    graph[source].append(destination)
    graph[destination].append(source)

print('Important streets:')
for el in important_streets:
    print(el)
