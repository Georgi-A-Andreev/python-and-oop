n = int(input())
w = input()

lst1 = []
lst2 = []
for i in range(n):
    s = input()
    lst1.append(s)

    if w in s:
        lst2.append(s)

print(lst1)
print(lst2)

