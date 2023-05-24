
from pydantic import BaseModel
from typing import  Any

class CurrencyResponse(BaseModel):
    target_amount: float