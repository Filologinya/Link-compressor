from fastapi import FastAPI
from shorter_router import shorter_router

app = FastAPI()
app.include_router(shorter_router)
