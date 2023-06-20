import redis

cache = redis.Redis(host='redis', port=6379)
from fastapi import FastAPI
from shorter_router import shorter_router

app = FastAPI()
app.include_router(shorter_router)
