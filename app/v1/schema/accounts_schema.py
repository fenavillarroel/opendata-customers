from pydantic import BaseModel
from pydantic import Field
from typing import Optional, Any, List
from app.v1.schema.tarifa_schema import Tarifa


class AccountBase(BaseModel):
    name: str = Field(...)
    cash: int = Field(...)
    warn_limit: int = Field(...)
    nobal_limit: int = Field(...)
    rut: Optional[str]
    type_customer: int
    id_tarifa: Tarifa

class AccountCreate(BaseModel):
    name: str = Field(...)
    cash: int = Field(...)
    warn_limit: int = Field(...)
    nobal_limit: int = Field(...)
    rut: Optional[str]
    type_customer: Optional[int]
    id_tarifa: int

class Account(AccountBase):
    id: int = Field(
        ...,
        example=1000
    )


class UpdateAccount(BaseModel):
    name: Optional[str] = None
    cash: Optional[int] = None
    warn_limit: Optional[int] = None
    nobal_limit: Optional[int] = None
    rut: Optional[str] = None
    type_customer: Optional[int] = None
    id_tarifa: Optional[int] = None




