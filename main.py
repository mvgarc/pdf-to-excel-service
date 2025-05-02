from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles


app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "PDF to Excel API is running 🚀"}
