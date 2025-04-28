class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)

    def calculate_average(self):
        if not self.grades:
            return 0.0
        return sum(self.grades) / len(self.grades)


class StudentManagement:
    def __init__(self):
        self.students = []

    def add_student(self, name):
        self.students.append(Student(name))

    def find_student(self, name):
        for student in self.students:
            if student.name == name:
                return student
        return None

    def update_student(self, old_name, new_name):
        student = self.find_student(old_name)
        if student:
            student.name = new_name

    def delete_student(self, name):
        student = self.find_student(name)
        if student:
            self.students.remove(student)

    def add_grade(self, student_name, grade):
        student = self.find_student(student_name)
        if student:
            student.add_grade(grade)

    def calculate_average(self, student_name):
        student = self.find_student(student_name)
        if student:
            return student.calculate_average()
        return 0.0
