import pytest


def test_convert_to_leet(instantiate_converter):
    leet_string = instantiate_converter("test string")
    assert isinstance(leet_string, str)


@pytest.mark.parametrize(
    'string, expected', [
        ("alex", "4l3x"),
        ("cool", "c00l"),
        ("love", "l0v3"),
        ("leet", "l337"),
        ("special charackters", "5p3c14l ch4r4ck73r5"),
    ]
)
def test_sample_strings(string, expected, instantiate_converter):
    leet_string = instantiate_converter(string)
    assert leet_string == expected
