def age_assignment(*args, **kwargs):
    result = []
    for k, v in sorted(kwargs.items(), key= lambda x: x[0]):
        for el in args:
            if el.startswith(k):
                result.append(f"{el} is {v} years old.")

    return '\n'.join(result)


print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))
