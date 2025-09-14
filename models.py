from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))  # specify length for MySQL compatibility
    email = Column(String(100), unique=True, index=True)
    phone = Column(String(10))




    
    