def find_node_without_dependencies(dependencies, graph):
    for k in dependencies:
        if dependencies[k] == 0:
            dependencies.pop(k)
            for child in graph[k]:
                dependencies[child] -= 1

            return k
    return None


def find_dependencies(dependencies, graph):
    for k, v in graph.items():
        if k not in dependencies:
            dependencies[k] = 0
        for child in v:
            if child not in dependencies:
                dependencies[child] = 0
            dependencies[child] += 1


nodes = int(input())
graph = {}

for _ in range(nodes):
    source, destination = input().split(' ->')

    graph[source] = [x.strip() for x in destination.split(', ')] if destination else []


dependencies = {}


find_dependencies(dependencies, graph)
result = []
while dependencies:
    node = find_node_without_dependencies(dependencies, graph)
    if node is None:
        print('Invalid topological sorting')
        break
    result.append(node)
else:
    print(f'Topological sorting: {", ".join(result)}')
