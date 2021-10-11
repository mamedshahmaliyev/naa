
from entities.studentGroup import StudentGroup
from inputs.entity import EntityInput

class StudentGroupInput(EntityInput):
    
    def getEmptyEntityObject(self) -> StudentGroup:
        return StudentGroup()
    
    def validateUserInput(self, operation: str, entity: StudentGroup):
        if operation == 'Create' and not entity.name:
            raise ValueError("Group name is required")
                
        