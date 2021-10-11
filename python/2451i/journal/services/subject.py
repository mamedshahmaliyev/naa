from services.entity import EntityService
from inputs.subject import SubjectInput

class SubjectService(EntityService):
    
    @classmethod
    def dbTable(cls) -> str:
        return 'subjects'
    
    @classmethod
    def getEntityInput(cls) -> SubjectInput:
        return SubjectInput()