from pydantic import BaseModel

class BlacklistResponse(BaseModel):
    numbers:  list[str]

