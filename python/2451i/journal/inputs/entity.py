from entities.entity import Entity
from dataclasses import fields

class EntityInput:
    
    def getEmptyEntityObject(self) -> Entity:
        return Entity()
    
    def createUserInputToEntity(self) -> Entity:
        '''This method is used to get, validate input from user for entity insert and create a new entity object and return it'''
        entityObj = self.getEmptyEntityObject()
        for field in fields(entityObj): 
            if field.name == 'id':
                continue
            humanFriendlyFieldName = field.name.replace('_', ' ').capitalize()
            value = input(f"Enter {humanFriendlyFieldName} or skip: ").strip() or None
            if value:
                if field.type == int:
                    if value:
                        value = int(value)
                entityObj.__setattr__(field.name, value)
                
        self.validateUserInput('Create', entityObj)
        
        return entityObj
    
    def updateUserInputToEntity(self) -> Entity:
        '''This method is used to get, validate input from user for entity insert and create a new entity object and return it'''
        entityObj = self.getEmptyEntityObject()
        for field in fields(entityObj): 
            if field.name == 'id':
                continue
            humanFriendlyFieldName = field.name.replace('_', ' ').capitalize()
            value = input(f"Enter new value for {humanFriendlyFieldName} or skip: ").strip() or None
            if value:
                if field.type == int:
                    if value:
                        value = int(value)
                entityObj.__setattr__(field.name, value)
        self.validateUserInput('Update', entityObj)
        return entityObj
    
    def askForSearchFilter(self) -> dict:
        filters = {}
        
        for field in fields(self.getEmptyEntityObject()): 
            humanFriendlyFieldName = field.name.replace('_', ' ').capitalize()
            value = input(f"Search by {humanFriendlyFieldName} or skip: ").strip() or None
            if value:
                filters[field.name] = value
        
        return filters
    
    def validateUserInput(self, operation: str, entity: Entity):
        '''Validate user input, check required fields etc. and raise ValueError if validation fails'''
        pass
    
    def askLimitOffset(self) -> tuple[int, int]:
        return int(input("Enter limit (default 10): ") or 10), int(input("Enter offset (default 0): ") or 0)
    
    def askForEntityId(self) -> int:
        return int(input(f"Enter {self.getEmptyEntityObject().entityName()} id: "))