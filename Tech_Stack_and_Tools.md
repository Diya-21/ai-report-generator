# Technology Stack & AI Frameworks

This document outlines the professional tools, libraries, and frameworks utilized to build the DDR Report Generator.

## 1. Backend Framework
- **FastAPI (Python)**: Chosen for its high performance, asynchronous capabilities, and automatic Swagger documentation. It handles the multi-part file uploads for the PDFs efficiently.
- **Uvicorn/Gunicorn**: Production-grade ASGI server used to serve the application with high concurrency.

## 2. Artificial Intelligence & LLM
- **Hugging Face Inference API**: Used for serverless AI execution, allowing the project to remain lightweight without requiring a dedicated GPU server.
- **Model: Llama-3.1-8B-Instruct**: A state-of-the-art Large Language Model from Meta, specifically fine-tuned for following complex instructions and generating structured JSON data.
- **HuggingFace Hub Library**: Facilitates the managed connection to the remote inference servers.

## 3. PDF Data Extraction (OCR & Parsing)
- **PyMuPDF (fitz)**: A high-performance PDF parsing library used to extract:
  - Raw text for AI analysis.
  - Paginated metadata to understand issue locations.
  - Embedded binary images from both Inspection and Thermal documents.

## 4. Document Engineering
- **python-docx**: Used to programmatically construct the final report. This library allows for:
  - Dynamic table creation (Severity matrices, action plans).
  - Automated image scaling and placement.
  - Professional typography and styling (headings, bold headers, bullet points).

## 5. Security & Configuration
- **python-dotenv**: Manages sensitive credentials (API tokens) via a `.env` file, ensuring no secret keys are leaked to version control.
- **Git & .gitignore**: Version control system to manage code changes and prevent committing bulky temporary files or environment secrets.

## 6. Frontend Stack
- **HTML5 & CSS3**: Clean, responsive layout designed for a SaaS-like experience.
- **JavaScript (ES6)**: Handles the asynchronous `fetch` requests to the backend, manages the progress state of the AI generation, and triggers the automated file download on success.
