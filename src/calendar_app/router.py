# router.py
# Ian Kollipara
# 2021.08.09
# Root Router

# Imports
from fastapi import FastAPI, Depends
from fastapi.param_functions import Query
from fastapi.responses import JSONResponse

# Dependency Imports
from .services import HolidayService

api = FastAPI()


@api.get("/today", response_class=JSONResponse)
def today(
    holiday_service: HolidayService = Depends(HolidayService),
):

    """Today API Controller.

    Handles all access and parameters for the endpoint /api/today
    """

    # Notice the call to holiday_service.
    return holiday_service.get_today()



@api.get("/date", response_class=JSONResponse)
def date(
    holiday_service: HolidayService = Depends(HolidayService),
    search_date = Query(...)
):
    """Date API Controller.

    Handles all access and parameters for the endpoint /api/date
    """

    raise NotImplementedError()
