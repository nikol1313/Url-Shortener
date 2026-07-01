from pydantic import BaseModel, HttpUrl, ConfigDict

class URLBase(BaseModel):
    original_url: HttpUrl

class URLCreate(URLBase):
    pass

class URL(URLBase):
    id: int
    short_url: str
    model_config = ConfigDict(from_attributes=True)
