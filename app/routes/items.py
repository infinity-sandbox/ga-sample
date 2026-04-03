from fastapi import APIRouter, HTTPException
from app.models.item import Item, ItemResponse

router = APIRouter()

# In-memory store (replace with a DB later)
items_db: dict = {}
counter: int = 1

@router.get("/", response_model=list[Item])
def get_all_items():
    return list(items_db.values())

@router.get("/{item_id}", response_model=ItemResponse)
def get_item(item_id: int):
    item = items_db.get(item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return ItemResponse(success=True, message="Item found", data=item)

@router.post("/", response_model=ItemResponse)
def create_item(item: Item):
    global counter
    item.id = counter
    items_db[counter] = item
    counter += 1
    return ItemResponse(success=True, message="Item created", data=item)

@router.put("/{item_id}", response_model=ItemResponse)
def update_item(item_id: int, updated: Item):
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    updated.id = item_id
    items_db[item_id] = updated
    return ItemResponse(success=True, message="Item updated", data=updated)

@router.delete("/{item_id}", response_model=ItemResponse)
def delete_item(item_id: int):
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    deleted = items_db.pop(item_id)
    return ItemResponse(success=True, message="Item deleted", data=deleted)