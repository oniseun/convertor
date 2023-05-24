# Currency Convertor
This is an API to convert currencies.

## Installation & Setup

Minimum requirements
* [Poetry](https://python-poetry.org)
* Python 3.9.13
* Sign up and get an api key from https://apilayer.com/marketplace/fixer-api

First run
```sh
poetry install
```
this should create a new virtual environment located in `.venv` or `venv` directory
(depending on how poetry config is set up).
## Run the service locally
```sh
poetry run python -m currency
```

## Run the service with docker
```sh
EXPORT CURRENCY_API_KEY=your-api-key
docker-compose up
```

## Objectives
* To improve this service however you see fit.
* This should be timeboxed to around 1-2 hours.
* Poetry is not a hard requirement, pip or conda would suffice.
* Example request body
```json
{
  "init_currency": "GBP",
  "target_currency": "EUR",
  "amount": 10.0
}
```
* The docs can be accessed through `http://localhost:9898/docs`

