
from requests.models import PreparedRequest
import requests
import logging
import simple_cache
from .dto.currency import Currency
from requests.exceptions import HTTPError
log = logging.getLogger("CurrencyService")




class CurrencyService:
    def __init__(self,  api_endpoint: str, api_key: str, cache_filename: str, cache_ttl: int):
        self.api_key = api_key
        self.api_endpoint = api_endpoint
        self.cache_filename = cache_filename
        self.cache_ttl = cache_ttl

    async def convert(self, amount: int, init_currency: Currency, target_currency: Currency) -> float:

            excp_msg = None
            if not isinstance(amount, int):
                excp_msg = 'The amount must be a numeric value!'
            elif amount <= 0:
                excp_msg = 'The amount must be greater than zero'

            
            if excp_msg != None:
                log.error(excp_msg)
                raise Exception(excp_msg)

            CACHE_KEY = str(init_currency) + str(target_currency) + str(amount)
            
            result = simple_cache.load_key(self.cache_filename, CACHE_KEY)
            if result:
                log.info('Found in cache !' + target_currency.value + '  rates for ' + init_currency.value + ' ' + str(amount) )
                return result

            try:
                # If the response was successful, no Exception will be raised
                params = {'to': target_currency.value,'from': init_currency.value, 'amount': amount}
                headers = {'apikey': self.api_key}
                response = requests.get(self.api_endpoint, params, headers=headers)
                response.raise_for_status() 
                log.info('Successfully fetched from server !' + target_currency.value + ' rates for ' + init_currency.value + ' ' + str(amount) )
                result = response.json()['result']
                simple_cache.save_key(self.cache_filename, CACHE_KEY, result, self.cache_ttl)
                return result

            except HTTPError as http_err:
                    log.error(f'HTTP error occurred: {http_err}') 
            except Exception as err:
                    log.error(f'Other error occurred: {err}')

               
