# Извлекаем список дат из списка операций
# Сортируем даты в копию списка по убыванию
# Выбираем 5 первых дат
# Ищем каждую операцию по дате
# Формируем новый отсортированный список операций
def get_dates(executed_operations):
    dates = []
    for operation in executed_operations:
        if operation:
            dates.append(operation['date'])
    return dates


def sort_dates(dates):
    dates_copy = dates.copy()
    dates_copy.sort(reverse=True)
    return dates_copy


def get_operation_by_date(operations, thedate):
    for operation in operations:
        if operation:
            if operation['date'] == thedate:
                return operation
    return {}


def sort_operations(executed_operations, count):
    sorted_operations = []
    dates = get_dates(executed_operations)
    sorted_dates = sort_dates(dates)
    for i in range(count):
        operation = get_operation_by_date(executed_operations, sorted_dates[i])
        sorted_operations.append(operation)
    return sorted_operations
