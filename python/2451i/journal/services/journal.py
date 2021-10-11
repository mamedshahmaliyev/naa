from services.entity import EntityService
from inputs.journal import JournalInput

class JournalService(EntityService):
    
    @classmethod
    def dbTable(cls) -> str:
        return 'journals'
    
    @classmethod
    def getEntityInput(cls) -> JournalInput:
        return JournalInput()