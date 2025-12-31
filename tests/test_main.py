from fastapi.testclient import TestClient
from main import app


client = TestClient(app)


def test_generate_endpoint_returns_200_and_output():
    payload = {"prompt": "Explique o FastAPI em poucas palavras"}
    resp = client.post("/ai/generate", json=payload)
    assert resp.status_code == 200, resp.text
    data = resp.json()
    assert "output" in data
    assert isinstance(data["output"], str)
