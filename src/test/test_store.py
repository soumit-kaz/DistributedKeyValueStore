
import pytest

from kv_store.store import KeyValueStore


def test_put_and_get():
    store = KeyValueStore()

    store.put("user:101", "Soumit")

    assert store.get("user:101") == "Soumit"


def test_put_updates_existing_key():
    store = KeyValueStore()

    store.put("user:101", "Soumit")
    store.put("user:101", "Rahim")

    assert store.get("user:101") == "Rahim"


def test_get_missing_key():
    store = KeyValueStore()

    with pytest.raises(KeyError):
        store.get("missing")


def test_put_rejects_empty_key():
    store = KeyValueStore()

    with pytest.raises(ValueError):
        store.put("", "value")


def test_put_rejects_non_string_key():
    store = KeyValueStore()

    with pytest.raises(ValueError):
        store.put(123, "value")
