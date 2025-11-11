from fastapi import FastAPI
from products.schemas import Product

app = FastAPI()


@app.api_route('/products', methods=['GET','POST'])
async def products(products: Product | None = None):
    if products:
        return {'message': 'Product created'}
    else:
        return {'message': 'List of Products'}
    