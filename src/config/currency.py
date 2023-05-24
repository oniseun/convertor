import os

API_ENDPOINT= os.getenv('CURRENCY_API_ENDPOINT') or "https://api.apilayer.com/currency_data/convert"
API_KEY = os.getenv('CURRENCY_API_KEY') or "xxxxxx"
CACHE_TTL = os.getenv('CACHE_TTL') or 3600
CACHE_FILENAME = os.getenv('CACHE_FILENAME') or os.getcwd() + '/src/currency/currency.cache'