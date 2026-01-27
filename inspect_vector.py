from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
import os
os.environ["ANONYMIZED_TELEMETRY"] = "False"

PERSIST_DIR = "chroma_db"
embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)
vectordb = Chroma(
    persist_directory=PERSIST_DIR,
    embedding_function=embedding_model
)
data = vectordb.get()
print(f"\n Total vectors stored: {len(data['documents'])}\n")
for i in range(len(data["documents"])):
    print("=" * 80)
    print(f" VECTOR #{i+1}")
    print(" METADATA:", data["metadatas"][i])
    print(" TEXT (first 300 chars):")
    print(data["documents"][i][:300])
print("=" * 80)
print(" FINAL SUMMARY")
print(f"Total vectors inspected: {len(data['documents'])}")
print(f"Vector database location: {PERSIST_DIR}")
print("=" * 80)