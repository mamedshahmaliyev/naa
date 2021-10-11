
from fastapi import FastAPI
from enum import Enum
from typing import Optional

class Gender(str, Enum):
    male = "male"
    female = "female"


app = FastAPI()


@app.get("/")
async def welcome_message():
    return {"message": "Salam NAA"}

@app.get("/gender/{gender}")
async def gender_title(gender: Gender):
    if gender == Gender.male:
        return {"title": "Male", 'gender': gender}
    elif gender == Gender.female:
        return {"title": "Female", 'gender': gender}


@app.get("/student/search")
async def search_student(name: Optional[str] = None):
    # fake database
    students = {
        1: {
            "name": "Rustam",
            "surname": "Azadaliyev"
        },
        2: {
            "name": "Firuza",
            "surname": "Hasanova"
        }
    }
    if name is not None:
        return [
            s for s in students.values() if name in s['name']
        ]
    else:
        return {"msg": "No search param defined"}


@app.get("/student/{id}")
async def get_student(id: int):

    # fake database
    students = {
        1: {
            "name": "Rustam",
            "surname": "Azadaliyev"
        },
        2: {
            "name": "Firuza",
            "surname": "Hasanova"
        }
    }

    if id in students:
        return students[id]
    else:
        return {"msg": "Student not found!"}



