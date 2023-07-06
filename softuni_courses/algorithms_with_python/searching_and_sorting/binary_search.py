line = [int(x) for x in input().split()]
target = int(input())


def binary(line, target):
    left = 0
    right = len(line) - 1

    while left <= right:
        mid_index = (left + right) // 2
        mid_el = line[mid_index]

        if mid_el == target:
            return mid_index

        if target < mid_el:
            right = mid_index - 1
        else:
            left = mid_index + 1

    return -1


print(binary(line, target))
