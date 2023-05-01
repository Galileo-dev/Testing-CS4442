import pytest

@pytest.fixture
def addition():
    return 1 + 2

def test_addition(addition):
    assert addition == 3
