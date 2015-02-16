from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('postgresql://action:action@localhost:5432/tbaytest')
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship

class Item(Base):
	__tablename__ = "items"
	
	id = Column(Integer, primary_key=True)
	name = Column(String, nullable=False)
	description = Column(String)
	start_time = Column(DateTime, default=datetime.utcnow)
	
	user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
	
class User(Base):
	__tablename__ = "user"
	
	id = Column(Integer, primary_key=True)
	username = Column(String, nullable=False)
	password = Column(String, nullable=False)
	
	items = relationship("Item", backref="Item")
	bids = relationship("Bid", backref="Bid")
	
class Bid(Base):
	__tablename__ = "bids"
	
	id = Column(Integer, primary_key=True)
	price = Column (Integer, nullable=False)
	
	user_id = Column (Integer, ForeignKey('user.id'), nullable=False)
	
Base.metadata.create_all(engine)
