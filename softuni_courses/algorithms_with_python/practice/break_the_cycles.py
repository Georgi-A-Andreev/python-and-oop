nodes = int(input())

graph = {}
edges_to_remove = []
visited = set()

for _ in range(nodes + 1):
    first, second = input().split(' -> ')
    graph[int(first)] = second.split()
