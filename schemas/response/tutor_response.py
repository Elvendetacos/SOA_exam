from pydantic import BaseModel


class TutorResponse(BaseModel):
    id: int
    name: str
    lastname: str
    age: int
