from sqlalchemy import Column, String, Uuid, Text, DECIMAL
from .database import Base

class Product(Base):
    __tablename__ = 'products'
    def __init__(self, id, name, desc, price):
        self.id = id
        self.name = name
        self.desc = desc
        self.price = price
    
    id = Column(Uuid, primary_key=True,index= True)
    name = Column(String(255),nullable=False)
    desc = Column(Text)
    price = Column(DECIMAL(10,2))



