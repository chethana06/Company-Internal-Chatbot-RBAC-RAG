import streamlit as st
import requests

BACKEND_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="Company Internal Chatbot", layout="wide")

# -----------------------------
# SESSION STATE INIT
# -----------------------------
if "token" not in st.session_state:
    st.session_state.token = None

if "role" not in st.session_state:
    st.session_state.role = None

if "documents" not in st.session_state:
    st.session_state.documents = []

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []


# -----------------------------
# LOGIN PAGE
# -----------------------------
if not st.session_state.token:
    st.title("🏢 Company Internal Chatbot")
    st.subheader("Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        response = requests.post(
            f"{BACKEND_URL}/login",
            params={"username": username, "password": password},
        )

        if response.status_code == 200:
            data = response.json()
            st.session_state.token = data["access_token"]

            # Decode role from token response if backend sends it
            # Otherwise manually map based on username
            st.session_state.role = username.upper()

            st.success("Login successful!")
            st.rerun()
        else:
            st.error("Invalid credentials")

    st.stop()


# -----------------------------
# SIDEBAR
# -----------------------------
with st.sidebar:
    st.markdown("### 👤 Logged in as")
    st.success(st.session_state.role)

    st.markdown("---")
    st.markdown("### 📂 Accessible Documents")

    # You can improve this by calling a backend endpoint later
    # For now simple mapping

    role_docs = {
        "CEO": [
            "employee_handbook.md",
            "engineering_master_doc.md",
            "financial_summary.md",
            "hr_data.csv",
            "marketing_report_q1_2024.md",
            "marketing_report_q2_2024.md",
            "marketing_report_q3_2024.md",
            "marketing_report_q4_2024.md",
            "quarterly_financial_report.md",
        ],
        "ENGINEERING": [
            "engineering_master_doc.md",
            "employee_handbook.md",
        ],
        "MARKETING": [
            "marketing_report_q1_2024.md",
            "marketing_report_q2_2024.md",
            "marketing_report_q3_2024.md",
            "marketing_report_q4_2024.md",
        ],
        "HR_USER": [
        "employee_handbook.md",
        "hr_data.csv",
        ],

        "FINANCE": [
        "financial_summary.md",
        "quarterly_financial_report.md",
        ],

        "EMPLOYEE": [
        "employee_handbook.md",
        ],
         
    }

    docs = role_docs.get(st.session_state.role, [])

    for d in docs:
        st.write("•", d)


# -----------------------------
# MAIN CHAT UI
# -----------------------------
st.title("💬 Internal Knowledge Chat")
st.caption("Ask questions based on your access level")

query = st.text_input("Ask a question")

if st.button("Send"):
    headers = {
        "Authorization": f"Bearer {st.session_state.token}"
    }

    response = requests.post(
        f"{BACKEND_URL}/chat",
        params={"query": query},
        headers=headers,
    )

    if response.status_code == 200:
        data = response.json()

        st.session_state.chat_history.append({
            "question": query,
            "answer": data["answer"],
            "sources": data["sources"],
            "confidence": data["confidence"],
        })
    else:
        st.error("Error communicating with backend")


# -----------------------------
# DISPLAY CHAT HISTORY
# -----------------------------
for chat in st.session_state.chat_history:

    st.markdown("### 🧑 You")
    st.info(chat["question"])

    st.markdown("### 🤖 Bot")
    st.success(chat["answer"])


    with st.expander("📄 Details"):
        st.write("**Sources:**")
        for s in chat["sources"]:
            st.write("-", s)

        st.write("**Confidence:**", chat["confidence"])
