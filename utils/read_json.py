import json


def get_data_from_json():
    with open("operations.json", "r", encoding="utf-8") as file:
        data = json.load(file)
    return data
