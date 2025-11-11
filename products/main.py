from fastapi import FastAPI
from products.schemas import Product
from products.database import engine
from . import models


app = FastAPI()


models.Base.metadata.create_all(bind=engine)



@app.get('/products')
async def get_products():
    return {'message': 'List of Products'}

@app.post('/products')
async def create_product(product: Product):
    return {'message': 'Product created'}
