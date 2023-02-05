from app.v1.model.payments_model import Payments
from app.v1.model.invoice_model import Invoices
from app.v1.schema.payment_schema import Payment, PaymentCreate
from app.v1.utils.settings import Settings
from fastapi import HTTPException, status
from playhouse.shortcuts import model_to_dict

settings = Settings()

PER_PAGE = settings.per_page

def get_all_payments(page: int):
    pays = Payments.select().paginate(page, PER_PAGE)
    list_payments = []
    for pay in pays:
        list_payments.append(
            Payment(
                id = pay.id,
                invoice_id = model_to_dict(pay.invoice_id),
                payment_date = pay.payment_date,
                amount = pay.amount,
                comments = pay.comments
            )
        )
    return list_payments

def get_payment(payment_id: int):
    pay = Payments.filter(Payments.id == payment_id).first()

    if not pay:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Payment Not Found"
        )
    return Payment(
                id = pay.id,
                invoice_id = model_to_dict(pay.invoice_id),
                payment_date = pay.payment_date,
                amount = pay.amount,
                comments = pay.comments
            )

def create_payment(payment: PaymentCreate):
    invoice = Invoices.filter(Invoices.id == payment.invoice_id).first()
    if not invoice:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Invoice Not Found"
        )

    db_payment = Payments(
        invoice_id = payment.invoice_id,
        payment_date = payment.payment_date,
        amount = payment.amount,
        comments = payment.comments
    )

    db_payment.save()

    return Payment(
                id = db_payment.id,
                invoice_id = model_to_dict(db_payment.invoice_id),
                payment_date = db_payment.payment_date,
                amount = db_payment.amount,
                comments = db_payment.comments
            )
