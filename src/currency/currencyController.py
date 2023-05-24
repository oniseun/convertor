
from config.currency import API_ENDPOINT, API_KEY, CACHE_TTL, CACHE_FILENAME
from .currencyService import CurrencyService
from .dto.currencyRequest import CurrencyRequest
from .dto.currencyResponse import CurrencyResponse
from fastapi_router_controller import Controller
from typing import Mapping, Any
from fastapi import APIRouter, FastAPI
import logging
log = logging.getLogger("CurrencyController")

router = APIRouter(
    tags=["CurrencyController"],
    responses={404: {"description": "No currency data found, sorry!"}},
)

controller = Controller(router)


@controller.resource()
class CurrencyController:

    dependencies = []
        
    @controller.route.get(
        "/", summary="Root Endpoint"
    )
    async def root(self) -> Mapping[str, str]:
        return {"message": "Welcome to the Currency Convertor API"}


    @controller.route.post(
        "/convert", summary="Convert a Currency", response_model=CurrencyResponse
    )
    async def convert(
            self, currency_request: CurrencyRequest
    ) -> CurrencyResponse:

        try:
            service = CurrencyService(API_ENDPOINT, API_KEY, CACHE_FILENAME, CACHE_TTL)
            response = await service.convert(currency_request.amount, currency_request.init_currency, currency_request.target_currency)
            log.info("CURRENCY FETCH SUCCESSFUL! " + str(response))
            return CurrencyResponse(target_amount=response)
        except:
            raise Exception("An Error Occured with your request, please try again!")
   