from app.v1.model.cdr_model import Cdr
from app.v1.schema.cdr_schema import CdrBase
from app.v1.utils.settings import Settings
from app.v1.schema.user_schema import User
from datetime import datetime

settings = Settings()

PER_PAGE = settings.per_page

def get_all_cdrs(page: int, from_date: str, to_date: str, user_id: int = None):
    if user_id:
        cdrs = Cdr.select().where((Cdr.inicio >= from_date) & (Cdr.inicio <= to_date) & (Cdr.accountcode == str(user_id))).order_by(Cdr.id.desc()).paginate(page, PER_PAGE).dicts()
    else:
        cdrs = Cdr.select().where((Cdr.inicio >= from_date) & (Cdr.inicio <= to_date)).order_by(Cdr.id.desc()).paginate(page, PER_PAGE).dicts()
    list_cdrs = []
    for cdr in cdrs:
        list_cdrs.append(
            CdrBase(
                id = cdr['id'],
                accountcode = cdr['accountcode'],
                ani = cdr['ani'],
                inicio = cdr['inicio'],
                answer = cdr['answer'],
                fin = cdr['fin'],
                duration = cdr['duration'],
                billsec = cdr['billsec'],
                disposicion = cdr['disposicion'],
                descripcion = cdr['descripcion'],
                rate_clte = cdr['rate_clte'],
                valor_llamada = cdr['valor_llamada'],
                rate_costo = cdr['rate_costo'],
                costo_llamada = cdr['costo_llamada'],
                carrier = cdr['carrier'],
                q850 = cdr['q850'],
                direccion = cdr['direccion'],
                tipo = cdr['tipo']

            )
        )
    return list_cdrs
