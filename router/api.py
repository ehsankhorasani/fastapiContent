from fastapi import APIRouter
from apps import views

router = APIRouter()
router.include_router(views.router)
