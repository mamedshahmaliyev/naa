from dataclasses import dataclass
from datetime import date

from .studentGroup import StudentGroup
from entities.entity import Entity

@dataclass
class Journal(Entity):
    kafedra: str = None
    faculty: str = None
    student_group: StudentGroup = None
    start_date: date = None
    end_date: date = None
    
    