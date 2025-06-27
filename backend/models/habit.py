from sqlalchemy import Column, Integer, String, Date, ForeignKey
from database import Base
from sqlalchemy.orm import relationship


class HabitCompletion(Base):
    __tablename__ = "habit_completions"
    id = Column(Integer, primary_key=True)
    habit_id = Column(Integer, ForeignKey("habits.id"))
    date = Column(Date)

class Habit(Base):
    __tablename__ = "habits"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    streak = Column(Integer, default=0)

    completions = relationship("HabitCompletion", backref="habit")
    