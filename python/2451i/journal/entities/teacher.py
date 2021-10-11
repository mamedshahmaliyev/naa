from entities.person import Person
from dataclasses import dataclass

@dataclass
class Teacher(Person):
    experience: int = None