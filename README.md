# PDF to Excel Microservice 📄➡️📊

This microservice allows you to convert PDF files into Excel format via a simple HTTP API. It is built using **FastAPI**, and designed to be easily integrated with other backend systems or front-end applications.

---

## 🚀 Features

- Accepts PDF files via POST requests
- Extracts text from PDF using `PyMuPDF`
- Converts the extracted text into a table-like structure
- Exports the data into an `.xlsx` file using `pandas` and `openpyxl`
- Returns the Excel file as a downloadable response

---

## 🔧 Tech Stack

- [FastAPI](https://fastapi.tiangolo.com/)
- [PyMuPDF](https://pymupdf.readthedocs.io/)
- [Pandas](https://pandas.pydata.org/)
- [Uvicorn](https://www.uvicorn.org/)
- [OpenPyXL](https://openpyxl.readthedocs.io/)

---

## 📦 Installation (local)

```bash
# Clone the repo
git clone https://github.com/your-username/pdf-to-excel-service.git
cd pdf-to-excel-service

# Create virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt

# Run the server
uvicorn main:app --reload
```

The service will be available at `http://localhost:8000`

---

## 🧪 API Usage

**Endpoint:**  
`POST /convert`

**Form Data:**
- `file`: PDF file to convert (type: `application/pdf`)

**Response:**  
Returns the `.xlsx` file as a downloadable response.

**Example with curl:**

```bash
curl -X POST "http://localhost:8000/convert" \
  -H "accept: application/json" \
  -F "file=@yourfile.pdf" \
  --output converted.xlsx
```

---

## ☁️ Deploy to Render

Create a `.render.yaml` file with the following content:

```yaml
services:
  - type: web
    name: pdf-to-excel
    runtime: python
    buildCommand: pip install -r requirements.txt
    startCommand: uvicorn main:app --host 0.0.0.0 --port 10000
```

Push to GitHub and create a **Web Service** in [Render](https://render.com/).

---

## 📄 License

This project is licensed under the MIT License.

---

## ✨ Author

Made with ❤️ by [Maria García](https://github.com/mvgarc)
