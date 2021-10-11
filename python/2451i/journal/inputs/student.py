
from entities.student import Student
from datetime import datetime
from inputs.entity import EntityInput

class StudentInput(EntityInput):
    
    def getEmptyEntityObject(self) -> Student:
        return Student()
    
    def validateUserInput(self, operation: str, student: Student):
        if operation == 'Create' and (not student.first_name or not student.last_name or 'NULL' in [student.first_name, student.last_name]):
            raise ValueError("First name and last name are required")
        
        if student.entry_year or student.entry_year == 0:
            if student.entry_year > datetime.now().year or student.entry_year < 2000:
                raise ValueError("Invalid entry year")
                
        