from fastapi import APIRouter, Response

router = APIRouter()

@router.get("/hello-world/{value}")
async def hello_world(value, name: str, city: str = "Londom"):
    print("Test", value)
    print(f"Name: {name.title()}, City: {city.title()}")
    return {f"Hello world.. {name.title()}, {city.title()}"}

