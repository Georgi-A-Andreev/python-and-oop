names = set()

for _ in range(int(input())):
    names.add(input())

print(*names, sep='\n')
