from fastapi import APIRouter


router = APIRouter(
    prefix="/sellers",
    tags=["Sellers"],
    responses={404: {"description": "Not found"}},
)