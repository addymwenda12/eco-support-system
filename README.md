# Eco Support System

Energy renewable management system with predictive analytics and automated customer support. This project aims to empower energy providers and consumers by using  machine learning models to forecast energy production and consumption while providing instant support through automated responses.

---

## Table of Contents

- Overview
- Key Features
- System Architecture
- Why These Tools
- Repository Layout
- Getting Started
  - Prerequisites
  - Local Setup
  - Configuration
  - Running the Services
- Data and Modeling
  - Data Ingestion
  - Feature Engineering
  - Forecasting
  - Anomaly Detection
  - Model Management
- API Walkthrough
- Automated Customer Support
- Observability, Logging, and Monitoring

---

## Overview

Eco Support System unifies short and medium term energy forecasting with an automated support assistant that can:
- Predict renewable generation and consumption using time series and signals (weather, calendar effects, tariff schedules).
- Highlight anomalies (unexpected consumption spikes, under‑performing generation).
- Provide instant answers and guided workflows to customers via a conversational interface.

---

## Key Features

- End to end forecasting pipeline for energy demand and renewable generation.
- Exogenous signal integration
- Real time and batch inferencing endpoints.
- Anomaly detection with alerting hooks.
- Automated customer support:
  - Knowledge base Q&A.
  - Account or device troubleshooting flows.
  - Escalation to human agents with full context.
- RESTful or GraphQL API for external integrations.
- Role‑based access and audit events.
- Observability: structured logs, metrics, and traces.

---

## System Architecture

High‑level components:
- Backend API (Python; FastAPI) in server/:
  - Prediction endpoints (`/predict`, `/forecasts/`)
  - Support automation endpoints (`/support/chat`)
  - Admin and health endpoints (`/health`, `/metrics`)
- Data connectors:
  - Smart meter ingestion (push or pull)
- ML services:
  - Feature engineering and windowing
  - Forecasting models
  - Anomaly detection
- Storage:
  - Operational DB for user, and metadata
  - Object storage or filesystem for datasets and models
  - Cache  for low latency feature lookup and rate limiting

---

## Why These Tools

- Python as the core: rich ecosystem for data, ML, and fast APIs.
- FastAPI  for the server:
  - Async IO for efficient IO‑bound workloads (API calls, DB, cache).
- Redis:
  - Caching recent features or forecasts; rate limiting chat endpoints.
- PostgreSQL:
  - Strong consistency and relational modeling for accounts, devices, tickets, audit logs.

## Getting Started

### Prerequisites

- Python 3.10+ recommended
- Optional: PostgreSQL and Redis if running services locally without containers

### Local Setup

1) Clone
- git clone
  ```bash
  https://github.com/mutuiris/eco-support-system.git
  ```
- cd
  ```bash
  eco-support-system
  ```

2) Create and activate a virtual environment
- ```bash
  python -m venv .venv
  ```
- ```bash
  source .venv/bin/activate  # Windows: .venv\Scripts\activate
  ```

3) Install dependencies
- ```python
  pip install --upgrade pip
  ```
- ```python
  pip install -r requirements.txt
  ```
- If using Poetry or uv, adapt:
  ```python
    poetry install
    ```
  or:
  ```python
  uv pip install -r requirements.txt
  ```

### Configuration

Create a .env file at the project root and set:
```env
APP_ENV=development
APP_PORT=8000
DATABASE_URL=postgresql+psycopg://user:pass@localhost:5432/eco_support
REDIS_URL=redis://localhost:6379/0
JWT_SECRET=change-me
LOG_LEVEL=INFO
MODEL_DIR=./models
DATA_DIR=./data
```

### Running the Services

Option A: Without Docker
```python
uvicorn server.main:app --host 0.0.0.0 --port 8000 --reload
```
- If your entrypoint differs: ```python uvicorn server.app:app``` ... or ```python python -m server.main```

Open the interactive API docs at:
```bash
http://localhost:8000/docs
```
```bash
http://localhost:8000/redoc
```

Option B: With Docker
```docker
docker build -t eco-support-system
```
```docker
docker run --env-file .env -p 8000:8000 eco-support-system
```
- Or ```docker compose up``` if a compose file exists.

Health check
```bash
curl http://localhost:8000/health
```

---

## Data and Modeling

### Data Ingestion

- Smart meters or device telemetry:
  - Batch CSV/Parquet ingest or streaming endpoints.
- Weather data:
  - External API client with retry/backoff, caching via Redis..

### Forecasting

- Approaches:
  - Deep learning: Temporal Fusion Transformers, LSTMs/GRUs for multi‑horizon forecasts.
- Multi‑horizon forecasting with quantiles to communicate uncertainty.



## Automated Customer Support

- Intent classification for typical queries:
  - Forecast interpretation.
- Knowledge base integration:
  - Retrieval augmented responses grounded in your docs.

Why: Reduces handle time, improves first contact resolution, and gives agents actionable context.

---

## Observability, Logging, and Monitoring

- Structured logs (JSON) with correlation IDs.
- Metrics:
  - Request throughput/latency, error rates, cache hit rate.
- Tracing:
  - Distributed traces across API, DB, cache, and external API calls.

Why: Faster incident response and safer iteration on ML systems.

---

## Security and Compliance

- Secrets management:
  - Use environment variables or a secrets manager; never commit secrets.
- Authentication/Authorization:
  - JWT/OIDC for API; role‑based access for admin endpoints.
- Data protection:
  - Encrypt in transit and at rest; minimize PII and apply retention policies.
- Audit logs for admin and model lifecycle actions.

---

## Performance and Scalability

- FastAPI async patterns; connection pooling for DB/Redis.
- Caching:
  - Hot features and recent forecasts to reduce recompute and latency.
- Pagination and streaming for large result sets.

---
