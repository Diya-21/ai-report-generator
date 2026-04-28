import json
import re
from huggingface_hub import InferenceClient

SYSTEM_PROMPT = """You are an expert building inspector report writer. 
You will be given raw text extracted from two documents:
1. An Inspection Report
2. A Thermal Report

Your job is to generate a structured DDR (Detailed Diagnostic Report) in JSON format.

STRICT RULES:
- Do NOT invent or assume any facts not present in the documents
- If information is missing → write "Not Available"
- If inspection and thermal reports conflict → write "Conflict noted: [explain both sides]"
- Use simple, client-friendly language. Avoid technical jargon.
- Deduplicate — if both documents mention the same issue, merge them into one point
- Be specific about locations/areas wherever mentioned

Return ONLY valid JSON in this exact structure:
{
  "property_issue_summary": "string",
  "area_wise_observations": [
    {
      "area": "area name",
      "observation": "what was found",
      "thermal_finding": "thermal data or Not Available",
      "image_hint": "description"
    }
  ],
  "probable_root_cause": [
    {
      "issue": "issue name",
      "root_cause": "explanation"
    }
  ],
  "severity_assessment": [
    {
      "issue": "issue name",
      "severity": "High / Medium / Low",
      "reasoning": "why"
    }
  ],
  "recommended_actions": [
    {
      "issue": "issue name",
      "action": "what should be done",
      "priority": "Immediate / Short-term / Long-term"
    }
  ],
  "additional_notes": "string or Not Available",
  "missing_or_unclear_information": ["list"]
}
"""

import requests

import openai

def generate_ddr_json(inspection_text: str, thermal_text: str, api_key: str):
    client = InferenceClient(api_key=api_key)
    
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT.replace("Return ONLY valid JSON", "Return ONLY a JSON object. No other text.")},
        {"role": "user", "content": f"INSPECTION:\n{inspection_text}\n\nTHERMAL:\n{thermal_text}"}
    ]
    
    try:
        response = client.chat_completion(
            messages=messages,
            model="meta-llama/Llama-3.1-8B-Instruct",
            max_tokens=3000,
            temperature=0.1
        )
        content = response.choices[0].message.content.strip()
        
        with open("ai_raw_output.txt", "w", encoding="utf-8") as f:
            f.write(content)

        # Cleaning step: Extract valid-looking JSON
        start_idx = content.find('{')
        end_idx = content.rfind('}')
        if start_idx != -1 and end_idx != -1:
            content = content[start_idx:end_idx+1]

        try:
            return json.loads(content)
        except json.JSONDecodeError:
            # Fallback cleanup
            content = re.sub(r'//.*', '', content) # Remove comments if any
            # Fix common quoting errors
            content = re.sub(r"'(.*?)':", r'"\1":', content)
            # Remove trailing commas before closing braces
            content = re.sub(r",\s*([\]}])", r"\1", content)
            return json.loads(content)
            
    except Exception as e:
        raise Exception(f"AI Generation Failed: {str(e)}")
