from fastapi import APIRouter

from apps.models.common import CommonModel, CommonResponse

router = APIRouter(
    prefix="/common",
    tags=["common"],
    responses={404: {"description": "Not Found"}}
)


@router.post("/h", response_model=CommonResponse)
async def hello(common: CommonModel):
    return common
