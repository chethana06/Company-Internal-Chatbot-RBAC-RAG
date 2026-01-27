import os
from langchain_community.document_loaders import TextLoader, CSVLoader
from role_mapping import ROLE_MAPPING

BASE_PATH = "Fintech-data"
def load_all_documents():
    documents = []
    for folder, config in ROLE_MAPPING.items():
        folder_path = os.path.join(BASE_PATH, folder)
        if not os.path.exists(folder_path):
            continue
        for file in os.listdir(folder_path):
            file_path = os.path.join(folder_path, file)
            if file.endswith(".md"):
                loader = TextLoader(file_path, encoding="utf-8")
                docs = loader.load()
            elif file.endswith(".csv"):
                loader = CSVLoader(file_path)
                docs = loader.load()
            else:
                continue
            for doc in docs:
                doc.metadata["source"] = file
                doc.metadata["department"] = config["department"]
                doc.metadata["allowed_roles"] = ",".join(config["allowed_roles"])
                documents.append(doc)
    return documents
if __name__ == "__main__":
    docs = load_all_documents()
    print(f"\n Total documents loaded: {len(docs)}\n")
    for idx, doc in enumerate(docs, start=1):
        print("=" * 80)
        print(f" DOCUMENT #{idx}")
        print(" METADATA:")
        for k, v in doc.metadata.items():
            print(f"   {k}: {v}")
        print("\n CONTENT (first 500 characters):")
        print(doc.page_content[:500])
        print("\n")
    print("=" * 80)
    print(" FINAL SUMMARY")
    print(f"Total documents loaded: {len(docs)}")
    print("=" * 80)