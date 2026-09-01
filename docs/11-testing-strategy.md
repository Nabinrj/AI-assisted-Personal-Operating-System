# Testing Strategy

## Backend
Unit tests for calculations and services; integration tests for API/database flows; authentication and authorization tests.

## Frontend
Component tests for critical forms and dashboards; end-to-end tests for onboarding, task completion, time logging, and review flows.

## Acceptance tests
- New user can complete onboarding.
- User can create a goal hierarchy.
- User can link a project and tasks to a goal.
- Completed work changes relevant metrics.
- Weekly review summarizes the correct period.
- Unauthorized users cannot access another user's data.

## Quality gates
No secrets committed. Lint and tests run in CI. Database migrations are tested against a fresh database.