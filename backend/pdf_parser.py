import fitz

def extract_pdf_data(pdf_bytes):
    try:
        doc = fitz.open(stream=pdf_bytes, filetype="pdf")
    except Exception as e:
        raise ValueError(f"Could not open PDF: {e}")
        
    text_content = ""
    images_info = {}
    
    for page_num in range(len(doc)):
        page = doc[page_num]
        page_text = page.get_text()
        
        current_page = page_num + 1
        text_content += f"\n--- [START OF PAGE {current_page}] ---\n"
        text_content += page_text.strip()
        text_content += f"\n--- [END OF PAGE {current_page}] ---\n"
        
        image_list = page.get_images(full=True)
        for img in image_list:
            xref = img[0]
            try:
                base_image = doc.extract_image(xref)
                image_bytes = base_image["image"]
                ext = base_image["ext"]
                if current_page not in images_info:
                    images_info[current_page] = []
                images_info[current_page].append({
                    "bytes": image_bytes,
                    "ext": ext
                })
            except Exception:
                pass
                
    if not text_content.strip().replace("--- [START OF PAGE", "").replace("--- [END OF PAGE", ""):
        raise ValueError("PDF appears to be scanned. Please upload a text-based PDF.")
        
    return text_content, images_info
