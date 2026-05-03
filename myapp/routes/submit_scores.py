from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


class Score(BaseModel):
    """Model representing a score"""
    name: str
    math_score: int
    english_score: int


@router.post("/submit-score")
def submit_score(score: Score):
    return{"Message": f"Gual, gracias {score.name}"}

# @router.get("/hello-world")
# def hello():
#     return{"Mensaje": "Ola mundo"}


