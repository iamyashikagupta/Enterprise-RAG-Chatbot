import streamlit as st
from pypdf import PdfReader

st.set_page_config(
    page_title="Enterprise RAG Chatbot",
    page_icon="🤖",
    layout="wide"
)

# ----------------------------
# Header
# ----------------------------

st.title("🤖 Enterprise RAG Chatbot")
st.write("Upload enterprise documents and chat with them using AI.")

st.divider()

# ----------------------------
# Sidebar
# ----------------------------

with st.sidebar:
    st.header("📌 Project Status")

    st.success("Project Started")

    st.write("### Roadmap")

    st.checkbox("Project Setup", value=True)
    st.checkbox("PDF Upload", value=True)
    st.checkbox("PDF Reader")
    st.checkbox("Text Chunking")
    st.checkbox("Embeddings")
    st.checkbox("FAISS")
    st.checkbox("Gemini API")
    st.checkbox("Chat Interface")

# ----------------------------
# File Upload
# ----------------------------

st.header("📂 Upload Document")

uploaded_file = st.file_uploader(
    "Upload a PDF file",
    type=["pdf"]
)

if uploaded_file is not None:

    st.success("✅ File Uploaded Successfully")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("File Name", uploaded_file.name)

    with col2:
        st.metric(
            "File Size",
            f"{round(uploaded_file.size/1024,2)} KB"
        )

    reader = PdfReader(uploaded_file)

    total_pages = len(reader.pages)

    st.metric("Total Pages", total_pages)

    st.success("✅ PDF read successfully!")

    st.subheader("📄 First Page Preview")

    first_page = reader.pages[0]

    page_text = first_page.extract_text()

    st.text_area(
    "Extracted Text",
    page_text,
    height=300
)
else:

    st.warning("Please upload a PDF file.")

st.divider()

st.caption("Enterprise RAG Chatbot | Built with Streamlit")