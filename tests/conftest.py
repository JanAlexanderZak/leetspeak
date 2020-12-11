import pytest
from leetspeak.leetspeak_app.views import LeetspeekConverter


@pytest.fixture
def instantiate_converter():
    def _method(string):
        """Kinda wrap to pass in parameter"""
        converter = LeetspeekConverter()
        leet_string = converter.convert_to_leet(string)
        return leet_string
    return _method


"""
@pytest.fixture
def my_fixture():
    return 7

"""
