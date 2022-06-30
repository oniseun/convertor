import logging

from brotli_asgi import BrotliMiddleware
from fastapi.applications import FastAPI
from starlette.middleware.cors import CORSMiddleware

from boilerplate.routers import root

log = logging.getLogger("simple_example")


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
    app.include_router(root.router, prefix="/root")
    return app
