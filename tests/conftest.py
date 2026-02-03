import pytest

@pytest.fixture
def user_data():
    return {'name': 'Ivan', 'age': 25}
