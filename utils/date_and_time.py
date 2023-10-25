from datetime import datetime


def get_datetime(thedate):
    """Получает дату из строки"""
    new_datetime = datetime.fromisoformat(thedate)
    return new_datetime

def format_date(thedate):
    """Преобразовывает дату в строку"""
    new_date = thedate.strftime("%d.%m.%Y")
    return new_date
