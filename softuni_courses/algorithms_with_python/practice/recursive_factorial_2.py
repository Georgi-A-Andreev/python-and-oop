n = int(input())


def find_recursive_fact(n):
    if n == 1:
        return 1

    return n * find_recursive_fact(n - 1)


print(find_recursive_fact(n))
