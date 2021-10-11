
from entities.journalRecord import JournalRecord
from inputs.entity import EntityInput

class JournalRecordInput(EntityInput):
    
    def getEmptyEntityObject(self) -> JournalRecord:
        return JournalRecord()
                
        