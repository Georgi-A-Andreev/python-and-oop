def get_predecessors_count(vertex):
    result = {}
    for node, child in vertex.items():
        if node not in result:
            result[node] = 0

        for c in child:
            if c not in result:
                result[c] = 1
            else:
                result[c] += 1

    return result


def find_node_without_dependencies(dependencies):
    for node, deps in dependencies.items():
        if deps == 0:
            return node
    return None


nodes = int(input())

vertex = {}

for _ in range(nodes):
    key = input().split('->')
    value = key[-1].strip().split(', ')
    key = key[0].strip()
    if value[0] == '':
        value = []
    vertex[key] = value

dependencies = get_predecessors_count(vertex)

has_cycle = False
sorted_nodes = []

while dependencies:
    node_to_remove = find_node_without_dependencies(dependencies)
    if node_to_remove is None:
        has_cycle = True
        break
    sorted_nodes.append(node_to_remove)
    dependencies.pop(node_to_remove)
    for child in vertex[node_to_remove]:
        dependencies[child] -= 1

if not has_cycle:
    print(f'Topological sorting: {", ".join(sorted_nodes)}')
else:
    print("Invalid topological sorting")