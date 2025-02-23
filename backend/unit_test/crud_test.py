import unittest
from unittest.mock import MagicMock
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from db.models import NewsArticle
from schemas.schemas import NewsArticleCreate
from crud.crud import create_article, get_articles

class TestCRUD(unittest.TestCase):

    def setUp(self):
        self.db = MagicMock(spec=Session)
        self.article_data = {
            "title": "Test Article",
            "source": "Test Source",
            "url": "http://example.com",
            "summary": "This is a test article."
        }
        self.article = NewsArticleCreate(**self.article_data)

    def test_create_article_success(self):
        self.db.query.return_value.filter_by.return_value.first.return_value = None  # No duplicate article
        self.db.commit.return_value = None
        self.db.refresh.return_value = None

        result = create_article(self.db, self.article)

        self.db.add.assert_called_once()
        self.db.commit.assert_called_once()
        self.db.refresh.assert_called_once()
        self.assertEqual(result.title, self.article.title)
        self.assertEqual(result.url, self.article.url)

    def test_create_article_duplicate(self):
        existing_article = NewsArticle(**self.article_data)
        self.db.query.return_value.filter_by.return_value.first.return_value = existing_article  # Mock existing article

        result = create_article(self.db, self.article)

        self.db.add.assert_not_called()
        self.db.commit.assert_not_called()
        self.db.refresh.assert_not_called()
        self.assertEqual(result, existing_article)

    def test_create_article_integrity_error(self):
        self.db.query.return_value.filter_by.return_value.first.return_value = None  # No duplicate
        self.db.commit.side_effect = IntegrityError("Integrity Error", "params", "orig")  # Error happens on commit

        result = create_article(self.db, self.article)

        self.db.add.assert_called_once()
        self.db.commit.assert_called_once()
        self.db.rollback.assert_called_once()
        self.assertIsNone(result)  # Ensure None is returned on integrity error


    def test_get_articles(self):
        mock_articles = [NewsArticle(**self.article_data), NewsArticle(**self.article_data)]
        self.db.query.return_value.offset.return_value.limit.return_value.all.return_value = mock_articles

        result = get_articles(self.db, skip=0, limit=10)

        self.db.query.assert_called_once_with(NewsArticle)
        self.db.query.return_value.offset.assert_called_once_with(0)
        self.db.query.return_value.offset.return_value.limit.assert_called_once_with(10)
        self.assertEqual(result, mock_articles)

if __name__ == '__main__':
    unittest.main()
