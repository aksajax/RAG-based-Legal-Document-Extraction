# src/pdf_parser.py
import pymupdf
import easyocr
import numpy as np
from PIL import Image
import io
from typing import List, Dict

# Initialize EasyOCR reader (loads English OCR model into memory)
reader = easyocr.Reader(['en'], gpu=False)

def extract_pdf_pages(pdf_path: str) -> List[Dict[str, any]]:
    doc = pymupdf.open(pdf_path)
    extracted_pages = []

    print("📖 Reading and extracting scanned PDF pages via EasyOCR...")
    for page_num in range(len(doc)):
        page = doc[page_num]
        text = page.get_text("text").strip()
        
        # If standard text extraction fails (scanned PDF), run EasyOCR
        if not text:
            pix = page.get_pixmap(dpi=150)
            img = Image.open(io.BytesIO(pix.tobytes()))
            img_np = np.array(img)
            
            # Extract text lines using EasyOCR
            results = reader.readtext(img_np, detail=0)
            text = "\n".join(results)

        clean_text = "\n".join([line.strip() for line in text.splitlines() if line.strip()])
        
        if clean_text:
            extracted_pages.append({
                "page_number": page_num + 1,
                "content": clean_text
            })
            
    doc.close()
    
    total_chars = sum(len(p['content']) for p in extracted_pages)
    print(f"📊 Total Text Pages Extracted: {len(extracted_pages)} / Total Characters: {total_chars}")
    
    return extracted_pages