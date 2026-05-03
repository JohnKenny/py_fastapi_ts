"""App entrypoint"""

from fastapi import FastAPI
from routes.submit_scores import router

def create_app() -> FastAPI:
    app = FastAPI(title="My fast API", description="this is my API")
    app.include_router(router)
    return app

app = create_app()




