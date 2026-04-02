from db import db
from sqlalchemy import (
    Column,
    Integer,
    String,
    DECIMAL,
    DateTime,
    ForeignKey,
    func
)

class Sale(db.Model):
    __tablename__ = 'sales'

    id = Column(Integer, primary_key=True, index=True)
    code = Column(String(20))
    total = Column(DECIMAL(10, 4))
    status = Column(String(255))
    created_at = Column(DateTime, default=func.now())
    customer_id = Column(Integer, ForeignKey('customers.id'))