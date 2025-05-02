
# PDF to Excel Conversion API

This project is a FastAPI-based microservice that allows users to upload PDF files and convert them into Excel format. It uses the Gemini API by Google to process the PDF and extract the content, which is then structured into a table and saved as an Excel file. The converted Excel file is then returned to the user for download.

## Features

- **PDF Upload**: Accepts PDF files for conversion.
- **Gemini API**: Uses Google's Gemini API to process and extract structured data from the PDF.
- **Excel Output**: Converts the extracted data into an Excel `.xlsx` file.
- **FastAPI**: Fast and efficient web framework for building the service.

## Requirements

- Python 3.8+
- FastAPI
- Uvicorn
- google-generativeai (Gemini API SDK)
- python-dotenv
- pandas
- openpyxl
- python-multipart

## Installation

1. Clone this repository:

```bash
git clone https://github.com/your-username/pdf-to-excel-service.git
cd pdf-to-excel-service
```

2. Create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # For Windows: venv/Scripts/activate
```

3. Install the required dependencies:

```bash
pip install -r requirements.txt
```

4. Add your Gemini API key in a `.env` file in the root directory:

```
GEMINI_API_KEY=your_actual_api_key_here
```

## Usage

1. Run the FastAPI server:

```bash
uvicorn main:app --reload
```

2. Open the API documentation at [http://localhost:8000/docs](http://localhost:8000/docs) to interact with the API.

3. Use the `/convert` endpoint to upload a PDF file and receive the converted Excel file.

## Example Request (via Swagger UI)

- **Method**: POST
- **Endpoint**: `/convert`
- **Body**: PDF file (type `application/pdf`)

The response will contain the Excel file in `.xlsx` format.

## Development

To run the project locally for development, ensure that you have set up the `.env` file with your Gemini API key, and install all required dependencies.

## License

This project is licensed under the MIT License.