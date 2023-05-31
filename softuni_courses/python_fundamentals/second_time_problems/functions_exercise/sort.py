def sort_a_list(a):
    return sorted(int(i) for i in a.split())


input_numbers = input()

print(sort_a_list(input_numbers))
