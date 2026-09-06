# NABU — AI-assisted Personal Operating System

NABU is a personal operating system for turning goals into projects, projects into next actions, and real activity into measurable feedback.

## What is implemented

- JWT authentication: register, login, current-user session
- Goals: measurable goal records with horizon, priority and success metric
- Projects: objective, next action and blocker tracking
- Tasks: priorities, estimates, actual effort and completion state
- Skills: current/target level tracking
- Time: categorized effort logging
- Money: income tracking in NPR or another currency
- Research: question, hypothesis and experiment tracking
- Reviews: daily and weekly reflection records
- Analytics: execution rate, active goals/projects, income and recent time distribution
- Reality Check: deterministic feedback based on planned vs actual work
- Coach page: practical system feedback without requiring an external AI API key
- Responsive React + TypeScript command center
- PostgreSQL persistence
- Alembic initial migration and migration-first Docker startup

## Architecture

```text
code/
├── backend/
│   ├── app/
│   │   ├── core/          # configuration
│   │   ├── routers/       # HTTP API endpoints
│   │   ├── services/      # reusable business logic
│   │   ├── tests/         # backend tests
│   │   ├── models.py      # SQLAlchemy models
│   │   ├── schemas.py     # Pydantic schemas
│   │   ├── schemas_extra.py
│   │   ├── security.py    # password/JWT handling
│   │   └── main.py
│   ├── alembic/           # database migrations
│   ├── Dockerfile
│   └── requirements.txt
├── frontend/
│   ├── src/
│   │   ├── main.tsx       # application shell + pages
│   │   └── styles.css
│   ├── Dockerfile
│   └── package.json
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

The backend container waits for PostgreSQL and runs `alembic upgrade head` before starting FastAPI.

## Run backend locally

```bash
cd code/backend
python -m venv .venv
# Windows: .venv\\Scripts\\activate
# Linux/macOS: source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
alembic upgrade head
uvicorn app.main:app --reload
```

## Run frontend locally

```bash
cd code/frontend
npm install
npm run dev
```

If the API is not on `http://localhost:8000`, set `VITE_API_URL` before starting Vite.

## Database migrations

Create a new migration after model changes:

```bash
alembic revision --autogenerate -m "describe change"
alembic upgrade head
```

Do not rely on `Base.metadata.create_all()` for production. The container uses Alembic as the authoritative schema mechanism.

## Environment and secrets

Never commit real `.env` files, JWT secrets, database passwords, or API keys. Use `backend/.env.example` as the template for local configuration.

## Product direction

The current foundation is deliberately deterministic. The next AI layer can consume the structured evidence already stored by NABU and generate explanations, prioritization suggestions, anomaly detection and weekly planning while keeping the database and deterministic metrics as the source of truth.
