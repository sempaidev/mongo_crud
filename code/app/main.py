from typing import Union
from fastapi import FastAPI
from app.routes.user import user
from app.docs import tags_metadata
app = FastAPI(
    title="API REST con FASTAPI y MONGODB",
    description="Una forma de usar fastapi y mongodb con un simple crud",
    version='0.0.1',
    openapi_tags= tags_metadata
)

app.include_router(user)

# @app.get("/")
# def read_root():
#     return {"Hello": "World"}


# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}
