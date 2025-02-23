# Container-Based Web Application for Super Bowl Article Aggregation

## Overview

This project is a containerized web application designed to fetch, store, and display the latest articles related to the 2025 Super Bowl. The application is built using **React.js** for the frontend, **FastAPI** for the backend, and **PostgreSQL** as the database. All services are containerized using **Docker** and orchestrated with **Docker Compose**.

---

## Project Structure

The application consists of three main services:

1. **Frontend Service**: Built with **React.js**, this service provides a user interface to display the latest Super Bowl articles.
2. **Backend Service**: Built with **FastAPI**, this service fetches articles from the web, stores them in the database, and exposes a REST API to serve the articles to the frontend.
3. **Database Service**: Uses **PostgreSQL** to store the fetched articles with relevant details such as title, source, URL, timestamp, and summary.

---

## Technical Requirements

### 1. Backend Service (FastAPI)

- Exposes a REST API endpoint (`/api/news`) to serve the latest Super Bowl articles.
- Implements a scheduled job (`appscheduler`) to fetch new articles periodically from the web.
- Stores the retrieved articles in the PostgreSQL database.
- Implements basic logging and error handling.
- Includes unit tests for key functionalities.

### 2. Frontend Service (React.js)

- Provides a simple and responsive web interface to display the latest Super Bowl articles.
- Fetches data from the backend API (`/api/news`) and renders it dynamically.
- Includes basic styling and user-friendly components.

### 3. Database Service (PostgreSQL)

- Stores news articles with the following fields:
  - `id` (Primary Key)
  - `title` (Article title)
  - `source` (Source of the article)
  - `url` (Link to the article)
  - `timestamp` (Publication date and time)
  - `summary` (Brief summary of the article)
- Ensures the database schema is optimized for efficient querying.

### 4. Containerization & Deployment

- Uses **Docker** to containerize all services (frontend, backend, and database).
- Defines a `docker-compose.yml` file to orchestrate the services and manage networking between them.
- Ensures seamless communication between the frontend, backend, and database containers.

---

## Getting Started

### Prerequisites

- Docker and Docker Compose installed on your machine.
- Basic knowledge of React.js, FastAPI, and PostgreSQL.

### Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone https://github.com/Shree-ranjan/News-Scraper.git
   cd News-Scraper
   cd backend

2. **Create a .env file**
  - Create a .env file in the backend directory with the following variables:
  ##### PostgreSQL Configuration
    POSTGRES_HOST=superbowl_db
    POSTGRES_PORT=5432
    POSTGRES_USER=your_db_user
    POSTGRES_PASSWORD=your_db_password
    POSTGRES_DB=superbowl_db

  ##### Backend Configuration
    DATABASE_URL=postgresql://your_db_user:your_db_password@db:5432/superbowl_db

3. **Build and Run the Application**
  - Use Docker Compose to build and start the containers:
    ``` bash
    docker-compose up --build

  - This will start the following services:
    - Frontend: Accessible at http://localhost:3000
    - Backend: Accessible at http://localhost:8093
    - Database: PostgreSQL running on port 5438

4. **Access the Application**
  - Open your browser and navigate to http://localhost:3000 to view the frontend.
  - The backend API will be available at http://localhost:8093/api/news.

5. **Stop the Application**
  - To stop the containers, run:
    ```bash
    docker-compose down

### Directory Structure
- News-Scraper/
- ├── front/
- │   ├── public/
- │   ├── src/
- │   ├── .env
- │   ├── Dockerfile
- │   └── package.json
- ├── backend/
- │   ├── __init__.py
- │   ├── app_scheduler/
- │   ├── constants/
- │   ├── crud/
- │   ├── db/
- │   ├── migrations/
- │   ├── schemas/
- │   ├── unit_tests/
- │   ├── Dockerfile
- │   ├── docker-compose.yml
- │   ├── .env
- │   ├── main.py
- │   └── requirements.txt
- └── README.md

## API Endpoints

### Backend API (/api/news)
  - GET /api/news
    - Fetches the latest Super Bowl articles.
    - Response:
      ```json
      [
        {
          "id": 1,
          "title": "Super Bowl 2025: Watch Chiefs vs. Eagles on Sunday, February 9",
          "source": "Yahoo Entertainment",
          "url": "https://consent.yahoo.com/v2/collectConsent?sessionId=1_cc-session_84522968-16c1-4227-8a5e-57155a64cf6c",
          "summary": "The Caesars Superdome will host Super Bowl LXI on Sunday, February 9. Here's how to tune in to the big game! (Photo by Chris Graythen/Getty Images)\n \r\n\n \n Chris Graythen via Getty Images\n \r\n\n \nSuper Bowl LIX is about a week away, and the hype is building for …",
          "timestamp": "2025-02-20T08:05:21.235768"
        },
        ...
      ]

## Technologies Used
  - Frontend: React.js
  - Backend: FastAPI
  - Database: PostgreSQL
  - Containerization: Docker, Docker Compose

## Future Enhancements
  - Add user authentication and authorization.
  - Implement a search functionality for articles.
  - Deploy the application to a cloud platform (e.g., AWS, GCP, or Azure).
