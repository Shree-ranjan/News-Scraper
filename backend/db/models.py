from sqlalchemy import Column, Integer, String, DateTime
from db.database import Database
from datetime import datetime

Base = Database().get_base()

class NewsArticle(Base):
    __tablename__ = "news_articles"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    source = Column(String, nullable=False)
    url = Column(String, unique=True, nullable=False)
    summary = Column(String, nullable=True)
    timestamp = Column(DateTime, default=datetime.utcnow)