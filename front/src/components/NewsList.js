import React, { useEffect, useState } from "react";
import { fetchNewsArticles } from "../api";
import NewsItem from "./NewsItem";

const NewsList = () => {
  const [articles, setArticles] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [currentPage, setCurrentPage] = useState(1);
  const articlesPerPage = 5; // Number of articles per page

  useEffect(() => {
    const loadArticles = async () => {
      try {
        const data = await fetchNewsArticles();
        setArticles(data);
      } catch (err) {
        setError("Failed to load news articles. Please try again later.");
      } finally {
        setLoading(false);
      }
    };
    loadArticles();
  }, []);

  if (loading) return <p>Loading news articles...</p>;
  if (error) return <p>{error}</p>;

  // Pagination Logic
  const indexOfLastArticle = currentPage * articlesPerPage;
  const indexOfFirstArticle = indexOfLastArticle - articlesPerPage;
  const currentArticles = articles.slice(indexOfFirstArticle, indexOfLastArticle);

  // Change page
  const nextPage = () => setCurrentPage((prev) => Math.min(prev + 1, Math.ceil(articles.length / articlesPerPage)));
  const prevPage = () => setCurrentPage((prev) => Math.max(prev - 1, 1));

  return (
    <div className="news-list">
      <h2>Latest Super Bowl 2025 News</h2>
      {currentArticles.length > 0 ? (
        currentArticles.map((article) => <NewsItem key={article.id} article={article} />)
      ) : (
        <p>No articles found.</p>
      )}

      {/* Pagination Controls */}
      <div className="pagination">
        <button onClick={prevPage} disabled={currentPage === 1}>
          Prev
        </button>
        <span>Page {currentPage} of {Math.ceil(articles.length / articlesPerPage)}</span>
        <button onClick={nextPage} disabled={currentPage === Math.ceil(articles.length / articlesPerPage)}>
          Next
        </button>
      </div>
    </div>
  );
};

export default NewsList;
