def students_credits(*args):
    courses = {}
    total_credits = 0
    result = ''
    for i in args:
        course, credit, max_test, diyan_test = i.split('-')
        credit, max_test, diyan_test = int(credit), int(max_test), int(diyan_test)
        total_credits += (diyan_test / max_test) * credit
        if course not in courses:
            courses[course] = 0
        courses[course] += (diyan_test / max_test) * credit

    if total_credits >= 240:
        result += f'Diyan gets a diploma with {total_credits:.1f} credits.\n'
    else:
        result += f'Diyan needs {240 - total_credits:.1f} credits more for a diploma.\n'

    sorted_courses = sorted(courses.items(), key=lambda x: -x[1])

    for k in sorted_courses:
        result += f'{k[0]} - {k[1]:.1f}\n'

    return result


print(
    students_credits(
        "Computer Science-12-300-250",
        "Basic Algebra-15-400-200",
        "Algorithms-25-500-490"
    )
)
