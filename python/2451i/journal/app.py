

from services.entity import EntityService
from services.student import StudentService
from services.studentGroup import StudentGroupService
from services.teacher import TeacherService
from services.journal import JournalService
from services.journalRecord import JournalRecordService
from services.subject import SubjectService

services = [JournalRecordService, StudentService, StudentGroupService, TeacherService, JournalService, SubjectService]
            
choosenEntityIdx = None

if __name__ == "__main__":
    while True:
        if not choosenEntityIdx:
            print('List of Entities:')
            for i, service in enumerate(services):
                print(f"{i + 1}. {service.entityName()}")
            print(f"{len(services) + 1}. Exit")
            print('-' * 50)
            
            try:
                idx = int(input("First choose entity index: "))
            except KeyboardInterrupt:
                print("Program interrupted by the user. Exiting...")
                raise
            except:
                print("Invalid entity index")
                continue
            
            if 0 < idx <= len(services):
                choosenEntityIdx = idx
            elif idx == len(services) + 1:
                print('Goodbye')
                break
            else:
                print("Invalid entity index")
        else:
            service: EntityService = services[choosenEntityIdx-1]
            operations = service.operations()
            print('-' * 50)
            print(f'Choosen Entity: {service.entityName()}')
            print('List of Operations:')
            for i, operation in enumerate(operations):
                print(f"{i + 1}. {operation}")
            print(f"{len(operations) + 1}. Go Back")
            print('-' * 50)
            
            try:
                operationIdx = int(input("Choose operation index: "))
            except KeyboardInterrupt:
                print("Program interrupted by the user. Exiting...")
                raise
            except:
                print("Invalid operation index")
                continue
            
            if 0 < operationIdx <= len(operations):
                try:
                    service.performOperation(operations[operationIdx-1])
                except KeyboardInterrupt:
                    print("Program interrupted by the user. Exiting...")
                    raise
                except Exception as e:
                    print('Operation failed:', e)
                    # raise e
            elif operationIdx == len(operations) + 1:
                choosenEntityIdx = None
            else:
                print("Invalid operation index")