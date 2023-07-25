from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from apps import crud
from apps.schemas import ContentBase, ContentResponse
from apps.utils import get_db

router = APIRouter(
    prefix="/content",
    tags=["content"],
    responses={404: {"description": "Not Found"}}
)


@router.post("/add", response_model=ContentResponse)
async def create_content(content: ContentBase, db: Session = Depends(get_db)):
    db_content = crud.create_content(db=db, c=content)
    return db_content


@router.get("/{content_id}", response_model=ContentResponse)
async def get_content(content_id: int, db: Session = Depends(get_db)):
    content = crud.get_content(db=db, content_id=content_id)
    return content
