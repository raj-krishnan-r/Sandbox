from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlite_ex import Customer,Base,Address
engine = create_engine('sqlite:///alchemy.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()
new_customer = Customer(name="Gokul")
session.add(new_customer)
session.commit()

new_address = Address(post_code="000000",customer=new_customer)
session.add(new_address)
session.commit()