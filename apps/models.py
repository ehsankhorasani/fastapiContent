import enum
from datetime import datetime

from sqlalchemy import Column, String, Integer, DateTime, Enum

from apps.database.connection import Base
from apps.utils import ContentType


class Content(Base):
    __tablename__ = "content"
    id = Column(Integer, primary_key=True, index=True)
    persian_title = Column(String, index=True)
    english_title = Column(String, nullable=True)
    age = Column(Integer)
    poster = Column(String, nullable=True)
    content_type = Column(Enum(ContentType))
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, onupdate=datetime.now)
