def possible_permutations(lst):
    if len(lst) <= 1:
        yield lst
        return
    for perm in possible_permutations(lst[1:]):
        for i in range(len(lst)):
            yield perm[:i] + lst[0:1] + perm[i:]


[print(n) for n in possible_permutations([1, 2, 3])]
