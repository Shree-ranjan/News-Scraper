import React from "react";

const NewsItem = ({ article }) => {
  return (
    <div className="news-item">
      <h3>{article.title}</h3>
      <p>{article.summary}</p>
      <a href={article.url} target="_blank" rel="noopener noreferrer">
        Read more
      </a>
      <p>
        <strong>Source:</strong> {article.source}
      </p>
      <p>
        <strong>Published:</strong> {new Date(article.timestamp).toLocaleString()}
      </p>
    </div>
  );
};

export default NewsItem;