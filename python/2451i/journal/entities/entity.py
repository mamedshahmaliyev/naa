from dataclasses import dataclass
import re

@dataclass
class Entity:
    
    id: int = None
    
    @classmethod
    def entityName(cls):
        return ' '.join(re.split(r'(?=[A-Z])', cls.__name__)).strip()