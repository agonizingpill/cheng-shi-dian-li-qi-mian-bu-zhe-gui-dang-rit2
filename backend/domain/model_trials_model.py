from sqlalchemy import Column, JSON, String, Table

from core.db import metadata


model_trials = Table('model_trials', metadata,
    Column('code', String(64), primary_key=True),
    Column('fit', JSON, nullable=False),
    Column('holdout', JSON, nullable=False),
    Column('baseline', String(64), nullable=True),
    Column('status', String(16), nullable=False),
    Column('token', String(64), nullable=False),
    Column('report', JSON, nullable=True),
)
