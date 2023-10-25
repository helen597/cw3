import json

def get_data_from_json(file_path):
    """Получаем список словарей"""
    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)
    return data
