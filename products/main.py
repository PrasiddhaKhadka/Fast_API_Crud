from fastapi import FastAPI, HTTPException
from fastapi.params import Depends
from fastapi import status
from sqlalchemy.orm import Session
from products.schemas import Product,DisplayProduct
from products.database import engine, SessionLocal
from . import models
import uuid

app = FastAPI()


models.Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



@app.get('/products')
async def get_products(db: Session = Depends(get_db)):
    db_products = db.query(models.Product).all()
    return {'message': 'List of Products', 'products': db_products}


@app.get('/products/{product_id}',response_model=DisplayProduct)
async def get_product(product_id: uuid.UUID , db: Session = Depends(get_db)):
    db_single_product =db.query(models.Product).filter(models.Product.id == product_id).first()
    if not db_single_product:
        raise HTTPException(status_code=404, detail="Product not found")
    return {'message': 'Single Product', 'product': db_single_product}

@app.delete('/products/{product_id}')
async def delete_product(product_id: uuid.UUID ,db: Session = Depends(get_db)):
    db.query(models.Product).filter(models.Product.id == product_id).delete()
    db.commit()
    return {'message': 'Product deleted'}



@app.post('/products',status_code=status.HTTP_201_CREATED)
async def create_product(product_req: Product,db: Session = Depends(get_db)):
    new_product = models.Product(id=uuid.uuid4(),name=product_req.name,desc=product_req.desc,price=product_req.price)
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return {'message': 'Product created', 'product': new_product}


@app.put('/products/{product_id}')
async def put_product(product_id: uuid.UUID,product_req: Product,db: Session = Depends(get_db)):
    updated_product=  db.query(models.Product).filter(models.Product.id == product_id).first()
    if not updated_product:
        return {'message': 'Product not found'}
    updated_product.update(product_req.dict())
    db.commit()
    return {'message': 'Product updated', 'product': updated_product}
