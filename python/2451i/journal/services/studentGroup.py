from services.entity import EntityService
from services.student import StudentService
from inputs.studentGroup import StudentGroupInput
from inputs.student import StudentInput
from helpers.db  import DB

class StudentGroupService(EntityService):
    
    @classmethod
    def dbTable(cls) -> str:
        return 'student_groups'
    
    @classmethod
    def getEntityInput(cls) -> StudentGroupInput:
        return StudentGroupInput()
    
    @classmethod
    def operations(cls) -> list[str]:
        return super().operations() + ['Add Student', 'Remove Student', 'Show Students', 'Show Student Count']
    
    @classmethod
    def addStudentToGroup(cls, groupId: int, studentId: int):
        DB.execute(f"INSERT INTO students_groups (group_id, student_id) VALUES ({groupId}, {studentId})")
    
    @classmethod
    def removeStudentFromGroup(cls, groupId: int, studentId: int):
        DB.execute(f"DELETE FROM students_groups WHERE group_id = {groupId} AND student_id = {studentId}")
    
    @classmethod
    def getStudentList(cls, groupId: int):
        return DB.select(f"""SELECT s.id as student_id, s.first_name, s.last_name
                               FROM students_groups sg
                              INNER JOIN students s ON sg.student_id = s.id
                              WHERE sg.group_id = {groupId}
                             ORDER BY s.id""", isDict=True)
    
    @classmethod
    def getStudentCount(cls, groupId: int):
        return DB.select(f"SELECT count(*) from students_groups where group_id = {groupId}")[0][0]
    
    @classmethod
    def performOperation(cls, operation: str) -> list[str]:
        super().performOperation(operation)
        entityInput = cls.getEntityInput()
        if operation in ['Add Student', 'Remove Student']:
            
            # first ask the group
            groupId = entityInput.askForEntityId()
            groupRecord = cls.getEntityRecordById(groupId)
            print(f"{cls.entityName()} found: {groupRecord}")
            
            # second ask for student
            studentId = StudentInput().askForEntityId()
            studentRecord = StudentService.getEntityRecordById(studentId)
            print(f"{StudentService.entityName()} found: {studentRecord}. Adding student to group...")
            
            if operation == 'Add Student':
                cls.addStudentToGroup(groupId, studentId)
                print(f"Student added to group successfully!")
            if operation == 'Remove Student':
                cls.removeStudentFromGroup(groupId, studentId)
                print(f"Student was removed from group successfully!")
        
        if operation == 'Show Students':
            
            # first ask the group
            groupId = entityInput.askForEntityId()
            groupRecord = cls.getEntityRecordById(groupId)
            print(f"{cls.entityName()} found: {groupRecord}")
            
            DB.printRows(cls.getStudentList(groupId))
        
        if operation == 'Show Student Count':
            
            # first ask the group
            groupId = entityInput.askForEntityId()
            groupRecord = cls.getEntityRecordById(groupId)
            print(f"{cls.entityName()} found: {groupRecord}")
            
            print("Student count: ", cls.getStudentCount(groupId))