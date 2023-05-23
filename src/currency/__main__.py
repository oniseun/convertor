import logging

import uvicorn

import currency
from currency.config import PORT
from currency.service import get_app

log = logging.getLogger("simple_example")


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
