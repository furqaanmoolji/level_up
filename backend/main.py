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


app = FastAPI()
# 👇 Allow frontend to call backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
habit_model.Base.metadata.create_all(bind=engine)


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



