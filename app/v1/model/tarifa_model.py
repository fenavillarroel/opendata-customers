import peewee

from app.v1.utils.db import db

class Tarifas(peewee.Model):
  name = peewee.CharField(unique=True, index=True)

  class Meta:
    database = db