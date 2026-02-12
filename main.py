from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import uvicorn

app = FastAPI(title="Checklist App", description="A simple, robust checklist application.")

class Item(BaseModel):
    id: int
    title: str
    completed: bool = False

class CreateItem(BaseModel):
    title: str

items = []
current_id = 0

@app.post("/items/", response_model=Item)
def create_item(item: CreateItem):
    global current_id
    current_id += 1
    new_item = Item(id=current_id, title=item.title, completed=False)
    items.append(new_item)
    return new_item

@app.get("/items/", response_model=List[Item])
def read_items():
    return items

@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, completed: bool):
    for item in items:
        if item.id == item_id:
            item.completed = completed
            return item
    raise HTTPException(status_code=404, detail="Item not found")

@app.get("/")
def read_root():
    return {"message": "Welcome to the Checklist App"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
