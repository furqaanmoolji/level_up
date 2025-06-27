from pydantic import BaseModel
from typing import List, Optional

# ---------------------- HABITS ----------------------

class HabitCreate(BaseModel):
    name: str

class HabitResponse(HabitCreate):
    id: int
    streak: int

    class Config:
        from_attributes = True  # use this if using Pydantic v2+ (instead of orm_mode)


# ---------------------- SUBTASKS ----------------------

class SubTaskBase(BaseModel):
    title: str

class SubTaskCreate(SubTaskBase):
    pass

class SubTask(SubTaskBase):
    id: int
    is_completed: bool

    class Config:
        from_attributes = True


# ---------------------- QUESTS ----------------------

class QuestBase(BaseModel):
    title: str
    difficulty: int = 1

class QuestCreate(QuestBase):
    subtasks: Optional[List[SubTaskCreate]] = []

class Quest(QuestBase):
    id: int
    subtasks: List[SubTask] = []

    class Config:
        from_attributes = True
