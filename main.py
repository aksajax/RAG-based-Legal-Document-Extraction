# main.py
import json
from src.pdf_parser import extract_pdf_pages
from src.chain_extractor import extract_legal_info_and_chain

def run_pipeline(pdf_path: str):
    print(f"📄 Step 1: Parsing PDF from {pdf_path}...")
    pdf_pages = extract_pdf_pages(pdf_path)
    
    print(f"✅ Extracted {len(pdf_pages)} pages.")
    
    print("🔍 Step 2: Extracting Key Entities and Title Chain...")
    structured_result = extract_legal_info_and_chain(pdf_pages)
    
    # Convert Pydantic object to dictionary / JSON
    output_dict = structured_result.model_dump()
    
    print("\n================ EXTRACTED LEGAL DATA ================\n")
    print(json.dumps(output_dict, indent=2, ensure_ascii=False))
    
    # Save output to JSON file
    with open("output_result.json", "w", encoding="utf-8") as f:
        json.dump(output_dict, f, indent=2, ensure_ascii=False)
        
    print("\n🎉 Output successfully saved to 'output_result.json'")

if __name__ == "__main__":
    PDF_FILE_PATH = "data/Shalendra.pdf"
    run_pipeline(PDF_FILE_PATH)