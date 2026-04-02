from db import db
from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean
)

class Category(db.Model):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))
    is_active = Column(Boolean, default=True)