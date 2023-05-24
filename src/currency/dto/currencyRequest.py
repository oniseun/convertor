
from pydantic import BaseModel
from .currency import Currency

class CurrencyRequest(BaseModel):
    init_currency: Currency
    target_currency: Currency
    amount: float