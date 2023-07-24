from typing import Optional, Union

from pydantic import BaseModel


class CommonModel(BaseModel):
    name: str
    day: float | int | None = "AAAa"


class CommonResponse(BaseModel):
    name: str
