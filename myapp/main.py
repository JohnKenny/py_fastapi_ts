"""App entrypoint"""

from fastapi import FastAPI
from pydantic import BaseModel

class Score(BaseModel):
    """Model representing a score"""
    name: str
    math_score: int
    english_score: int

app = FastAPI(title="My fast API", description="this is my API")

@app.get("/hello-world")
def hello():
    return{"Mensaje": "Ola mundo"}

@app.post("/submit-score")
def submit_score():
    return{"Message":"posted to, gual"}