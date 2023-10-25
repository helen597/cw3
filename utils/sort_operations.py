def get_dates(executed_operations):
    """Извлекает список дат из списка операций"""
    dates = []
    for operation in executed_operations:
        if operation:
            dates.append(operation['date'])
    return dates


def sort_dates(dates):
    """Сортирует даты в копию списка по убыванию"""
    dates_copy = dates.copy()
    dates_copy.sort(reverse=True)
    return dates_copy


def get_operation_by_date(operations, thedate):
    """Получает операцию по дате"""
    for operation in operations:
        if operation:
            if operation['date'] == thedate:
                return operation
    return {}


def sort_operations(executed_operations, count):
    """Получает список последних операций,
    где count - заданное количество операций"""
    sorted_operations = []
    # Извлекаем список дат из списка операций
    dates = get_dates(executed_operations)
    # Сортируем даты по убыванию
    sorted_dates = sort_dates(dates)
    # Выбираем count первых дат и получаем каждую операцию по дате
    # Формируем новый отсортированный список count операций,
    # добавляя к нему полученные операции
    for i in range(count):
        operation = get_operation_by_date(executed_operations, sorted_dates[i])
        sorted_operations.append(operation)
    return sorted_operations
