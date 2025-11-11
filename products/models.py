from sqlalchemy import Column, Integer, String, Uuid
from .database import Base

class Product(Base):
    __tablename__ = 'products'
    def __init__(self, id, name, desc, price):
        self.id = id
        self.name = name
        self.desc = desc
        self.price = price
    
    id = Column(Uuid, primary_key=True,index= True)
    name = Column(String)
    desc = Column(String)
    price = Column(Integer)



