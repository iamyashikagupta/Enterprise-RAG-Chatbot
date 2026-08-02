# Enterprise RAG Chatbot

## Overview

Enterprise RAG Chatbot is an AI-powered application that enables users to upload documents (PDF, DOCX, TXT) and interact with them using natural language. The system leverages Retrieval-Augmented Generation (RAG) to retrieve relevant context and generate accurate, context-aware responses using Large Language Models.

## Key Features

- 📄 Multi-document Upload (PDF, DOCX, TXT)
- 🔍 Semantic Search using Vector Embeddings
- 🤖 AI-powered Question Answering
- 📚 Context-aware Responses
- 💾 Vector Database Integration
- ⚡ Fast Document Retrieval
- 🖥️ Interactive Streamlit Web Interface

## Tech Stack

- Python
- Streamlit
- LangChain
- FAISS
- Hugging Face
- Google Gemini
- Sentence Transformers

## Project Structure

```text
Enterprise-RAG-Chatbot/
├── app.py
├── requirements.txt
├── README.md
├── .env
├── .gitignore
├── assets/
├── data/
└── utils/
```

---

## ▶️ Run Project

```bash
pip install -r requirements.txt

streamlit run app.py

```
## Future Enhancements

- Multi-user Authentication
- Chat Memory
- Support for Excel & PowerPoint
- Cloud Deployment
- Citation-based Responses
