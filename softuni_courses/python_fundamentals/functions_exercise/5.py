def my_f(n3):
    if n3 % 2 == 0:
        return True
    return False


n = input().split()
n1 = []

for i in n:
    n1.append(int(i))

x = filter(my_f, n1)
print(list(x))
