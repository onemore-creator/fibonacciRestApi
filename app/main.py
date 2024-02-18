from fastapi import FastAPI

from .routers import *

app = FastAPI()

app.include_router(
    fibonacci.router
)

@app.get("/")
async def root():
    return {"message": "This is the root"}

