def fibonacci():
    sequence = [0, 1]
    idx = 0
    while True:
        yield sequence[idx]
        idx += 1
        sequence.append(sequence[-1] + sequence[-2])


generator = fibonacci()
for i in range(5):
    print(next(generator))
generator = fibonacci()
for i in range(1):
    print(next(generator))
