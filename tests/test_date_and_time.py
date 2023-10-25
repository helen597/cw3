import pytest
from utils import date_and_time
from datetime import datetime

def test_get_datetime(date_fixture):
    assert isinstance(date_and_time.get_datetime(date_fixture), datetime)
    assert date_and_time.get_datetime(date_fixture).strftime("%d.%m.%Y") == "15.01.2019"
    assert date_and_time.get_datetime(date_fixture).strftime("%d.%m.%Y %H:%M:%S") == "15.01.2019 17:58:27"
    assert date_and_time.get_datetime(date_fixture) == datetime.fromisoformat("2019-01-15 17:58:27.064377")
    with pytest.raises(ValueError):
        date_and_time.get_datetime("")

def test_format_date(date_fixture):
    assert date_and_time.format_date(datetime.fromisoformat(date_fixture)) == '15.01.2019'
    assert date_and_time.format_date(datetime.fromisoformat('2023-10-25 23:58:27.064377')) == '25.10.2023'
    with pytest.raises(AttributeError):
        date_and_time.format_date("")