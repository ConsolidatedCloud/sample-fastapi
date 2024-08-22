from fastapi import APIRouter

router = APIRouter()

@router.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

@router.get("/items_2/{item_id}")
def read_item(item_id: int, q: str = None, r: str = None):
    return {"item_id": item_id, "q": q, "r" : r}
