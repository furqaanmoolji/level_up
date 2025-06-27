from models.user import User
from sqlalchemy.orm import Session

def create_test_user(db: Session):
    existing = db.query(User).filter_by(username="solo_player").first()
    if not existing:
        user = User(username="solo_player")
        db.add(user)
        db.commit()
        db.refresh(user)
    return existing or user
