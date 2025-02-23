from pydantic import BaseModel
from datetime import datetime

class NewsArticleBase(BaseModel):
    title: str
    source: str
    url: str
    summary: str | None = None

class NewsArticleCreate(NewsArticleBase):
    pass

class NewsArticle(NewsArticleBase):
    id: int
    timestamp: datetime

    class Config:
        orm_mode = True