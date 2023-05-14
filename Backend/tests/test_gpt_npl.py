import pytest
from Backend.gptparser import GPTParser

parameters = [
    ("The eleventh of november at ten o'clock", "11-11 10:00"),
    ("The 26th of aug at 11.15", "26-08 11:15"),
    ("11th of Nov at 1 o'clock", "11-11 01:00"),
    ("The thirteenth of april at one am", "13-04 01:00"),
    ("The 13th of dec at one pm", "13-12 13:00")
]

@pytest.mark.skip(reason="openAI key is missing")
@pytest.mark.parametrize("param, expected_result", parameters)
def test_my_function(param, expected_result):
    result = GPTParser.datetime_parser(param)
    assert result == expected_result

