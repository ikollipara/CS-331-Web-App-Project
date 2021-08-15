# router.py
# Ian Kollipara
# 2021.08.09
# Root Router

# Imports
from fastapi import APIRouter, Depends, Request, Form
from fastapi.param_functions import Query
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

# Dependency Imports
from .services import HolidayService
from .dependencies import get_template

router = APIRouter()


@router.get("/", response_class=HTMLResponse)
def index(
    request: Request,
    template: Jinja2Templates = Depends(get_template),
):
    """Index Page Controller.

    Return the index.html file
    from the templates folder.
    This is the home page.
    """

    return template.TemplateResponse("index.html", {"request": request})


@router.get("/today", response_class=HTMLResponse)
def today(
    request: Request,
    holiday_service: HolidayService = Depends(HolidayService),
    template: Jinja2Templates = Depends(get_template),
):

    """Today Page Controller.

    Return the today.html file from the templates
    folder. This is the today page. Uses HolidayService
    as a dependency that is provided through Dependency
    Injection (DI).
    """

    # Notice the call to holiday_service.
    return template.TemplateResponse(
        "today.html", {"request": request, "holidays": holiday_service.get_today()}
    )


@router.get("/results", response_class=HTMLResponse)
def results(
    request: Request,
    template: Jinja2Templates = Depends(get_template),
    holiday_service: HolidayService = Depends(HolidayService),
    search_date: str = Query(""),
):
    return template.TemplateResponse(
        "results.html",
        {"request": request, "holidays": holiday_service.get_by_date(search_date)},
    )


@router.get("/search", response_class=HTMLResponse)
def search(
    request: Request,
    template: Jinja2Templates = Depends(get_template),
):
    return template.TemplateResponse("search.html", {"request": request})
