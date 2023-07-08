def get_dependencies(graph, dependencies):
    for source, destination in graph.items():
        if source not in dependencies:
            dependencies[source] = 0
        for d in destination:
            if d not in dependencies:
                dependencies[d] = 0

            dependencies[d] += 1


x = int(input())

graph = {}
dependencies = {}
end_result = []

for line in range(x):
    nodes = input()
    if nodes.endswith('->'):
        graph[nodes.split(' ')[0]] = []
        continue

    s, d = nodes.split(' -> ')
    if s not in graph:
        graph[s] = d.split(', ')


get_dependencies(graph, dependencies)


def find_node_to_remove(dependencies, graph):
    for k, v in dependencies.items():
        if v == 0:
            dependencies.pop(k)
            for el in graph[k]:
                dependencies[el] -= 1
            return k
    return None


has_cycle = False
while dependencies:
    result = find_node_to_remove(dependencies, graph)
    if result is None:
        has_cycle = True
    end_result.append(result)

if has_cycle:
    print('Invalid topological sorting')
else:
    print(f'Topological sorting: {", ".join(end_result)}')
