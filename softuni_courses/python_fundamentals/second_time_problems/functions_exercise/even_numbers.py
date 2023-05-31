def filter_even_numbers(sequence):
    sequence = [int(i) for i in sequence.split()]
    return list(filter(lambda x: x % 2 == 0, sequence))


input_numbers = input()

print(filter_even_numbers(input_numbers))
