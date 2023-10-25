import pytest
from utils.read_json import get_data_from_json


def test_get_data_from_json(file_path_fixture):
    assert get_data_from_json(file_path_fixture) != None
    assert isinstance(get_data_from_json(file_path_fixture), list)
    with pytest.raises(FileNotFoundError):
        assert get_data_from_json("")
