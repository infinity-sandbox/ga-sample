from pydantic import BaseModel
from typing import Optional

class Item(BaseModel):
    id: Optional[int] = None
    name: str
    description: Optional[str] = None
    price: float
    in_stock: bool = True

class ItemResponse(BaseModel):
    success: bool
    message: str
    data: Optional[Item] = None