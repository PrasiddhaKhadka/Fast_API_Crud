from pydantic import BaseModel
from uuid import UUID

class Product(BaseModel):
    id: UUID
    name: str
    desc: str
    price: float
    seller_id: UUID



class DisplaySeller(BaseModel):
    name: str
    id: UUID

    class Config:
        orm_mode = True


class DisplayProduct(BaseModel):
    name: str
    desc: str
    price: float
    seller_id: DisplaySeller


class Seller(BaseModel):
    id: UUID
    name: str
    password: str


class Login(BaseModel):
    name: str
    password: str
    