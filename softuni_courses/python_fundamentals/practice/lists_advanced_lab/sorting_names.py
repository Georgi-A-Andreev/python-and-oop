name_list = input().split(', ')

print(sorted(name_list, key=lambda x: (-len(x), x)))

