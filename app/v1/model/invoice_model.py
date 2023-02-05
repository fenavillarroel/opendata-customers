import peewee

from app.v1.utils.db import db
from .account_model import Accounts

class Invoices(peewee.Model):
  invoice_number = peewee.IntegerField()
  date_emited = peewee.DateField()
  net_amount = peewee.IntegerField()
  tax_rate = peewee.DecimalField(4,2)
  tax = peewee.IntegerField()
  total_amount = peewee.IntegerField()
  account_id = peewee.ForeignKeyField(Accounts, related_name='account_details', column_name='account_id')

  class Meta:
    database = db