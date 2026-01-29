import streamlit as st
import requests

st.set_page_config(page_title="AI Knowledge Assistant", layout="centered")

st.title("📄 AI Knowledge Assistant")
st.write("Upload a PDF and ask questions from it.")

BACKEND_URL = "http://127.0.0.1:8000"

# Upload PDF
uploaded_file = st.file_uploader("Upload PDF", type=["pdf"])

if uploaded_file:
    files = {
    "file": (
        uploaded_file.name,          # filename
        uploaded_file.getvalue(),    # bytes
        uploaded_file.type           # content-type (application/pdf)
    )
}

    response = requests.post(f"{BACKEND_URL}/api/upload-pdf", files=files)

    if response.status_code == 200:
        st.success("PDF uploaded and processed successfully!")

# Ask question
question = st.text_input("Ask a question from the document")

if st.button("Ask") and question:
    response = requests.post(
        f"{BACKEND_URL}/api/ask",
        json={"question": question}
    )

    if response.status_code == 200:
        st.subheader("Answer")
        st.write(response.json()["answer"])
