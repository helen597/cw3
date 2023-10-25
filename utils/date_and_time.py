from datetime import datetime


def get_datetime(thedate):
    new_datetime = datetime.fromisoformat(thedate)
    return new_datetime

def format_date(thedate):
    new_date = thedate.strftime("%d.%m.%Y")
    return new_date