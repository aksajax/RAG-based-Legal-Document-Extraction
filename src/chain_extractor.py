# src/chain_extractor.py
import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from src.schema import LegalReportExtractionSchema

load_dotenv()

def extract_legal_info_and_chain(pdf_pages: list) -> LegalReportExtractionSchema:
    """
    Combines PDF pages and extracts structured entities and ownership history.
    """
    # Combine pages with page number markers
    page_texts = []
    for page in pdf_pages:
        content = page['content'].strip()
        if content:
            page_texts.append(f"--- PAGE {page['page_number']} ---\n{content}")

    full_document_text = "\n\n".join(page_texts)

    # Use active Groq 70B model for high precision on legal documents
    llm = ChatGroq(
        model_name="llama-3.3-70b-versatile",
        groq_api_key=os.getenv("GROQ_API_KEY"),
        temperature=0.0
    )
    
    structured_llm = llm.with_structured_output(LegalReportExtractionSchema)

    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are an expert Indian Legal and Property Title Search Report Analyzer."),
        ("human", """Carefully review the provided Indian Legal Title Search Report / Legal Opinion document.

Extraction Directives:
1. Extract values for Sub Registrar Office, District, Loan Account Number, Property Flat/Plot Details, Total Area, Boundaries (East, West, North, South), and Present Owner names.
2. If a field contains blank underlines like '------' or '_____', output null. If actual names or values exist, extract them accurately.
3. Reconstruct the full step-by-step chronological Title Ownership History / Flow Chain (from initial owner -> intermediate deeds/co-owners -> present owner) including transfer type, deed numbers, and dates.

Document Text:
{context}""")
    ])

    chain = prompt | structured_llm
    
    # Passing context (keeping within safe token window limits)
    context_payload = full_document_text[:50000]
    
    print("🤖 Processing document with Groq (llama-3.3-70b-versatile)...")
    extracted_data = chain.invoke({"context": context_payload})
    return extracted_data   