
from datetime import datetime
from subject import Subject
from student import Student

class Record:
    student: Student
    date: datetime
    is_present: bool
    type: str
    subject: Subject

    def __init__(self, student, date, is_present, type, subject) -> None:
        self.student = student
        self.date = date
        self.is_present = is_present
        self.type = type
        self.subject = subject

    def __str__(self) -> str:
        return "{}, {}, {}, {}".format(self.date.strftime('%d-%m-%Y'), self.subject.name, self.student, self.is_present)