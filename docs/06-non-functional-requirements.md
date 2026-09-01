# Non-Functional Requirements

## Performance
Typical API responses should target under 500 ms excluding external AI calls.

## Security
HTTPS in production; bcrypt/Argon2 password hashing; JWT expiration; server-side validation; rate limiting for authentication; secrets only in environment variables.

## Reliability
Database migrations; backups; structured logs; health endpoint.

## Privacy
Users own their data. Collect the minimum required. Do not send data to an AI provider without clear feature-level consent.

## Maintainability
Typed frontend and backend schemas, modular services, tests for critical business logic, API documentation.

## Accessibility
Keyboard navigation, semantic HTML, readable contrast, responsive layouts.

## Scope discipline
The MVP must remain usable with one account and one active user even before multi-user scale is optimized.