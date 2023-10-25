from utils import date_and_time
from utils import cards_and_accounts

def output(operation):
    """Выводит одну операцию в формате
    14.10.2018 Перевод организации
    Visa Platinum 7000 79** **** 6361 -> Счет ** 9638
    82771.72 руб.
    """
    # Получаем дату операции
    thedate = date_and_time.get_datetime(operation['date'])
    # Преобразовываем дату в строку
    thedate = date_and_time.format_date(thedate)
    # Выводим дату и описание операции
    print(thedate, operation['description'])
    # Преобразовываем формат номера счета или карты получателя
    operation_to = cards_and_accounts.format_number(operation['to'])
    # Если указан отправитель,
    if 'from' in operation:
        # преобразовываем формат номера счета или карты отправителя
        operation_from = cards_and_accounts.format_number(operation['from'])
        # выводим номера отправителя и получателя
        print(operation_from, '->', operation_to)
    # а если отправитель не указан,
    else:
        # выводим номер счета или карты получателя
        print(operation_to)
    # выводим сумму операции и наименование валюты, переносим строку
    print(operation['operationAmount']['amount'], operation['operationAmount']['currency']['name'], '\n')
