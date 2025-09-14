from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from . import schemas, crud
from .database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/customers/", response_model=schemas.CustomerOut)
def create_customer(customer: schemas.CustomerCreate, db: Session = Depends(get_db)):
    return crud.create_customer(db, customer)

@router.get("/customers/", response_model=list[schemas.CustomerOut])
def read_customers(db: Session = Depends(get_db)):
    return crud.get_customers(db)
