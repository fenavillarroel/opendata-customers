from fastapi import APIRouter, Depends, Path, Body
from fastapi import status


from app.v1.schema.invoice_schema import Invoice, InvoiceCreate
from app.v1.service.invoice_service import get_all_invoices, get_invoice, create_invoice
from typing import List
from app.v1.schema.user_schema import User
from app.v1.service.auth_service import get_current_user

from app.v1.utils.db import get_db


router = APIRouter(
    prefix="/api/v1",
    tags=["invoices"]
)

@router.get(
    "/invoices",
    status_code=status.HTTP_200_OK,
    response_model=List[Invoice],
    dependencies=[Depends(get_db)],
    description="Get a list of all Invoices"
)

def show_invoices(page: int = 1,
    current_user: User = Depends(get_current_user)):
    return  get_all_invoices(page)

@router.get(
    "/invoices/{invoice_id}",
    status_code=status.HTTP_200_OK,
    response_model=Invoice,
    dependencies=[Depends(get_db)],
    description="Get single Invoice"
)
def show_invoice(invoice_id: int = Path(...),
    current_user: User = Depends(get_current_user)):
    return get_invoice(invoice_id)

@router.post(
    "/invoices",
    status_code=status.HTTP_200_OK,
    response_model=Invoice,
    dependencies=[Depends(get_db)],
    description="Create Invoice"
)
def create(invoice: InvoiceCreate = Body(...),
    current_user: User = Depends(get_current_user)):
    return create_invoice(invoice)
