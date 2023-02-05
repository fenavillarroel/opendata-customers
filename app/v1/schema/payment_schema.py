from pydantic import BaseModel
from pydantic import Field
from datetime import date
from app.v1.schema.invoice_schema import Invoice

class PaymentBase(BaseModel):
    invoice_id: Invoice
    payment_date: date
    amount: int
    comments: str

class Payment(PaymentBase):
    id: int = Field(
        ...,
        example=1000
    )

class PaymentCreate(BaseModel):
    invoice_id: int
    payment_date: date
    amount: int
    comments: str