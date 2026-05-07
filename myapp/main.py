"""App entrypoint"""

from fastapi import FastAPI
from routes.submit_scores import router as scores_router
from routes.recieve_file import router as file_router
from routes.hello_world import router as hello_world


def create_app() -> FastAPI:
    app = FastAPI(title="My fast API", description="this is my API")
    app.include_router(scores_router)
    app.include_router(file_router)
    app.include_router(hello_world)
    return app

app = create_app()




