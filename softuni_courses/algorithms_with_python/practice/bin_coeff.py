row = int(input())
col = int(input())


def find_bin(row, col, memo):
    key = (row, col)
    if row < 1 or col < 1 or col == row:
        return 1
    if key in memo:
        return memo[key]

    result = find_bin(row - 1, col - 1, memo) + find_bin(row - 1, col, memo)
    if key not in memo:
        memo[key] = result
    return result


print(find_bin(row, col, {}))

