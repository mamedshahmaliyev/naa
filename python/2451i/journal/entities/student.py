from entities.person import Person
from dataclasses import dataclass

@dataclass
class Student(Person):
    
    entry_year: int = None
    
    def __str__(self) -> str:
        return f'{self.fullName()} [Year: {self.entry_year}]'
    
    
    