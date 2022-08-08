from typing import Protocol
from datetime import datetime


class IDateTimeHelper(Protocol):
    ...


class DateTimeHelper:
    month = datetime.now().strftime("%m")
    day = datetime.now().strftime("%d")
    year = datetime.now().strftime("%y")
    today = datetime.now().strftime("%m-%d-%y")
