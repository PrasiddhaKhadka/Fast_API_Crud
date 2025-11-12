from sqlalchemy import Column, String, Uuid, Text, DECIMAL, ForeignKey
from sqlalchemy.orm import relationship
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
    seller_id = Column(Uuid,ForeignKey('sellers.id'),nullable=False)
    seller = relationship("Seller", back_populates="products")


class Seller(Base):
    __tablename__ = 'sellers'
    def __init__(self, id, name, password):
        self.id = id
        self.name = name
        self.password = password
   

    id = Column(Uuid, primary_key=True,index= True)
    name = Column(String(255),nullable=False)
    password = Column(String(255),nullable=False)
    products = relationship("Product", back_populates="seller")


class Login(Base):
    __tablename__ = 'login'
    def __init__(self, id, name, password):
        self.id = id
        self.name = name
        self.password = password

    
    id = Column(Uuid, primary_key=True,index= True)
    name = Column(String(255),nullable=False)
    password = Column(String(255),nullable=False)