from fastapi import APIRouter, HTTPException, status
from models import Transaction

router = APIRouter()

@router.post("/transactions", tags=["Transactions"])
async def create_transactions(transaction_data: Transaction):
    return transaction_data