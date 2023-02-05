from pydantic import BaseModel
from pydantic import Field


class TarifaBase(BaseModel):
    name: str = Field(
        ...,
    )

class Tarifa(TarifaBase):
    id: int = Field(
        ...,
        example="5"
    )
