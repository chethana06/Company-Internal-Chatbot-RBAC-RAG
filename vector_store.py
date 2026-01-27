from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores.utils import filter_complex_metadata
from chunk_documents import chunk_documents

PERSIST_DIR = "chroma_db"
def create_vector_store():
    print("\n Loading and chunking documents...")
    chunks = chunk_documents()
    print(f" Total chunks received: {len(chunks)}")
    chunks = filter_complex_metadata(chunks)
    print(" Initializing embedding model...")
    embedding_model = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )
    print(" Creating & persisting vector database...")
    vectordb = Chroma.from_documents(
        documents=chunks,
        embedding=embedding_model,
        persist_directory=PERSIST_DIR
    )
    vectordb.persist()
    print(" Vector database successfully created!")
if __name__ == "__main__":
    create_vector_store()