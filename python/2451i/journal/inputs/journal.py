
from entities.journal import Journal
from inputs.entity import EntityInput

class JournalInput(EntityInput):
    
    def getEmptyEntityObject(self) -> Journal:
        return Journal()
                
        