# Project model or data classes
from pydantic import BaseModel, Field

class TestModel(BaseModel):
    name: str
    age: int=Field(default=0,ge=0,le=200)
    is_active: bool
