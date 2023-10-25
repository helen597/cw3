def get_executed_operations(operations_list):
    """Получает выполненные операции из списка всех операций"""
    executed_operations = []
    for operation in operations_list:
        if operation:
            if operation['state'] == 'EXECUTED':
                executed_operations.append(operation)
    return executed_operations
