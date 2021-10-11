
class Subject:
    name = ""
    credit: int = 0
    hours: int = 0

    def __init__(self, name, credit, hours) -> None:
        self.name = name
        self.credit = credit
        self.hours = hours

    def __str__(self) -> str:
        return "{} ({} - {})".format(self.name, self.credit, self.hours)