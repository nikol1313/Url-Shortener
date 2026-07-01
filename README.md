# URL Shortener API

A simple, containerized URL shortening service built with FastAPI.

## Features
- **URL Shortening**: Convert long URLs into short, unique codes.
- **Redirection**: Redirect from short codes to original URLs.
- **Dockerized**: Fully orchestrated with PostgreSQL using Docker Compose.

## Prerequisites
- Docker & Docker Compose installed.

1. ** Clone and Start the application after creating .env file**
   ```bash
   docker-compose up --build
   ```
   
The API will be available at `http://localhost:8080`.

## API Endpoints
- `POST /shorten`: Input `{ "original_url": "https://example.com" }` to get a short URL.
- `GET /{short_code}`: Redirects to the original URL.
