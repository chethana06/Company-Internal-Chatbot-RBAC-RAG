# Company Internal Chatbot with Role-Based Access Control (RBAC)

##  Overview
This project implements a secure internal company chatbot using Retrieval-Augmented Generation (RAG) with Role-Based Access Control (RBAC). The system ensures that users can access only the documents authorized for their role.


#  Milestone 1 – Document Processing & Vector Storage

- Load department-specific company documents
- Add metadata (department, allowed roles, source)
- Split large documents into smaller chunks
- Generate embeddings using Sentence Transformers
- Store embeddings in Chroma vector database
- Enable semantic similarity search


#  Milestone 2 – Role-Based Access Control (RBAC)

- Implement department-based role mapping
- Filter retrieved documents using metadata
- Ensure users can access only authorized documents
- Secure document retrieval pipeline


#  Milestone 3 – Backend API & RAG Integration

- Built FastAPI backend
- Implemented JWT authentication
- Integrated RBAC with semantic search
- Implemented Retrieval-Augmented Generation (RAG)
- Used Facebook BART model for summarization
- Added confidence score based on similarity distance
- Created protected /chat endpoint

# Architecture:

- User → FastAPI → RBAC Filter → Vector DB → LLM → Response


#  Milestone 4 – Frontend & System Integration

- Built interactive Streamlit frontend
- Implemented login interface
- Displayed accessible documents in sidebar
- Integrated frontend with FastAPI backend
- Displayed:
  - Chat responses
  - Document sources
  - Confidence score
- Maintained conversation history
- End-to-end integration testing completed


#  Tech Stack

- Python
- FastAPI
- Streamlit
- ChromaDB
- Sentence Transformers
- Facebook BART (Summarization Model)
- JWT Authentication


#  Security Features

- JWT-based authentication
- Role-Based Access Control
- Metadata-based document filtering
- Department-level isolation


#  How to Run

- Backend:
- cd backend
- uvicorn app:app --reload

- Frontend:
- cd frontend
- streamlit run streamlit_app.py