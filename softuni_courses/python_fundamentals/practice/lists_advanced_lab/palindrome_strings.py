result = []
number = 0

words = input().split()
palindrome = input()

for i in words:
    if i == i[::-1]:
        result.append(i)
    if palindrome == i:
        number += 1

print(result)
print(f"Found palindrome {number} times")
