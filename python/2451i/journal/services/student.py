from services.entity import EntityService
from inputs.student import StudentInput

class StudentService(EntityService):
    
    @classmethod
    def dbTable(cls) -> str:
        return 'students'
    
    @classmethod
    def getEntityInput(cls) -> StudentInput:
        return StudentInput()