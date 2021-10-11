
from student import Student

class Group:
    id = None
    specialty = None
    students = []

    def addStudent(self, student: Student):
        self.students.append(student)

    def __init__(self, id, specialty) -> None:
        self.id = id
        self.specialty = specialty

    def __str__(self) -> str:
        return self.id