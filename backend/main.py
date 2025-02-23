from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from db.database import get_db
from crud.crud import get_articles
from schemas.schemas import NewsArticle
from typing import List
from sqlalchemy.orm import Session
from app_scheduler.scheduler import scheduler, start_scheduler

app = FastAPI()

origins = [
    "http://localhost:3000", "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def on_startup():
    start_scheduler()


@app.on_event("shutdown")
async def shutdown_scheduler():
    if scheduler.running:  # Check if scheduler is running before shutting down
        scheduler.shutdown()

@app.get("/api/news", response_model=List[NewsArticle])
def read_news(db: Session = Depends(get_db)):
    articles = get_articles(db=db)
    return articles