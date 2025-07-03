import streamlit as st
import os
import json
import PyPDF2
from io import StringIO

# Title
st.set_page_config(page_title="File Chunk Converter", layout="centered")
st.title("📚 File Chunk Converter - Knowledge Base Generator")

# Read uploaded file content
def read_file_content(uploaded_file):
    ext = os.path.splitext(uploaded_file.name)[1].lower()

    try:
        if ext in ['.txt', '.md']:
            return uploaded_file.read().decode("utf-8", errors="ignore")
        elif ext == '.json':
            json_data = json.load(uploaded_file)
            return json.dumps(json_data, indent=2)
        elif ext == '.pdf':
            try:
                reader = PyPDF2.PdfReader(uploaded_file)
                return '\n'.join([page.extract_text() or "" for page in reader.pages])
            except Exception as e:
                st.error(f"PDF read error: {e}")
                return ""
        else:
            raise ValueError(f"Unsupported file type: {ext}")
    except Exception as e:
        st.error(f"Error reading file: {e}")
        return ""

# Split text into overlapping chunks
def split_into_chunks(text, chunk_size=500, overlap=50):
    words = text.split()
    chunks = []
    for i in range(0, len(words), chunk_size - overlap):
        chunk = ' '.join(words[i:i + chunk_size])
        chunks.append(chunk)
    return chunks

# Format chunks as downloadable knowledge base
def convert_to_knowledge_base(text_chunks):
    kb = ""
    for i, chunk in enumerate(text_chunks):
        kb += f"--- Chunk {i+1} ---\n{chunk}\n\n"
    return kb

# File uploader
uploaded_file = st.file_uploader("Upload a file (.txt, .md, .json, .pdf)", type=["txt", "md", "json", "pdf"])

# Settings
chunk_size = st.slider("Chunk Size (words)", min_value=100, max_value=1000, value=500, step=100)
overlap = st.slider("Chunk Overlap (words)", min_value=0, max_value=200, value=50, step=10)

# Main logic
if uploaded_file:
    st.success(f"Uploaded: {uploaded_file.name}")
    raw_text = read_file_content(uploaded_file)

    if raw_text:
        chunks = split_into_chunks(raw_text, chunk_size, overlap)
        st.info(f"✅ Created {len(chunks)} chunks")

        knowledge_base = convert_to_knowledge_base(chunks)

        st.download_button(
            label="📥 Download Knowledge Base",
            data=knowledge_base,
            file_name=f"{os.path.splitext(uploaded_file.name)[0]}_chunks.txt",
            mime="text/plain"
        )

        with st.expander("🔍 Preview First 2 Chunks"):
            for i, chunk in enumerate(chunks[:2]):
                st.text(f"--- Chunk {i+1} ---\n{chunk}\n")
    else:
        st.warning("⚠️ No readable content found in the file.")
