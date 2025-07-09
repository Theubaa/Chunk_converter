http://13.232.39.95:8502/    also you can directly use from here


# 📚 File Chunk Converter – Knowledge Base Generator

Easily convert `.txt`, `.md`, `.json`, and `.pdf` files into small, clean, overlapping text chunks — perfect for feeding into Chatbots, LLMs, semantic search, and vector databases.

🔗 GitHub Repo: [Theubaa/Chunk_converter](https://github.com/Theubaa/Chunk_converter)

---

## 🚀 Why Use This?

Large documents are too big for LLMs (like GPT) to process at once.  
This tool solves that by breaking them into small, overlapping chunks, so you can:

✅ Feed content into AI chatbots  
✅ Generate semantic search knowledge bases  
✅ Prepare data for vector databases like Pinecone, Qdrant, ChromaDB  
✅ Keep context preserved in each chunk

---

## 🌐 Live Streamlit App (Optional)

> Coming soon — or deploy yourself using Streamlit Cloud or locally.

---

## 🧠 Features

- ✅ Upload `.txt`, `.md`, `.json`, or `.pdf`
- ✅ Auto-extract and clean content
- ✅ Chunk text with customizable size & overlap
- ✅ Download the full knowledge base as a `.txt` file
- ✅ Clean UI using Streamlit

---

## 📦 Installation

Clone the repo and install the requirements:

```bash
git clone https://github.com/Theubaa/Chunk_converter.git
cd Chunk_converter
pip install -r requirements.txt
▶️ How to Run

streamlit run chunk_converter_app.py
Then open in your browser: http://localhost:8501

🖼️ Screenshot Preview
Upload your file, tweak chunk settings, and download your knowledge base.


![image](https://github.com/user-attachments/assets/c746b8d5-21ea-4b38-8202-2c26ccb53e7e)


🔧 Configuration
You can customize:

Chunk Size: Number of words per chunk

Overlap: Number of overlapping words between chunks

📤 Output Format
Example output in .txt:



--- Chunk 1 ---
This is the first chunk of text...

--- Chunk 2 ---
This is the second chunk, overlapping with the first...
🛠 Built With
Streamlit – UI framework

PyPDF2 – For reading PDF files

Python 3.8+

📁 Requirements
ini

streamlit==1.35.0
PyPDF2==3.0.1
Install with:

bash

pip install -r requirements.txt
📌 To-Do / Future Ideas
 Add .docx and .csv support

 Export chunks as .json or .csv

 Integrate with LangChain or vector DBs

 Deploy to Streamlit Cloud

📝 License
MIT License – use it, modify it, improve it. 😄

Made with ❤️ by @Theubaa to speed up your AI development workflows.
