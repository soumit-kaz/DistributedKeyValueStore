
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from kv_store.store import KeyValueStore


app = FastAPI(title="Distributed Key-Value Store")

store = KeyValueStore()


class PutRequest(BaseModel):
    value: str


@app.put("/items/{key}")
def put_item(key: str, request: PutRequest):
    try:
        store.put(key, request.value)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc

    return {"key": key, "value": request.value}


@app.get("/items/{key}")
def get_item(key: str):
    try:
        value = store.get(key)
    except KeyError as exc:
        raise HTTPException(status_code=404, detail="Key not found") from exc

    return {"key": key, "value": value}


@app.delete("/items/{key}")
def delete_item(key: str):
    try:
        store.delete(key)
    except KeyError as exc:
        raise HTTPException(status_code=404, detail="Key not found") from exc

    return {"key": key, "message": "Item deleted"}