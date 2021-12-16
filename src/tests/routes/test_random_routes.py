from fastapi.testclient import TestClient


def test_random_int(client: TestClient):
    response = client.get("/random/range", params={"a": 0, "b": 10})
    assert response.status_code == 200
    assert 0 <= int(response.text) <= 10


def test_random_string(client: TestClient):
    response = client.get("/random/secure", params={"n": 10})
    assert response.status_code == 200
    assert len(response.text)-2 == 10  # -2 for the starting <"> and ending <">
