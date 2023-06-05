def vectors(idx, n):
    if idx == len(n):
        print(*n, sep='')
        return

    for i in range(2):

        n[idx] = i
        vectors(idx + 1, n)


n = [0] * int(input())

vectors(0, n)
