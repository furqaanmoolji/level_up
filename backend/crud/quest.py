from sqlalchemy.orm import Session
from models.quests import Quest
from models.subtask import SubTask
import schemas


def get_quests(db: Session):
    return db.query(Quest).all()


def create_quest(db: Session, quest_data: schemas.QuestCreate):
    quest = Quest(title=quest_data.title, difficulty=quest_data.difficulty)

    if quest_data.subtasks:
        for task_data in quest_data.subtasks:
            subtask = SubTask(title=task_data.title, is_completed=False)
            quest.subtasks.append(subtask)

    db.add(quest)
    db.commit()
    db.refresh(quest)
    return quest


def add_subtask_to_quest(db: Session, quest_id: int, subtask_data: schemas.SubTaskCreate):
    quest = db.query(Quest).filter(Quest.id == quest_id).first()
    if not quest:
        return None

    subtask = SubTask(title=subtask_data.title, is_completed=False, quest_id=quest.id)
    db.add(subtask)
    db.commit()
    db.refresh(subtask)
    return subtask


def toggle_subtask_completion(db: Session, subtask_id: int):
    subtask = db.query(SubTask).filter(SubTask.id == subtask_id).first()
    if not subtask:
        return None

    subtask.is_completed = not subtask.is_completed
    db.commit()
    db.refresh(subtask)
    return subtask
