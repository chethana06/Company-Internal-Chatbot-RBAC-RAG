from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PERSIST_DIR = os.path.join(BASE_DIR, "chroma_db")


embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vectordb = Chroma(
    persist_directory=PERSIST_DIR,
    embedding_function=embedding_model
)


def rbac_search(query, user_role, k=5):
    results = vectordb.similarity_search(query, k=k)
    authorized_docs = []

    for doc in results:
        allowed_roles = doc.metadata.get("allowed_roles", "")
        allowed_roles = [r.strip().lower() for r in allowed_roles.split(",")]

        if user_role.lower() in allowed_roles:
            authorized_docs.append(doc)

    return authorized_docs


if __name__ == "__main__":
    print("\n COMPANY INTERNAL CHATBOT \n")

    user_role = input("Enter your role: ").strip()
    query = input(
        "Enter data filter (hr / finance / engineering / marketing / general): "
    ).strip()

    print("\n Searching...\n")

    results = rbac_search(query, user_role)

    if not results:
        print(" Access denied = No data\n")
    else:
        print(" Access granted\n")

        for idx, doc in enumerate(results, start=1):
            print("=" * 70)
            print(f" RESULT #{idx}")
            print(" METADATA:")

            for k, v in doc.metadata.items():
                print(f" {k}: {v}")

            print("\n CONTENT (first 300 chars):")
            print(doc.page_content[:300])
            print("\n")

    print(" End of search\n")
