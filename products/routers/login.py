from fastapi import APIRouter,status, HTTPException
from products.schemas import Login
from products.database import get_db
from sqlalchemy.orm import Session
from fastapi.params import Depends
from passlib.context import CryptContext
from .. import models


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


router = APIRouter(
    prefix="/login",
    tags=["Login"],
    responses={404: {"description": "Not found"}},
)


@router.post('/')
async def login(request: Login, db: Session = Depends(get_db)):
    seller = db.query(models.Seller).filter(models.Seller.name == request.name).first()
    if not seller:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    if not pwd_context.verify(request.password, seller.password):
        return HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect password")
    # GENERATE JWT TOKEN:
    return {'message': 'Login successful', 'user': seller}

