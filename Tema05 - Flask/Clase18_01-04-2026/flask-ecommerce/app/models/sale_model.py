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
from sqlalchemy.orm import relationship

class Sale(db.Model):
    __tablename__ = 'sales'

    id = Column(Integer, primary_key=True, index=True)
    code = Column(String(20))
    total = Column(DECIMAL(10, 4))
    status = Column(String(255)) # PENDING, COMPLETED, CANCELLED
    created_at = Column(DateTime, default=func.now())
    customer_id = Column(Integer, ForeignKey('customers.id'))

    customer = relationship('Customer')
    sale_details = relationship('SaleDetail')

    def to_json(self):
        return {
            'id': self.id,
            'code': self.code,
            'total': str(self.total),
            'status': self.status,
            'customer': {
                'id': self.customer.id,
                'name': self.customer.name,
                'last_name': self.customer.last_name,
                'email': self.customer.email,
                'document_number': self.customer.document_number,
                'address': self.customer.address
            },
            'sale_details': [detail.to_json() for detail in self.sale_details]
        }