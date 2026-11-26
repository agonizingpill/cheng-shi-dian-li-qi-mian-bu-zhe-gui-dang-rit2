from sqlalchemy import Boolean, CheckConstraint, Column, Float, ForeignKey, Integer, JSON, String, Table

from core.db import metadata


flag_archive = Table('flag_archive', metadata,
    Column('code', String(64), primary_key=True),
    Column('material', String(160), nullable=False),
    Column('heritage', Boolean, nullable=False),
    Column('displayed', Boolean, nullable=False),
)
