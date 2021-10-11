
class Person:
    name  = ""
    surname = ""
    patronym = ""

    __gender = ""

    def setGender(self, gender: str):
        if gender != 'male' and gender != 'female':
            print("Error, wrong gender, please use male or female!")
            return
        self.__gender = gender

    def getGender(self) -> str:
        return self.__gender

    def __init__(self, name, surname, patronym = "") -> None:
        self.name = name
        self.surname = surname
        self.patronym = patronym

    # magic function, string representation of the object
    def __str__(self) -> str:
        s = self.name + " " + self.surname
        if self.patronym != "":
            s += " " + self.patronym
        return s
    