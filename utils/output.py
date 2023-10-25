from utils import date_and_time
from utils import cards_and_accounts

def output(operation):
    # Выводим операции в формате
    # 14.10.2018 Перевод организации
    # Visa Platinum 7000 79** **** 6361 -> Счет ** 9638
    # 82771.72 руб.
    thedate = date_and_time.get_datetime(operation['date'])
    thedate = date_and_time.format_date(thedate)
    print(thedate, operation['description'])
    operation_to = cards_and_accounts.format_number(operation['to'])
    if 'from' in operation:
        operation_from = cards_and_accounts.format_number(operation['from'])
        print(operation_from, '->', operation_to)
    else:
        print(operation_to)
    print(operation['operationAmount']['amount'], operation['operationAmount']['currency']['name'], '\n')
