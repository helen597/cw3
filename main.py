from utils import read_json
from utils import filter_operations
from utils import sort_operations
from utils import output

file_path = "operations.json"


def main():
    """Главная"""
    #Получаем список словарей из файла
    #Находим выполненные операции
    #Сортируем выполненные операции по дате в обратном порядке (от новой к старой)
    #Извлекаем первые 5 операций
    #Преобразовываем дату
    #Преобразовываем номер карты
    #Преобразовываем номер счета
    #Выводим операции в формате
    #14.10.2018 Перевод организации
    #Visa Platinum 7000 79** **** 6361 -> Счет ** 9638
    #82771.72 руб.
    operations = read_json.get_data_from_json(file_path)
    executed_operations = filter_operations.get_executed_operations(operations)
    sorted_operations = sort_operations.sort_operations(executed_operations, 5)
    for operation in sorted_operations:
        output.output(operation)


if __name__ == '__main__':
    main()
