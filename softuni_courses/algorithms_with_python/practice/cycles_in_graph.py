def find_dependencies(dependencies, vectors):
    for source, destination in vectors:
        if source not in dependencies:
            dependencies[source] = 0
        if destination not in dependencies:
            dependencies[destination] = 0

        dependencies[destination] += 1


cycle = False
vectors = []
dependencies = {}
while True:
    vector = input()
    if vector == 'End':
        break
    vectors.append(vector.split('-'))

find_dependencies(dependencies, vectors)


def find_node_to_remove(dependencies):
    for k, v in dependencies.items():
        if v == 0:
            return k
    return None


while dependencies:
    node = find_node_to_remove(dependencies)
    if node is None:
        cycle = True
        break
    dependencies.pop(node)
    for s, d in vectors:
        if s == node:
            dependencies[d] -= 1

if cycle:
    print('Acyclic: No')
else:
    print('Acyclic: Yes')
