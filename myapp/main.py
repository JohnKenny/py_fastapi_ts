"""App entrypoint"""

from fastapi import FastAPI

app = FastAPI(title="My fast API", description="this is my API")

@app.get("/hello-world")
def ola():
    return{"Mensaje": "Ola mundo"}