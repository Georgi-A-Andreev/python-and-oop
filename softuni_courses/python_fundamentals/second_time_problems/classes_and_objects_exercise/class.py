class Class:
    __students_count = 22

    def __init__(self, name):
        self.name = name
        self.students = []
        self.grades = []

    def add_student(self, name, grade):
        if len(self.students) < Class.__students_count:
            self.students.append(name)
            self.grades.append(grade)

    def get_average_grade(self):
        if self.grades:
            return float(f'{sum(self.grades) / len(self.grades):.2f}')
        return 0.00

    def __repr__(self):
        students = ', '.join(self.students)

        return f"The students in {self.name}: {students}. Average grade: {self.get_average_grade()}"


