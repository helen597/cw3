from utils import date_and_time

def output(operation):
    # Выводим операции в формате
    # 14.10.2018 Перевод организации
    # Visa Platinum 7000 79** **** 6361 -> Счет ** 9638
    # 82771.72 руб.
    thedate = date_and_time.get_datetime(operation['date'])
    thedate = date_and_time.format_date(thedate)
    print(thedate, operation['description'])
    if operation['from']:
        print(operation['from'], '->', operation['to'])
    else:
        print(operation['to'])
    print(operation['operationAmount']['amount'], operation['operationAmount']['currency']['name'], '\n')
