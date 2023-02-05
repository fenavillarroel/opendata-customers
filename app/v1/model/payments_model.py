import peewee

from app.v1.utils.db import db
from .invoice_model import Invoices

class Payments(peewee.Model):
  invoice_id = peewee.ForeignKeyField(Invoices, related_name='payment_details', column_name='invoice_id')
  payment_date = peewee.DateField(constraints=[peewee.SQL('DEFAULT CURRENT_DATE')])
  amount = peewee.IntegerField()
  comments = peewee.CharField()
  
  class Meta:
    database = db