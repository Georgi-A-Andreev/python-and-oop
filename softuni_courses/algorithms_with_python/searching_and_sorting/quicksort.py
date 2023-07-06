line = [int(x) for x in input().split()]


def quicksort(line, start, end):
    if end <= start:
        return
    pivot = start
    left = start + 1
    right = end
    while right >= left:
        if line[left] > line[pivot] > line[right]:
            line[left], line[right] = line[right], line[left]
        if line[left] < line[pivot]:
            left += 1
        if line[right] > line[pivot]:
            right -= 1

    line[pivot], line[right] = line[right], line[pivot]

    quicksort(line, start, right - 1)
    quicksort(line, right + 1, end)


quicksort(line, 0, len(line) - 1)
print(' '.join(str(x) for x in line))
