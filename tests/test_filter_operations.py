import pytest
from utils.filter_operations import get_executed_operations


def test_get_executed_operations(operations_fixture):
    assert get_executed_operations(operations_fixture) == [{
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
    assert get_executed_operations([]) == []
