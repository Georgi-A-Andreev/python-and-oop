def dfs(node, nodes, visited_nodes, component):
    if visited_nodes[node]:
        return

    visited_nodes[node] = True
    for child in nodes[node]:
        dfs(child, nodes, visited_nodes, component)
    component.append(node)


n = int(input())

nodes = []
visited_nodes = [False] * n
for _ in range(n):
    nodes.append(int(x) for x in input().split())

for node in range(n):
    if visited_nodes[node]:
        continue
    component = []
    dfs(node, nodes, visited_nodes, component)

    print(f'Connected component: {" ".join(str(x) for x in component)}')
