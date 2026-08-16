# app.py
import streamlit as st
import json
import os
import pymupdf
from src.chain_extractor import extract_legal_info_and_chain

st.set_page_config(page_title="Legal Title & Ownership Flow Extractor", layout="wide")

st.title("📜 Legal Document RAG & Title Chain Extractor")
st.write("Upload a Legal Title Search / Sale Deed PDF to extract entity details and visual ownership flow.")

uploaded_file = st.file_uploader("Upload Legal PDF", type=["pdf"])

if uploaded_file is not None:
    # Save uploaded file temporarily
    os.makedirs("temp", exist_ok=True)
    temp_path = os.path.join("temp", uploaded_file.name)
    with open(temp_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.success(f"File uploaded: {uploaded_file.name}")
    
    if st.button("Extract Legal Data & Title Flow"):
        with st.spinner("Parsing PDF & Processing via Llama-3..."):
            # Step 1: Parse PDF
            doc = pymupdf.open(temp_path)
            pdf_pages = []
            for i, page in enumerate(doc):
                pdf_pages.append({"page_number": i + 1, "content": page.get_text()})
            doc.close()
            
            # Step 2: Extract Data
            result = extract_legal_info_and_chain(pdf_pages)
            result_dict = result.model_dump()
            
            st.subheader("🔗 Ownership Flow Chain (Title History)")
            chain_data = result_dict.get("ownership_flow_chain", [])
            
            if chain_data:
                for step in chain_data:
                    with st.expander(f"Step {step.get('step_number')}: {step.get('owner_name')}"):
                        st.write(f"**Transfer Type:** {step.get('transfer_type')}")
                        st.write(f"**Deed / Record Details:** {step.get('deed_details')}")
                        st.write(f"**Share Percentage:** {step.get('share_percentage')}")
            else:
                st.info("No ownership flow steps detected.")

            st.subheader("📋 Key Extracted Entities & Blank Fields")
            st.json(result_dict)