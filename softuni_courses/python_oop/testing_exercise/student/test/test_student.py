import unittest
from project2.student import Student


class TestStudent(unittest.TestCase):
    def setUp(self) -> None:
        self.student = Student('L', None)
        self.student2 = Student('G', {'P': [1, 2, 3], 'OOP': [4, 5, 6]})

    def test_constructor(self):
        self.assertEqual(self.student.courses, {})
        self.assertEqual(self.student2.courses, {'P': [1, 2, 3], 'OOP': [4, 5, 6]})
        self.assertEqual(self.student.name, 'L')

    def test_enroll_course_already_in(self):
        self.assertEqual(self.student2.enroll('P', [7, 8], ''), "Course already added. Notes have been updated.")
        self.assertEqual(self.student2.courses, {'P': [1, 2, 3, 7, 8], 'OOP': [4, 5, 6]})

    def test_enroll_course_not_in_add_Y(self):
        self.assertEqual(self.student.enroll('P', [1, 2], 'Y'), "Course and course notes have been added.")
        self.assertEqual(self.student.courses, {'P': [1, 2]})

    def test_enroll_course_not_in_add_empty(self):
        self.assertEqual(self.student.enroll('P', [1, 2]), "Course and course notes have been added.")
        self.assertEqual(self.student.courses, {'P': [1, 2]})

    def test_enroll_with_different_add(self):
        self.assertEqual(self.student.enroll('P', [1, 2], 'Z'), 'Course has been added.')
        self.assertEqual(self.student.courses, {'P': []})

    def test_add_notes_course_not_found(self):
        with self.assertRaises(Exception) as ex:
            self.student.add_notes('P', [1, 2, 3])
        self.assertEqual(str(ex.exception), "Cannot add notes. Course not found.")

        self.student2.add_notes('P', [9, 10])
        self.assertEqual(self.student2.courses, {'P': [1, 2, 3, [9, 10]], 'OOP': [4, 5, 6]})

    def test_leave_course(self):
        with self.assertRaises(Exception) as ex:
            self.student.leave_course('PPP')
        self.assertEqual(str(ex.exception), "Cannot remove course. Course not found.")

        self.assertEqual(self.student2.leave_course('OOP'), "Course has been removed")
        self.assertEqual(self.student2.courses, {'P': [1, 2, 3]})


if __name__ == "__main__":
    unittest.main()
