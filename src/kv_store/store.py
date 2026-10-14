
class KeyValueStore:
    def __init__(self):
        self._data = {}

    def put(self, key: str, value: object) -> None:
        if not isinstance(key, str) or not key:
            raise ValueError("Key must be a non-empty string")

        self._data[key] = value

    def get(self, key: str) -> object:
        if key not in self._data:
            raise KeyError(key)

        return self._data[key]

    def delete(self, key: str) -> None:
        if key not in self._data:
            raise KeyError(key)

        del self._data[key]
