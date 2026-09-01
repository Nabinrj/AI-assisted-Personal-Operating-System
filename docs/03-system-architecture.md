# System Architecture

## Architecture
Client → API → PostgreSQL
              ↘ AI provider (later)

## Frontend
React, TypeScript, Tailwind CSS, React Router, TanStack Query, Recharts.

## Backend
Python, FastAPI, SQLAlchemy, Alembic, Pydantic.

## Infrastructure
Docker for local and production environments. Start with a simple managed PostgreSQL and API/frontend deployment.

## Core modules
- Identity/Auth
- Goals
- Tasks
- Projects
- Skills
- Time Logs
- Income
- Research
- Reviews
- Analytics
- AI Coach (phase 2)

## API style
REST, JSON, JWT authentication, UUID identifiers, UTC timestamps, role-ready authorization.

## AI boundary
AI receives only necessary user context and structured metrics. Rules and calculations remain deterministic in application code where possible.