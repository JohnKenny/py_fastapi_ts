"""App entrypoint"""

from fastapi import FastAPI

app = FastAPI(title="My fast API", description="this is my API")

@app.get("/hello-world")
def hello():
    return{"Mensaje": "Ola mundo"}

@app.post("/hello-world-post")
def goodbye():
    return{"Message":"posted to, gual"}