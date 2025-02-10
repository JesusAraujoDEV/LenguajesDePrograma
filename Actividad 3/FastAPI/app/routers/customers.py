from fastapi import APIRouter, HTTPException, status
from sqlmodel import select
from models import Customer, CustomerCreate, CustomerUpdate
from db import SessionDep

router = APIRouter()

@router.post("/customers", response_model=Customer, tags=["Customers"])
async def create_customer(customer_data: CustomerCreate, session: SessionDep):
    customer = Customer.model_validate(customer_data.model_dump())
    session.add(customer)
    session.commit()
    session.refresh(customer)
    return customer

@router.get("/customers", response_model=list[Customer], tags=["Customers"])
async def list_customer(session: SessionDep):
    return session.exec(select(Customer)).all()
