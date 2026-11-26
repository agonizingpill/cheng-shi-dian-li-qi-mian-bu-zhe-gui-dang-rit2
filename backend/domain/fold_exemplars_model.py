from sqlalchemy import Boolean, CheckConstraint, Column, Float, ForeignKey, Integer, JSON, String, Table

from core.db import metadata


fold_exemplars = Table('fold_exemplars', metadata,
    Column('code', String(64), primary_key=True),
    Column('sample', String(160), ForeignKey('crease_samples.code'), nullable=False),
    Column('example', String(160), ForeignKey('crease_samples.code'), nullable=False),
    Column('group_size', Integer, nullable=False),
    Column('token', String(64), nullable=False, unique=True),
)
