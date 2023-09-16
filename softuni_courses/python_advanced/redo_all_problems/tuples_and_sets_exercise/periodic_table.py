count = int(input())
elements = set()
for _ in range(count):
    el = input().split()
    for e in el:
        elements.add(e)

print(*elements, sep='\n')