from sqlalchemy import create_engine
from sqlite_ex import Customer,Address,Base
from sqlalchemy.orm import sessionmaker
engine = create_engine("sqlite:///alchemy.db")
Base.metadata.bind=engine
DBSession = sessionmaker()
DBSession.bind = engine
session = DBSession()
session.query(Customer).all()

customer = session.query(Customer).first()
print(customer.name)

address = session.query(Address).filter(Address.customer == customer).one()
print(address.post_code)