from sqlalchemy.orm import Session
from models.habit import Habit
from schemas import HabitCreate
from models import habit as models 
from models.habit import Habit, HabitCompletion
from datetime import date

def get_habits(db: Session):
    return db.query(Habit).all()


def create_habit(db: Session, habit: HabitCreate):
    db_habit = Habit(name=habit.name, streak=0)
    db.add(db_habit)
    db.commit()
    db.refresh(db_habit)
    return db_habit


def increment_habit(db: Session, habit_id: int):
    today = date.today()

    # Fetch the habit
    habit = db.query(Habit).filter(Habit.id == habit_id).first()

    if habit:
        # Check if there's already a completion for today
        existing = db.query(HabitCompletion).filter_by(habit_id=habit_id, date=today).first()

        if not existing:
            # Log completion
            completion = HabitCompletion(habit_id=habit_id, date=today)
            db.add(completion)

            # Increment streak
            habit.streak += 1

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
