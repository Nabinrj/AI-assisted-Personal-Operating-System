# NABU Codebase

This directory contains the executable application code for NABU.

## Structure

```text
code/
├── backend/       # FastAPI + PostgreSQL API
├── frontend/      # React + TypeScript UI
└── docker-compose.yml
```

## Run with Docker

```bash
cd code
cp backend/.env.example backend/.env
docker compose up --build
```

Open:
- Frontend: http://localhost:5173
- API: http://localhost:8000
- Swagger: http://localhost:8000/docs

## Current implementation

The first code increment contains the backend foundation, PostgreSQL connection, JWT authentication API, goals/projects/tasks endpoints, Docker services, and the first responsive Command Center UI.

## Important

The development database currently uses SQLAlchemy `create_all` at startup to keep the first local increment simple. Alembic migrations will replace this before production deployment.

Never commit real `.env` files or secrets.
