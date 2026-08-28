class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no
        self.scores = []

class Gradebook:
    def __init__(self):
        self.students = []

    def add_student(self, name, roll_no):
        for student in self.students:
            if student.roll_no == roll_no:
                return False

        self.students.append(Student(name, roll_no))
        return True
