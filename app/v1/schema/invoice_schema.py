from pydantic import BaseModel
from pydantic import Field
from datetime import date
from app.v1.schema.accounts_schema import Account

class InvoiceBase(BaseModel):
    invoice_number: int
    date_emited: date
    net_amount: int
    tax_rate: float
    tax: int
    total_amount: int
    account_id: Account

class Invoice(InvoiceBase):
    id: int = Field(
        ...,
        example=1000
    )

class InvoiceCreate(BaseModel):
    invoice_number: int
    date_emited: date
    net_amount: int
    tax_rate: float
    tax: int
    total_amount: int
    account_id: int