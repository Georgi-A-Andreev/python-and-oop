def print_result(seq):
    positive = []
    negative = []

    for el in seq:
        if el > 0:
            positive.append(el)
        else:
            negative.append(el)

    print(sum(negative))
    print(sum(positive))

    if abs(sum(positive)) > abs(sum(negative)):
        print("The positives are stronger than the negatives")
    else:
        print("The negatives are stronger than the positives")


seq = [int(x) for x in input().split()]
print_result(seq)