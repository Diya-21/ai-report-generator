# Loom Video Presentation Guide

Here is a structured script and talking points for your 3-5 minute Loom video. 

## 1. What You Built
"Hi, I'm [Your Name], and for the Applied AI Builder assignment, I built an automated Detailed Diagnostic Report (DDR) Generator.
It's an end-to-end AI pipeline that takes unstructured raw site inspection data and thermal imaging reports, intelligently merges them, and generates a client-ready, fully formatted Word Document."

## 2. How it Works
"The system is built using Python with FastAPI for the backend, and vanilla HTML/JS for a clean frontend interface. Here is how the pipeline operates:
1. **Document Parsing**: When the user uploads the PDFs, I use `PyMuPDF` to extract not just the text, but also the page context and embedded images.
2. **AI Data Fusion**: The raw text from both reports is passed to the Hugging Face Serverless Inference API. I specifically chose the `Llama-3.1-8B-Instruct` model because of its high reliability with prompt following. The AI is instructed via a strict system prompt to cross-reference observations, find thermal overlaps, eliminate duplicates, and output a strict JSON structure.
3. **Self-Healing Logic**: To ensure the pipeline never breaks, I implemented a robust JSON extraction regex and a cleaning script that repairs common AI formatting errors like single quotes or trailing commas. 
4. **Context-Aware Visuals**: Finally, the system maps the extracted images to the correct JSON sections by doing fuzzy string matching against the page text, inserting the pictures dynamically into an automated `python-docx` document."

## 3. Limitations
"While the tool works beautifully, there are a few limitations in its current state:
1. **Free-Tier API Constraints**: Relying on Hugging Face's free inference API means the system could occasionally face latency, model-swaps, or rate limits.
2. **Vision-to-Text Mapping**: The heuristic that maps images to text relies on locating matching keywords on the same page. If a PDF has images placed completely separately from the text descriptions (e.g., an 'Appendix' at the end of a 50-page document), the code might fail to pair the image to the correct finding."

## 4. How You Would Improve It
"If I were to take this to production, I would improve it by:
1. **Dedicated AI Endpoints**: I would swap the free Hugging Face endpoint for a dedicated OpenAI (GPT-4o) or Anthropic backend for faster parsing, uptime guarantees, and a much larger context window for massive documents.
2. **Database & Cloud Storage**: I would integrate a PostgreSQL database and AWS S3 object storage to securely store past reports and images. I would also add user authentication so different inspectors can access their history.
3. **Vision-Language Models (VLMs)**: Instead of just extracting images using standard PDF libraries, I would pass the actual images directly to a multimodal LLM. This would let the AI 'see' the thermal heat maps or physical cracks, analyze the severity visually, and write its own insights based on those images."
