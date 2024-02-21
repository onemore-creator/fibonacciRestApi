from pydantic import BaseModel

class Blacklist(BaseModel):
    numbers:  list[str]

