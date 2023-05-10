n = input().split()
c = int(input())
for _ in range(c):
    first_half = []
    second_half = []

    for i in range(len(n)):
        if i < len(n) / 2:
            first_half.append(n[i])
        else:
            second_half.append(n[i])
    for m in range(c):
        shuffled = []
        first = 0
        second = 0
        for j in range(len(n)):
            if j % 2 == 0:
                shuffled.append(first_half[first])
                first += 1
            else:
                shuffled.append(second_half[second])
                second += 1
        n = shuffled


print(n)
