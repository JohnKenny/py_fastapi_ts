"""Endpoint to recieve and process a file """
from fastapi import APIRouter, File, UploadFile
from fastapi.responses import JSONResponse

router = APIRouter()

@router.post("/post-file")
async def post_file(file: UploadFile = File(...)): 
    """Endpoint to recieve a file"""
    contents = await file.read()
    return JSONResponse(content={"filename": file.filename, "Contents:": str(contents)})
    
    # print(f"contents: {contents}")
    # return 200

