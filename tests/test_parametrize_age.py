import pytest


@pytest.mark.parametrize(
    "age, expected",
    [
        (17, False),
        (18, True),
        (19, True),
    ],
)
def test_is_adult_by_age(age, expected):
    is_adult = age >= 18
    assert is_adult is expected