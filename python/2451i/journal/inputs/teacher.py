
from entities.teacher import Teacher
from inputs.entity import EntityInput

class TeacherInput(EntityInput):
    
    def getEmptyEntityObject(self) -> Teacher:
        return Teacher()
    
    def validateUserInput(self, operation: str, entity: Teacher):
        if operation == 'Create' and (not entity.first_name or not entity.last_name or 'NULL' in [entity.first_name, entity.last_name]):
            raise ValueError("First name and last name are required")
                
        