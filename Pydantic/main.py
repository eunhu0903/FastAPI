from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Union

app = FastAPI()

class Item(BaseModel):
    name: str
    tags: List[str]
    variant: Union[int, str]

@app.post("/items/")
def create_item(item: Item):
    return {"item": item.dict()}