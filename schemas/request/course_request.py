from pydantic import BaseModel
from typing import Optional


class CourseRequest(BaseModel):
    name: str
    student_id: Optional[list[int]]
