n = int(input())


def find_c(n, current_sum, combination, total_combinations):
    if current_sum == n:
        new = sorted(combination,reverse=True)
        len_set = len(total_combinations)
        total_combinations.add(''.join(str(x) for x in new))
        if len(total_combinations) == len_set + 1:
            print(*new, sep=' + ')
        return
    if current_sum > n:
        return

    for i in range(n, 0, -1):
        find_c(n, current_sum + i, combination + [i], total_combinations)


find_c(n, 0, [], set())
