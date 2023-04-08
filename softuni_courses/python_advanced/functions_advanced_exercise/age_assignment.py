def age_assignment(*names, **age):
    result = []
    for i in names:
        result.append(f"{i} is {age[i[0]]} years old.")

    return '\n'.join(sorted(result))


print(age_assignment("Peter", "George", G=26, P=19))
