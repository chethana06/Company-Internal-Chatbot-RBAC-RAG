import requests

BASE_URL = "http://127.0.0.1:8000"


def login(username, password):
    try:
        res = requests.post(
            f"{BASE_URL}/login",
            params={"username": username, "password": password}
        )
        return res.json()
    except:
        return {"error": "Backend not reachable"}


def send_query(token, query):
    try:
        headers = {"Authorization": f"Bearer {token}"}

        res = requests.post(
            f"{BASE_URL}/chat",
            params={"query": query},
            headers=headers
        )

        return res.json()

    except:
        return {"error": "Chat request failed"}
