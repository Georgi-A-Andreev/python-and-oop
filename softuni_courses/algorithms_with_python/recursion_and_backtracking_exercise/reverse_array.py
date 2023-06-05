def reverse_array(sequence, idx):
    if idx == len(sequence):
        return

    reverse_array(sequence, idx + 1)
    print(sequence[idx], end=' ')


seq = [int(i) for i in input().split()]
reverse_array(seq, 0)
