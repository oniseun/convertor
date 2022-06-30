# Model Service
This is a boilerplate REST microservice in Python.

## Installation & Setup

Minimum requirements
* [Poetry](https://python-poetry.org)
* Python 3.9+

First run
```sh
poetry install
```
this should create a new virtual environment located in `.venv` or `venv` directory
(depending on how poetry config is set up).
## Run the service locally
```sh
poetry run python -m boilerplate
```

To build and run the docker image, run the following
```sh
docker build -t boilerplate .
docker run boilerplate
```