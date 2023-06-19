def dfs(node, graph, visited):
    if visited[node]:
        return
    visited[node] = True
    for child in graph[node]:
        dfs(child, graph, visited)


nodes = int(input())
edges = int(input())

graph = []
[graph.append([]) for _ in range(nodes)]

important_streets = []
edges_total = []
for _ in range(edges):
    first, seconds = [int(x) for x in input().split(" - ")]
    graph[first].append(seconds)
    graph[seconds].append(first)
    edges_total.append((min(first, seconds), max(first, seconds)))

print('Important streets:')
for f, s in edges_total:
    graph[f].remove(s)
    graph[s].remove(f)

    visited = [False] * nodes
    dfs(0, graph, visited)

    if not all(visited):
        important_streets.append((f, s))

    graph[f].append(s)
    graph[s].append(f)

for el in important_streets:
    print(' '.join(str(x) for x in el))
