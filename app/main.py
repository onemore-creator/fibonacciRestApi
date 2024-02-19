from fastapi import FastAPI
from fastapi_pagination import add_pagination

from .routers import *

app = FastAPI()

app.include_router(
    fibonacci.router
)
add_pagination(app)

@app.get("/")
async def root():
    return {"message": "This is the root"}

