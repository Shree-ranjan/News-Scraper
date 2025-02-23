import unittest
from unittest import mock
from apscheduler.schedulers.background import BackgroundScheduler
from scheduler import fetch_news_articles, start_scheduler, scheduler
from crud.crud import create_article
from db.database import Database
import requests
from schemas.schemas import NewsArticleCreate
from sqlalchemy.orm import Session


class TestScheduler(unittest.TestCase):

    # Mock the Database session and the create_article function
    @mock.patch("requests.get")
    @mock.patch("crud.create_article")
    @mock.patch("database.Database.get_session")
    def test_fetch_news_articles(self, mock_get_session, mock_create_article, mock_requests_get):
        # Mock the database session and instance
        mock_session = mock.MagicMock(spec=Session)
        mock_get_session.return_value = mock_session

        # Mock the response of requests.get
        mock_requests_get.return_value.json.return_value = {
            "articles": [
                {
                    "title": "Super Bowl 2025: The Ultimate Showdown",
                    "source": {"name": "Sports News"},
                    "url": "https://sportsnews.com/super-bowl-2025",
                    "description": "A preview of the biggest game of the year."
                }
            ]
        }

        # Call the fetch_news_articles function to test
        fetch_news_articles()

        # Verify that requests.get was called with the correct URL
        mock_requests_get.assert_called_once_with("https://newsapi.org/v2/everything?q=Super+Bowl+2025&apiKey=b28e88afc49e457eab42747cf1c5f4b9")

        # Verify that create_article was called with the expected arguments
        mock_create_article.assert_called_once_with(
            mock_session,
            NewsArticleCreate(
                title="Super Bowl 2025: The Ultimate Showdown",
                source="Sports News",
                url="https://sportsnews.com/super-bowl-2025",
                summary="A preview of the biggest game of the year."
            )
        )

    # Mock the start method of BackgroundScheduler
    @mock.patch.object(BackgroundScheduler, 'start')
    def test_start_scheduler(self, mock_start):
        # Call the start_scheduler function to test
        start_scheduler()

        # Verify that the scheduler's start method was called
        mock_start.assert_called_once()

    # Mock the running property of BackgroundScheduler
    @mock.patch.object(BackgroundScheduler, 'shutdown')
    @mock.patch.object(BackgroundScheduler, 'running', new_callable=mock.PropertyMock)
    def test_shutdown_scheduler(self, mock_running, mock_shutdown):
        # Simulate that the scheduler is running by setting the mock value to True
        mock_running.return_value = True

        # Call shutdown method to test
        scheduler.shutdown()

        # Verify that the shutdown method was called
        mock_shutdown.assert_called_once()


if __name__ == '__main__':
    unittest.main()
