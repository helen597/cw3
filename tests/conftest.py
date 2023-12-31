import pytest


TEST_DATE = '2019-01-15T17:58:27.064377'
FILE_PATH = "operations.json"
OPERATIONS = [{
    "id": 873106923,
    "state": "CANCELED",
    "date": "2019-03-23T01:09:46.296404",
    "operationAmount": {
      "amount": "43318.34",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод со счета на счет",
    "from": "Счет 44812258784861134719",
    "to": "Счет 74489636417521191160"
  },
  {
    "id": 214024827,
    "state": "EXECUTED",
    "date": "2018-12-20T16:43:26.929246",
    "operationAmount": {
      "amount": "70946.18",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод организации",
    "from": "Счет 10848359769870775355",
    "to": "Счет 21969751544412966366"
  },
  {
    "id": 522357576,
    "state": "EXECUTED",
    "date": "2019-07-12T20:41:47.882230",
    "operationAmount": {
      "amount": "51463.70",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
      "description": "Перевод организации",
      "from": "MasterCard 9175985085449563",
      "to": "Счет 82781399328834147668"
  }]


@pytest.fixture
def date_fixture():
    return TEST_DATE

@pytest.fixture
def file_path_fixture():
    return FILE_PATH

@pytest.fixture
def operations_fixture():
    return OPERATIONS
