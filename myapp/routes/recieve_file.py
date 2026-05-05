"""Endpoint to recieve and process a file """
from fastapi import APIRouter, File, UploadFile

router = APIRouter()