from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from db.models import NewsArticle
from schemas.schemas import NewsArticleCreate

def create_article(db: Session, article: NewsArticleCreate):
    existing_article = db.query(NewsArticle).filter_by(url=article.url).first()
    if existing_article:
        return existing_article  # Prevent duplicate insert
    db_article = NewsArticle(**article.dict())
    db.add(db_article)
    try:
        db.commit()
        db.refresh(db_article)
    except IntegrityError:
        db.rollback()  # Handle the case where another process inserted the same article
        return db.query(NewsArticle).filter_by(url=article.url).first()
    
    return db_article

def get_articles(db: Session):
    return db.query(NewsArticle).all()