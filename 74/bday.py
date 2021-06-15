import calendar

WEEKDAYS = (
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday",
)


def weekday_of_birth_date(date):
    """Takes a date object and returns the corresponding weekday string"""
    return WEEKDAYS[calendar.weekday(date.year, date.month, date.day)]
