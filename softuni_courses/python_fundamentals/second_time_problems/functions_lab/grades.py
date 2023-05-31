def grade_filter(grade):

    if 2 <= grade <= 2.99:
        score = 'Fail'

    elif 3 <= grade <= 3.49:
        score = 'Poor'

    elif 3.5 <= grade <= 4.49:
        score = 'Good'

    elif 4.5 <= grade <= 5.49:
        score = 'Very Good'

    else:
        score = 'Excellent'

    return score


grade = float(input())

print(grade_filter(grade))
