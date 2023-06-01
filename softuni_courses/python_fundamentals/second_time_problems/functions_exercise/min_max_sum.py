def min_max_and_sum(sequence):
    return f"The minimum number is {min(sequence)}\n" \
           f"The maximum number is {max(sequence)}\n" \
           f"The sum number is: {sum(sequence)}"


nums = [int(i) for i in input().split()]

print(min_max_and_sum(nums))
