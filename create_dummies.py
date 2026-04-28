from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os

def create_inspection_report():
    path = "dummy_inspection_report.pdf"
    c = canvas.Canvas(path, pagesize=letter)
    c.setFont("Helvetica-Bold", 16)
    c.drawString(100, 750, "BUILDING INSPECTION REPORT")
    
    c.setFont("Helvetica", 12)
    c.drawString(100, 720, "Property: Sunshine Apartments, Block A")
    c.drawString(100, 705, "Date: April 25, 2026")
    
    c.setFont("Helvetica-Bold", 14)
    c.drawString(100, 670, "Observations:")
    
    c.setFont("Helvetica", 12)
    lines = [
        "1. Living Room: Visible water staining on the ceiling near the north window.",
        "2. Master Bedroom: Minor cracks observed in the plaster on the west wall.",
        "3. Roof: Blocked gutters on the northeast corner causing overflow during rain.",
        "4. Kitchen: Cabinet hinges are loose and need adjustment."
    ]
    y = 650
    for line in lines:
        c.drawString(100, y, line)
        if "Living Room" in line:
            # Add a dummy image for testing extraction
            if os.path.exists("dummy_img.png"):
                c.drawImage("dummy_img.png", 100, y - 120, width=150, height=100)
                y -= 120
        y -= 20
        
    c.save()
    print(f"Created {path}")

def create_thermal_report():
    path = "dummy_thermal_report.pdf"
    c = canvas.Canvas(path, pagesize=letter)
    c.setFont("Helvetica-Bold", 16)
    c.drawString(100, 750, "THERMAL IMAGING ANALYSIS")
    
    c.setFont("Helvetica", 12)
    c.drawString(100, 720, "Property: Sunshine Apartments, Block A")
    c.drawString(100, 705, "Date: April 25, 2026")
    
    c.setFont("Helvetica-Bold", 14)
    c.drawString(100, 670, "Thermal Findings:")
    
    c.setFont("Helvetica", 12)
    findings = [
        "Area: Living Room Ceiling",
        "Finding: Significant moisture detected behind the drywall. Temperature 14°C (Ambient 22°C).",
        "",
        "Area: Master Bedroom Wall",
        "Finding: No significant thermal anomalies detected. Surface temperature uniform at 21.5°C.",
        "",
        "Area: Electrical Panel",
        "Finding: Circuit breaker #4 is showing signs of overheating (45°C). Immediate inspection required."
    ]
    y = 650
    for line in findings:
        c.drawString(100, y, line)
        if "Electrical Panel" in line:
            if os.path.exists("dummy_img.png"):
                c.drawImage("dummy_img.png", 100, y - 120, width=150, height=100)
                y -= 120
        y -= 20
        
    c.save()
    print(f"Created {path}")

if __name__ == "__main__":
    create_inspection_report()
    create_thermal_report()
