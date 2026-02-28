
# AI-Powered Worker Productivity Dashboard

## Run with Docker

docker-compose up --build

Visit:
http://localhost:8000/docs

Use POST /seed to load dummy data.
Then GET /metrics to view productivity metrics.

Architecture:
Edge AI Cameras -> FastAPI Backend -> SQLite DB -> Metrics Engine -> Dashboard

Includes:
- Event ingestion API
- Persistent database
- Computed productivity metrics
- Seedable dummy data
- Dockerized deployment
