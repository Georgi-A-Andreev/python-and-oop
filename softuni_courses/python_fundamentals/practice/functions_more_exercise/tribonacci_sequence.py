def tribonacci_sequence(integer):
    result = []
    a = 1
    b = 1
    c = 2

    for i in range(integer - 3):
        result.append(a + b + c)
        a, b, c = b, c, a + b + c

    if integer == 1:
        return 1

    if integer == 2:
        return '1 1'

    if integer == 3:
        return '1 1 2'

    return f'1 1 2 {" ".join(str(x) for x in result)}'


n = int(input())

print(tribonacci_sequence(n))