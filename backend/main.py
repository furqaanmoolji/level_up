from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, engine
import models.habit as habit_model
import crud.habit as habit_crud
from schemas import HabitCreate, HabitResponse
from typing import List
import schemas
import crud 
from fastapi.middleware.cors import CORSMiddleware
from models.habit import Habit, HabitCompletion
from datetime import date
from models import user  # this ensures table gets created
from database import Base, engine
from models import quests, subtask  # ensures tables get created
from crud import quest as quest_crud
from schemas import QuestCreate, Quest, SubTaskCreate, SubTask



app = FastAPI()
# 👇 Allow frontend to call backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


Base.metadata.create_all(bind=engine)



def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/habits", response_model=List[HabitResponse])
def read_habits(db: Session = Depends(get_db)):
    return habit_crud.get_habits(db)

@app.post("/habits", response_model=HabitResponse)
def create_habit(habit: HabitCreate, db: Session = Depends(get_db)):
    return habit_crud.create_habit(db, habit)

@app.patch("/habits/{habit_id}/increment", response_model=schemas.HabitResponse)
def increment_habit_route(habit_id: int, db: Session = Depends(get_db)):
    return habit_crud.increment_habit(db, habit_id)


@app.delete("/habits/{habit_id}")
def delete_habit_route(habit_id: int, db:Session = Depends(get_db)):
    return habit_crud.delete_habit(db, habit_id)


# in your FastAPI routes
@app.get("/habits/{habit_id}/completions")
def get_completions(habit_id: int, db: Session = Depends(get_db)):
    completions = db.query(HabitCompletion).filter(HabitCompletion.habit_id == habit_id).all()
    return [{"date": c.date.isoformat()} for c in completions]


@app.get("/create-user")
def create_user(db: Session = Depends(get_db)):
    from crud.user import create_test_user
    return create_test_user(db)


@app.get("/quests", response_model=List[Quest])
def get_quests(db: Session = Depends(get_db)):
    return quest_crud.get_quests(db)

@app.post("/quests", response_model=Quest)
def create_quest(quest: QuestCreate, db: Session = Depends(get_db)):
    return quest_crud.create_quest(db, quest)

@app.post("/quests/{quest_id}/subtasks", response_model=SubTask)
def add_subtask(quest_id: int, subtask: SubTaskCreate, db: Session = Depends(get_db)):
    return quest_crud.add_subtask_to_quest(db, quest_id, subtask)

@app.patch("/subtasks/{subtask_id}/toggle", response_model=SubTask)
def toggle_subtask(subtask_id: int, db: Session = Depends(get_db)):
    return quest_crud.toggle_subtask_completion(db, subtask_id)


