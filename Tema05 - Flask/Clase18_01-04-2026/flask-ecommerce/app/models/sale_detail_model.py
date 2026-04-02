from db import db
from sqlalchemy import (
    Column,
    Integer,
    DECIMAL,
    ForeignKey,
)

class SaleDetail(db.Model):
    __tablename__ = 'sale_details'

    id = Column(Integer, primary_key=True, index=True)
    quantity = Column(Integer)
    price = Column(DECIMAL(10, 4))
    subtotal = Column(DECIMAL(10, 4))
    product_id = Column(Integer, ForeignKey('products.id'))
    sale_id = Column(Integer, ForeignKey('sales.id'))