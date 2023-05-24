import logging

import uvicorn

import currency
from config.app import PORT
from main import get_app

logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger("convertor app")


def main(port: int = PORT) -> None:
    log.info(
        f"Starting service {currency.__version__ or '???'} on port {port}",
    )
    app = get_app()

    uvicorn.run(
        app,
        host="0.0.0.0",
        port=port,
        workers=1,
    )


if __name__ == "__main__":
    main()
