from utils import read_json
from utils import filter_operations
from utils import sort_operations
from utils import output

file_path = "operations.json"


def main():
    """Главная функция, которая выводит на экран список из 5
    последних выполненных клиентом операций в формате:
    <дата перевода> <описание перевода>
    <откуда> -> <куда>
    <сумма перевода> <валюта>"""

    # Получаем список операций в виде словарей из файла json
    operations = read_json.get_data_from_json(file_path)

    # Находим выполненные операции
    executed_operations = filter_operations.get_executed_operations(operations)

    # Сортируем выполненные операции по дате в обратном порядке (от новой к старой)
    # Извлекаем первые 5 операций
    sorted_operations = sort_operations.sort_operations(executed_operations, 5)

    # Выводим операции в формате
    # 14.10.2018 Перевод организации
    # Visa Platinum 7000 79** **** 6361 -> Счет ** 9638
    # 82771.72 руб.
    for operation in sorted_operations:
        output.output(operation)


if __name__ == '__main__':
    main()
