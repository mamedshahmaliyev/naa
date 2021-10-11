
from group import Group


class Journal:
    records = []
    group: Group

    def __str__(self) -> str:
        return self.group.id