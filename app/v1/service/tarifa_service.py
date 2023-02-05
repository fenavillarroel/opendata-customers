from app.v1.model.tarifa_model import Tarifas
from app.v1.schema.tarifa_schema import Tarifa, TarifaBase
from app.v1.utils.settings import Settings
from fastapi import HTTPException, status

settings = Settings()

PER_PAGE = settings.per_page

def get_all_tarifs(page: int):
    tarifas = Tarifas.select().order_by(Tarifas.name).paginate(page, PER_PAGE).dicts()
    list_tarifas = []
    for tarifa in tarifas:
        list_tarifas.append(
            Tarifa(
                id = tarifa['id'],
                name = tarifa['name']
            )
        )
    return list_tarifas

def get_tarif(tarif_id: int):
    tarifa = Tarifas.filter(Tarifas.id == tarif_id).first()
    if not tarifa:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Tarif Not Found"
        )
    return Tarifa(
        id = tarifa.id,
        name = tarifa.name
    )

def create_tarif(tarifa: TarifaBase):
    db_tarifa = Tarifas(
        name=tarifa.name
    )

    db_tarifa.save()

    return Tarifa(
        id = db_tarifa.id,
        name = db_tarifa.name
    )

def update_tarif(tarif_id: int, tarifa: TarifaBase):

    db_tarifa = Tarifas.filter(Tarifas.id == tarif_id).first()

    if not tarifa:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Tarif Not Found"
        )

    db_tarifa.name = tarifa.name
    
    db_tarifa.save()

    return Tarifa(
        id = db_tarifa.id,
        name = db_tarifa.name
    )