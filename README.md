# AI Knowledge Assistant

AI Knowledge Assistant is an **LLM-powered question answering system** that allows users to query a knowledge base using natural language.

The system uses **Retrieval Augmented Generation (RAG)** to retrieve relevant information from documents and generate contextual answers using a large language model.

A **Streamlit interface** provides an interactive UI for users to easily ask questions and view responses.

---

## 🚀 Live Demo

**Streamlit App**  
https://your-streamlit-app-link

**API Documentation (FastAPI Swagger)**  
http://127.0.0.1:8000/docs

---

## 🧠 Features

- Natural language question answering  
- Retrieval Augmented Generation (RAG)  
- Semantic document search  
- Vector embeddings for similarity search  
- LLM-based response generation  
- Interactive Streamlit UI  
- FastAPI backend API  

---

## 🏗 Architecture

```
User (Streamlit UI)
        ↓
User Query
        ↓
FastAPI Backend
        ↓
Embedding Generation
        ↓
Vector Search
        ↓
Retrieve Relevant Context
        ↓
LLM Generates Response
        ↓
Answer Returned to UI
```

---

## 🧩 Project Structure

```
AI-Knowledge-Assistant
│
├── main.py
├── streamlit_app.py
│
├── routes
│   └── query_router.py
│
├── services
│   ├── embedding_service.py
│   ├── retrieval_service.py
│   ├── rag_service.py
│   └── llm_service.py
│
├── data
│
└── requirements.txt
```

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/yourusername/AI-Knowledge-Assistant.git
cd AI-Knowledge-Assistant
```

Create virtual environment

```bash
python -m venv venv
```

Activate environment

Windows
```bash
venv\Scripts\activate
```

Linux / Mac
```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

Start FastAPI backend

```bash
uvicorn main:app --reload
```

Run Streamlit interface

```bash
streamlit run streamlit_app.py
```

Streamlit will open at:

```
http://localhost:8501
```

---

## 🧠 Technologies Used

- Python  
- FastAPI  
- Streamlit  
- LangChain  
- Sentence Transformers  
- LLM APIs  

---

## 📖 What This Project Demonstrates

- Retrieval Augmented Generation (RAG)  
- Semantic search with embeddings  
- LLM-powered knowledge assistants  
- Full-stack AI application using FastAPI + Streamlit  

---


