import pytest
from utils.output import output


def test_output(operations_fixture):
    for operation in operations_fixture:
        assert output(operation) == None
    with pytest.raises(KeyError):
        output({
        "id": 893507143,
        "state": "EXECUTED",
        "date": "2018-02-03T07:16:28.366141",
        "operationAmount": {
            "amount": "90297.21",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Открытие вклада",
        "to": "Счет 37653295304860108767"
    })
