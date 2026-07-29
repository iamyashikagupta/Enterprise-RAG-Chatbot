import streamlit as st

st.set_page_config(
    page_title="Enterprise RAG Chatbot",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 Enterprise RAG Chatbot")

st.markdown("""
### Welcome!

This application allows users to upload enterprise documents and interact with them using AI-powered Retrieval-Augmented Generation (RAG).

### Planned Features

- 📄 Upload PDF, DOCX & TXT files
- 🔍 Semantic Search
- 🤖 AI-powered Question Answering
- 📚 Context-aware Responses
- 💾 FAISS Vector Database
- ⚡ Google Gemini Integration
- 🖥️ Streamlit Interface
""")

st.info("🚀 Enterprise RAG Chatbot initialized successfully.")