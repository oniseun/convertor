import logging

from brotli_asgi import BrotliMiddleware
from fastapi.applications import FastAPI
from starlette.middleware.cors import CORSMiddleware

from currency.routers import convertor

log = logging.getLogger("currency_convertor")


def get_app() -> FastAPI:
    app = FastAPI()
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    app.add_middleware(BrotliMiddleware)
    app.include_router(convertor.router, prefix="/currency")
    return app
