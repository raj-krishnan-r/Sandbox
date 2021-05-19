import os
import sys
from sqlalchemy import Column,ForeignKey,Integer,String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class Customer(Base):
    __tablename__ = 'customer'
    id = Column(Integer,primary_key=True)
    name = Column(String(250),nullable=False)
class Address(Base):
    __tablename__ = 'address'
    id = Column(Integer,primary_key=True)
    street_name = Column(String(250))
    street_number = Column(String(250))
    post_code = Column(String(250))
    customer_id = Column(Integer,ForeignKey('customer.id'))
    customer = relationship(Customer)
engine = create_engine('sqlite:///alchemy.db')
Base.metadata.create_all(engine)