from fastapi import APIRouter, Depends, Path, Body
from fastapi import status
from datetime import datetime

from app.v1.schema.cdr_schema import CdrBase
from app.v1.service.cdr_service import get_all_cdrs
from typing import List
from app.v1.schema.user_schema import User
from app.v1.service.auth_service import get_current_user

from app.v1.utils.db import get_db


router = APIRouter(
    prefix="/api/v1",
    tags=["cdrs"]
)

@router.get(
    "/cdrs",
    status_code=status.HTTP_200_OK,
    response_model=List[CdrBase],
    dependencies=[Depends(get_db)],
    description="Get all calls from cdr"
)

def show_cdrs(page: int = 1,
    from_date: str = datetime.now().strftime("%Y-%m-%d 00:00:00"),
    to_date: str = datetime.now().strftime("%Y-%m-%d 23:59:59"),
    user_id: int = None,
    current_user: User = Depends(get_current_user)):
    return get_all_cdrs(page, from_date, to_date, user_id)
