from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class SubTask(Base):
    __tablename__ = "subtasks"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    is_completed = Column(Boolean, default=False)
    quest_id = Column(Integer, ForeignKey("quests.id"))

    quest = relationship("Quest", back_populates="subtasks")
