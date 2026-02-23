import sys
import os

# Add project root to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from rbac_search import vectordb
from role_mapping import ROLE_MAPPING
from transformers import pipeline

# Summarization model
llm = pipeline(
    "summarization",
    model="facebook/bart-large-cnn",
    max_length=250,
    min_length=60,
    do_sample=False
)


def generate_rag_response(query: str, role: str, username: str):

    # -----------------------------------------
    # 1️⃣  Determine allowed departments
    # -----------------------------------------

    allowed_departments = []

    for key, value in ROLE_MAPPING.items():
        if role in value["allowed_roles"]:
            allowed_departments.append(value["department"])

    # -----------------------------------------
    # 2️⃣  Retrieve documents ONLY from allowed departments
    # -----------------------------------------

    docs_and_scores = vectordb.similarity_search_with_score(query, k=5)

    filtered_docs = [
        (doc, score)
        for doc, score in docs_and_scores
        if doc.metadata.get("department") in allowed_departments
    ]

    if not filtered_docs:
        return (
            "The requested information is not available in the provided documents.",
            [],
            0.2
        )

    docs = [doc for doc, _ in filtered_docs]
    scores = [score for _, score in filtered_docs]

    # -----------------------------------------
    # 🎯 PRACTICAL CONFIDENCE SCORE
    # -----------------------------------------

    best_score = min(scores)  # Lower = better match

    confidence = 1 - best_score

    # Clamp between 0 and 1
    confidence = max(0.0, min(1.0, confidence))
    confidence = round(confidence, 2)

    # -----------------------------------------
    # 3️⃣  Combine text
    # -----------------------------------------

    combined_text = "\n\n".join(
        doc.page_content for doc in docs
    )

    try:
        summary = llm(combined_text[:3000])[0]["summary_text"]

        sources = list(set(
            doc.metadata.get("source", "Unknown")
            for doc in docs
        ))

        return summary.strip(), sources, confidence

    except Exception:
        return (
            "Relevant information found but could not generate summary.",
            [],
            round(confidence * 0.6, 2)
        )
