from db import db
from sqlalchemy import (
    Column,
    Integer,
    String,
)

class Customer(db.Model):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))
    last_name = Column(String(255))
    email = Column(String(255), unique=True)
    document_number = Column(String(255), unique=True)
    address = Column(String(255))