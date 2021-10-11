from services.entity import EntityService
from inputs.teacher import TeacherInput

class TeacherService(EntityService):
    
    @classmethod
    def dbTable(cls) -> str:
        return 'teachers'
    
    @classmethod
    def getEntityInput(cls) -> TeacherInput:
        return TeacherInput()