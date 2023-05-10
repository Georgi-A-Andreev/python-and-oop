def get_primes(lst):

    for i in lst:
        is_prime = True
        for num in range(2, i):
            if i % num == 0:
                is_prime = False
        if is_prime and i >= 2:
            yield i


print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))
print(list(get_primes([-2, 0, 0, 1, 1, 0])))