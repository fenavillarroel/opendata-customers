from app.v1.model.invoice_model import Invoices
from app.v1.model.account_model import Accounts
from app.v1.schema.invoice_schema import Invoice, InvoiceBase, InvoiceCreate
from app.v1.utils.settings import Settings
from fastapi import HTTPException, status
from playhouse.shortcuts import model_to_dict

settings = Settings()

PER_PAGE = settings.per_page

def get_all_invoices(page: int):
    invoices = Invoices.select().paginate(page, PER_PAGE)
    list_invoices = []
    for invoice in invoices:
        list_invoices.append(
            Invoice(
                id = invoice.id,
                invoice_number = invoice.invoice_number,
                date_emited = invoice.date_emited,
                net_amount = invoice.net_amount,
                tax_rate = invoice.tax_rate,
                tax = invoice.tax,
                total_amount = invoice.total_amount,
                account_id = model_to_dict(invoice.account_id)
            )
        )
    return list_invoices

def get_invoice(invoice_id: int):
    invoice = Invoices.filter(Invoices.id == invoice_id).first()

    if not invoice:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Invoice Not Found"
        )
    return Invoice(
                id = invoice.id,
                invoice_number = invoice.invoice_number,
                date_emited = invoice.date_emited,
                net_amount = invoice.net_amount,
                tax_rate = invoice.tax_rate,
                tax = invoice.tax,
                total_amount = invoice.total_amount,
                account_id = model_to_dict(invoice.account_id)
            )

def create_invoice(invoice: InvoiceCreate):
    account = Accounts.filter(Accounts.id == invoice.account_id).first()
    if not account:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Account Not Found"
        )

    db_invoice = Invoices(
        invoice_number = invoice.invoice_number,
        date_emited = invoice.date_emited,
        net_amount = invoice.net_amount,
        tax_rate = invoice.tax_rate,
        tax = invoice.tax,
        total_amount = invoice.total_amount,
        account_id = invoice.account_id
    )

    db_invoice.save()

    return Invoice(
        id = db_invoice.id,
        invoice_number = db_invoice.invoice_number,
        date_emited = db_invoice.date_emited,
        net_amount = db_invoice.net_amount,
        tax_rate = db_invoice.tax_rate,
        tax = db_invoice.tax,
        total_amount = db_invoice.total_amount,
        account_id = model_to_dict(db_invoice.account_id)
    )