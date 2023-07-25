from datetime import datetime

from pydantic import BaseModel

from apps.utils import ContentType


class ContentBase(BaseModel):
    persian_title: str
    english_title: str
    age: int
    poster: str
    content_type: ContentType

    class Config:
        orm_mode = True


class ContentResponse(BaseModel):
    persian_title: str
    english_title: str
    age: int
    poster: str
    content_type: ContentType
    created_at: datetime
