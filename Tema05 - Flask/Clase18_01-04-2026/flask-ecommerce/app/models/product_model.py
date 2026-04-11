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
from app.utils.helpers import cloudinary_helper

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

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'code': self.code,
            'description': self.description,
            'image': cloudinary_helper.get_secure_url(self.image),
            'brand': self.brand,
            'size': self.size,
            'price': str(self.price),
            'stock': self.stock,
            'category_id': self.category_id
        }