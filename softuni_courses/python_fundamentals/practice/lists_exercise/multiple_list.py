factor = int(input())
count = int(input())

lst = []

for i in range(factor, factor * count + 1, factor):
    lst.append(i)

print(lst)
