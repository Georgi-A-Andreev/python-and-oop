count = int(input())
names = set()
for _ in range(count):
    names.add(input())

print(*names, sep='\n')
