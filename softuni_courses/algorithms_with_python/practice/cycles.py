def dfs(node, graph, cycle):
    if node in cycle:
        raise Exception
    cycle.add(node)

    for child in graph[node]:
        dfs(child, graph, cycle)
    cycle.remove(node)


graph = {}

while True:
    text = input()

    if text == 'End':
        break

    source, destination = text.split('-')
    if source not in graph:
        graph[source] = []
    if destination not in graph:
        graph[destination] = []
    graph[source].append(destination)


has_cycle = False


try:
    for node in graph:
        dfs(node, graph, set())
    print('Acyclic: Yes')
except Exception:
    print('Acyclic: No')