from db import db
from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    Boolean,
    DECIMAL,
    ForeignKey,
)
from sqlalchemy.orm import relationship

class Product(db.Model):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))
    code = Column(String(20))
    description = Column(Text)
    image = Column(String(255))
    brand = Column(String(255))
    size = Column(String(100))
    price = Column(DECIMAL(10, 4))
    stock = Column(Integer)
    is_active = Column(Boolean, default=True)
    category_id = Column(Integer, ForeignKey('categories.id'))