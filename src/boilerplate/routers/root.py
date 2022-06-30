import logging
from typing import Mapping

from fastapi import APIRouter

log = logging.getLogger("simple_example")

router = APIRouter(
    tags=["root"],
    responses={404: {"description": "No data found."}},
)


@router.get("/")
async def root() -> Mapping[str, str]:
    return {"message": "Welcome to the Boilerplate Service API"}
