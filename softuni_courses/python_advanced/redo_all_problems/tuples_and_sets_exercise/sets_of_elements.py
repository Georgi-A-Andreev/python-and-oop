lengths = [int(x) for x in input().split()]
first = set()
second = set()

for _ in range(lengths[0]):
    first.add(input())

for _ in range(lengths[1]):
    second.add(input())

print(*first.intersection(second), sep='\n')

