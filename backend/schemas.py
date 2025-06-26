from pydantic import BaseModel

class HabitCreate(BaseModel):
    name:str

class HabitResponse(HabitCreate):
    id:int
    streak:int

    class Config:
        orm_mode = True