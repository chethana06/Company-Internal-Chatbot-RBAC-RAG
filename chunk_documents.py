from langchain_text_splitters import RecursiveCharacterTextSplitter
from load_documents import load_all_documents
def chunk_documents():
    documents = load_all_documents()
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1500,   
        chunk_overlap=50
    )
    chunks = splitter.split_documents(documents)
    return chunks
if __name__ == "__main__":
    chunks = chunk_documents()
    print(f"\n Total chunks created: {len(chunks)}\n")
    for idx, chunk in enumerate(chunks, start=1):
        print("=" * 90)
        print(f" CHUNK #{idx}")
        print(" METADATA:")
        for k, v in chunk.metadata.items():
            print(f"   {k}: {v}")
        print("\n CONTENT (first 400 characters):")
        print(chunk.page_content[:400])  
        print("\n")
    print("=" * 90)
    print(" FINAL SUMMARY")
    print(f"Total chunks created: {len(chunks)}")
    print("=" * 90)