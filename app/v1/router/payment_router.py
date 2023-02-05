from fastapi import APIRouter, Depends, Path, Body
from fastapi import status


from app.v1.schema.payment_schema import Payment, PaymentCreate
from app.v1.service.payment_service import get_all_payments, get_payment, create_payment
from typing import List
from app.v1.schema.user_schema import User
from app.v1.service.auth_service import get_current_user

from app.v1.utils.db import get_db


router = APIRouter(
    prefix="/api/v1",
    tags=["payments"]
)

@router.get(
    "/payments",
    status_code=status.HTTP_200_OK,
    response_model=List[Payment],
    dependencies=[Depends(get_db)],
    description="Get a list of all Payments"
)

def show_payments(page: int = 1,
    current_user: User = Depends(get_current_user)):
    return  get_all_payments(page)

@router.get(
    "/payments/{payment_id}",
    status_code=status.HTTP_200_OK,
    response_model=Payment,
    dependencies=[Depends(get_db)],
    description="Get single Invoice"
)
def show_invoice(payment_id: int = Path(...),
    current_user: User = Depends(get_current_user)):
    return get_payment(payment_id)

@router.post(
    "/payments",
    status_code=status.HTTP_200_OK,
    response_model=Payment,
    dependencies=[Depends(get_db)],
    description="Create Payment"
)
def create(payment: PaymentCreate = Body(...),
    current_user: User = Depends(get_current_user)):
    return create_payment(payment)