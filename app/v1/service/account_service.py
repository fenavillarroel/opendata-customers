from app.v1.model.account_model import Accounts
from app.v1.model.tarifa_model import Tarifas
from app.v1.schema.accounts_schema import Account, AccountCreate, UpdateAccount
from app.v1.utils.settings import Settings
from fastapi import HTTPException, status
from app.v1.schema.tarifa_schema import Tarifa
from playhouse.shortcuts import model_to_dict

settings = Settings()

PER_PAGE = settings.per_page

def get_all_accounts(page: int):
    accounts = Accounts.select().order_by(Accounts.name).paginate(page, PER_PAGE)
    list_accounts = []
    for account in accounts:
        list_accounts.append(
            Account(
                id = account.id,
                name = account.name,
                cash = account.cash,
                warn_limit = account.warn_limit,
                nobal_limit = account.nobal_limit,
                rut = account.rut,
                type_customer = account.type_customer,
                id_tarifa = model_to_dict(account.id_tarifa)
            )
        )
    return list_accounts

def get_account(account_id: int):
    account = Accounts.filter(Accounts.id == account_id).first()

    if not account:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Account Not Found"
        )
    return Account(
                id = account.id,
                name = account.name,
                cash = account.cash,
                warn_limit = account.warn_limit,
                nobal_limit = account.nobal_limit,
                rut = account.rut,
                type_customer = account.type_customer,
                id_tarifa = model_to_dict(account.id_tarifa)
            )

def create_account(account: AccountCreate):
    tarifa = Tarifas.filter(Tarifas.id == account.id_tarifa).first()
    if not tarifa:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Tarif Not Found"
        )

    db_account = Accounts(
        name=account.name,
        cash=account.cash,
        warn_limit=account.warn_limit,
        nobal_limit=account.nobal_limit,
        rut=account.rut,
        type_customer = account.type_customer,
        id_tarifa=account.id_tarifa
    )

    db_account.save()

    return Account(
        id = db_account.id,
        name = db_account.name,
        cash = db_account.cash,
        warn_limit = db_account.warn_limit,
        nobal_limit = db_account.nobal_limit,
        rut = db_account.rut,
        type_customer = db_account.type_customer,
        id_tarifa = model_to_dict(db_account.id_tarifa)
    )

def update_acc(account_id: int, account: UpdateAccount):
    if account.id_tarifa:
        tarifa = Tarifas.filter(Tarifas.id == account.id_tarifa).first()

        if not tarifa:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Error Tarif Not Found"
            )
        db_account.id_tarifa = account.id_tarifa

    db_account = Accounts.filter(Accounts.id == account_id).first()
    if not db_account:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Error Account Not Found"
        )
    if account.name:
        db_account.name = account.name
    if account.rut:
        db_account.rut = account.rut
    if account.type_customer == 0 or account.type_customer:
        db_account.type_customer = account.type_customer
    if account.cash == 0 or account.cash:
        db_account.cash = account.cash
    if account.warn_limit == 0 or account.warn_limit:
        db_account.warn_limit = account.warn_limit
    if account.nobal_limit == 0 or account.nobal_limit:
        db_account.nobal_limit = account.nobal_limit


    db_account.save()

    return Account(
        id = db_account.id,
        name = db_account.name,
        cash = db_account.cash,
        warn_limit = db_account.warn_limit,
        nobal_limit = db_account.nobal_limit,
        rut = db_account.rut,
        type_customer = db_account.type_customer,
        id_tarifa = model_to_dict(db_account.id_tarifa)
    )