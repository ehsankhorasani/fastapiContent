from fastapi import APIRouter
from apps.endpoints import common

router = APIRouter()
router.include_router(common.router)
