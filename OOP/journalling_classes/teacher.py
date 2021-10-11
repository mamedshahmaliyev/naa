
from person import Person


class Teacher(Person):
    degree = None
    __salary: float = None

    def setSalary(self, salary: float):
        if salary < 0 or salary > 10000:
            print("Please enter real salary")
            return
        self.__salary = salary

    def __str__(self) -> str:
        return super().__str__() + ", salary = {}".format(self.__salary)