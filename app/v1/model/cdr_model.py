import peewee

from app.v1.utils.db import db

class Cdr(peewee.Model):
  accountcode = peewee.CharField()
  ani = peewee.CharField()
  destino = peewee.CharField()
  inicio = peewee.DateTimeField()
  answer = peewee.DateTimeField()
  fin = peewee.DateTimeField()
  duration = peewee.IntegerField()
  billsec = peewee.IntegerField()
  disposicion = peewee.CharField()
  descripcion = peewee.CharField()
  rate_clte = peewee.DecimalField()
  valor_llamada = peewee.DecimalField()
  rate_costo = peewee.DecimalField()
  costo_llamada = peewee.DecimalField()
  carrier = peewee.CharField()
  q850 = peewee.IntegerField()
  direccion = peewee.CharField()
  tipo = peewee.IntegerField()

  class Meta:
    database = db