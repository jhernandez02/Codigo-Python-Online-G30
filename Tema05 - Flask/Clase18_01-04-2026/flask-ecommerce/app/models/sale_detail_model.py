from db import db
from sqlalchemy import (
    Column,
    Integer,
    DECIMAL,
    ForeignKey,
)
from sqlalchemy.orm import relationship

class SaleDetail(db.Model):
    __tablename__ = 'sale_details'

    id = Column(Integer, primary_key=True, index=True)
    quantity = Column(Integer)
    price = Column(DECIMAL(10, 4))
    subtotal = Column(DECIMAL(10, 4))
    product_id = Column(Integer, ForeignKey('products.id'))
    sale_id = Column(Integer, ForeignKey('sales.id'))

    product = relationship('Product')

    def to_json(self):
        return {
            'id': self.id,
            'quantity': self.quantity,
            'price': str(self.price),
            'subtotal': str(self.subtotal),
            'product': {
                'id': self.product.id,
                'name': self.product.name,
                'code': self.product.code,
            }
        }