from services.entity import EntityService
from inputs.journalRecord import JournalRecordInput

class JournalRecordService(EntityService):
    
    @classmethod
    def dbTable(cls) -> str:
        return 'journal_records'
    
    @classmethod
    def getEntityInput(cls) -> JournalRecordInput:
        return JournalRecordInput()