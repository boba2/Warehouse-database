from fastapi import FastAPI
from routes import categories, parts


app = FastAPI()

app.include_router(categories.router)
app.include_router(parts.router)
