# models.py
# Ian Kollipara
# 2021.08.09
# Pydantic Models

# Imports
from datetime import date
from pydantic import BaseModel


class Holiday(BaseModel):
    """Holiday Model for Calendarific API.

    This model contains the important data
    drawn from the API for each holiday.

    Name        | Type
    ------------+------
    name        | str
    description | str
    date        | datetime.date
    """

    name: str
    description: str
    date: date
