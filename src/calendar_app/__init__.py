# __init__.py
# Ian Kollipara
# 2021.08.09
# Calendar App Package Init File

# Imports
from typing import List
from fastapi import FastAPI, APIRouter
from fastapi.staticfiles import StaticFiles

# Routers
from .router import api

def fast_api_factory() -> FastAPI:
    app = FastAPI()

    app.mount("/static", StaticFiles(directory="static"), name="static")
    app.mount("/api", api)
    app.mount("/", StaticFiles(directory="pages", html=True), name="pages")


    return app
