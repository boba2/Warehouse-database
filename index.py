from fastapi import FastAPI
from routes.categories import category
from routes.parts import part

app = FastAPI()
app.include_router(category)
# app.include_router(part)