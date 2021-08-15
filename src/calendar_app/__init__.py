# __init__.py
# Ian Kollipara
# 2021.08.09
# Calendar App Package Init File

# Imports
from typing import List
from fastapi import FastAPI, APIRouter
from fastapi.staticfiles import StaticFiles

# Routers
from .router import router

ROUTERS: List[APIRouter] = [router]


def fast_api_factory() -> FastAPI:
    app = FastAPI()

    app.mount("/static", StaticFiles(directory="static"), name="static")

    for router in ROUTERS:
        app.include_router(router)

    return app
