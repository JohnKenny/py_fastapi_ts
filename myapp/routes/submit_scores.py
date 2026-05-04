from fastapi import APIRouter
from pydantic import BaseModel
from processing.add_to_csv import add_student_score

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


