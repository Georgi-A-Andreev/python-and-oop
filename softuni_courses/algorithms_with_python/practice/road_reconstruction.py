def dfs(node, visited, graph):
    if visited[node]:
        return
    visited[node] = True

    for child in graph[node]:
        dfs(child, visited, graph)


nodes = int(input())
streets = int(input())

important_streets = []
graph = []
[graph.append([]) for _ in range(nodes)]
edges = []

for _ in range(streets):
    source, destination = input().split(' - ')
    source = int(source)
    destination = int(destination)
    graph[source].append(destination)
    graph[destination].append(source)
    edges.append((min(destination, source), max(destination, source)))

print('Important streets:')
for s, d in edges:
    graph[s].remove(d)
    graph[d].remove(s)

    visited = [False] * nodes

    dfs(0, visited, graph)

    graph[s].append(d)
    graph[d].append(s)

    if all(visited):
        continue

    print(s, d)


