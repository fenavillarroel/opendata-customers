import peewee

from app.v1.utils.db import db
from .tarifa_model import Tarifas

class Accounts(peewee.Model):
  name = peewee.CharField(unique=True, index=True)
  cash = peewee.DoubleField()
  warn_limit = peewee.DoubleField(default=0)
  nobal_limit = peewee.DoubleField(default=0)
  rut = peewee.CharField()
  type_customer = peewee.IntegerField(default=0)
  id_tarifa = peewee.ForeignKeyField(Tarifas, related_name='tariff_details', column_name='id_tarifa')

  class Meta:
    database = db