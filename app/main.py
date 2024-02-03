from fastapi import FastAPI

from app.routes import categories, parts


app = FastAPI()

app.include_router(categories.router)
app.include_router(parts.router)
