import requests

BASE_URL = "http://127.0.0.1:8000"

def test_login():
    r = requests.post(
        f"{BASE_URL}/login",
        params={"username": "ceo", "password": "ceo123"}
    )
    assert r.status_code == 200
    print("Login test passed")

def test_chat():
    login_res = requests.post(
        f"{BASE_URL}/login",
        params={"username": "ceo", "password": "ceo123"}
    ).json()

    token = login_res["access_token"]

    headers = {"Authorization": f"Bearer {token}"}

    r = requests.post(
        f"{BASE_URL}/chat",
        params={"query": "leave policy"},
        headers=headers
    )

    assert r.status_code == 200
    print("Chat test passed")


test_login()
test_chat()
