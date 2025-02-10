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

@router.get("/customers/{id_customer}", response_model=Customer, tags=["Customers"])
async def get_customer(id_customer: int, session: SessionDep):
    try:
        # customer = session.exec(select(Customer).where(Customer.id == id_customer)).first()
        customer = session.get(Customer, id_customer)
        if customer is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Customer not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    return customer

@router.delete("/customers/{id_customer}", tags=["Customers"])
async def delete_customer(id_customer: int, session: SessionDep):
    try:
        # customer = session.exec(select(Customer).where(Customer.id == id_customer)).first()
        customer = session.get(Customer, id_customer)
        if customer is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Customer not found")
        session.delete(customer)
        session.commit()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    return {"detail": "ok"}
