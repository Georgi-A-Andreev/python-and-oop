n = [int(x) for x in input().split(", ")]

if max(n) % 10 == 0:
    maxx = max(n) // 10
else:
    maxx = max(n) // 10 + 1

boundary = 10
min_boundary = 1
for i in range(maxx):
    result = []
    for j in n:
        if min_boundary <= j <= boundary:
            result.append(j)

    print(f"Group of {boundary}'s: {result}")
    boundary += 10
    min_boundary += 10
