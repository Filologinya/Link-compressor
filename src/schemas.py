from pydantic import BaseModel, AnyUrl

class Link(BaseModel):
    id: int
    short: str
    target: AnyUrl
    counter: int
