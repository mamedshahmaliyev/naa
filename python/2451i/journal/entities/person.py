from dataclasses import dataclass
from helpers.enums import Gender
from entities.entity import Entity

@dataclass
class Person(Entity):

    first_name: str = None
    last_name: str = None
    father_name: str = None
    gender: Gender = None
        
    def fullName(self) -> str:
        ogluQizi = ''
        if self.gender == Gender.MALE:
            ogluQizi = 'OĞLU'
        if self.gender == Gender.FEMALE:
            ogluQizi = 'QIZI'
        return f"{self.last_name} {self.first_name} {self.father_name} {ogluQizi}"
    
    def __str__(self) -> str:
        return self.fullName()