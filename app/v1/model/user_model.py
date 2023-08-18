import peewee

from app.v1.utils.db import db
from .account_model import Accounts

class Users(peewee.Model):
  email = peewee.CharField(unique=True, index=True)
  username = peewee.CharField(unique=True, index=True)
  password = peewee.CharField()
  account_id = peewee.ForeignKeyField(Accounts, backref="accounts")

  class Meta:
    database = db

  def mini_serialize(self):
    d = dict()
    d['username'] = self.username
    d['password'] = self.password
    d['email'] = self.email
    d['account_id'] = self.account_id.id
    return d
