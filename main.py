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

# IMPORTANTE: Configurar el modelo de Gemini usando la librería de Google
# Placeholder, debo de integrar según la implementación de Gemini que voy a usar
def process_pdf_with_gemini(pdf_bytes: bytes) -> pd.DataFrame:
    # TODO: Aquí va la lógica real de llamada a Gemini API con el contenido del PDF
    # Ejemplo ficticio: asumimos que el modelo devuelve una tabla con columnas y filas.
    data = {
        "Column A": ["Row 1", "Row 2"],
        "Column B": [123, 456],
    }
    df = pd.DataFrame(data)
    return df

@app.post("/convert")
async def convert_pdf(file: UploadFile = File(...)):
    if file.content_type != "application/pdf":
        raise HTTPException(status_code=400, detail="Only PDF files are accepted.")

    pdf_bytes = await file.read()

    try:
        df = process_pdf_with_gemini(pdf_bytes)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing PDF: {str(e)}")

    with NamedTemporaryFile(delete=False, suffix=".xlsx") as tmp:
        df.to_excel(tmp.name, index=False)
        return FileResponse(path=tmp.name, filename="converted.xlsx", media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")