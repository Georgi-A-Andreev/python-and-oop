first = set()
second = set()

n, m = input().split()
[first.add(int(input())) for _ in range(int(n))]
[second.add(int(input())) for _ in range(int(m))]

print(*first.intersection(second), sep='\n')
