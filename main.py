from typing import Optional

from fastapi import FastAPI

# from pydantic import BaseModel


# class Item(BaseModel):
#     name: str
#     description: Optional[str] = None
#     price: float
#     tax: Optional[float] = None

app = FastAPI()

#@app --> path operation decorator
#get --> operation
#'/' --> path

#index to return --> path operation function


@app.get("/")
def index():
    return {'data': {"firstname": "Olanrewaju"}}

# @app.post("/items/")
# async def create_item(item: Item):
#     return {'item': f"blog is created with name {item.name}"}

@app.get("/items/{item_id}")
def get_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}