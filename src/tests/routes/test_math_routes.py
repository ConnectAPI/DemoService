from fastapi.testclient import TestClient


def test_sum_numbers(client: TestClient):
    response = client.get("/math/sum", params={"a": 5, "b": 10})
    assert response.status_code == 200
    assert response.text == "15"


def test_multiply_numbers(client: TestClient):
    response = client.get("/math/mul", params={"a": 5, "b": 6})
    assert response.status_code == 200
    assert response.text == "30"
