from pydantic import BaseModel


class TutorRequest(BaseModel):
    name: str
    lastname: str
    age: int
    email: str
