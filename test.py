import pytest

from src.main import Converter
from src.utils import load_data

converter = Converter()

@pytest.mark.parametrize("number, expected_french", load_data(file_path='groundtruth_data.yml').items())
def test_convert_to_french(number, expected_french):
    result = converter.convert_to_french(number)
    assert result == expected_french, f"Expected {expected_french}, but got {result}"