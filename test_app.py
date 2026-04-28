import requests
import os
from dotenv import load_dotenv

load_dotenv()

def test_api():
    url = "http://localhost:8000/generate"
    files = {
        "inspection_report": open("dummy_inspection_report.pdf", "rb"),
        "thermal_report": open("dummy_thermal_report.pdf", "rb")
    }
    
    print("Testing API endpoint...")
    try:
        response = requests.post(url, files=files, timeout=60)
        if response.status_code == 200:
            print("SUCCESS: Report generated!")
            with open("test_output.docx", "wb") as f:
                f.write(response.content)
            print("Output saved to test_output.docx")
        else:
            print(f"FAILED: Status {response.status_code}")
            print(f"Response: {response.text}")
    except Exception as e:
        print(f"ERROR: {str(e)}")

if __name__ == "__main__":
    test_api()
