"""initial NABU schema

Revision ID: 0001_initial
Revises:
"""
from alembic import op
import sqlalchemy as sa

revision='0001_initial'
down_revision=None
branch_labels=None
depends_on=None

def upgrade():
    op.create_table('users',sa.Column('id',sa.Integer(),primary_key=True),sa.Column('email',sa.String(255),nullable=False),sa.Column('password_hash',sa.String(255),nullable=False),sa.Column('display_name',sa.String(120),nullable=False),sa.Column('created_at',sa.DateTime(),nullable=False)); op.create_index('ix_users_email','users',['email'],unique=True)
    op.create_table('goals',sa.Column('id',sa.Integer(),primary_key=True),sa.Column('user_id',sa.Integer(),sa.ForeignKey('users.id'),nullable=False),sa.Column('parent_id',sa.Integer(),sa.ForeignKey('goals.id')),sa.Column('title',sa.String(200),nullable=False),sa.Column('description',sa.Text(),nullable=False),sa.Column('horizon',sa.String(30),nullable=False),sa.Column('status',sa.String(30),nullable=False),sa.Column('priority',sa.Integer(),nullable=False),sa.Column('target_date',sa.DateTime()),sa.Column('success_metric',sa.String(255),nullable=False)); op.create_index('ix_goals_user_id','goals',['user_id'])
    op.create_table('projects',sa.Column('id',sa.Integer(),primary_key=True),sa.Column('user_id',sa.Integer(),sa.ForeignKey('users.id'),nullable=False),sa.Column('goal_id',sa.Integer(),sa.ForeignKey('goals.id')),sa.Column('title',sa.String(200),nullable=False),sa.Column('objective',sa.Text(),nullable=False),sa.Column('status',sa.String(30),nullable=False),sa.Column('next_action',sa.String(255),nullable=False),sa.Column('blocker',sa.String(255),nullable=False),sa.Column('repository_url',sa.String(500),nullable=False)); op.create_index('ix_projects_user_id','projects',['user_id'])
    op.create_table('tasks',sa.Column('id',sa.Integer(),primary_key=True),sa.Column('user_id',sa.Integer(),sa.ForeignKey('users.id'),nullable=False),sa.Column('project_id',sa.Integer(),sa.ForeignKey('projects.id')),sa.Column('goal_id',sa.Integer(),sa.ForeignKey('goals.id')),sa.Column('title',sa.String(255),nullable=False),sa.Column('status',sa.String(30),nullable=False),sa.Column('priority',sa.Integer(),nullable=False),sa.Column('due_at',sa.DateTime()),sa.Column('estimated_minutes',sa.Integer(),nullable=False),sa.Column('actual_minutes',sa.Integer(),nullable=False),sa.Column('completed',sa.Boolean(),nullable=False)); op.create_index('ix_tasks_user_id','tasks',['user_id'])
    op.create_table('skills',sa.Column('id',sa.Integer(),primary_key=True),sa.Column('user_id',sa.Integer(),sa.ForeignKey('users.id'),nullable=False),sa.Column('name',sa.String(120),nullable=False),sa.Column('current_level',sa.Integer(),nullable=False),sa.Column('target_level',sa.Integer(),nullable=False)); op.create_index('ix_skills_user_id','skills',['user_id'])
    op.create_table('skill_evidence',sa.Column('id',sa.Integer(),primary_key=True),sa.Column('skill_id',sa.Integer(),sa.ForeignKey('skills.id'),nullable=False),sa.Column('description',sa.Text(),nullable=False),sa.Column('url',sa.String(500),nullable=False),sa.Column('completed_at',sa.DateTime(),nullable=False)); op.create_index('ix_skill_evidence_skill_id','skill_evidence',['skill_id'])
    op.create_table('time_entries',sa.Column('id',sa.Integer(),primary_key=True),sa.Column('user_id',sa.Integer(),sa.ForeignKey('users.id'),nullable=False),sa.Column('category',sa.String(60),nullable=False),sa.Column('started_at',sa.DateTime(),nullable=False),sa.Column('duration_minutes',sa.Integer(),nullable=False),sa.Column('note',sa.Text(),nullable=False)); op.create_index('ix_time_entries_user_id','time_entries',['user_id'])
    op.create_table('income_entries',sa.Column('id',sa.Integer(),primary_key=True),sa.Column('user_id',sa.Integer(),sa.ForeignKey('users.id'),nullable=False),sa.Column('source',sa.String(120),nullable=False),sa.Column('amount',sa.Numeric(12,2),nullable=False),sa.Column('currency',sa.String(8),nullable=False),sa.Column('received_at',sa.DateTime(),nullable=False),sa.Column('note',sa.Text(),nullable=False)); op.create_index('ix_income_entries_user_id','income_entries',['user_id'])
    op.create_table('daily_reviews',sa.Column('id',sa.Integer(),primary_key=True),sa.Column('user_id',sa.Integer(),sa.ForeignKey('users.id'),nullable=False),sa.Column('review_date',sa.Date(),nullable=False),sa.Column('completed_summary',sa.Text(),nullable=False),sa.Column('blocker',sa.Text(),nullable=False),sa.Column('tomorrow_priority',sa.String(255),nullable=False)); op.create_index('ix_daily_reviews_user_id','daily_reviews',['user_id'])
    op.create_table('weekly_reviews',sa.Column('id',sa.Integer(),primary_key=True),sa.Column('user_id',sa.Integer(),sa.ForeignKey('users.id'),nullable=False),sa.Column('week_start',sa.Date(),nullable=False),sa.Column('wins',sa.Text(),nullable=False),sa.Column('failures',sa.Text(),nullable=False),sa.Column('lessons',sa.Text(),nullable=False),sa.Column('next_week_priority',sa.String(255),nullable=False)); op.create_index('ix_weekly_reviews_user_id','weekly_reviews',['user_id'])
    op.create_table('research_notes',sa.Column('id',sa.Integer(),primary_key=True),sa.Column('user_id',sa.Integer(),sa.ForeignKey('users.id'),nullable=False),sa.Column('question',sa.String(500),nullable=False),sa.Column('hypothesis',sa.Text(),nullable=False),sa.Column('experiment',sa.Text(),nullable=False),sa.Column('result',sa.Text(),nullable=False),sa.Column('conclusion',sa.Text(),nullable=False),sa.Column('status',sa.String(30),nullable=False)); op.create_index('ix_research_notes_user_id','research_notes',['user_id'])

def downgrade():
    for table in ['research_notes','weekly_reviews','daily_reviews','income_entries','time_entries','skill_evidence','skills','tasks','projects','goals','users']:
        op.drop_table(table)
