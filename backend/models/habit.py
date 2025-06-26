from sqlalchemy import Column, Integer, String 
from database import Base

class Habit(Base):
    __tablename__ = "habits"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    streak = Column(Integer, default=0)

    