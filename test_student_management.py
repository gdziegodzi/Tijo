import unittest
from student_management import StudentManagement

class TestStudentManagement(unittest.TestCase):
    def setUp(self):
        self.manager = StudentManagement()

    def test_add_student_should_add_student_to_list(self):
        self.manager.add_student('John Doe')
        student = self.manager.find_student('John Doe')
        self.assertIsNotNone(student)
        self.assertEqual(student.name, 'John Doe')

    def test_update_student_should_update_student_name(self):
        self.manager.add_student('John Doe')
        self.manager.update_student('John Doe', 'Jane Doe')
        student = self.manager.find_student('Jane Doe')
        self.assertIsNotNone(student)
        self.assertEqual(student.name, 'Jane Doe')
        self.assertIsNone(self.manager.find_student('John Doe'))

    def test_delete_student_should_remove_student_from_list(self):
        self.manager.add_student('John Doe')
        self.manager.delete_student('John Doe')
        student = self.manager.find_student('John Doe')
        self.assertIsNone(student)

    def test_add_grade_should_add_grade_to_student(self):
        self.manager.add_student('John Doe')
        self.manager.add_grade('John Doe', 5)
        student = self.manager.find_student('John Doe')
        self.assertEqual(student.grades, [5])

    def test_calculate_average_should_return_correct_average(self):
        self.manager.add_student('John Doe')
        self.manager.add_grade('John Doe', 4)
        self.manager.add_grade('John Doe', 5)
        average = self.manager.calculate_average('John Doe')
        self.assertEqual(average, 4.5)

    def test_calculate_average_should_return_zero_when_no_grades(self):
        self.manager.add_student('John Doe')
        average = self.manager.calculate_average('John Doe')
        self.assertEqual(average, 0.0)

if __name__ == '__main__':
    unittest.main()
