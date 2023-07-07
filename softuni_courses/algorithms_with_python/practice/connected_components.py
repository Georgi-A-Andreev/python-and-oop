n = int(input())

graph = []

for _ in range(n):
    graph.append([int(x) for x in input().split()])

visited = [None] * n


def dfs(graph, node, visited, component):
    if visited[node]:
        return
    visited[node] = True
    for child in graph[node]:
        dfs(graph, child, visited, component)
    component.append(node)


for node in range(len(graph)):
    if visited[node]:
        continue
    component = []
    dfs(graph, node, visited, component)
    print(f'Connected component: {" ".join(str(x) for x in component)}')
