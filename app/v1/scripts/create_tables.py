from app.v1.model.user_model import User
from app.v1.model.account_model import Accounts
from app.v1.model.cdr_model import Cdr
from app.v1.model.invoice_model import Invoice
from app.v1.model.payments_model import Payments
from app.v1.model.tarifa_model import Tarifas

from app.v1.utils.db import db

def create_tables():
    with db:
        db.create_tables([User, Accounts, Cdr, Invoice,
            Payments, Tarifas])