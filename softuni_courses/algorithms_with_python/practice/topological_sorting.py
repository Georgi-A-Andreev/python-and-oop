
n = int(input())
graph = {}

for _ in range(n):
    line = input().split(' ->')
    a = line.pop(0)
    graph[a] = line[-1].strip().split(', ')
    if graph[a] == ['']:
        graph[a] = []


def get_predeccesors(graph):
    result = {}
    for  k, v in graph.items():
        if k not in result:
            result[k] = 0

        for child in v:
            if child not in result:
                result[child] = 0
            result[child] += 1

    return result


dependencies = get_predeccesors(graph)


def find_node_without_dep(dependencies):
    for k, v in dependencies.items():
        if v == 0:
            return k
    return None


result = []
cycle = False
while dependencies:
    node_to_remove = find_node_without_dep(dependencies)
    if node_to_remove is None:
        cycle = True
        break
    result.append(node_to_remove)
    dependencies.pop(node_to_remove)
    for child in graph[node_to_remove]:
        dependencies[child] -= 1

if cycle:
    print('Invalid topological sorting')
else:
    print(f"Topological sorting: {', '.join(result)}")