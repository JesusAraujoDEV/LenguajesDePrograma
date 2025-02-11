from fastapi import APIRouter, HTTPException, status
from models import Invoice

router = APIRouter()

@router.post("/invoices", tags=["Invoice"])
async def create_invoices(invoice_data: Invoice):
    return invoice_data