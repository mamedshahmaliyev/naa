from dataclasses import dataclass
from entities.entity import Entity

@dataclass
class StudentGroup(Entity):
    name: str = None
    
    def getNumberOfStudents(self) -> int:
        return 0