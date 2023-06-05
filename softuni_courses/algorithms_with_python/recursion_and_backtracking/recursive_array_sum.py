def recursive_sum(number_list, idx):
    if idx == len(number_list) - 1:
        return number_list[idx]

    return number_list[idx] + recursive_sum(number_list, idx + 1)


input_list = [int(i) for i in input().split()]

print(recursive_sum(input_list, 0))
