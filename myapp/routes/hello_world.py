from fastapi import APIRouter, Response

router = APIRouter()

@router.get("/hello-world")
async def hello_world():
    return {"Hello world"}