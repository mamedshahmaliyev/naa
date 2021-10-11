from dataclasses import dataclass
from datetime import date
from .student import Student
from .teacher import Teacher

from helpers.enums import JournalRecordType, Presence
from entities.entity import Entity

@dataclass
class JournalRecord(Entity):
    record_date: date = None
    student: Student = None
    teacher: Teacher = None
    record_type: JournalRecordType = None
    mark: int = None
    presence: Presence = None
    hour: int = None