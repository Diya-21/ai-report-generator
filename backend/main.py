from fastapi import FastAPI, File, UploadFile, Form, HTTPException
from fastapi.responses import HTMLResponse, StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
import os
import json
import traceback

from backend.pdf_parser import extract_pdf_data
from backend.ai_client import generate_ddr_json
from backend.docx_generator import generate_report_docx

import os
from dotenv import load_dotenv

load_dotenv()
os.environ["HUGGINGFACEHUB_API_TOKEN"] = os.getenv("HF_API_TOKEN", "")

app = FastAPI(title="DDR Report Generator")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/", response_class=HTMLResponse)
async def read_index():
    try:
        with open("frontend/index.html", "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return "Frontend not found"

@app.post("/generate")
async def generate_report(
    inspection_report: UploadFile = File(...),
    thermal_report: UploadFile = File(...)
):
    load_dotenv() # Force reload to catch latest manual edits
    api_key = os.getenv("HF_API_TOKEN")
    if not api_key:
        raise HTTPException(status_code=500, detail="Hugging Face API Token not found in .env file (HF_API_TOKEN)")
        
    try:
        insp_bytes = await inspection_report.read()
        therm_bytes = await thermal_report.read()
        
        # 1. Parse PDFs
        try:
            insp_text, insp_images = extract_pdf_data(insp_bytes)
        except ValueError as e:
            raise HTTPException(status_code=400, detail=f"Inspection Report Error: {str(e)}")
            
        try:
            therm_text, therm_images = extract_pdf_data(therm_bytes)
        except ValueError as e:
            raise HTTPException(status_code=400, detail=f"Thermal Report Error: {str(e)}")
            
        # 2. Get AI JSON
        try:
            ddr_json = generate_ddr_json(insp_text, therm_text, api_key)
        except Exception as e:
            if "invalid JSON" in str(e).lower() or isinstance(e, json.JSONDecodeError):
                raise HTTPException(status_code=500, detail=f"AI returned invalid JSON: {str(e)}")
            raise HTTPException(status_code=500, detail=f"AI Generation Failed: {str(e)}")
            
        # 3. Generate Docx
        try:
            docx_stream = generate_report_docx(ddr_json, insp_text, therm_text, insp_images, therm_images)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error generating document: {str(e)}")
            
        headers = {
            "Content-Disposition": 'attachment; filename="DDR_Report.docx"'
        }
        return StreamingResponse(docx_stream, headers=headers, media_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document")
        
    except HTTPException:
        raise
    except Exception as e:
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=f"An unexpected error occurred: {str(e)}")
        
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
