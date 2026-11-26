from sqlalchemy import Boolean, CheckConstraint, Column, Float, ForeignKey, Integer, JSON, String, Table

from core.db import metadata


crease_samples = Table('crease_samples', metadata,
    Column('code', String(64), primary_key=True),
    Column('flag', String(160), ForeignKey('flag_archive.code'), nullable=False),
    Column('depth', Float, nullable=False),
    Column('width', Float, nullable=False),
    Column('lines', Integer, nullable=False),
    Column('signed', Boolean, nullable=False),
    CheckConstraint('depth > 0'),
    CheckConstraint('width > 0'),
    CheckConstraint('lines > 0'),
)
