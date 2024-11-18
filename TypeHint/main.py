from fastapi import FastAPI, Query
from typing import List, Dict, Tuple, Set

app = FastAPI()

# 기본 타입 힌트
@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id,}

@app.get("/getdata/")
def read_items(data: str = "funcoding"):
    return {"data": data}

# 고급 타입 힌트
@app.get("/items/")
async def read_items(q: List[int] = Query([])):
    return {"q": q}

@app.post("/create-item/")
async def create_item(item: Dict[str, int]):
    return item
