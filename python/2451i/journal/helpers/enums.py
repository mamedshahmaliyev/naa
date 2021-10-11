from enum import Enum

class Gender(str, Enum):
    MALE = 'male'
    FEMALE = 'female'
   
class JournalRecordType(str, Enum):
    LECTURE = 'lecture'
    PRACTICE = 'practice'
    KOLLOKVIUM = 'kollokvium'
    LAB = 'lab'

class Presence(str, Enum):
    PRESENT = 'present'
    ABSENT = 'absent'
    HOLIDAY = 'holiday'
    VALID_REASON = 'valid_reason'