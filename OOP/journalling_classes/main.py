
from datetime import datetime
from operator import sub
from journal import Journal
from record import Record
from subject import Subject
from teacher import Teacher
from person import Person
from group import Group

# students
ahmad = Person('Ahmad', 'Mammadov')
ahmad.setGender('male')
firuza = Person('Firuza', 'Hasanova', 'Ilham')
firuza.setGender('female')

# group
group = Group('1459i', 'Computer engineering')

print("Student list: ", group.students)
group.addStudent(ahmad)
group.addStudent(firuza)
print("Student list: ", group.students)
print("Student list: ", 
    # list comprehension
    [str(student) for student in group.students]
    )

mammad = Teacher("Mammad", "Shahmaliyev")
mammad.degree = "PhD"
mammad.setSalary(300)

print("Mammad: ", mammad)

subject = Subject('Object Oriented Programming', 5, 75)
print('Subject:', subject)

record1 = Record(firuza, datetime.now(), True, 'lecture', subject)
record2 = Record(ahmad, datetime.now(), True, 'lecture', subject)

print('Record1', record1)
print('Record2', record2)

journal = Journal()
journal.records.append(record1)
journal.records.append(record2)
journal.group = group

print('Journal:', journal)
print('Journal records:', [str(r) for r in journal.records])

