from pydantic import BaseModel


class PostBase(BaseModel):
    abbreviation: str
    state: str

    class Config:
        orm_mode = True


class CreatePost(PostBase):
    class Config:
        orm_mode = True