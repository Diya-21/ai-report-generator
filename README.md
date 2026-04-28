---
title: AI Report Generator
emoji: 🏢
colorFrom: blue
colorTo: indigo
sdk: docker
app_port: 7860
---

# AI-Powered DDR Report Generator

An Applied AI project that automatically converts raw site inspection documents and thermal sensor reports into a structured, client-ready Detailed Diagnostic Report (DDR) in DOCX format.

## 🚀 Features
- **Multi-modal Document Parsing:** Extracts both text and images from PDF documents using `PyMuPDF`.
- **Intelligent Data Fusion:** Uses the `Llama-3.1-8B-Instruct` model on Hugging Face to logically merge observations, detect conflicting details, and eliminate duplicates.
- **Context-Aware Image Mapping:** Extracts thermal and visual images from the source PDFs and inserts them directly under the corresponding area-wise observations in the final report.
- **Structured Report Generation:** Dynamically generates a professional Word Document (`.docx`) containing issue summaries, root cause analyses, severity matrices, and recommended actions.
- **Self-Healing AI Logic:** Built-in safeguards extract and sanitize JSON output to prevent hallucinations and schema breaks.

## 🛠️ Technology Stack
- **Backend:** Python, FastAPI, python-docx, PyMuPDF (fitz)
- **Frontend:** Vanilla HTML/CSS/JS (Clean, responsive UI)
- **AI Integration:** Hugging Face Inference API (`meta-llama/Llama-3.1-8B-Instruct` via `InferenceClient`)

## ⚙️ Setup Instructions

### 1. Requirements
- Python 3.9+
- A Hugging Face account and API Token (with access to the Serverless Inference API)

### 2. Installation
Clone the repository:
```bash
git clone https://github.com/Diya-21/ai-report-generator.git
cd ai-report-generator
```

Create a virtual environment:
```bash
python -m venv venv
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate
```

Install the dependencies:
```bash
pip install -r requirements.txt
```

### 3. Environment Variables
Create a `.env` file in the root directory and add your Hugging Face API key:
```env
HF_API_TOKEN=your_hugging_face_token_here
```

### 4. Run the Application
Start the FastAPI server:
```bash
uvicorn backend.main:app --host 0.0.0.0 --port 8000 --reload
```
Open your browser and navigate to `http://localhost:8000` to interact with the UI.

## 📁 Project Structure
- `backend/main.py`: Entry point for the FastAPI server and upload routes.
- `backend/ai_client.py`: Handles Hugging Face Inference API requests and intelligent strict JSON parsing.
- `backend/pdf_parser.py`: Extracts raw text, captures paginated metadata, and saves document images.
- `backend/docx_generator.py`: Converts the AI JSON object and maps the extracted images into a formatted Word document.
- `frontend/index.html`: The user interface for the AI builder.

## 🎯 Evaluation Objectives Met
- **System Thinking:** End-to-end data pipeline moving from raw unstructured PDFs to structured JSON to a client-ready generated DOCX file.
- **Logic & Reliability:** Avoids standard 'chatbot' behavior by writing a headless autonomous pipeline. Designed to handle missing information gracefully ("Not Available") keeping the AI completely grounded without inventing facts.
