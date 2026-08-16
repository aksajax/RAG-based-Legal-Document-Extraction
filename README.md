<img width="1355" height="680" alt="Screenshot 2026-08-16 184243" src="https://github.com/user-attachments/assets/245c587d-305a-4561-a3fb-77345558eb18" />
<img width="1365" height="679" alt="Screenshot 2026-08-16 184321" src="https://github.com/user-attachments/assets/7f7d1f36-3a74-4287-a53e-1bce50ba1878" />
<img width="1350" height="487" alt="Screenshot 2026-08-16 184211" src="https://github.com/user-attachments/assets/cb3ce325-76fa-4ca2-9ae3-9087dabf4b22" />
<img width="1360" height="685" alt="Screenshot 2026-08-16 184154" src="https://github.com/user-attachments/assets/6b7ce74c-358d-49f5-8c73-97474957e8a2" />
# ⚖️ RAG-based Legal Document Extraction & Title Chain Parser

<div align="center">

### 🤖 AI-Powered Indian Property Legal Document Intelligence

**OCR • PyMuPDF • LangChain • Groq Llama-3 • Pydantic • Streamlit**

<br/>

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge\&logo=python\&logoColor=white)](https://www.python.org/)
[![LangChain](https://img.shields.io/badge/LangChain-LLM%20Pipeline-1C3C3C?style=for-the-badge)](https://www.langchain.com/)
[![Groq](https://img.shields.io/badge/Groq-Llama--3-F55036?style=for-the-badge)](https://groq.com/)
[![Pydantic](https://img.shields.io/badge/Pydantic-Structured%20Output-E92063?style=for-the-badge)](https://docs.pydantic.dev/)
[![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-FF4B4B?style=for-the-badge\&logo=streamlit\&logoColor=white)](https://streamlit.io/)

</div>

---

## 📌 Overview

The **RAG-based Legal Document Extraction & Title Chain Parser** is an AI-powered document intelligence pipeline designed to process complex **Indian property title search reports, sale deeds, and related legal documents**.

The system combines **PDF parsing, OCR, Large Language Models, structured data validation, and chronological reasoning** to extract critical property information and reconstruct the complete **ownership/title chain** of a property.

Instead of simply extracting text from a legal document, the system converts unstructured legal content into structured, machine-readable information.

### 🎯 Core Objective

> **Legal PDF → Extract text → OCR when required → Identify legal entities → Reconstruct ownership history → Validate structured output → Generate JSON**

---

# ✨ Key Features

### 📄 Smart PDF Parsing

Supports both:

* Text-based PDFs
* Scanned/image-based PDFs

The parser automatically attempts normal text extraction and can fall back to OCR when required.

---

### 🔍 OCR Support

Handles scanned legal documents using OCR-based processing.

Supported approaches include:

* PyMuPDF
* Tesseract OCR
* EasyOCR

This allows the pipeline to process documents that do not contain machine-readable text.

---
<img width="1360" height="685" alt="Screenshot 2026-08-16 184154" src="https://github.com/user-attachments/assets/c5fdd73f-e61e-4d00-9941-1fa995666736" />
<img width="1350" height="487" alt="Screenshot 2026-08-16 184211" src="https://github.com/user-attachments/assets/05ba0cb6-debc-4c9b-b68a-59d7e8090d57" />


### 🧠 Legal Entity Extraction

The system extracts important property-related entities such as:

* Sub-Registrar Office
* District
* Plot Number
* Flat Number
* Survey/Khasra details
* Property address
* Total area
* Boundaries
* Loan account number
* Present owners
* Historical owners
* Deed details
* Transfer types
* Ownership shares

---

### ⬜ Blank / Unfilled Field Detection

Legal documents frequently contain fields that are intentionally blank or unavailable.

For example:

```text
Loan Account No.: ----------------

Flat No.: ----------------

East Boundary: ----------------
```

The system converts these fields into structured `null` values:

```json
{
  "loan_account_no": null,
  "flat_no": null,
  "east": null
}
```

This makes downstream processing significantly easier.

---

### 🔗 Chronological Title Chain Reconstruction

One of the core capabilities of the system is reconstructing the **ownership history of a property**.

The system identifies ownership events and organizes them chronologically:

```text
Original Owner
      │
      ▼
Ownership / Mutation
      │
      ▼
Transfer / Co-Ownership
      │
      ▼
Sale / Deed Execution
      │
      ▼
Current Owner
```

Each ownership event can contain:

* Step number
* Owner name
* Transfer type
* Deed details
* Ownership percentage

---

### 📦 Structured Output

The system uses **Pydantic schemas** to enforce a predictable output structure.

Instead of returning unstructured LLM text:

```text
"The property appears to have been transferred..."
```

the system produces structured JSON:

```json
{
  "present_owners": "Current Owner",
  "ownership_flow_chain": []
}
```

This makes the output suitable for:

* APIs
* Databases
* Dashboards
* Legal workflows
* Automated downstream processing

---

### 🖥️ Interactive Streamlit Dashboard

The project includes a Streamlit interface that allows users to:

* Upload legal PDFs
* Process documents
* Extract property information
* View extracted entities
* Review ownership history
* Inspect structured results

---

# 🏗️ System Architecture

```text
                         LEGAL DOCUMENT
                               │
                               ▼
                    ┌────────────────────┐
                    │     PDF Upload     │
                    └─────────┬──────────┘
                              │
                              ▼
                    ┌────────────────────┐
                    │    PDF Parser      │
                    │     PyMuPDF        │
                    └─────────┬──────────┘
                              │
                    ┌─────────┴─────────┐
                    │                   │
              Text Available?      Scanned PDF?
                    │                   │
                    │                   ▼
                    │            ┌──────────────┐
                    │            │ OCR Engine   │
                    │            │ Tesseract /  │
                    │            │ EasyOCR      │
                    │            └──────┬───────┘
                    │                   │
                    └─────────┬─────────┘
                              │
                              ▼
                    ┌────────────────────┐
                    │ Extracted Document │
                    │       Text         │
                    └─────────┬──────────┘
                              │
                              ▼
                    ┌────────────────────┐
                    │ Legal Information  │
                    │    Extraction      │
                    └─────────┬──────────┘
                              │
                              ▼
                    ┌────────────────────┐
                    │ LangChain + Groq   │
                    │    Llama-3 LLM     │
                    └─────────┬──────────┘
                              │
                              ▼
                    ┌────────────────────┐
                    │ Title Chain        │
                    │ Reconstruction     │
                    └─────────┬──────────┘
                              │
                              ▼
                    ┌────────────────────┐
                    │ Pydantic Validation│
                    └─────────┬──────────┘
                              │
                  ┌───────────┴───────────┐
                  │                       │
                  ▼                       ▼
           JSON / CLI Output       Streamlit Dashboard
```

---

# 🧠 RAG / LLM Processing Flow

The project uses an LLM-driven document processing workflow rather than treating the PDF as a simple text-generation task.

```text
PDF
 │
 ▼
Document Extraction
 │
 ▼
Text / OCR
 │
 ▼
Relevant Legal Information
 │
 ▼
LLM Processing
 │
 ▼
Structured Extraction
 │
 ▼
Ownership Reasoning
 │
 ▼
Pydantic Schema
 │
 ▼
Validated JSON
```

The LLM is responsible for interpreting legal-language patterns and identifying relationships between owners, deeds, transfers, and property information.

---
<img width="1355" height="680" alt="Screenshot 2026-08-16 184243" src="https://github.com/user-attachments/assets/4bc1ed7a-1ad3-48fa-a00a-bfa8ca20c481" />
<img width="1365" height="679" alt="Screenshot 2026-08-16 184321" src="https://github.com/user-attachments/assets/569189b1-d326-4f37-8874-fcb3b786151e" />

# 🔗 Title Chain Processing

The title-chain parser converts historical ownership information into a chronological sequence.

### Example

```text
                    PROPERTY
                       │
                       ▼
              Original Owner
                       │
              Khasra / Mutation
                       │
                       ▼
              Ownership Transfer
                       │
              ┌────────┴────────┐
              │                 │
              ▼                 ▼
          Owner A            Owner B
              │                 │
              └────────┬────────┘
                       │
                       ▼
                  Sale Deed
                       │
                       ▼
                Current Owners
```

---

# 📊 Title Chain Example

The system can transform extracted legal information into:

```json
{
  "ownership_flow_chain": [
    {
      "step_number": 1,
      "owner_name": "Mr. Ramgopal alias Gaurav Patel",
      "transfer_type": "Khasra Entry (2014-15)",
      "deed_details": "P-II Khasra Record",
      "share_percentage": "100%"
    },
    {
      "step_number": 2,
      "owner_name": "Mrs. Suchita Patel",
      "transfer_type": "Co-Ownership Transfer",
      "deed_details": "Deed No. MP179092024A1060405 dated 15-01-2024",
      "share_percentage": "50%"
    },
    {
      "step_number": 3,
      "owner_name": "Mrs. Kanupriya Gangrade & Mr. Amit Gangrade",
      "transfer_type": "Sale Deed Execution",
      "deed_details": "Deed No. MP179132019A1618424 dated 02-09-2019",
      "share_percentage": "100%"
    }
  ]
}
```

---

# 📁 Repository Structure

```text
legal-rag-extractor/
│
├── data/
│   └── sample_sale_deed.pdf
│       # Sample legal property document
│
├── src/
│   ├── __init__.py
│   │
│   ├── pdf_parser.py
│   │   # PDF text extraction
│   │   # OCR fallback logic
│   │
│   ├── chain_extractor.py
│   │   # LLM processing
│   │   # Legal entity extraction
│   │   # Title chain reconstruction
│   │
│   └── schema.py
│       # Pydantic structured schemas
│
├── app.py
│   # Streamlit web application
│
├── main.py
│   # CLI execution pipeline
│
├── requirements.txt
│   # Python dependencies
│
├── .gitignore
│   # Secrets and environment exclusions
│
├── .env
│   # Local environment variables
│
└── README.md
    # Project documentation
```

---

# 🛠️ Technology Stack

| Technology              | Purpose                             |
| ----------------------- | ----------------------------------- |
| 🐍 Python               | Core programming language           |
| 📄 PyMuPDF              | PDF parsing and text extraction     |
| 👁️ Tesseract / EasyOCR | OCR for scanned documents           |
| 🔗 LangChain            | LLM document-processing pipeline    |
| ⚡ Groq                  | High-speed LLM inference            |
| 🧠 Llama-3              | Legal document reasoning/extraction |
| 📐 Pydantic             | Structured output validation        |
| 🖥️ Streamlit           | Interactive dashboard               |
| 📦 JSON                 | Machine-readable output             |

---

# 🚀 Getting Started

## Prerequisites

Make sure the following are installed:

* Python 3.10+
* pip
* Git
* Groq API Key
* Tesseract OCR *(optional, depending on OCR configuration)*

---

# 📥 Installation

## 1. Clone the Repository

```bash
git clone https://github.com/aksajax/RAG-based-Legal-Document-Extraction.git
cd RAG-based-Legal-Document-Extraction
```

---

## 2. Create Virtual Environment

### Windows

```bash
python -m venv env
env\Scripts\activate
```

### macOS / Linux

```bash
python3 -m venv env
source env/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔐 Environment Configuration

Create a `.env` file in the root directory:

```env
GROQ_API_KEY=your_actual_groq_api_key_here
```

### ⚠️ Security

Never commit your API key to GitHub.

Add the following to `.gitignore`:

```gitignore
.env
env/
venv/
__pycache__/
*.pyc
output_result.json
```

---

# 👁️ OCR Configuration

For scanned PDFs, an OCR engine may be required.

### Tesseract

Install Tesseract OCR on your operating system and ensure it is available to the application.

The pipeline can use OCR when a PDF does not provide sufficient machine-readable text.

```text
Scanned PDF
     │
     ▼
Render PDF Pages
     │
     ▼
OCR
     │
     ▼
Extracted Text
```

---

# 💻 Usage

## Option 1 — Command Line

Place the legal PDF inside:

```text
data/
```

For example:

```text
data/sample_sale_deed.pdf
```

Run:

```bash
python main.py
```

The pipeline will process the document and generate structured output.

Example output:

```text
output_result.json
```

---

# 🖥️ Option 2 — Streamlit Dashboard

Start the interactive web application:

```bash
streamlit run app.py --server.fileWatcherType=none
```

The dashboard allows you to upload a legal document and inspect:

```text
PDF Upload
    ↓
Document Processing
    ↓
Extracted Information
    ↓
Property Details
    ↓
Ownership Chain
    ↓
Structured JSON
```

---

# 📄 Supported Document Types

The pipeline is designed primarily for Indian property-related legal documents such as:

* Property title search reports
* Sale deeds
* Ownership documents
* Property transfer records
* Khasra-related records
* Mutation records
* Registration/deed documents

> Actual extraction quality depends on document structure, scan quality, OCR quality, language, and the information available in the document.

---

# 📦 Structured Data Schema

The Pydantic schema defines the expected structure of the extracted information.

Conceptually:

```text
Property Information
│
├── Sub-Registrar Office
├── District
├── Loan Account Number
├── Flat Number
├── Plot Number / Address
├── Total Area
│
├── Boundaries
│   ├── East
│   ├── West
│   ├── North
│   └── South
│
├── Present Owners
│
└── Ownership Flow Chain
    ├── Step Number
    ├── Owner Name
    ├── Transfer Type
    ├── Deed Details
    └── Share Percentage
```

---

# 📊 Sample JSON Output

```json
{
  "sub_registrar_office": "Indore",
  "district": "Indore",
  "loan_account_no": null,
  "flat_no": null,
  "plot_no_and_address": "Survey No. 29/6/2/1, Gram Baroli",
  "total_area_sq_m": "2530.00",
  "boundaries": {
    "east": null,
    "west": null,
    "north": null,
    "south": null
  },
  "present_owners": "Mrs. Kanupriya Gangrade & Mr. Amit Gangrade",
  "ownership_flow_chain": [
    {
      "step_number": 1,
      "owner_name": "Mr. Ramgopal alias Gaurav Patel",
      "transfer_type": "Khasra Entry (2014-15)",
      "deed_details": "P-II Khasra Record",
      "share_percentage": "100%"
    },
    {
      "step_number": 2,
      "owner_name": "Mrs. Suchita Patel",
      "transfer_type": "Co-Ownership Transfer",
      "deed_details": "Deed No. MP179092024A1060405 dated 15-01-2024",
      "share_percentage": "50%"
    },
    {
      "step_number": 3,
      "owner_name": "Mrs. Kanupriya Gangrade & Mr. Amit Gangrade",
      "transfer_type": "Sale Deed Execution",
      "deed_details": "Deed No. MP179132019A1618424 dated 02-09-2019",
      "share_percentage": "100%"
    }
  ]
}
```

---

# 🔄 End-to-End Pipeline

```text
                 ┌──────────────────┐
                 │   Legal PDF      │
                 └────────┬─────────┘
                          │
                          ▼
                 ┌──────────────────┐
                 │ PDF Text Parser  │
                 │    PyMuPDF       │
                 └────────┬─────────┘
                          │
                    Text Available?
                       /       \
                     YES        NO
                      │          │
                      │          ▼
                      │    ┌──────────────┐
                      │    │ OCR Engine   │
                      │    │ Tesseract /  │
                      │    │ EasyOCR      │
                      │    └──────┬───────┘
                      │           │
                      └─────┬─────┘
                            │
                            ▼
                   ┌──────────────────┐
                   │ Extracted Text   │
                   └────────┬─────────┘
                            │
                            ▼
                   ┌──────────────────┐
                   │ LangChain        │
                   │ Processing       │
                   └────────┬─────────┘
                            │
                            ▼
                   ┌──────────────────┐
                   │ Groq Llama-3     │
                   │ LLM Extraction   │
                   └────────┬─────────┘
                            │
                            ▼
                   ┌──────────────────┐
                   │ Entity Extraction│
                   └────────┬─────────┘
                            │
                            ▼
                   ┌──────────────────┐
                   │ Title Chain      │
                   │ Reconstruction   │
                   └────────┬─────────┘
                            │
                            ▼
                   ┌──────────────────┐
                   │ Pydantic Schema  │
                   │ Validation       │
                   └────────┬─────────┘
                            │
                   ┌────────┴────────┐
                   │                 │
                   ▼                 ▼
               JSON Output      Streamlit UI
```

---

# 🧪 Testing the Pipeline

### Test 1 — Text-Based PDF

```text
Legal PDF
   ↓
PyMuPDF
   ↓
Text Extraction
   ↓
LLM Processing
   ↓
Structured JSON
```

---

### Test 2 — Scanned PDF

```text
Scanned PDF
   ↓
PDF Rendering
   ↓
OCR
   ↓
Extracted Text
   ↓
LLM Processing
   ↓
Structured JSON
```

---

### Test 3 — Blank Fields

Input:

```text
Loan Account No.: ----------------
Flat No.: ----------------
East Boundary: ----------------
```

Expected:

```json
{
  "loan_account_no": null,
  "flat_no": null,
  "boundaries": {
    "east": null
  }
}
```

---

### Test 4 — Title Chain

Input document contains multiple historical ownership records.

Expected:

```text
Original Owner
      ↓
Transfer
      ↓
Co-Owner
      ↓
Sale Deed
      ↓
Current Owner
```

---

# 🧠 Why This Project Is Different

A traditional PDF parser might return:

```text
Raw text from the document...
```

This project goes further:

```text
Raw Legal Document
       ↓
Understand Document
       ↓
Extract Legal Entities
       ↓
Identify Ownership Events
       ↓
Reconstruct Timeline
       ↓
Validate Structured Data
       ↓
Machine-Readable Legal Information
```

This makes the system useful as a foundation for **legal-tech document intelligence and property due-diligence workflows**.

---

# ⚠️ Important Legal Disclaimer

This project is an **AI-assisted document extraction and analysis tool**.

It should **not be considered a substitute for legal advice, title verification, advocate review, or official government/property records**.

LLMs and OCR systems can make extraction or interpretation errors. Any extracted ownership chain or property information should be independently verified against the original legal documents and authoritative records before being used for legal, financial, or property decisions.

---

# 🚀 Future Improvements

### 🧠 AI / RAG

* [ ] Retrieval-Augmented Generation with document chunking
* [ ] Vector database integration
* [ ] Semantic legal-document retrieval
* [ ] Citation-aware answers
* [ ] Multi-document reasoning
* [ ] Cross-document ownership verification
* [ ] Legal entity relationship graphs

### 📄 Document Processing

* [ ] Multi-language OCR
* [ ] Hindi / regional-language document support
* [ ] Table extraction
* [ ] Handwritten document processing
* [ ] Document classification
* [ ] Page-level confidence scoring

### 🔗 Title Chain Intelligence

* [ ] Automatic ownership timeline visualization
* [ ] Ownership graph generation
* [ ] Share-transfer validation
* [ ] Missing-link detection
* [ ] Conflicting ownership detection
* [ ] Duplicate deed detection
* [ ] Timeline consistency checks

### 🏭 Production

* [ ] FastAPI backend
* [ ] PostgreSQL
* [ ] Vector database
* [ ] Authentication
* [ ] Cloud document storage
* [ ] Docker deployment
* [ ] Background document processing
* [ ] Celery/Redis task queue
* [ ] Monitoring and logging
* [ ] Document processing audit trail

---

# 🏭 Future Production Architecture

```text
                           USER
                            │
                            ▼
                    ┌───────────────┐
                    │ Web Dashboard │
                    │   Streamlit   │
                    └───────┬───────┘
                            │
                            ▼
                    ┌───────────────┐
                    │    FastAPI    │
                    │      API      │
                    └───────┬───────┘
                            │
             ┌──────────────┼──────────────┐
             │              │              │
             ▼              ▼              ▼
       ┌──────────┐   ┌──────────┐   ┌──────────┐
       │ PDF/OCR  │   │   RAG    │   │ Database │
       │ Pipeline │   │ Pipeline │   │          │
       └────┬─────┘   └────┬─────┘   └──────────┘
            │              │
            │              ▼
            │        ┌────────────┐
            │        │ Vector DB  │
            │        └─────┬──────┘
            │              │
            └──────┬───────┘
                   ▼
            ┌───────────────┐
            │  Llama / LLM  │
            │  Extraction   │
            └───────┬───────┘
                    │
                    ▼
            ┌───────────────┐
            │ Pydantic      │
            │ Validation    │
            └───────┬───────┘
                    │
                    ▼
             Structured JSON
                    │
              ┌─────┴─────┐
              ▼           ▼
        Title Chain    Property
        Timeline       Entities
```

---

# 📚 Key Technologies & Concepts

This project demonstrates practical experience with:

* Python
* PDF Processing
* OCR
* Natural Language Processing
* Large Language Models
* LangChain
* RAG Architecture
* Prompt Engineering
* Structured LLM Output
* Pydantic
* Legal Document Intelligence
* Information Extraction
* Entity Extraction
* Temporal Reasoning
* Ownership Graph Reconstruction
* Streamlit
* JSON Data Pipelines

---

# 🤝 Contributing

Contributions are welcome.

### 1. Fork the repository

```bash
git fork https://github.com/aksajax/RAG-based-Legal-Document-Extraction.git
```

### 2. Create a feature branch

```bash
git checkout -b feature/new-feature
```

### 3. Make your changes

### 4. Commit your changes

```bash
git add .
git commit -m "Add: new legal document processing feature"
```

### 5. Push the branch

```bash
git push origin feature/new-feature
```

### 6. Create a Pull Request

---

# 📜 License

Distributed under the **MIT License**.

See the `LICENSE` file for more information.

---

# 👨‍💻 Author

<div align="center">

## Abhishek Singh

### AI/ML • Generative AI • Full-Stack Development

[![GitHub](https://img.shields.io/badge/GitHub-aksajax-181717?style=for-the-badge\&logo=github)](https://github.com/aksajax)

<br/>

⭐ **If you found this project useful, consider giving the repository a star!**

</div>

---

<div align="center">

# ⚖️ Legal Documents → Structured Intelligence

### 📄 Extract • 🧠 Understand • 🔗 Reconstruct • 📦 Structure

**Built with Python • OCR • LangChain • Groq • Llama-3 • Pydantic • Streamlit**

</div>
