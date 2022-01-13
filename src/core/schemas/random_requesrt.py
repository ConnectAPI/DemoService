from dataclasses import Field
from typing import Tuple

from pydantic import BaseModel, constr


class RandomRequest(BaseModel):
    range: Tuple[int, int] = Field(default=(0, 100))
    name: constr(min_length=2, max_length=10)


class RandomResponse(BaseModel):
    value: int
