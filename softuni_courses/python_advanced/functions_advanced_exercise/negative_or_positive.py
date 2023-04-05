def positive_negative(numbers):
    positive = []
    negative = []

    [positive.append(i) if i > 0 else negative.append(i) for i in numbers]

    print(sum(negative))
    print(sum(positive))
    if abs(sum(negative)) > sum(positive):
        print('The negatives are stronger than the positives')
    else:
        print('The positives are stronger than the negatives')


line = [int(i) for i in input().split()]

positive_negative(line)