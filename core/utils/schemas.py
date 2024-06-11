from pydantic import BaseModel


class ScoreValidator(BaseModel):
    subject: int
    point: int
