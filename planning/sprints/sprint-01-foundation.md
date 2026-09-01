# Sprint 1 — Foundation

## Status
ACTIVE

## Objective
Create a working, reproducible foundation for NABU: React frontend, FastAPI backend, PostgreSQL, authentication, Docker, and basic API integration.

## Definition of Done
- [ ] Repository structure created
- [ ] FastAPI application starts locally
- [ ] GET /health returns a successful response
- [ ] OpenAPI documentation works
- [ ] PostgreSQL connection works
- [ ] Alembic migrations work
- [ ] User registration works
- [ ] User login works
- [ ] Passwords are securely hashed
- [ ] JWT access token is issued
- [ ] Protected GET /api/v1/auth/me works
- [ ] React application starts
- [ ] Login and registration forms work
- [ ] Frontend communicates with backend
- [ ] Docker Compose starts the development stack
- [ ] README setup instructions are updated
- [ ] Critical backend tests pass

## Tasks

### 1. Repository and environment
- [ ] Create backend directory
- [ ] Create frontend directory
- [ ] Add root .gitignore
- [ ] Add .env.example files
- [ ] Define local environment conventions

### 2. Backend skeleton
- [ ] Install FastAPI and dependencies
- [ ] Create app package
- [ ] Create application factory/main entry point
- [ ] Add /health
- [ ] Add /api/v1 prefix
- [ ] Verify Swagger at /docs

### 3. Database
- [ ] Add SQLAlchemy
- [ ] Configure DATABASE_URL
- [ ] Create engine and session
- [ ] Add Alembic
- [ ] Create users table migration

### 4. Authentication
- [ ] User ORM model
- [ ] Register schema
- [ ] Login schema
- [ ] Password hashing
- [ ] JWT creation and validation
- [ ] Register endpoint
- [ ] Login endpoint
- [ ] Current-user dependency
- [ ] Protected /me endpoint

### 5. Frontend
- [ ] Initialize React + TypeScript
- [ ] Add Tailwind
- [ ] Configure API client
- [ ] Registration page
- [ ] Login page
- [ ] Auth state
- [ ] Protected placeholder dashboard

### 6. Containers
- [ ] Backend Dockerfile
- [ ] Frontend Dockerfile
- [ ] PostgreSQL service
- [ ] docker-compose.yml
- [ ] Health checks

### 7. Quality
- [ ] Backend tests
- [ ] Lint/format baseline
- [ ] Manual end-to-end auth test

## Acceptance Criteria
A new user can start the project, register through the frontend, log in, receive an authenticated session, call the protected /me endpoint, and run the stack with documented local commands.

## Out of Scope
Goals, tasks, projects, skills, AI features, analytics, mobile application, and advanced deployment.

## Commit checkpoints
1. chore: initialize NABU monorepo
2. feat(api): add FastAPI health endpoint
3. feat(db): add PostgreSQL and migrations
4. feat(auth): add registration and JWT authentication
5. feat(web): add authentication screens
6. chore(docker): containerize development stack
7. test: add Sprint 1 coverage
