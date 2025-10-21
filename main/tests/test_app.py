import json
from app import app

def test_home():
    client = app.test_client()
    resp = client.get("/")
    assert resp.status_code == 200
    # Expect HTML page
    assert b"Flask Lab Project" in resp.data

def test_health():
    client = app.test_client()
    resp = client.get("/health")
    assert resp.status_code == 200
    assert b"OK" in resp.data

def test_post_data_json():
    client = app.test_client()
    payload = {"a": 1, "b": "two"}
    resp = client.post("/data", json=payload)
    assert resp.status_code == 201
    data = resp.get_json()
    assert data["received"] == payload
