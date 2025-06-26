from sqlalchemy.orm import Session
from models.habit import Habit
from schemas import HabitCreate
from models import habit as models 

def get_habits(db: Session):
    return db.query(Habit).all()


def create_habit(db: Session, habit: HabitCreate):
    db_habit = Habit(name=habit.name, streak=0)
    db.add(db_habit)
    db.commit()
    db.refresh(db_habit)
    return db_habit


def increment_habit(db: Session, habit_id:int):
    habit = db.query(models.Habit).filter(models.Habit.id==habit_id).first()
    if habit:
        habit.streak +=1
        db.commit()
        db.refresh(habit)
    return habit


def delete_habit(db:Session, habit_id:int):
    habit = db.query(models.Habit).filter(models.Habit.id == habit_id).first()
    if habit:
        db.delete(habit)
        db.commit()
        return True 
    
    return False
