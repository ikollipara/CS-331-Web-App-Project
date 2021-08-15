# holiday_service.py
# Ian Kollipara
# 2021.08.09
# Holiday Service Definition

# Imports
from typing import Dict, List
from os import getenv
import requests
from datetime import date, datetime
from ..models import Holiday


class HolidayService:
    """Service Class for Holiday data.

    This class is only to be instantiated
    by FastAPI's dependency injection. This
    class handles all logic assoicated with
    Holiday data.

    methods:
    get_today -> List[Holiday]
    """

    def __init__(self) -> None:
        self._api_key = getenv("API_KEY")

    def _fetch_date(self, fetch_date: date) -> Dict:
        """Return raw json data for the current date.

        Call the Calendarific API filtering by the
        current date via year, month, and day. Then
        query through the json object to find the
        raw holiday list.
        """

        request_params = {
            "api_key": self._api_key,
            "country": "US",
            "year": fetch_date.year,
            "month": fetch_date.month,
            "day": fetch_date.day,
        }

        return (
            requests.get(
                f"https://calendarific.com/api/v2/holidays", params=request_params
            )
            .json()
            .get("response")
            .get("holidays")
        )

    def get_today(self) -> List[Holiday]:
        """Return all Holidays for the current date.

        Returns a list of holidays, formatted in the
        Holiday Model, for the current day. This
        day is drawn from Python's datetime module.
        If there are no holidays, the method returns
        an empty list.
        """

        # Fetch the date using a private method
        raw_data = self._fetch_date(date.today())

        holidays: List[Holiday] = []

        for raw_holiday in raw_data:

            name = raw_holiday.get("name")
            description = raw_holiday.get("description")
            current_date = datetime.fromisoformat(raw_holiday.get("date").get("iso"))

            holiday = Holiday(name=name, description=description, date=current_date)

            holidays.append(holiday)

        return holidays

    def get_by_date(self, raw_date: str) -> List[Holiday]:
        """Return all Holidays for the given date.

        Returns a list of holidays, formatted in the
        Holiday Model, for the current day.
        If there are no holidays, the method returns
        an empty list.
        """

        holidays: List[Holiday] = []

        # Translate the raw iso date into a Python Date
        # then fetch from that date
        # Notice the same private function as in get_today
        search_date = date.fromisoformat(raw_date)
        raw_data = self._fetch_date(search_date)

        for raw_holiday in raw_data:

            name = raw_holiday.get("name")
            description = raw_holiday.get("description")
            current_date = datetime.fromisoformat(raw_holiday.get("date").get("iso"))

            holiday = Holiday(name=name, description=description, date=current_date)

            holidays.append(holiday)

        return holidays
