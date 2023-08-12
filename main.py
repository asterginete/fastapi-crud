from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

class Item(BaseModel):
    name: str
    description: Optional[str] = None

items = {}

@app.post("/items/")
async def create_item(item: Item):
    item_id = len(items) + 1
    items[item_id] = item
    return {"id": item_id, "item": item}

@app.get("/items/")
async def read_items():
    return items

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    item = items.get(item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    items[item_id] = item
    return item

@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    del items[item_id]
    return {"status": "Item deleted successfully"}

@app.get("/items/search/{name}")
async def search_items_by_name(name: str):
    result = {k: v for k, v in items.items() if v.name == name}
    return result

@app.patch("/items/{item_id}/name")
async def update_item_name(item_id: int, name: str):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    items[item_id].name = name
    return items[item_id]

@app.patch("/items/{item_id}/description")
async def update_item_description(item_id: int, description: str):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    items[item_id].description = description
    return items[item_id]

@app.get("/items/count")
async def count_items():
    return {"count": len(items)}

@app.delete("/items/")
async def delete_all_items():
    items.clear()
    return {"status": "All items deleted successfully"}

