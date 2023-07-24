def dfs(node, graph, visited):
    if visited[node]:
        return 0
    if not graph[node]:
        return 1
    result = 0
    for child in graph[node]:
        result += dfs(child, graph, visited)

    return result


nodes = int(input())
graph = []
[graph.append([]) for _ in range(nodes)]
for row in range(nodes):
    for idx, el in enumerate(input()):
        if el == 'Y':
            graph[row].append(idx)

visited = [False] * nodes


total_salary = 0
for node in range(nodes):
    total_salary += dfs(node, graph, visited)

print(total_salary)
