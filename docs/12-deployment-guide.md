# Deployment Guide

## Local
Use Docker Compose for frontend, API, and PostgreSQL. Store configuration in .env files excluded from Git.

## Production
- Frontend: managed static hosting
- API: managed container or Python service
- Database: managed PostgreSQL
- Secrets: platform secret manager
- HTTPS: platform-managed TLS

## Required environment variables
DATABASE_URL
JWT_SECRET
JWT_ALGORITHM
ACCESS_TOKEN_EXPIRE_MINUTES
CORS_ORIGINS

Later AI variables:
AI_PROVIDER
AI_API_KEY
AI_MODEL

## Before launch
Run migrations, create backup strategy, configure production CORS, test health endpoint, verify logs, and confirm environment secrets are not exposed.