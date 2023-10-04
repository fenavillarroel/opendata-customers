from pydantic import BaseModel
from datetime import datetime, date
from typing import Optional

class CdrBase(BaseModel):
    id: int
    accountcode: str
    ani: str
    destino: str
    inicio: datetime
    answer: Optional[datetime]
    fin: Optional[datetime]
    duration: int
    billsec: int
    disposicion: str
    descripcion: str
    rate_clte: float
    valor_llamada: float
    rate_costo: float
    costo_llamada: float
    carrier: str
    q850: int
    direccion: str
    tipo: int