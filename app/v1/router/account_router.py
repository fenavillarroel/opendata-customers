from fastapi import APIRouter, Depends, Path, Body
from fastapi import status


from app.v1.schema.accounts_schema import Account, UpdateAccount,AccountCreate
from app.v1.service.account_service import get_all_accounts, get_account, create_account, update_acc
from typing import List
from app.v1.schema.user_schema import User
from app.v1.service.auth_service import get_current_user

from app.v1.utils.db import get_db


router = APIRouter(
    prefix="/api/v1",
    tags=["accounts"]
)

@router.get(
    "/accounts",
    status_code=status.HTTP_200_OK,
    response_model=List[Account],
    dependencies=[Depends(get_db)],
    description="Get a list of all Accounts"
)

def show_accounts(page: int = 1,
    current_user: User = Depends(get_current_user)):
    get_accounts = get_all_accounts(page)
    return get_accounts

@router.get(
    "/accounts/{account_id}",
    status_code=status.HTTP_200_OK,
    response_model=Account,
    dependencies=[Depends(get_db)],
    description="Get single Account"
)
def show_account(account_id: int = Path(...),
    current_user: User = Depends(get_current_user)):
    return get_account(account_id)
    
@router.post(
    "/accounts",
    status_code=status.HTTP_200_OK,
    response_model=Account,
    dependencies=[Depends(get_db)],
    description="Create Account"
)
def create(account: AccountCreate = Body(...),
    current_user: User = Depends(get_current_user)):
    return create_account(account)

@router.put(
    "/accounts/{account_id}",
    status_code=status.HTTP_200_OK,
    response_model=Account,
    dependencies=[Depends(get_db)],
    description="Update single Account"
)
def update_account(account_id: int = Path(...),
    account: UpdateAccount = Body(...),
    current_user: User = Depends(get_current_user)):
    return update_acc(account_id, account)
    