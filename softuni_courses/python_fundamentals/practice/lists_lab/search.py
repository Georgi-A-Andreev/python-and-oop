n = int(input())
word = input()

lst = []

for i in range(n):
    lst.append(input())

print(lst)
print([i for i in lst if word in i])
