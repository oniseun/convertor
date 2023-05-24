from brotli_asgi import BrotliMiddleware
from fastapi.applications import FastAPI
from starlette.middleware.cors import CORSMiddleware

from currency.currencyController import CurrencyController


def get_app() -> FastAPI:
    app = FastAPI(
        title="A sample application using fastapi_router_controller", version="0.1.0"
    )
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    app.add_middleware(BrotliMiddleware)
    
    app.include_router(CurrencyController.router(), prefix="/currency")
    return app
