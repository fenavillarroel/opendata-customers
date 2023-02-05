from fastapi import APIRouter, Depends, Path, Body
from fastapi import status


from app.v1.schema.tarifa_schema import Tarifa, TarifaBase
from app.v1.service.tarifa_service import get_all_tarifs, get_tarif, create_tarif, update_tarif
from typing import List
from app.v1.schema.user_schema import User
from app.v1.service.auth_service import get_current_user

from app.v1.utils.db import get_db


router = APIRouter(
    prefix="/api/v1",
    tags=["tarifas"]
)

@router.get(
    "/tarifas",
    status_code=status.HTTP_200_OK,
    response_model=List[Tarifa],
    dependencies=[Depends(get_db)],
    description="Get a list  of all Tarifs"
)

def show_tarifas(page: int = 1,
    current_user: User = Depends(get_current_user)):
    alls = get_all_tarifs(page)
    return alls

@router.get(
    "/tarifas/{tarifa_id}",
    status_code=status.HTTP_200_OK,
    response_model=Tarifa,
    dependencies=[Depends(get_db)],
    description="Get single Tarifs"
)
def show_tarifa(tarifa_id: int = Path(...),
    current_user: User = Depends(get_current_user)):
    tarif = get_tarif(tarifa_id)
    return tarif

@router.post(
    "/tarifas",
    status_code=status.HTTP_200_OK,
    response_model=Tarifa,
    dependencies=[Depends(get_db)],
    description="Create tafif"
)
def create(tarifa: TarifaBase = Body(...),
    current_user: User = Depends(get_current_user)):
    tarif = create_tarif(tarifa)
    return tarif

@router.put(
    "/tarifas/{tarifa_id}",
    status_code=status.HTTP_200_OK,
    response_model=Tarifa,
    dependencies=[Depends(get_db)],
    description="Update single Tarifs"
)
def update_tarifa(tarifa_id: int = Path(...),
    tarifa: TarifaBase = Body(...),
    current_user: User = Depends(get_current_user)):
    tarif = update_tarif(tarifa_id, tarifa)
    return tarif