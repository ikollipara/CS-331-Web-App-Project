# dependencies.py
# Ian Kollipara
# 2021.09.13
# Functional Dependencies

# Imports
from fastapi.templating import Jinja2Templates


def get_template() -> Jinja2Templates:
    """Return the template object.

    A functional dependency that
    returns an instance of FastAPI's
    Jinja2 Templating Engine. The
    template folder is provided
    in the function.
    """
    return Jinja2Templates("templates")
