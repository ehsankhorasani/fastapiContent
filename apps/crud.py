from sqlalchemy.orm import Session

from apps.models import Content
from apps.schemas import ContentBase


def create_content(db: Session, c: ContentBase):
    content = Content(**c.model_dump())
    db.add(content)
    db.commit()
    db.refresh(content)
    return content


def get_content(db: Session, content_id: int):
    content = db.query(Content).filter(Content.id == content_id).first()
    return content
