from fastapi import FastAPI, HTTPException
from fastapi.params import Depends
from fastapi import status
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from products.schemas import Product,DisplayProduct, Seller
from products.database import engine, SessionLocal
from .database import get_db
from . import models
from . routers import product
import uuid

app = FastAPI(
    title="Products API",
    description="API for managing products",
    terms_of_service="http://google.com/",
    contact={
        "Developer name": "Prasiddha",
        "url": "https://prasiddhakhadka.com.np",
    },

    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0",     
    },
    docs_url="/docs",
    version="1.0.0"

)

app.include_router(product.router)

models.Base.metadata.create_all(bind=engine)

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")






# FOR SELLER
@app.get('/sellers',tags=['Sellers'])
async def get_sellers(db: Session = Depends(get_db)):
    db_sellers = db.query(models.Seller).all()
    return {'message': 'List of Sellers', 'sellers': db_sellers}


@app.post('/sellers',status_code=status.HTTP_201_CREATED,tags=['Sellers'])
async def create_seller(request: Seller ,db: Session = Depends(get_db)):
    hash_password = pwd_context.hash(request.password)
    new_seller = models.Seller(id=uuid.uuid4(),name=request.name,password=hash_password)
    db.add(new_seller)
    db.commit()
    db.refresh(new_seller)
    return {'message': 'Seller created', 'seller': new_seller}
