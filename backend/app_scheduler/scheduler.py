import urllib.parse
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.schedulers.base import SchedulerAlreadyRunningError
from crud.crud import create_article
from db.database import Database
import requests
from schemas.schemas import NewsArticleCreate
from sqlalchemy.orm import Session
import urllib
from constants.constants import API_KEY


# Singleton Database instance
db_instance = Database()

# Importing API Key as string
api_key = urllib.parse.quote(str(API_KEY))


def fetch_news_articles():
    db_session: Session = db_instance.get_session()()
    try:
        news_api_url = f"https://newsapi.org/v2/everything?q=Super+Bowl+2025&apiKey={api_key}"
        response = requests.get(news_api_url)
        articles = response.json().get("articles", [])

        for article in articles:
            article_data = {
                "title": article["title"],
                "source": article["source"]["name"],
                "url": article["url"],
                "summary": article["description"]
            }
            create_article(db_session, NewsArticleCreate(**article_data))
    finally:
        db_session.close()  # Always close the session


scheduler = BackgroundScheduler()
scheduler.add_job(fetch_news_articles, 'interval', minutes=10)


def start_scheduler():
    try:
        if not scheduler.running:
            scheduler.start()
    except SchedulerAlreadyRunningError:
        pass
