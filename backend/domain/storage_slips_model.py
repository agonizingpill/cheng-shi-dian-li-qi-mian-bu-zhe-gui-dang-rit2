from sqlalchemy import Boolean, CheckConstraint, Column, Float, ForeignKey, Integer, JSON, String, Table

from core.db import metadata


storage_slips = Table('storage_slips', metadata,
    Column('code', String(64), primary_key=True),
    Column('guide', String(160), ForeignKey('fold_exemplars.code'), nullable=False),
    Column('flag', String(160), ForeignKey('flag_archive.code'), nullable=False),
    Column('action', String(160), nullable=False),
    Column('locker', String(160), nullable=False),
    Column('witness', String(160), nullable=False),
)
