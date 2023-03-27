def grade(a):
    result = ''
    if 2 <= a <= 2.99:
        result = 'Fail'
    elif a <= 3.49:
        result = 'Poor'
    elif a <= 4.49:
        result = 'Good'
    elif a <= 5.49:
        result = 'Very Good'
    elif a <= 6:
        result = 'Excellent'

    return result


score = float(input())

print(grade(score))
