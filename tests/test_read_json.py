from utils.read_json import get_data_from_json


def test_get_data_from_json():
    assert get_data_from_json() != None
    