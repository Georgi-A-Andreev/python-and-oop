n = int(input())

graph = []

for _ in range(n):
    graph.append([int(x) for x in input().split()])

visited = [None] * n
components = []


def dfs(node, graph, components, visited):
    if visited[node]:
        return

    visited[node] = True

    for child in graph[node]:
        dfs(child, graph, components, visited)
    components.append(node)


for node in range(len(graph)):
    if visited[node]:
        continue
    components = []
    dfs(node, graph, components, visited)
    print(f'Connected component: {" ".join(str(x) for x in components)}')
