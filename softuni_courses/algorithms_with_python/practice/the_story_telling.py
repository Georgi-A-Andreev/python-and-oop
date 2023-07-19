from collections import deque

graph = {}

while True:
    text = input()

    if text == 'End':
        break

    source, destination = text.split(' ->')

    graph[source] = destination.split()

dependencies = {}


def find_dependencies(dependencies, graph):
    for k, v in graph.items():
        if k not in dependencies:
            dependencies[k] = 0
        for el in v:
            if el not in dependencies:
                dependencies[el] = 0
            dependencies[el] += 1

    return dependencies


find_dependencies(dependencies, graph)


def find_node_to_remove(dependencies):
    best_node = None
    for k, v in dependencies.items():
        if v == 0:
            best_node = k
    for el in graph[best_node]:
        dependencies[el] -= 1

    dependencies.pop(best_node)
    return best_node


path = deque()
while dependencies:
    node = find_node_to_remove(dependencies)
    path.append(node)

print(*path, sep=' ')
