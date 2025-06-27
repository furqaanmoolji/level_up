from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Date, ForeignKey
from database import Base
from sqlalchemy.orm import relationship


class Quest(Base):
    __tablename__ = "quests"
    id = Column(Integer, primary_key=True)
    title = Column(String)
    difficulty = Column(Integer, default=1)

    subtasks = relationship("SubTask", back_populates="quest", cascade="all, delete-orphan")
