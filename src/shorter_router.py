from fastapi import APIRouter, HTTPException
from pydantic import AnyUrl
from starlette.responses import RedirectResponse

from config.redis import cache
from schemas import Link
from utils import create_random_key

shorter_router = APIRouter()

@shorter_router.post("/squeeze", response_model=Link)
async def squeeze(link: AnyUrl):
    random_key = create_random_key()
    while cache.get(f'link:{random_key}:value') is not None:
        random_key = create_random_key()
    link_id = cache.incr(f'link:global_id', 1)
    cache.set(f'link:{random_key}:id', link_id)
    cache.set(f'link:{random_key}:value', link)
    cache.set(f'link:{random_key}:counter', 0)
    return Link(id=1, short=random_key, target=link, counter=0)

@shorter_router.get("/s/{key}", response_class=RedirectResponse)
async def redirect(key: str):
    target_url = cache.get(f'link:{key}:value')
    if target_url is None:
        raise HTTPException(status_code=404,
                            detail='not target for short path')
    cache.incr(f'link:{key}:counter', 1)
    return target_url
