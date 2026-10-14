
import pytest
from fastapi.testclient import TestClient

from kv_store.main import app
from kv_store.store import KeyValueStore


@pytest.fixture
def client(monkeypatch):
    import kv_store.main as main

    monkeypatch.setattr(main, "store", KeyValueStore())

    return TestClient(app)


def test_put_item(client):
    response = client.put(
        "/items/user:101",
        json={"value": "Soumit"},
    )

    assert response.status_code == 200
    assert response.json() == {
        "key": "user:101",
        "value": "Soumit",
    }


def test_get_item(client):
    client.put("/items/user:101", json={"value": "Soumit"})

    response = client.get("/items/user:101")

    assert response.status_code == 200
    assert response.json() == {
        "key": "user:101",
        "value": "Soumit",
    }


def test_get_missing_item_returns_404(client):
    response = client.get("/items/missing")

    assert response.status_code == 404


def test_delete_item(client):
    client.put("/items/user:101", json={"value": "Soumit"})

    response = client.delete("/items/user:101")

    assert response.status_code == 200
    assert response.json() == {
        "message": "Item deleted",
        "key": "user:101",
    }

    get_response = client.get("/items/user:101")
    assert get_response.status_code == 404


def test_delete_missing_item_returns_404(client):
    response = client.delete("/items/missing")

    assert response.status_code == 404
