from pydantic import BaseModel
from uuid import UUID

class Product(BaseModel):
    id: UUID
    name: str
    desc: str
    price: float


class DisplayProduct(BaseModel):
    name: str
    desc: str
    price: float