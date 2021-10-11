from entities.teacher import *
from helpers.db import *
from helpers.enums import *
from cmd.generalCmd import *


class TeacherCmd(GeneralCmd):

    @staticmethod
    def getEntityTitle()-> str:
        return 'Teacher'

    @staticmethod
    def getActions() -> dict:
        return {
            'Add': TeacherCmd.add,
            'Delete': TeacherCmd.delete,
            'Show': TeacherCmd.show,
        }
    
    @staticmethod
    def add():

        name = input("Enter teacher name: ")
        surname = input("Enter teacher surname: ")
        patronymic = input("Enter teacher patronymic: ")
        gender = input("Enter teacher gender (male, female): ")

        if gender not in [Gender.MALE.value, Gender.FEMALE.value]:
            raise Exception("Wrong gender!")

        teacher = Teacher(name=name, surname=surname, patronymic=patronymic, gender=Gender(gender))
        teacher.save()

        print("Teacher added successfully:", teacher, teacher.__dict__)

    @staticmethod
    def delete():
        id = int(input("Enter teacher id: "))
        teacher = Teacher.byId(id)
        teacher.delete()
        print("Teacher removed successfully:", teacher, teacher.__dict__)

    @staticmethod
    def show():

        sql = 'select * from {} where 1=1'.format(Teacher.getTableName())

        print("Set filters below:")

        # exact filters
        for field in ['id']:
            value = input("Enter filter for field '{}': ".format(field))
            if value != '':
                sql += " and `{}` = '{}'".format(field, value)
        
        # wildcard filters
        for field in ['name', 'surname', 'patronymic']:
            value = input("Enter filter for field '{}': ".format(field))
            if value != '':
                sql += " AND `{}` like '%{}%'".format(field, value)

        Db.selectAndPrettyPrint(sql)