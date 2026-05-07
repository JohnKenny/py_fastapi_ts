from fastapi import APIRouter, Response

router = APIRouter()

@router.get("/hello-world")
async def hello_world(name: str, city: str = "Londom"):
    print(f"Name: {name.title()}, City: {city.title()}")
    return {f"Hello world.. {name.title()}, {city.title()}"}

