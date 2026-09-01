# Database Design

## Core tables
users(id, email, password_hash, display_name, created_at)

goals(id, user_id, parent_id, title, description, horizon, status, priority, target_date, success_metric)

milestones(id, goal_id, title, target_date, status)

projects(id, user_id, goal_id, title, objective, status, start_date, target_date, next_action, blocker, repository_url)

tasks(id, user_id, project_id, goal_id, title, status, priority, due_at, estimated_minutes, actual_minutes)

skills(id, user_id, name, current_level, target_level)
skill_evidence(id, skill_id, description, url, completed_at)

time_entries(id, user_id, category, started_at, ended_at, duration_minutes, note)

income_entries(id, user_id, source, amount, currency, received_at, note)

daily_reviews(id, user_id, review_date, completed_summary, blocker, tomorrow_priority)
weekly_reviews(id, user_id, week_start, wins, failures, lessons, next_week_priority)

research_notes(id, user_id, question, hypothesis, experiment, result, conclusion, status)

## Relationships
User owns all personal records. Goals form a self-referencing tree. Projects and tasks may link to goals. Time and reviews provide behavioral evidence.