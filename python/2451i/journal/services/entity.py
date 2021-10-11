from dataclasses import dataclass, asdict
from inputs.entity import EntityInput
from helpers.db  import DB
from entities.entity import Entity
import re

@dataclass
class EntityService:
    
    @classmethod
    def dbTable(cls) -> str:
        pass
    
    @classmethod
    def entityName(cls) -> str:
        return ' '.join(re.split(r'(?=[A-Z])', cls.__name__.replace('Service', ''))).strip()
    
    @classmethod
    def getEntityInput(cls) -> EntityInput:
        return EntityInput()
    
    @classmethod
    def operations(cls) -> list[str]:
        return ['Create', 'Update', 'Delete', 'Search']    
    
    @classmethod
    def getEntityRecordById(cls, id) -> dict:
        try:
            return DB.select(f"SELECT * FROM {cls.dbTable()} WHERE id = %s", (id,), isDict=True)[0]
        except:
            raise Exception(f"{cls.entityName()} with id {id} not found")
    
    @classmethod
    def insert(cls, entity: Entity) -> int:
        fieldValues = {field: value for field, value in asdict(entity).items() if value is not None and field != 'id'}
        fields = ', '.join(fieldValues.keys())
        placeHolders = ', '.join([f'%({field})s' for field in fieldValues])
        return DB.execute(f"INSERT INTO {cls.dbTable()} ({fields}) VALUES ({placeHolders})", fieldValues)
    
    @classmethod
    def update(cls, id: int, updatedEntity: Entity):
        fieldValues = {field: (value if value != 'NULL' else None) for field, value in asdict(updatedEntity).items() if value is not None and field != 'id'}
        if not fieldValues:
            print('No fields to update')
            return
        sql = f"UPDATE {cls.dbTable()} SET "
        sql += ', '.join([f"{field} = %({field})s" for field in fieldValues])
        fieldValues['id'] = id
        return DB.execute(sql + " where id = %(id)s", fieldValues)
    
    @classmethod
    def delete(cls, id: int):
        DB.execute(f"DELETE FROM {cls.dbTable()} WHERE id = %s", (id,))
    
    @classmethod
    def search(cls, filters: dict, limit: int = 10, offset: int = 0) -> list[dict]:
        where = ' AND '.join([f"{field} {'=' if filters[field].isnumeric() else 'like'} %({field})s" for field in filters])
        if where:
            where = ' WHERE ' + where
        sql = f"SELECT * FROM {cls.dbTable()} {where} LIMIT {limit} OFFSET {offset}"
        return DB.select(sql, filters, isDict=True)
    
    @classmethod
    def performOperation(cls, operation: str) -> list[str]:
        entityInput = cls.getEntityInput()
        if operation == 'Create':
            entity = entityInput.createUserInputToEntity()
            id = cls.insert(entity=entity)
            entity.id = id
            print(f"{entity.entityName()} with id {id} added successfully: {entity}")
        elif operation == 'Update':
            id = entityInput.askForEntityId()
            entityRecord = cls.getEntityRecordById(id)
            print(f"{cls.entityName()} found: {entityRecord}")
            entity = entityInput.updateUserInputToEntity()
            entity.id = id
            cls.update(id, entity)
            print(f"{cls.entityName()} with id {id} updated successfully: {cls.getEntityRecordById(id)}.")
        elif operation == 'Delete':
            id = entityInput.askForEntityId()
            entityRecord = cls.getEntityRecordById(id)
            print(f"{cls.entityName()} found: {entityRecord}")
            cls.delete(id)
            print(f"{cls.entityName()} with id {id} deleted successfully!")
        elif operation == 'Search':
            filter = entityInput.askForSearchFilter()
            limit, offset = entityInput.askLimitOffset()
            results = cls.search(filters=filter, limit=limit, offset=offset)
            DB.printRows(results)
            