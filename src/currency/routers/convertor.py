import logging
from typing import Mapping, Any

import requests
from fastapi import APIRouter
from pydantic import BaseModel

log = logging.getLogger("simple_example")

router = APIRouter(
    tags=["convertor"],
    responses={404: {"description": "No currency data found, sorry!"}},
)


@router.get("/")
async def root() -> Mapping[str, str]:
    return {"message": "Welcome to the Currency Convertor API"}


class CurrencyRequest(BaseModel):
    init_currency: str
    target_currency: str
    amount: float


class CurrencyResponse(BaseModel):
    target_amount: Any


@router.post("/convert", response_model=CurrencyResponse)
async def convert(
        currency_request: CurrencyRequest
) -> CurrencyResponse:
    amount = None
    while True:
        try:
            amount = currency_request.amount
        except:
            print('The amount must be a numeric value!')
            continue

        if not amount > 0:
            print('The amount must be greater than 0')
            continue
        else:
            break

    url = ('https://api.apilayer.com/fixer/convert?to='+ currency_request.target_currency + '&from=' + currency_request.init_currency +'&amount=' + str(amount))

    payload = {}
    headers = {'apikey': 'YOUR-API-KEY'}
    response = requests.request('GET', url, headers=headers, data=payload)
    status_code = response.status_code

    if status_code != 200:
        print('Uh oh, there was a problem. Please try again later')
        raise Exception("Something went wrong")

    result = response.json()
    return CurrencyResponse(target_amount=result['result'])
