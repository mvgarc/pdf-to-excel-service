from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import FileResponse
from google.generativeai import GenerativeModel
from dotenv import load_dotenv
import os
import pandas as pd
from tempfile import NamedTemporaryFile

load_dotenv()

app = FastAPI()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

@app.get("/")
def read_root():
    return {"message": "PDF to Excel conversion service is running."}
