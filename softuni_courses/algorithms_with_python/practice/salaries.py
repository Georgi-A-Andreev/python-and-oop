nodes_n = int(input())
nodes = []
[nodes.append([]) for _ in range(nodes_n)]

for i in range(nodes_n):
    vectors = input()
    for idx, el in enumerate(vectors):
        if el == 'Y':
            nodes[i].append(idx)

salaries = [0] * nodes_n
result = 0


def dfs(node, nodes, salaries):
    if salaries[node] != 0:
        return salaries[node]
    if len(nodes[node]) == 0:
        salaries[node] = 1
        return 1

    salary = 0
    for child in nodes[node]:
        salary += dfs(child, nodes, salaries)

    salaries[node] = salary

    return salary


for node in range(nodes_n):
    result += dfs(node, nodes, salaries)

print(result)