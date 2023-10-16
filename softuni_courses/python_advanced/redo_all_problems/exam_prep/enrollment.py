def gather_credits(*args):
    needed_credits = args[0]
    courses = args[1:]
    result = []
    enrolled_into = []
    credits = 0

    for c in courses:
        if needed_credits >= 1:
            if c[0] not in enrolled_into:
                enrolled_into.append(c[0])
                needed_credits -= c[1]
                credits += c[1]
            else:
                continue

        if needed_credits <= 0:
            break

    if needed_credits <= 0:
        result.append(f"Enrollment finished! Maximum credits: {credits}.")
        result.append('Courses: ' + ', '.join(el for el in sorted(enrolled_into)))
    else:
        return f"You need to enroll in more courses! You have to gather {needed_credits} credits more."

    return '\n'.join(result)



print(gather_credits(
    80,
    ("Advanced", 30),
    ("Basics", 27),
    ("Fundamentals", 27),
))
