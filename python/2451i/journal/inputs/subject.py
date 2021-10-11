
from entities.subject import Subject
from inputs.entity import EntityInput

class SubjectInput(EntityInput):
    
    def getEmptyEntityObject(self) -> Subject:
        return Subject()
                
        