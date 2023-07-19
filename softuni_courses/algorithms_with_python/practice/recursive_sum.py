array = [int(x) for x in input().split()]


def find_sum(idx, array):
    if idx == len(array) - 1:
        return array[idx]
    result = array[idx] + find_sum(idx + 1, array)

    return result


print(find_sum(0, array))