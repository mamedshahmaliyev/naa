
from dataclasses import dataclass
from entities.entity import Entity

@dataclass
class Subject(Entity):
    name: str = None
    code: str = None
    hours: int = None
    credits: int = None