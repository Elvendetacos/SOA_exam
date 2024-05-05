from pydantic import BaseModel
from typing import Optional


class StudentRequest(BaseModel):
    name: str
    lastname: str
    age: int
    email: str
    tutor_id: int
    courses: Optional[list[int]]
