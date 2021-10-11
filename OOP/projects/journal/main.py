
import sqlite3

class Journal:
    __id = None
    __group_id = None
    __faculty = None

    def __init__(self, group_id, faculty) -> None:
        self.__group_id = group_id
        self.__faculty = faculty

    def insert(self):
        cur = con.cursor()
        cur.execute('''
                      INSERT INTO journals (group_id, faculty) 
                      VALUES (?, ?)
                      ''', [self.__group_id, self.__faculty])
        con.commit()
    
    def list(self):
        cur = con.cursor()
        journals = cur.execute('''select * from journals''').fetchall()
        return journals

def journals():
    menu = '''
    1. Create Journal
    2. List Journals
    '''
    print(menu)
    menu_number = int(input("Please choose number from above: "))
    if menu_number == 1:
        group_id = input("Please enter group id: ")
        faculty = input("Please enter faculty: ")
        journal = Journal(group_id, faculty)
        journal.insert()
    elif menu_number == 2:
        journal = Journal('', '')
        print(journal.list())

class Subject:
    __id = None
    __name = None
    __hours = None
    __credit = None

    def __init__(self, name, hours, credit) -> None:
        self.__name = name
        self.__hours = hours
        self.__credit = credit

    def insert(self):
        cur = con.cursor()
        cur.execute('''
                      INSERT INTO subjects (name, hours, credit) 
                      VALUES (?, ?, ?)
                      ''', [self.__name, self.__hours, self.__credit])
        con.commit()
    
    def list(self):
        cur = con.cursor()
        items = cur.execute('''select * from subjects''').fetchall()
        return items

def subjects():
    menu = '''
    1. Create Subject
    2. List Subjects
    '''
    print(menu)
    menu_number = int(input("Please choose number from above: "))
    if menu_number == 1:
        name = input("Please enter name: ")
        hours = input("Please enter hours: ")
        credit = input("Please enter credit: ")
        subject = Subject(name, hours, credit)
        subject.insert()
    elif menu_number == 2:
        subjects = Subject('', '', '')
        print(subjects.list())

class Student:
    __id = None
    __name = None
    __surname = None
    __patronym = None

    def __init__(self, name, surname, patronym = None) -> None:
        self.__name = name
        self.__surname = surname
        self.__patronym = patronym

    def insert(self):
        cur = con.cursor()
        cur.execute('''
                      INSERT INTO students (name, surname, patronym) 
                      VALUES (?, ?, ?)
                      ''', [self.__name, self.__surname, self.__patronym])
        con.commit()
    
    def list(self):
        cur = con.cursor()
        items = cur.execute("SELECT * FROM students").fetchall()
        return items

def students():
    menu = '''
    1. Create Student
    2. List Students
    '''
    print(menu)
    menu_number = int(input("Please choose number from above: "))
    if menu_number == 1:
        name = input("Please enter name: ")
        surname = input("Please enter surname: ")
        patronym = input("Please enter patronym: ")
        student = Student(name, surname, patronym)
        student.insert()
    elif menu_number == 2:
        students = Student('', '', '')
        print(students.list())

class JournalRecord:
    __id = None,
    __student_id = None,
    __subject_id = None,
    __record_type = None,
    __date = None,
    __class_number = None,
    __mark = None,
    __present_hours = None

    def __init__(self, student_id, subject_id, record_type, date, class_number, mark, present_hours) -> None:
        self.__student_id = student_id
        self.__subject_id = subject_id
        self.__record_type = record_type
        self.__date = date
        self.__class_number = class_number
        self.__mark = mark
        self.__present_hours = present_hours

    def insert(self):
        cur = con.cursor()
        cur.execute('''
                      INSERT INTO journal_records (student_id, subject_id, record_type, date, class_number, mark, present_hours) 
                      VALUES (?, ?, ?, ?, ?, ?, ?)
                      ''', [
                          self.__student_id, self.__subject_id, self.__record_type,
                          self.__date, self.__class_number, self.__mark, self.__present_hours
                          ])
        con.commit()
    
    def list(self):
        cur = con.cursor()
        items = cur.execute("SELECT * FROM journal_records").fetchall()
        return items

def journal_records():
    menu = '''
    1. Create Record
    2. List Records
    '''
    print(menu)
    menu_number = int(input("Please choose number from above: "))
    if menu_number == 1:
        student_id = input("Please enter student_id: ")
        subject_id = input("Please enter subject_id: ")
        record_type = input("Please enter record type: ")
        date = input("Please enter record date (Y-m-d): ")
        class_number = input("Please enter class number: ")
        mark = input("Please enter mark: ")
        present_hours = input("Please enter present hours: ")
        record = JournalRecord(student_id, subject_id, record_type, date, class_number, mark, present_hours)
        record.insert()
    elif menu_number == 2:
        records = JournalRecord('', '', '', '', '', '', '')
        print(records.list())

def main():

    menu = '''
    1. Journal
    2. Subject
    3. Student
    4. Journal Record
    '''
    print(menu)

    menu_number = int(input("Please choose number from above: "))
    if menu_number == 1: journals()
    if menu_number == 2: subjects()
    if menu_number == 3: students()
    if menu_number == 4: journal_records()

        


    



if __name__ == '__main__':
    con = sqlite3.connect('journal.db')
    main()
    con.close()